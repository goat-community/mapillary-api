# mapillary-api
This repository will contain a series of scripts, that collect information from the Mapillary API

## Set of features for requests in Mapillary API 
 https://www.mapillary.com/developer/api-documentation/#traffic-signs

# Set of all features related to Germany(trafficsigns may vary depending on country) This set is for Germany
keys:
> traffic_signs (for Germany)
>> groups:
>>> regulatory
>>> information
>>> warning
>>> complementary
> objects
>> points:
>>> construction--(barrier--temporary, crosswalk-plain, driveway)
>>> marking--(descrete--(stop-line, arrow--straight, crosswalk-zebra, etc.))
>>> object--(bench, mailbox, street-light, trash-can, etc.)
> lines
>> groups:
>>> construction--(barrier--(curb, fence, etc.), flat--(parking, sidewalk, bike-lane, etc.))
>>> marking--(continious--(dashed,solid))
>>> nature--(snow, vegetation, water)

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

# Set of all objects (from images Mapillary database), (trafficsigns may vary deneding on country (this set related to Germany))
Documentation can be find here: https://www.mapillary.com/developer/api-documentation/#traffic-signs
 keys:
> traffic_signs (for Germany)
>> groups:
>>> regulatory
>>> information
>>> warning
>>> complementary
> instances
>> points:
>>> construction--(barrier--temporary, crosswalk-plain, driveway)
>>> marking--(descrete--(stop-line, arrow--straight, crosswalk-zebra, etc.))
>>> object--(bench, mailbox, street-light, trash-can, etc.)
> segmentations
>> groups:
>>> animal--(bird, ground-animal)
>>> construction--(barrier--(curb, fence, etc.), flat--(parking, sidewalk, bike-lane, etc.))
>>> marking--(continious--(dashed,solid))
>>> nature--(snow, vegetation, water, etc.)
>>> object--(bench, bike-rack, etc)

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
