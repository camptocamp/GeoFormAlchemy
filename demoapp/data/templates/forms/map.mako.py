from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272622938.4603231
_template_filename='/home/tsauerwein/Documents/tryz/geoalchemy_dev/geoformalchemy/demoapp/demoapp/templates/forms/map.mako'
_template_uri='/forms/map.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        read_only = context.get('read_only', UNDEFINED)
        map_width = context.get('map_width', UNDEFINED)
        map_height = context.get('map_height', UNDEFINED)
        geometry_type = context.get('geometry_type', UNDEFINED)
        openlayers_lib = context.get('openlayers_lib', UNDEFINED)
        zoom = context.get('zoom', UNDEFINED)
        input_field = context.get('input_field', UNDEFINED)
        default_lon = context.get('default_lon', UNDEFINED)
        is_collection = context.get('is_collection', UNDEFINED)
        default_lat = context.get('default_lat', UNDEFINED)
        base_layer = context.get('base_layer', UNDEFINED)
        field_name = context.get('field_name', UNDEFINED)
        wkt = context.get('wkt', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

# default configuration options that will be used when
# no field options were set, e.g. with:
#
# Place = FieldSet(model.places.Place)
# Place.the_geom.set(options=[('zoom', 12), ..]) 

        options = {}
        options['default_lon'] = 10
        options['default_lat'] = 45
        options['zoom'] = 4
        options['map_width'] = 512
        options['map_height'] = 256
        options['base_layer'] = 'new OpenLayers.Layer.WMS("WMS", "http://labs.metacarta.com/wms/vmap0", {layers: "basic"})'
        options['openlayers_lib'] = 'http://openlayers.org/api/OpenLayers.js'
        
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['options'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 17
        __M_writer(u'\n\n<script src="')
        # SOURCE LINE 19
        __M_writer(escape(openlayers_lib or options['openlayers_lib']))
        __M_writer(u'"></script>\n\n<style>\n.formmap_')
        # SOURCE LINE 22
        __M_writer(escape(field_name))
        __M_writer(u' {\n    width: ')
        # SOURCE LINE 23
        __M_writer(escape(map_width or options['map_width']))
        __M_writer(u'px;\n    height: ')
        # SOURCE LINE 24
        __M_writer(escape(map_height or options['map_height']))
        __M_writer(u'px;\n    border: 1px solid #ccc;\n}\n\n.olControlAttribution {\n    bottom: 2px; \n}\n\n.olControlEditingToolbar .olControlModifyFeatureItemActive { \n    background-image: url("http://openlayers.org/api/theme/default/img/draw_point_on.png")\n}\n.olControlEditingToolbar .olControlModifyFeatureItemInactive { \n    background-image: url("http://openlayers.org/api/theme/default/img/draw_point_off.png")\n}\n</style>\n\n<div>\n    ')
        # SOURCE LINE 41
        __M_writer(escape(input_field))
        __M_writer(u'\n    <div id="map_')
        # SOURCE LINE 42
        __M_writer(escape(field_name))
        __M_writer(u'" class="formmap_')
        __M_writer(escape(field_name))
        __M_writer(u'"></div>\n    <script type="text/javascript">\n        ')
        # SOURCE LINE 44
        runtime._include_file(context, 'map_js.mako', _template_uri)
        __M_writer(u"\n        init_map(\n                '")
        # SOURCE LINE 46
        __M_writer(escape(field_name))
        __M_writer(u"',\n                ")
        # SOURCE LINE 47
        __M_writer(escape(read_only))
        __M_writer(u',\n                ')
        # SOURCE LINE 48
        __M_writer(escape(is_collection))
        __M_writer(u",\n                '")
        # SOURCE LINE 49
        __M_writer(escape(geometry_type))
        __M_writer(u"',\n                ")
        # SOURCE LINE 50
        __M_writer(escape(default_lon or options['default_lon']))
        __M_writer(u',\n                ')
        # SOURCE LINE 51
        __M_writer(escape(default_lat or options['default_lat']))
        __M_writer(u',\n                ')
        # SOURCE LINE 52
        __M_writer(escape(zoom or options['zoom']))
        __M_writer(u',\n                ')
        # SOURCE LINE 53
        __M_writer(base_layer or options['base_layer'] )
        __M_writer(u",\n                '")
        # SOURCE LINE 54
        __M_writer(escape(wkt))
        __M_writer(u"'\n        );\n    </script>\n    <br />\n</div>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


