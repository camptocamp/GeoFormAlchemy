==============
GeoFormAlchemy
==============

GeoFormAlchemy is an extension for `FormAlchemy <http://code.google.com/p/formalchemy/>`_ 
that makes it possible to generate forms for model classes that use the geometry types of 
`GeoAlchemy <http://www.geoalchemy.org>`_. 

Requirements
------------

Requires FormAlchemy and GeoAlchemy >=0.3.

Installation
------------

**Installing using easy_install**::

    $ easy_install geoformalchemy
    
**Manual installation for development**:

Download the source code as `archive <http://github.com/camptocamp/GeoFormAlchemy/zipball/master>`_
or clone the GIT repository::

    git clone http://github.com/camptocamp/GeoFormAlchemy.git GeoFormAlchemy
    
Then run the setup::

    cd GeoFormAlchemy/GeoFormAlchemy
    python setup.py develop

Usage in Pylons applications
----------------------------

GeoFormAlchemy includes a Paster `Pylons template <http://wiki.pylonshq.com/display/pylonsprojects/Pylons+Project+Templates>`_
that builds upon `FormAlchemy's administration interface <http://docs.formalchemy.org/ext/pylons.html>`_ 
for Pylons. 

If you want to use GeoFormAlchemy in your Pylons application, run ``paster create`` with the 
GeoFormAlchemy template::

    $ paster create -t geo_fa your_app
    [..]
    Enter admin_controller (Add formalchemy's admin controller) [False]: True
    Enter template_engine (mako/genshi/jinja2/etc: Template language) ['mako']: mako
    Enter sqlalchemy (True/False: Include SQLAlchemy 0.5 configuration) [False]: True
    [..]
    
Then the GeoFormAlchemy extension has to be activated. Open the file ``your_app/forms/__init__.py`` and
add the following lines at the end of the file::

    # [..]
    
    from geoformalchemy.base import GeometryFieldRenderer
    from geoalchemy import geometry
    FieldSet.default_renderers[geometry.Geometry] = GeometryFieldRenderer

GeoFormAlchemy is now set up and a map will be displayed in the forms for your geometry fields. Note that 
you will have to tell FormAlchemy for which model classes it should create forms. To do so import your model 
classes in the file ``your_app/model/__init__.py``. For more information please refer to the `FormAlchemy documentation
<http://docs.formalchemy.org/ext/pylons.html>`_.

Configuration
-------------

Field modifications
~~~~~~~~~~~~~~~~~~~~

The rendering of geometry fields can be customized with additional options. For example the following statement
called on the field ``the_geom`` of the custom ``FieldSet`` changes the background map (inside the file
``your_app/forms/__init__.py``)::

    Place = FieldSet(model.places.Place)
    Place.the_geom.set(options=[
        ('map_srid', 900913),
        ('base_layer', 'new OpenLayers.Layer.OSM("OSM")')
    ])

.. _geoformalchemy-options:

**The following options are available in GeoFormAlchemy:**

``default_lat`` and ``default_lon``
    If the geometry is ``None`` or when creating a new geometry, the map
    is centered at (default_lon, default_lat). Otherwise the map is centered
    at the centroid of the geometry.

``zoom``
    The zoom-level on start-up.

``map_width`` and ``map_height``
    The size of the ``DIV`` container in which the map is displayed.

``base_layer``
    The OpenLayers layer which will be used as background map, for example::
    
        ('base_layer', 'new OpenLayers.Layer.OSM("OSM")') 

``map_srid``
    If the map uses a different CRS than the geometries, the geometries will be
    reprojected to this CRS. For example::
    
        ('map_srid', 900913)

``openlayers_lib``
    The path to the OpenLayers JavaScript library, for example if ``OpenLayers.js`` is
    located at ``your_app/public/js/lib/OpenLayers.js`` use the following path::
    
        ('openlayers_lib', '/js/lib/OpenLayers.js') 

``show_map`` (default: ``True``)
    If ``show_map`` is set to ``False``, the geometry will be displayed as WKT string 
    inside a text input field.

Template files
~~~~~~~~~~~~~~~

If you want to change the look of your forms, you can modify the template files used by
FormAlchemy and GeoFormAlchemy. The template files are located in the folder 
``your_app/templates/forms``. 

GeoFormAlchemy uses the template files ``map_js.mako`` and ``map.mako``. In ``map.mako`` you can set most of the
options that you can also use as field modification. But unlike to field modifications,
the options set in the template file are used for the geometry fields of all models, whereas the options
set as field modification are only used for the field they were set on. ::

    <%
    # default configuration options that will be used when
    # no field options were set
    
    options = {}
    options['default_lon'] = 10
    options['default_lat'] = 45
    options['zoom'] = 4
    options['map_width'] = 512
    options['map_height'] = 256
    options['base_layer'] = 'new OpenLayers.Layer.WMS("WMS", "http://labs.metacarta.com/wms/vmap0", {layers: "basic"})'
    options['openlayers_lib'] = 'http://openlayers.org/api/OpenLayers.js'
    
    %>

If you want to customize the OpenLayers map, for example to add a further OpenLayers control or to add a 
second background layer, modify the file ``map_js.mako``. 
