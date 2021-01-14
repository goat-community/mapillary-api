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

def MappilaryObjFromStudyArea(path, fact, values, client_id, min_score, max_score, token, layers):

    import json
    import os
    import time
    import MapSegmentations
    import StudyArea2Bboxes
    
    # create filename for result geojson file from 'values' variable
    if type(values) == tuple:
        filename = '_'.join(values)
    else:
        filename = values
    
    # create result geojson
    output_result = {"type": "FeatureCollection", "features": []}
    with open(filename + '.geojson', 'w') as outfile:
        json.dump(output_result, outfile)

    # disaggregate bbox of shapefile to grid of bboxes
    bboxes = StudyArea2Bboxes.Shp2Bbox(path, fact)

    # filename for Mapillary request
    filename = 'request'
    # iterate through each bbox
    for bb in bboxes:
        # write geojson file with object for given bbox as request.geojson
        MapSegmentations.Object_Detection(bb, values, client_id, max_score, min_score, token, layers, filename)
        # open request.geojson
        with open('request.geojson') as r:
            request = json.load(r)
        # open result.geojson
        with open(filename + '.geojson') as res:
            result = json.load(res)
        # append features form request.geojson to result.geojson
        for f in request['features']:
            result['features'].append(f)
        # write down new result.geojson
        with open(filename + '.geojson', 'w') as outfile:
            json.dump(result, outfile)
        print(filename + '.UPDATED')
        # remove request.geojson
        os.remove('request.geojson')
        # sleep for 1 minute
        time.sleep(60)

    return print('DONE')