from formalchemy.fields import FieldRenderer, deserialize_once
from formalchemy.forms import FieldSet
from formalchemy.tables import Grid
from formalchemy import helpers as h, config

from geoalchemy.geometry import (Point, Curve, LineString, 
    Polygon, MultiPoint, MultiLineString, MultiPolygon)
from geoalchemy.base import PersistentSpatialElement, WKTSpatialElement
from geoalchemy.functions import functions

from mako.lookup import TemplateLookup
from mako.exceptions import TemplateLookupException

import os

class GeometryFieldRenderer(FieldRenderer):
    """An extension for FormAlchemy that renders GeoAlchemy's geometry type
    
    To enable this extension, it has to be registered as 'default_renderer'::
        
        from geoformalchemy.base import GeometryFieldRenderer
        from geoalchemy import geometry
        from formalchemy.forms import FieldSet
        FieldSet.default_renderers[geometry.Geometry] = GeometryFieldRenderer
        
        
    The rendering of a specific field can be customized without having to change
    the template files. If an option is not set, the default value specified in
    the template file 'map.mako' will be used::
        
        Place = FieldSet(model.places.Place)
        Place.the_geom.set(options=[
            ('map_srid', 900913),
            ('base_layer', 'new OpenLayers.Layer.OSM("OSM")')])
            
            
    Following options can be used::
        
        default_lat
        default_lon
            If the geometry is ''None'' or when creating a new geometry, the map
            is centered at (default_lon, default_lat).
        
        zoom
            The zoom-level on start-up.
        
        map_width
        map_height
            The size of the DIV container in which the map is displayed.
            
        base_layer
            The OpenLayers layer which will be used as background map, for example::
                ('base_layer', 'new OpenLayers.Layer.OSM("OSM")') 
        
        map_srid
            If the map uses a different CRS than the geometries, the geometries will be
            reprojected to this CRS.
            
        openlayers_lib
            The path to the OpenLayers JavaScript library, for example::
                ('openlayers_lib', 'http://openlayers.org/api/OpenLayers.js') 
            
        show_map (default: True)
            If ``show_map`` is set to ``False``, the geometry will be displayed as WKT string 
            inside a text input field.
            
    """
    
    def __init__(self, field):
        self.__templates = None
        
        FieldRenderer.__init__(self, field)
    
    def render(self, **kwargs):
        return self.__render_map(False)
    
    def render_readonly(self, **kwargs):
        if isinstance(self.field.parent, FieldSet):
            # if rendering for a FieldSet (when a single entry is displayed),
            # show a read-only map where you can pan and zoom around
            return self.__render_map(True)
        elif isinstance(self.field.parent, Grid):
            # if rendering for a Grid (when a table/list of all entries is displayed),
            # do not show a map but the geometry type
            if self.raw_value is None:
                return ''
            else:
                # geometry type
                return self.field.type.__class__.name
        
    @deserialize_once
    def deserialize(self):
        """Turns the user input into a GeoAlchemy geometry, which
        can be stored in the database.
        
        If necessary the geometry is reprojected by making a database query. 
        """
        form_value = self.params.getone(self.name)
        
        if form_value is not None and form_value.strip() != '':
            options = self.__get_options()
            geom_srid = self.field.type.srid
            map_srid = options.get('map_srid', geom_srid)
            wkt_elt = WKTSpatialElement(form_value, srid=map_srid)
            
            if geom_srid != map_srid:
                # if the map uses a different CRS, we have to reproject
                query = functions.wkt(functions.transform(wkt_elt, geom_srid))
                session = self.field.parent.session
                return session.scalar(query)

            return wkt_elt
                
        return None
    
    def __render_map(self, read_only):
        options = self.__get_options()
        geometry_type = self.__get_type_information()
        
        if len(self.field.errors) > 0:
            # if re-displaying a form with errors, get the WKT string
            # from the form submission
            wkt = self.params.getone(self.name)
        else:
            # if displaying a new form, try to query the geometry in WKT
            wkt = self.__get_wkt_for_field(options);
        
        if not options.get('show_map', True):
            # if no map should be shown, just display a text field
            if read_only:
                return h.text_field(self.name, value=wkt, readonly='readonly')
            else: 
                return h.text_field(self.name, value=wkt)
        
        template_args = {
                        'field_name' : self.name,
                        'wkt' : wkt,
                        'input_field' : h.hidden_field(self.name, value=wkt),
                        #'input_field' : h.text_field(self.name, value=wkt), # for debug
                        'read_only' : 'true' if read_only else 'false',
                        'is_collection' : 'true' if geometry_type['is_collection'] else 'false',
                        'geometry_type' : geometry_type['geometry_type'] ,
                        'default_lat' : options.get('default_lat', None),
                        'default_lon' : options.get('default_lon', None),
                        'zoom' : options.get('zoom', None),
                        'map_width' : options.get('map_width', None),
                        'map_height' : options.get('map_height', None),
                        'base_layer' : options.get('base_layer', None),
                        'openlayers_lib' : options.get('openlayers_lib', None)   
                    }
        
        try:
            """Try to render the template with the FormAlchemy template engine which assumes that
            the 'map.mako' template file is in the same folder as the other FormAlchemy template files.
            This is the case when used inside a Pylons app."""
            return config.engine.render('map', **template_args)
        except (TemplateLookupException, AttributeError, ValueError):
            # otherwise render the default template using an own template engine
            map_template = self.get_templates().get_template('map.mako')
            return map_template.render(**template_args)

    def __get_wkt_for_field(self, options):
        """Returns the WKT string for the value of a field by making
        a database query.
        
        If necessary the geometry is reprojected.  
        """
        if self.raw_value is not None and isinstance(self.raw_value, PersistentSpatialElement): 
            geom_srid = self.field.type.srid
            map_srid = options.get('map_srid', geom_srid)
            
            if geom_srid != map_srid:
                # if the map uses a different CRS we have to ask the database
                # to reproject the geometry
                query = functions.wkt(functions.transform(self.raw_value, map_srid))
            else:
                query = self.raw_value.wkt
            
            session = self.field.parent.session
            return session.scalar(query)
        else:
            return '';

    def __get_type_information(self):
        """This method maps GeoAlchemy geometry types to the
        equivalent OpenLayers geometries.
        
        A dictionary is returned with two keys:
            is_collection: True for Multi* geometry types
            geometry_type: The OpenLayers geometry type
        """
        geom_type = self.field.type
        
        if isinstance(geom_type, (Point, MultiPoint)):
            is_collection = isinstance(geom_type, MultiPoint)
            geometry_type = 'Point'
        elif isinstance(geom_type, (Curve, LineString, MultiLineString)):
            is_collection = isinstance(geom_type, MultiLineString)
            geometry_type = 'Path'
        elif isinstance(geom_type, (Polygon, MultiPolygon)):
            is_collection = isinstance(geom_type, MultiPolygon)
            geometry_type = 'Polygon'
        else:
            is_collection = True
            geometry_type = 'Collection'
        
        return {
                'is_collection' : is_collection,
                'geometry_type' : geometry_type
                }
    
    def __get_options(self):
        """Turns the options list, a list of tuples e.g. [('..', '..'), ('..', '..')],
        into a real dictionary.
        """
        options_list = self.field.render_opts.get('options', [])
        return dict(options_list)
    
    def get_templates(self):
        if self.__templates == None:
            dirname = os.path.join(os.path.dirname(__file__), 'pylons', 'project', '+package+', 'templates', 'forms')
            self.__templates = TemplateLookup([dirname], input_encoding='utf-8', output_encoding='utf-8')
        
        return self.__templates
