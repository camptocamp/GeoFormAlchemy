from pylons import config
from demoapp import model
from demoapp.lib.base import render
from formalchemy import config as fa_config
from formalchemy import templates
from formalchemy import validators
from formalchemy import fields
from formalchemy import forms
from formalchemy import tables
from formalchemy.ext.fsblob import FileFieldRenderer
from formalchemy.ext.fsblob import ImageFieldRenderer

fa_config.encoding = 'utf-8'

class TemplateEngine(templates.TemplateEngine):
    def render(self, name, **kwargs):
        return render('/forms/%s.mako' % name, extra_vars=kwargs)
fa_config.engine = TemplateEngine()

class FieldSet(forms.FieldSet):
    pass

class Grid(tables.Grid):
    pass

# enable GeoFormAlehemy renderer
from geoformalchemy import GeometryFieldRenderer
from geoalchemy import geometry
FieldSet.default_renderers[geometry.Geometry] = GeometryFieldRenderer

## Initialize fieldsets
Place = FieldSet(model.places.Place)
Place.configure(options=[Place.the_geom.label('Geometry').required()])

Place.the_geom.set(options=[
    ('map_srid', 900913),
    ('base_layer', 'new OpenLayers.Layer.OSM("OSM")'),
    ('default_lon', 733500),
    ('default_lat', 5863900),
    ('zoom', 10)
    ])

Lake = FieldSet(model.lakes.Lake)
Lake.configure(options=[Lake.the_geom.label('Geometry').required()])
Lake.the_geom.set(options=[('zoom', 8)])

Category = FieldSet(model.categories.Category)
Category.configure(options=[Category.description.textarea()])


#Foo = FieldSet(model.Foo)
#Reflected = FieldSet(Reflected)

## Initialize grids

#FooGrid = Grid(model.Foo)
#ReflectedGrid = Grid(Reflected)