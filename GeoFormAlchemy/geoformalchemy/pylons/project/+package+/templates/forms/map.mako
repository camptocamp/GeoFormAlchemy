<%
# default configuration options that will be used when
# no field options were set, e.g. with:
#
# Place = FieldSet(model.places.Place)
# Place.the_geom.set(options=[('zoom', 12), ..])

options = {}
options['map_width'] = 512
options['map_height'] = 256
options['openlayers_lib'] = 'http://openlayers.org/dev/OpenLayers.js'

%>

% if insert_libs:
<script src="${openlayers_lib or options['openlayers_lib']}"></script>
<style>
.formmap {
    border: 1px solid #ccc;
    ## temporarily fix issue addressed in openlayers ticket #1635 :
    ## http://trac.osgeo.org/openlayers/ticket/1635#comment:7
    ## (to be remove when this ticket is closed)
    position: relative;
    z-index: 0;
}

.olControlAttribution {
    bottom: 2px;
}

.olControlEditingToolbar .olControlModifyFeatureItemActive {
    background-image: url("/adminapp/images/select_feature_on.png");
}
.olControlEditingToolbar .olControlModifyFeatureItemInactive {
    background-image: url("/adminapp/images/select_feature_off.png");
}

.olControlEditingToolbar .olControlDeleteFeatureItemActive {
    background-image: url("/adminapp/images/remove_feature_on.png");
}
.olControlEditingToolbar .olControlDeleteFeatureItemInactive {
    background-image: url("/adminapp/images/remove_feature_off.png");
}
</style>
<script type="text/javascript">
    <%include file="map_js.mako" />
</script>
% endif

<div>
    ${input_field}
    <div id="map_${field_name}" class="formmap"
        style="width: ${map_width or options['map_width']}px; height: ${map_height or options['map_height']}px;"></div>
    % if run_js:
    <script>
    ${_renderer.render_runjs()}
    </script>
    % endif
    <br />
</div>
