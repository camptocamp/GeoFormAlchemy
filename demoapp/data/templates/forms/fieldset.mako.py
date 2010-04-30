from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272622938.3988581
_template_filename='/home/tsauerwein/Documents/tryz/geoalchemy_dev/geoformalchemy/demoapp/demoapp/templates/forms/fieldset.mako'
_template_uri='/forms/fieldset.mako'
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
        F_ = context.get('F_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2

        _ = F_
        _focus_rendered = False
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['_focus_rendered','_'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 5
        __M_writer(u'')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        for error in fieldset.errors.get(None, []):
            # SOURCE LINE 8
            __M_writer(u'<div class="fieldset_error">\n  ')
            # SOURCE LINE 9
            __M_writer(escape(_(error)))
            __M_writer(u'\n</div>\n')
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        for field in fieldset.render_fields.itervalues():
            # SOURCE LINE 14
            if field.requires_label:
                # SOURCE LINE 15
                __M_writer(u'<div>\n  <label class="')
                # SOURCE LINE 16
                __M_writer(escape(field.is_required() and 'field_req' or 'field_opt'))
                __M_writer(u'" for="')
                __M_writer(escape(field.renderer.name))
                __M_writer(u'">')
                __M_writer(filters.html_escape(escape([field.label_text, fieldset.prettify(field.key)][int(field.label_text is None)])))
                __M_writer(u'</label>\n  ')
                # SOURCE LINE 17
                __M_writer(field.render())
                __M_writer(u'\n')
                # SOURCE LINE 18
                if 'instructions' in field.metadata:
                    # SOURCE LINE 19
                    __M_writer(u'  <span class="instructions">')
                    __M_writer(escape(field.metadata['instructions']))
                    __M_writer(u'</span>\n')
                # SOURCE LINE 21
                for error in field.errors:
                    # SOURCE LINE 22
                    __M_writer(u'  <span class="field_error">')
                    __M_writer(escape(_(error)))
                    __M_writer(u'</span>\n')
                # SOURCE LINE 24
                __M_writer(u'</div>\n\n')
                # SOURCE LINE 26
                if (fieldset.focus == field or fieldset.focus is True) and not _focus_rendered:
                    # SOURCE LINE 27
                    if not field.is_readonly():
                        # SOURCE LINE 28
                        __M_writer(u'<script type="text/javascript">\n//<![CDATA[\ndocument.getElementById("')
                        # SOURCE LINE 30
                        __M_writer(escape(field.renderer.name))
                        __M_writer(u'").focus();\n//]]>\n</script>\n')
                        # SOURCE LINE 33
                        _focus_rendered = True 
                        
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['_focus_rendered'] if __M_key in __M_locals_builtin()]))
                        __M_writer(u'')
                # SOURCE LINE 36
            else:
                # SOURCE LINE 37
                __M_writer(field.render())
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


