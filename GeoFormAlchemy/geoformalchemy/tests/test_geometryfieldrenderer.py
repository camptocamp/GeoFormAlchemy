
import unittest

from sqlalchemy import Column, types
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session

from geoalchemy import GeometryColumn, Point, geometry

from formalchemy.forms import FieldSet

from geoformalchemy.base import GeometryFieldRenderer
from geoalchemy.base import PersistentSpatialElement, WKBSpatialElement, WKTSpatialElement
from geoalchemy.functions import functions

from nose.tools import ok_, eq_


metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Spot(Base):
    __tablename__ = 'spots'
    
    id = Column(types.Integer, primary_key=True)
    name = Column(types.String, nullable=False)
    the_geom = GeometryColumn(Point(dimension=2, srid=4326))

class FakeSession(Session):
    
    def __init__(self):
        pass
    
    def scalar(self, *args, **kwargs):
        self.scalar_args = args
        self.scalar_kwargs = kwargs
        
        return 'geometry'
  
    def add(self, instance):
        self.add_instance = instance

FieldSet.default_renderers[geometry.Geometry] = GeometryFieldRenderer

class TestGeometryFieldRenderer(unittest.TestCase):

    def test_render(self):
        session = FakeSession()
        spot_fieldset = FieldSet(Spot, session=session)
        
        spot = Spot()
        spot.id = 1
        spot.the_geom = PersistentSpatialElement(PersistentSpatialElement(WKBSpatialElement('010')));
        
        spot_fieldset = spot_fieldset.bind(spot)
        
        form = spot_fieldset.render()
        
        ok_("geoformalchemy.init_map(" in form, 'Template was not rendered')
        ok_("'Point'," in form, 'OpenLayers geometry was not mapped correctly ')
        ok_("false," in form, 'Geometry should not be a collection')
        ok_(isinstance(session.scalar_args[0], functions.wkt), 'The geometry was not queried as WKT');
        
    def test_render_reproject(self):
        session = FakeSession()
        spot_fieldset = FieldSet(Spot, session=session)
        spot_fieldset.the_geom.set(options=[('map_srid', 900913)])
        
        spot = Spot()
        spot.id = 1
        spot.the_geom = PersistentSpatialElement(PersistentSpatialElement(WKBSpatialElement('010')));
        
        spot_fieldset = spot_fieldset.bind(spot)
        
        spot_fieldset.render()
        ok_(isinstance(session.scalar_args[0], functions.wkt), 'The geometry was not queried as WKT');
        ok_(isinstance(session.scalar_args[0].arguments[0], functions.transform), 'The geometry was not reprojected');
        
    def test_render_options(self):
        spot_fieldset = FieldSet(Spot)
        spot_fieldset.the_geom.set(options=[
                        ('default_lat', 1),
                        ('default_lon', 2),
                        ('zoom', 3),
                        ('map_width', 4),
                        ('map_height', 5),
                        ('base_layer', 'new OpenLayers.Layer.DummyLayer("OSM")'),
                        ('openlayers_lib', '/js/OpenLayers.js')])
        
        form = spot_fieldset.render()
        
        ok_('1,\n            2,\n            3,            \'Point\',            new OpenLayers.Layer.DummyLayer("OSM"),', form)
        ok_('<script src="/js/OpenLayers.js"></script>' in form)
        
    def test_render_validate(self):
        params = {'Spot--the_geom': 'Point(0 1)', 'Spot--name': ''}
        
        spot_fieldset = FieldSet(Spot, data = params)
        
        spot_fieldset.validate()
        form = spot_fieldset.render()
        ok_("Point(0 1)'" in form, 'submitted value was not re-displayed in case of validation error')
        
    def test_deserialize_reproject(self):
        params = {'Spot--the_geom': 'Point(0 1)', 'Spot--name': 'dummy'}
        session = FakeSession()
        
        spot_fieldset = FieldSet(Spot, data = params, session=session)
        spot_fieldset.the_geom.set(options=[('map_srid', 900913)])
        
        spot_fieldset.validate()
        spot_fieldset.sync()
        ok_(isinstance(spot_fieldset.model.the_geom, WKTSpatialElement), 'Geometry was not assigned to model')
        eq_(spot_fieldset.model.the_geom.desc, 'geometry', 'The geometry was not reprojected for the insertion into the db')
        
        spot_fieldset.render()
        ok_(isinstance(session.scalar_args[0], functions.wkt), 'The geometry was not queried as WKT')
        ok_(isinstance(session.scalar_args[0].arguments[0], functions.transform), 'The geometry was not reprojected')
        
        
