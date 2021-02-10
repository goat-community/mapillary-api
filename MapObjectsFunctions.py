#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:17:06 2020

@author: Santiago
"""
def Object_Detection(bbox, values, client_id, max_score, min_score, token, layers, filename, path):
    import json, requests, os

    # create our empty geojson
    output = {"type":"FeatureCollection","features":[]}

    # define the header that will be passed to the API request--it needs to include the token to authorize access to subscription data
    header =  {"Authorization" : "Bearer {}".format(token)}
    
    # build the API call
    if layers == 'segmentations':
        url = (('https://a.mapillary.com/v3/object_detections/segmentations?client_id={}&&bbox={}&values={}&min_score={}&max_score={}&per_page=1000').format(client_id,bbox,values,min_score,max_score))
    elif layers == 'trafficsigns':
        url = (('https://a.mapillary.com/v3/object_detections/trafficsigns?client_id={}&&bbox={}&values={}&min_score={}&max_score={}&per_page=1000').format(client_id,bbox,values,min_score,max_score))
    else:
        url = (('https://a.mapillary.com/v3/object_detections/instances?client_id={}&&bbox={}&values={}&min_score={}&max_score={}&per_page=1000').format(client_id,bbox,values,min_score,max_score))

    # print the URL so we can preview it
    print(url)
                                                                                                                                                                                                                                                                                                                        
    # send the API request with the header and no timeout
    r = requests.get(url,timeout=None,headers=header)

    # if call fails, keeping trying until it succeeds with a 200 status code
    while r.status_code != 200:
        r = requests.get(url,timeout=None,headers=header)

    # get data response as a JSON and count how many features were found
    data = r.json()
    data_length = len(data['features'])

    # print number of features
    print(data_length)

    # add each feature to the empty GeoJSON we created
    for f in data['features']:
        output['features'].append(f)

    # loop through each new page and continue adding the results to the empty GeoJSON
    while data_length == 1000:
        link = r.links['next']['url']
        r = requests.get(link,timeout=None,headers=header)
        while r.status_code != 200:
            r = requests.get(url,timeout=None,headers=header)
        data = r.json()
        for f in data['features']:
            output['features'].append(f)

        # print total number of features found so far
        print("Total features: {}".format(len(output['features'])))

        # update length of data in last call to see if it still remains at 1000 (maximum) indicating a next page
        data_length = len(data['features'])

    with open((os.path.join(path, '{}.geojson'.format(filename))), 'w') as outfile:
        print('DONE')
        json.dump(output, outfile)

"""
Created on Wed Dec 23 2020

@author: gregoriiv
"""
# function returns objects from Mapillary API for given shapefile
# --variables-- #
# path - path to shapefile
# fact - factor for disaggregation boundingbox of shapefile in degrees (ex. 0.02)
# values - reference values you'd like here, separate multiple by comma, leave empty quotes to get all values from Mapillary docs
# (ex. 'regulatory--priority-road--g1') https://www.mapillary.com/developer/api-documentation/#traffic-signs
# max_score/min_score -  (ex. 0/1) percentage of object we are looking for in each image in Mapillary database
# token - token from Mapillary API for authorized request 
# layers - choose 'trafficsigns' or 'instances' or 'segmentations'

def MapillaryObjFromStudyArea(path, fact, values, client_id, min_score, max_score, token, layers, dir_feat):

    import json
    import os
    import time
    import StudyArea2Bboxes
    
    # create filename for result geojson file from 'values' variable
    filename_fin = values
    
    # create result geojson
    output_result = {"type": "FeatureCollection", "features": []}
    with open(os.path.join(dir_feat, (filename_fin + '.geojson')), 'w') as outfile:
        json.dump(output_result, outfile)

    # disaggregate bbox of shapefile to grid of bboxes
    bboxes = StudyArea2Bboxes.Shp2Bbox(path, fact)

    # filename for Mapillary request
    filename = 'request'
    # iterate through each bbox
    for bb in bboxes:
        # write geojson file with object for given bbox as request.geojson
        Object_Detection(bb, values, client_id, max_score, min_score, token, layers, filename, dir_feat)
        # open request.geojson
        with open(os.path.join(dir_feat, (filename + '.geojson'))) as r:
            request = json.load(r)
        # open result.geojson
        with open(os.path.join(dir_feat, (filename_fin + '.geojson'))) as res:
            result = json.load(res)
        # append features form request.geojson to result.geojson
        for f in request['features']:
            result['features'].append(f)
        # write down new result.geojson
        with open(os.path.join(dir_feat, (filename_fin + '.geojson')), 'w') as outfile:
            json.dump(result, outfile)
        print(filename_fin + '.UPDATED')
        # remove request.geojson
        os.remove(os.path.join(dir_feat, (filename + '.geojson')))
        # sleep for 1 minute
        #time.sleep(60) #60sec

    return print('DONE')

# fuction returns geojson with objects(from images), set of value been requested for given shapefile
def MapillaryMultiObjectsRequest(client_id, token):

    import json, os
    import yaml
    import geopandas

    #import data from config.yaml
    with open('mapil_request_config.yaml') as m:
        config = yaml.safe_load(m)
    var = config['VARIABLES_SET']

    #create directory 'data' if not exists
    for area in var:
        dir_main = os.path.join('data', area)
        if not os.path.exists(dir_main):
            os.mkdir(dir_main)
        dir_feat = os.path.join(dir_main, 'objects')
        if not os.path.exists(dir_feat):
            os.mkdir(dir_feat)
        
        #set variables from config yaml
        fact = var[area]['fact']
        path = var[area]['path']
        max_score = var[area]['max_score']
        min_score = var[area]['min_score']

        #create result files for each group of features with name of group
        for v_cat in var[area]['custom_object_set']:
            if len(var[area]['custom_object_set'][v_cat]) > 0:
                output_val_cat = {"type": "FeatureCollection", "features": []}
                with open(dir_feat + '/' + v_cat + '.geojson', 'w') as outfile:
                    json.dump(output_val_cat, outfile)

                # make request for each feature in each group
                for object_ in var[area]['custom_object_set'][v_cat]:
                    MapillaryObjFromStudyArea(path, fact, object_, client_id, min_score, max_score, token, v_cat, dir_feat)

                    # open request.geojson
                    with open(os.path.join(dir_feat, (object_ + '.geojson'))) as r:
                        request = json.load(r)
                    # open result.geojson
                    with open(os.path.join(dir_feat, (v_cat +'.geojson'))) as res:
                        result = json.load(res)
                    # append features form request.geojson to result.geojson
                    for f in request['features']:
                        result['features'].append(f)
                    # write down new result.geojson
                    with open(os.path.join(dir_feat, (v_cat +'.geojson')), 'w') as outfile:
                        json.dump(result, outfile)
                    print(v_cat +'.UPDATED')
                    # remove request.geojson
                    os.remove(os.path.join(dir_feat, (object_  + '.geojson')))

                #remove objects located outside the study area with geopandas
                #open files with objects and shapefile
                categ_gjson = geopandas.read_file(os.path.join(dir_feat, (v_cat +'.geojson')))
                st_area = geopandas.read_file(path + '.shp')
                #create mask for intersected objects and filter them
                categ_mask = categ_gjson.within(st_area.loc[0,'geometry'])
                categ_cut = categ_gjson[categ_mask]
                #remove initial geojson file and save cut one
                if categ_cut.empty:
                    pass
                else:
                    os.remove(os.path.join(dir_feat, (v_cat +'.geojson')))
                    categ_cut.to_file(os.path.join(dir_feat, (v_cat +'.geojson')), driver='GeoJSON')