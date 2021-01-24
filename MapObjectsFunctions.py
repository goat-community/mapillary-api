#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:17:06 2020

@author: Santiago
"""
def Object_Detection(bbox, values, client_id, max_score, min_score, token, layers, filename):
    import json, requests

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

    with open('{}.geojson'.format(filename), 'w') as outfile:
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
# layers - choose 'trafficsigns' or 'points' or 'lines'

def MapillaryObjFromStudyArea(path, fact, values, client_id, min_score, max_score, token, layers):

    import json
    import os
    import time
    import StudyArea2Bboxes
    
    # create filename for result geojson file from 'values' variable
    if type(values) == tuple:
        filename_fin = '_'.join(values)
    else:
        filename_fin = values
    
    # create result geojson
    output_result = {"type": "FeatureCollection", "features": []}
    with open(filename_fin + '.geojson', 'w') as outfile:
        json.dump(output_result, outfile)

    # disaggregate bbox of shapefile to grid of bboxes
    bboxes = StudyArea2Bboxes.Shp2Bbox(path, fact)

    # filename for Mapillary request
    filename = 'request'
    # iterate through each bbox
    for bb in bboxes:
        # write geojson file with object for given bbox as request.geojson
        Object_Detection(bb, values, client_id, max_score, min_score, token, layers, filename)
        # open request.geojson
        with open('request.geojson') as r:
            request = json.load(r)
        # open result.geojson
        with open(filename_fin + '.geojson') as res:
            result = json.load(res)
        # append features form request.geojson to result.geojson
        for f in request['features']:
            result['features'].append(f)
        # write down new result.geojson
        with open(filename_fin + '.geojson', 'w') as outfile:
            json.dump(result, outfile)
        print(filename_fin + '.UPDATED')
        # remove request.geojson
        os.remove('request.geojson')
        # sleep for 1 minute
        time.sleep(60)

    return print('DONE')
