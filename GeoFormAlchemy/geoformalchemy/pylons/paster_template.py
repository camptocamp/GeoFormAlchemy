from paste.script.templates import Template

class PylonsTemplate(Template):
    _template_dir = 'project'
    required_templates = ['pylons_fa']
    summary = 'Pylons application template with GeoFormAlchemy support'
