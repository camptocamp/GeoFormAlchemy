## http://trac.openlayers.org/attachment/ticket/1882/ModifyFeature-delete.diff
OpenLayers.Control.ModifyFeature.prototype.handleKeypress = function(evt) {
        var code = evt.keyCode;
        
        // check for delete key
        if(this.feature &&
           !this.dragControl.handlers.drag.dragging &&
           OpenLayers.Util.indexOf(this.deleteCodes, code) != -1) {
            var vertex = this.dragControl.feature;
            if(vertex &&
               OpenLayers.Util.indexOf(this.vertices, vertex) != -1 &&
               vertex.geometry.parent) {
                // remove the vertex
                vertex.geometry.parent.removeComponent(vertex.geometry);
                this.layer.drawFeature(this.feature, this.standalone ?
                                       undefined :
                                       this.selectControl.renderIntent);
                this.resetVertices();
                this.setFeatureState();
                this.onModification(this.feature);
                this.layer.events.triggerEvent("featuremodified", 
                                               {feature: this.feature});
            } else {
                // if not pointing to a vertex, remove the whole feature
                var feature = this.feature;
                
                var continueRemoving = this.layer.events.triggerEvent("beforefeatureremoved", 
                                               {feature: feature});
                if (continueRemoving === false) {
                    return;
                }

                this.layer.removeFeatures([feature], {silent: true});
                feature.state = OpenLayers.State.DELETE;
                this.layer.events.triggerEvent("featureremoved", 
                                           {feature: feature});
                this.unselectFeature(feature);
            }
        }
    };

var geoformalchemy = {};
geoformalchemy.init_map = function (
        field_name,
        read_only,
        is_collection,
        geometry_type,
        lon,
        lat,
        zoom,
        base_layer,
        wkt
                           ) {    
    var map, layer, vlayer, panelControls;
    var geometry_field = document.getElementById(field_name);
    var wkt_parser = new OpenLayers.Format.WKT();
    
    layer = base_layer;
    vlayer = new OpenLayers.Layer.Vector("Geometries");
    
    if (read_only) {
        // in read-mode, only show navigation control
        panelControls = [new OpenLayers.Control.Navigation()];
    } else {
        /**
         * When the geometry of a feature changes, then the WKT string of
         * this feature has to be written to a input field. So that
         * when the form is submitted, the data can be read from this
         * input field.
         */
        var update_geometry_field = function (feature) {
            var wkt = null;
            if (feature === null || 
                    ((feature instanceof Array) && (feature.length <= 0))) {
                wkt = '';
            } else {
                wkt = wkt_parser.write(feature);
            }
            geometry_field.value = wkt;
        };
        
        /**
         * Creates an array containing all features of
         * the vector layer. OpenLayers can not create 
         * WKT string from a GeometryCollection, so that's
         * why we are constructing an array of Geometries.
         */
        var get_feature_collection = function () {
            var collection_feature = [];
            for (var i = 0; i < vlayer.features.length; i++) {
                collection_feature.push(vlayer.features[i]);
            }
            return collection_feature;
        };
        
        /**
         * When a features is modified, update the geometry field.
         */
        var feature_modified_handler = function (event) {
            var features = null;
            if (is_collection) {
                features = get_feature_collection();
            } else {
                if (event.feature.state !== OpenLayers.State.DELETE) {
                    features = event.feature;
                }
            }
            update_geometry_field(features);
        };
        
        /**
         * When a features is added, update the geometry field. If the geometry
         * type is 'Collection', construct an array of the already existing 
         * features and add the new feature to this array.
         */
        var before_feature_added_handler = function (event) {
            if (is_collection) {
                var collection_feature = get_feature_collection();
                //collection_feature.push(event.feature);

                update_geometry_field(collection_feature);

                return true;
            } else if (vlayer.features.length > 1) {
                // remove old feature(s)
                var old_features = [vlayer.features[0]];
                vlayer.removeFeatures(old_features);
                vlayer.destroyFeatures(old_features);
            }

            update_geometry_field(event.feature);

            return true;
        };
        
        vlayer.events.on({"featuremodified": feature_modified_handler});
        vlayer.events.on({"beforefeatureadded": before_feature_added_handler});
        vlayer.events.on({"afterfeaturemodified": feature_modified_handler});
        
        panelControls = [new OpenLayers.Control.Navigation()];
        
        if (geometry_type === 'Polygon' || geometry_type === 'Collection') {
            panelControls.push(new OpenLayers.Control.DrawFeature(vlayer,
                     OpenLayers.Handler.Polygon,
                     {'displayClass': 'olControlDrawFeaturePolygon'}));
        }    

        
        if (geometry_type === 'Point' || geometry_type === 'Collection') {
            panelControls.push(new OpenLayers.Control.DrawFeature(vlayer,
                     OpenLayers.Handler.Point,
                     {'displayClass': 'olControlDrawFeaturePoint'}));
        }  
        

        
        if (geometry_type === 'Path' || geometry_type === 'Collection') {
            panelControls.push(new OpenLayers.Control.DrawFeature(vlayer,
                     OpenLayers.Handler.Path,
                     {'displayClass': 'olControlDrawFeaturePath'}));
        }  
        
        var controlModifyFeature = new OpenLayers.Control.ModifyFeature(vlayer,
                {'displayClass': 'olControlModifyFeature'});
        panelControls.push(controlModifyFeature);
    }
    
    map = new OpenLayers.Map('map_' + field_name);
    
    var toolbar = new OpenLayers.Control.Panel({
        displayClass: 'olControlEditingToolbar',
        defaultControl: panelControls[0]
    });
    toolbar.addControls(panelControls);
    map.addControl(toolbar);

    map.addLayers([layer, vlayer]);

    // try to get the geometry
    if (wkt !== '') {
        var features = wkt_parser.read(wkt);
        if (!(features instanceof Array)) {
            features = [features];
        }
        vlayer.addFeatures(features, {'silent': true});
        
        /* OpenLayers creates an array of features when the WKT string 
         * represents a GeometryCollection. To get the centroid of all
         * features, we have to create a 'real' GeometryCollection.
         */
        var geometry_collection = new OpenLayers.Geometry.Collection();
        for (var i = 0; i < features.length; i++) {
            geometry_collection.addComponents(features[i].geometry);
        }
        var centroid = geometry_collection.getCentroid();
        
        map.setCenter(new OpenLayers.LonLat(centroid.x, centroid.y), zoom);
    } else {
        map.setCenter(new OpenLayers.LonLat(lon, lat), zoom);
    }   
};
