# Mapillary-API
HowTo for Mapillary-API

## STEP1: Create set of variables
### Structure of mapil_request_config.yaml
Request for each study area should be saved in form of set of variables.
```yaml
VARIABLES_SET:
  City_Name_1:
    custom_feature_set : 
      trafficsigns : ["trafficsign-1", "trafficsign-2"]
      points : ["point-1", "point-2"]
      lines : ["line-1"]

    custom_object_set :
      trafficsigns : ["trafficsign-1", "trafficsign-2"]
      instances : ["instance-1"]
      segmentations : ["segmentation-1"]
    
    min_score : 0.7
    max_score : 1

    fact : 0.035
    path : 'path_of_shapefile'
  City_Name_2:
      custom_feature_set : 
        trafficsigns : [ ...
    ....
    ....
```
### Variables 
**City_Name_1** - name of study area, it will be used as folder name for output data storage.(don't use spaces in naming)

**custom_feature_set** - set of _features_ which will be used in request to Mapillary database. _Features_ - is a real world objects placed on the Mapillary map. It could be any object detected in images, manually added in images, or added on the map.

Map features are groupped into the following layers:
>**trafficsigns** - Traffic signs that are recognized from trafficsigns detections. May vary depending on country. A traffic sign value represents a specific traffic sign type or class. The traffic sign values follow a naming convention:
{category}--{name-of-the-traffic-sign}--{appearance-group}
_Categories_ summarize the signs by their higher level type, namely: _regulatory, information, warning, complementary_. The _appearance-group_ represents variations of the same sign in different countries or regions.

>**points** - Point features that are recognized from instances detections.

>**lines** - Line features that are recognized from segmentations detections as lines. The values from lines set of values can be used.
For each study area it is neccessary create individual feature set. 

Additional information about variables could be used for request stored in mapillary official site. https://www.mapillary.com/developer/api-documentation/

Example of full feature set (trafficsigns for Germany):
``` full_feature_set
full_feature_set = {
    "trafficsigns" : ["regulatory--bicycles-only--g1","regulatory--dual-path-bicycles-and-pedestrians--g1",
                       "regulatory--dual-path-pedestrians-and-bicycles--g1",     "regulatory--end-of-dual-path-bicycles-and-pedestrians--g1", "regulatory--end-of-dual-path-pedestrians-and-bicycles--g1", "regulatory--end-of-maximum-speed-limit-10--g1", "regulatory--end-of-maximum-speed-limit-100--g",
                       "regulatory--end-of-maximum-speed-limit-120--g1", "regulatory--end-of-maximum-speed-limit-130--g1", "regulatory--end-of-maximum-speed-limit-20--g1", "regulatory--end-of-maximum-speed-limit-30--g1", "regulatory--end-of-maximum-speed-limit-40--g1", "regulatory--end-of-maximum-speed-limit-50--g1", "regulatory--end-of-maximum-speed-limit-60--g1", "regulatory--end-of-maximum-speed-limit-70--g1", 
                       "regulatory--end-of-maximum-speed-limit-80--g1", "regulatory--end-of-maximum-speed-limit-90--g1", "regulatory--end-of-no-heavy-goods-vehicles--g1", "regulatory--end-of-no-horn--g1", "regulatory--end-of-no-parking--g1", "regulatory--end-of-pedestrians-only--g1", "regulatory--end-of-prohibition--g1", "regulatory--maximum-speed-limit-10--g1", "regulatory--maximum-speed-limit-100--g1",
                       "regulatory--maximum-speed-limit-130--g1", "regulatory--maximum-speed-limit-20--g1", "regulatory--maximum-speed-limit-30--g1", "regulatory--maximum-speed-limit-40--g1", "regulatory--maximum-speed-limit-50--g1", "regulatory--maximum-speed-limit-70--g1", "regulatory--maximum-speed-limit-80--g1", "regulatory--maximum-speed-limit-90--g1", "regulatory--no-bicycles--g1", 
                       "regulatory--no-buses--g1", "regulatory--no-caravan-trailers--g1", "regulatory--no-caravans-or-caravan-trailers--g1", "regulatory--no-heavy-goods-vehicles--g1", "regulatory--no-motor-vehicles--g1", "regulatory--no-motor-vehicles-except-motorcycles--g1", "regulatory--no-parking--g1", "regulatory--no-pedestrians--g1", "regulatory--pedestrians-only--g1", "regulatory--road-closed-to-vehicles--g3", 
                       "regulatory--shared-path-pedestrians-and-bicycles--g1", "regulatory--speed-limit-zone--g1", 
                       "information--parking--g1", "information--pedestrians-crossing--g1", "information--stairs--g4", 
                       "warning--icy-road--g1", "warning--other-danger--g1", "warning--pedestrians-crossing--g1", "warning--railroad-crossing-without-barriers--g1", "warning--slippery-road-surface--g1", "warning--uneven-road--g1", 
                       "complementary--bicycles--g1", "complementary--bike-route--g1", "complementary--except-bicycles--g1", "complementary--including-bicycles-and-motorcycles--g1", "complementary--including-buses-vehicles--g1", "complementary--pedestrians-left--g1", "complementary--pedestrians-right--g1", "complementary--traffic-queues--g1"],
    "points" : ["construction--barrier--temporary", "construction--flat--crosswalk-plain", 
                "marking--discrete--crosswalk-zebra", "marking--discrete--other-marking", "marking--discrete--symbol--bicycle", "marking--discrete--text", "object--banner", "object--bench", "object--bike-rack",
                "object--catch-basin", "object--cctv-camera", "object--fire-hydrant", "object--junction-box", "object--mailbox", "object--manhole", "object--parking-meter", "object--phone-booth", "object--sign--advertisement", "object--sign--information", "object--sign--store", "object--street-light", "object--support--pole", "object--support--traffic-sign-frame",
                "object--support--utility-pole", "object--traffic-cone", "object--traffic-light--cyclists", "object--traffic-light--general-horizontal", "object--traffic-light--general-single", "object--traffic-light--general-upright", "object--traffic-light--other", "object--traffic-light--pedestrians", "object--trash-can", "object--water-valve"],
    "lines" : ["construction--barrier--curb","construction--barrier--fence", "construction--barrier--guard-rail","construction--barrier--separator", "construction--flat--bike-lane", "construction--flat--curb-cut", "construction--flat--parking", "construction--flat--rail-track", "construction--flat--road-shoulder", "construction--flat--road",
               "construction--flat--service-lane", "construction--flat--sidewalk", "construction--flat--traffic-island", "marking--continuous--dashed", "marking--continuous--solid", "nature--snow", "nature--vegetation", "nature--water"]
}
```

**custom_object_set** - set of _objects detections_ which will be used in request to Mapillary database. _An object detection_ is a semantic pixel area or point in an image. The area could indicate fire cars, fire hydrants, sky, trees, sidewalk in the image. A detection can be a polygon, a bounding box, or a point in an image.

Map object detections are groupped into the following layers:
>**trafficsigns** - Traffic signs that are recognized from trafficsigns detections. May vary depending on country. They are the same as for _features_.

>**instances** - Values can be chosen from the points value set. The same as points values in _features_.

>**segmentations** - Values can be chosen from segmentation values data set.

Additional information about variables could be used for request stored in mapillary official site. https://www.mapillary.com/developer/api-documentation/

Example of full object set (trafficsigns for Germany):
``` full_object_set
full_object_set = {
    "trafficsigns" : ["regulatory--bicycles-only--g1", "regulatory--dual-path-bicycles-and-pedestrians--g1",
                      "regulatory--dual-path-pedestrians-and-bicycles--g1", "regulatory--end-of-dual-path-bicycles-and-pedestrians--g1", 
                      "regulatory--end-of-dual-path-pedestrians-and-bicycles--g1", "regulatory--end-of-maximum-speed-limit-10--g1", "regulatory--end-of-maximum-speed-limit-100--g",
                       "regulatory--end-of-maximum-speed-limit-120--g1", "regulatory--end-of-maximum-speed-limit-130--g1", "regulatory--end-of-maximum-speed-limit-20--g1", "regulatory--end-of-maximum-speed-limit-30--g1", "regulatory--end-of-maximum-speed-limit-40--g1", "regulatory--end-of-maximum-speed-limit-50--g1", "regulatory--end-of-maximum-speed-limit-60--g1", "regulatory--end-of-maximum-speed-limit-70--g1", 
                       "regulatory--end-of-maximum-speed-limit-80--g1", "regulatory--end-of-maximum-speed-limit-90--g1", "regulatory--end-of-no-heavy-goods-vehicles--g1", "regulatory--end-of-no-horn--g1", "regulatory--end-of-no-parking--g1", "regulatory--end-of-pedestrians-only--g1", "regulatory--end-of-prohibition--g1", "regulatory--maximum-speed-limit-10--g1", "regulatory--maximum-speed-limit-100--g1",
                       "regulatory--maximum-speed-limit-130--g1", "regulatory--maximum-speed-limit-20--g1", "regulatory--maximum-speed-limit-30--g1", "regulatory--maximum-speed-limit-40--g1", "regulatory--maximum-speed-limit-50--g1", "regulatory--maximum-speed-limit-70--g1", "regulatory--maximum-speed-limit-80--g1", "regulatory--maximum-speed-limit-90--g1", "regulatory--no-bicycles--g1", 
                       "regulatory--no-buses--g1", "regulatory--no-caravan-trailers--g1", "regulatory--no-caravans-or-caravan-trailers--g1", "regulatory--no-heavy-goods-vehicles--g1", "regulatory--no-motor-vehicles--g1", "regulatory--no-motor-vehicles-except-motorcycles--g1", "regulatory--no-parking--g1", "regulatory--no-pedestrians--g1", "regulatory--pedestrians-only--g1", "regulatory--road-closed-to-vehicles--g3", 
                       "regulatory--shared-path-pedestrians-and-bicycles--g1", "regulatory--speed-limit-zone--g1", 
                       "information--parking--g1", "information--pedestrians-crossing--g1", "information--stairs--g4", 
                       "warning--icy-road--g1", "warning--other-danger--g1", "warning--pedestrians-crossing--g1", "warning--railroad-crossing-without-barriers--g1", "warning--slippery-road-surface--g1", "warning--uneven-road--g1", 
                       "complementary--bicycles--g1", "complementary--bike-route--g1", "complementary--except-bicycles--g1", "complementary--including-bicycles-and-motorcycles--g1", "complementary--including-buses-vehicles--g1", "complementary--pedestrians-left--g1", "complementary--pedestrians-right--g1", "complementary--traffic-queues--g1"],
    "instances" : ["construction--barrier--temporary", "construction--flat--crosswalk-plain", 
                   "marking--discrete--crosswalk-zebra", "marking--discrete--other-marking", "marking--discrete--symbol--bicycle", "marking--discrete--text", "object--banner", "object--bench", "object--bike-rack",
                   "object--catch-basin", "object--cctv-camera", "object--fire-hydrant", "object--junction-box", "object--mailbox", "object--manhole", "object--parking-meter", "object--phone-booth", "object--sign--advertisement", "object--sign--information", "object--sign--store", "object--street-light", "object--support--pole", "object--support--traffic-sign-frame",
                   "object--support--utility-pole", "object--traffic-cone", "object--traffic-light--cyclists", "object--traffic-light--general-horizontal", "object--traffic-light--general-single", "object--traffic-light--general-upright", "object--traffic-light--other", "object--traffic-light--pedestrians", "object--trash-can", "object--water-valve"],
    "segmentations" : ["animal--bird", "animal--ground-animal", 
                       "construction--barrier--curb", "construction--barrier--fence", "construction--barrier--guard-rail", "construction--barrier--other-barrier", "construction--barrier--separator", "construction--barrier--wall", "construction--flat--bike-lane","construction--flat--crosswalk-plain", "construction--flat--curb-cut",
                       "construction--flat--parking", "construction--flat--pedestrian-area", "construction--flat--rail-track", "construction--flat--road-shoulder", "construction--flat--road", "construction--flat--service-lane", "construction--flat--sidewalk", "construction--flat--traffic-island", "construction--structure--bridge", "construction--structure--building", 
                       "construction--structure--garage", "construction--structure--tunnel", 
                       "human--person", "human--rider--bicyclist", "human--rider--motorcyclist", "human--rider--other-rider", 
                       "marking--continuous--dashed", "marking--continuous--solid", "marking--discrete--crosswalk-zebra", "marking--discrete--other-marking", "marking--discrete--stop-line", "marking--discrete--text", 
                       "nature--beach", "nature--desert", "nature--mountain", "nature--sand", "nature--sky", "nature--snow", "nature--terrain", "nature--vegetation", "nature--water", 
                       "object--banner", "object--bench", "object--bike-rack", "object--billboard", "object--catch-basin", "object--cctv-camera", "object--fire-hydrant", "object--junction-box", "object--mailbox", "object--manhole", 
                       "object--parking-meter", "object--phone-booth", "object--pothole", "object--ramp", "object--street-light", "object--support--pole", "object--support--traffic-sign-frame", "object--support--utility-pole", "object--traffic-cone", "object--traffic-light--cyclists", "object--traffic-light--general-horizontal-back", "object--traffic-light--general-horizontal-front", 
                       "object--traffic-light--general-horizontal-side", "object--traffic-light--general-upright-back", "object--traffic-light--general-upright-front", "object--traffic-light--general-upright-side", "object--traffic-light--other-traffic-light", "object--traffic-light--pedestrians", "object--traffic-light--temporary", "object--traffic-sign--back", "object--traffic-sign--direction-back", 
                       "object--traffic-sign--direction-front", "object--traffic-sign--front", "object--traffic-sign--information-parking", "object--traffic-sign--temporary-back", "object--traffic-sign--temporary-front", "object--trash-can", "object--vehicle--bicycle", "object--vehicle--boat", "object--vehicle--bus", "object--vehicle--car", "object--vehicle--caravan", "object--vehicle--motorcycle", 
                       "object--vehicle--on-rails", "object--vehicle--other-vehicle", "object--vehicle--trailer", "object--vehicle--truck", "object--vehicle--wheeled-slow", "object--water-valve", "object--wire-group", "void--car-mount", "void--dynamic", "void--ego-vehicle", "void--ground", "void--static"
                        ]
}
```

**min_score** - Related to object detection. Minimum score of normalized probability of the object detection in image. Value in range (0, 1).Should be lower then **max_score**. Recommended value **0.7**.

**max_score** - Related to object detection. Maximum score of normalized probability of the object detection in image. Value in range (0, 1).Should be higher then **min_score**. Recommended value **1**.

**fact** - Factor for disaggregation of bounding box of study area. Maximum length of the side of the cell in the formed grid. Counted in grad. Depending on the number of requested objects and features, the saturation of the study area with them, the request can be excessively large and excessively can load the Mapillari server. To avoid this, the request area is divided into equal parts and requests are sent for each of them separately, using breaks between them. Depending on the input data, the factor should be adjusted up or down. Default value **0.035**

**path** - is a path to shapefile of study area. Should be presented without extension at the end.

### Result of request
Result file of request will be stored in folder **data/City_Name_1/..**. Inside the main directory with the name of the study area there will be two folders _features_ and _objects_ with geojson files with layer names from queries for features and objects.