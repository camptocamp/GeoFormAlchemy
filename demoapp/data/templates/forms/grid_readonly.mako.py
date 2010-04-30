from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272622932.846097
_template_filename='/home/tsauerwein/Documents/tryz/geoalchemy_dev/geoformalchemy/demoapp/demoapp/templates/forms/grid_readonly.mako'
_template_uri='/forms/grid_readonly.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        enumerate = context.get('enumerate', UNDEFINED)
        collection = context.get('collection', UNDEFINED)
        F_ = context.get('F_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<thead>\n  <tr>\n')
        # SOURCE LINE 4
        for field in collection.render_fields.itervalues():
            # SOURCE LINE 5
            __M_writer(u'      <th>')
            __M_writer(filters.html_escape(escape(F_(field.label_text or collection.prettify(field.key)))))
            __M_writer(u'</th>\n')
        # SOURCE LINE 7
        __M_writer(u'  </tr>\n</thead>\n\n<tbody>\n')
        # SOURCE LINE 11
        for i, row in enumerate(collection.rows):
            # SOURCE LINE 12
            __M_writer(u'  ')
            collection._set_active(row) 
            
            __M_writer(u'\n  <tr class="')
            # SOURCE LINE 13
            __M_writer(escape(i % 2 and 'odd' or 'even'))
            __M_writer(u'">\n')
            # SOURCE LINE 14
            for field in collection.render_fields.itervalues():
                # SOURCE LINE 15
                __M_writer(u'    <td>')
                __M_writer(field.render_readonly())
                __M_writer(u'</td>\n')
            # SOURCE LINE 17
            __M_writer(u'  </tr>\n')
        # SOURCE LINE 19
        __M_writer(u'</tbody>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


