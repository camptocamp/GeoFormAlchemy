from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272623429.6119411
_template_filename='/home/tsauerwein/Documents/tryz/geoalchemy_dev/geoformalchemy/demoapp/demoapp/templates/forms/fieldset_readonly.mako'
_template_uri='/forms/fieldset_readonly.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        int = context.get('int', UNDEFINED)
        fieldset = context.get('fieldset', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<tbody>\n')
        # SOURCE LINE 3
        for field in fieldset.render_fields.itervalues():
            # SOURCE LINE 4
            __M_writer(u'  <tr>\n    <td class="field_readonly">')
            # SOURCE LINE 5
            __M_writer(filters.html_escape(escape([field.label_text, fieldset.prettify(field.key)][int(field.label_text is None)])))
            __M_writer(u':</td>\n    <td>')
            # SOURCE LINE 6
            __M_writer(field.render_readonly())
            __M_writer(u'</td>\n  </tr>\n')
        # SOURCE LINE 9
        __M_writer(u'</tbody>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


