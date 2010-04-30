from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272622929.9767809
_template_filename='/home/tsauerwein/Documents/tryz/geoalchemy_dev/geoformalchemy/demoapp/demoapp/templates/forms/restfieldset.mako'
_template_uri='/forms/restfieldset.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['buttons', 'h1']


# SOURCE LINE 2

from formalchemy.ext.pylons.controller import model_url
from pylons import url


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        fs = context.get('fs', UNDEFINED)
        models = context.get('models', UNDEFINED)
        collection_name = context.get('collection_name', UNDEFINED)
        id = context.get('id', UNDEFINED)
        def h1(title,href=None):
            return render_h1(context.locals_(__M_locals),title,href)
        is_grid = context.get('is_grid', UNDEFINED)
        F_ = context.get('F_', UNDEFINED)
        def buttons():
            return render_buttons(context.locals_(__M_locals))
        dict = context.get('dict', UNDEFINED)
        member_name = context.get('member_name', UNDEFINED)
        action = context.get('action', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        pager = context.get('pager', UNDEFINED)
        model_name = context.get('model_name', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n<html>\n  <head>\n    <title>\n    ')
        # SOURCE LINE 34
        __M_writer(escape(collection_name.title()))
        __M_writer(u'\n    </title>\n    <link rel="stylesheet" type="text/css" href="')
        # SOURCE LINE 36
        __M_writer(escape(url('fa_static', path_info='/admin.css')))
        __M_writer(u'" />\n  </head>\n  <body>\n<div id="content" class="ui-admin ui-widget">\n')
        # SOURCE LINE 40
        if isinstance(models, dict):
            # SOURCE LINE 41
            __M_writer(u'    <h1 id="header" class="ui-widget-header ui-corner-all">')
            __M_writer(escape(F_('Models')))
            __M_writer(u'</h1>\n')
            # SOURCE LINE 42
            for name in sorted(models):
                # SOURCE LINE 43
                __M_writer(u'      <p>\n        <a class="ui-state-default ui-corner-all" href="')
                # SOURCE LINE 44
                __M_writer(escape(models[name]))
                __M_writer(u'">')
                __M_writer(escape(name))
                __M_writer(u'</a>\n      </p>\n')
            # SOURCE LINE 47
        elif is_grid:
            # SOURCE LINE 48
            __M_writer(u'    ')
            __M_writer(escape(h1(model_name)))
            __M_writer(u'\n    <div class="ui-pager">\n      ')
            # SOURCE LINE 50
            __M_writer(pager)
            __M_writer(u'\n    </div>\n    <table class="layout-grid">\n    ')
            # SOURCE LINE 53
            __M_writer(fs.render())
            __M_writer(u'\n    </table>\n    <p>\n      <a class="ui-widget-header ui-widget-link ui-corner-all" href="')
            # SOURCE LINE 56
            __M_writer(escape(model_url('new_%s' % member_name)))
            __M_writer(u'">\n          <span class="ui-icon ui-icon-circle-plus"></span>\n          ')
            # SOURCE LINE 58
            __M_writer(escape(F_('New')))
            __M_writer(u' ')
            __M_writer(escape(model_name))
            __M_writer(u'\n      </a>\n    </p>\n')
            # SOURCE LINE 61
        else:
            # SOURCE LINE 62
            __M_writer(u'    ')
            __M_writer(escape(h1(model_name, href=model_url(collection_name))))
            __M_writer(u'\n')
            # SOURCE LINE 63
            if action == 'show':
                # SOURCE LINE 64
                __M_writer(u'      <table>\n        ')
                # SOURCE LINE 65
                __M_writer(fs.render())
                __M_writer(u'\n      </table>\n      <p class="fa_field">\n        <a class="ui-widget-header ui-widget-link ui-corner-all" href="')
                # SOURCE LINE 68
                __M_writer(escape(model_url('edit_%s' % member_name, id=id)))
                __M_writer(u'">\n          <span class="ui-icon ui-icon-pencil"></span>\n          ')
                # SOURCE LINE 70
                __M_writer(escape(F_('Edit')))
                __M_writer(u'\n        </a>\n      </p>\n')
                # SOURCE LINE 73
            elif action == 'edit':
                # SOURCE LINE 74
                __M_writer(u'      <form action="')
                __M_writer(escape(model_url(member_name, id=id)))
                __M_writer(u'" method="POST" enctype="multipart/form-data">\n        ')
                # SOURCE LINE 75
                __M_writer(fs.render())
                __M_writer(u'\n        <input type="hidden" name="_method" value="PUT" />\n        ')
                # SOURCE LINE 77
                __M_writer(escape(buttons()))
                __M_writer(u'\n      </form>\n')
                # SOURCE LINE 79
            else:
                # SOURCE LINE 80
                __M_writer(u'      <form action="')
                __M_writer(escape(model_url(collection_name)))
                __M_writer(u'" method="POST" enctype="multipart/form-data">\n        ')
                # SOURCE LINE 81
                __M_writer(fs.render())
                __M_writer(u'\n        ')
                # SOURCE LINE 82
                __M_writer(escape(buttons()))
                __M_writer(u'\n      </form>\n')
        # SOURCE LINE 86
        __M_writer(u'</div>\n<script type="text/javascript">\n  var icons = document.getElementsByClassName(\'ui-icon\')\n  for (var i = 0; i < icons.length-1; i++) {\n    icons[i].setAttribute(\'value\', \' \');\n  } \n</script>\n</body></html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context):
    context.caller_stack._push_frame()
    try:
        collection_name = context.get('collection_name', UNDEFINED)
        F_ = context.get('F_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n    <p class="fa_field">\n      <a class="ui-widget-header ui-widget-link ui-widget-button ui-corner-all" href="#">\n        <input type="submit" value="')
        # SOURCE LINE 23
        __M_writer(escape(F_('Save')))
        __M_writer(u'" />\n      </a>\n      <a class="ui-widget-header ui-widget-link ui-corner-all" href="')
        # SOURCE LINE 25
        __M_writer(escape(model_url(collection_name)))
        __M_writer(u'">\n        <span class="ui-icon ui-icon-circle-arrow-w"></span>\n        ')
        # SOURCE LINE 27
        __M_writer(escape(F_('Cancel')))
        __M_writer(u'\n      </a>\n    </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_h1(context,title,href=None):
    context.caller_stack._push_frame()
    try:
        breadcrumb = context.get('breadcrumb', UNDEFINED)
        u = context.get('u', UNDEFINED)
        n = context.get('n', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    <h1 id="header" class="ui-widget-header ui-corner-all">\n')
        # SOURCE LINE 8
        if breadcrumb:
            # SOURCE LINE 9
            __M_writer(u'        <div class="breadcrumb">\n         /')
            # SOURCE LINE 10
            __M_writer('/'.join([u and '<a href="%s">%s</a>' % (u,n.lower()) or n.lower() for u,n in breadcrumb]))
            __M_writer(u' \n        </div>\n')
        # SOURCE LINE 13
        if href:
            # SOURCE LINE 14
            __M_writer(u'        <a href="')
            __M_writer(escape(href))
            __M_writer(u'">')
            __M_writer(escape(title.title()))
            __M_writer(u'</a>\n')
            # SOURCE LINE 15
        else:
            # SOURCE LINE 16
            __M_writer(u'        ')
            __M_writer(escape(title.title()))
            __M_writer(u'\n')
        # SOURCE LINE 18
        __M_writer(u'    </h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


