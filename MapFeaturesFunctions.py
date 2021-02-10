"""
Created on Tue Oct 27 11:50:33 2020

@author: Santiago
"""
def GetFeatures(bbox, values, client_id, token, layers, filename, path):

    import json, requests, os
    # create our empty geojson
    output = {"type":"FeatureCollection","features":[]}

    # define the header that will be passed to the API request--it needs to include the token to authorize access to subscription data
    header =  {"Authorization" : "Bearer {}".format(token)}

    # build the API call
    url = ('https://a.mapillary.com/v3/map_features?layers={}&sort_by=key&client_id={}&per_page=500&values={}&bbox={}').format(layers,client_id,values,bbox)

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
    while data_length == 500:
        link = r.links['next']['url']
        r = requests.get(link,timeout=None,headers=header)
        while r.status_code != 200:
            r = requests.get(url,timeout=None,headers=header)
        data = r.json()
        for f in data['features']:
            output['features'].append(f)

        # print total number of features found so far
        print("Total features: {}".format(len(output['features'])))

        # update length of data in last call to see if it still remains at 500 (maximum) indicating a next page
        data_length = len(data['features'])
    finalfile = "%s.geojson" % filename
    with open(os.path.join(path, finalfile), 'w') as outfile:
        print('DONE')
        json.dump(output, outfile)
    
    
"""
Created on Fri Jan 08 2021

@author: gregoriiv
"""
# function returns features from Mapillary API for given shapefile
# --variables-- #
# path - path to shapefile
# fact - factor for disaggregation boundingbox of shapefile in degrees (ex. 0.02)
# values - reference values you'd like here, separate multiple by comma, leave empty quotes to get all values from Mapillary docs
# (ex. 'regulatory--priority-road--g1') https://www.mapillary.com/developer/api-documentation/#traffic-signs
# token - token from Mapillary API for authorized request 
# layers - choose 'trafficsigns' or 'points' or 'lines'

def MapillaryFeaturesFromStudyArea(path, fact, values, client_id, token, layers, dir_feat):

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
        GetFeatures(bb, values, client_id, token, layers, filename, dir_feat)
        # open request.geojson
        with open(os.path.join(dir_feat,(filename + '.geojson'))) as r:
            request = json.load(r)
        # open result.geojson
        with open(os.path.join(dir_feat, (filename_fin +'.geojson'))) as res:
            result = json.load(res)
        # append features form request.geojson to result.geojson
        for f in request['features']:
            result['features'].append(f)
        # write down new result.geojson
        with open(os.path.join(dir_feat, (filename_fin +'.geojson')), 'w') as outfile:
            json.dump(result, outfile)
        print(filename_fin +'.UPDATED')
        # remove request.geojson
        os.remove(os.path.join(dir_feat,(filename + '.geojson')))
        # sleep for 1 minute!!!
        #time.sleep(60) #60sec

    return print('DONE')


"""
Created on Sun Jan 24 2021

@author: gregoriiv
"""
# fuction returns geojson with features, set of value been requested for given shapefile 
def MapillaryMultiFeaturesRequest(client_id, token):

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
        dir_feat = os.path.join(dir_main, 'features')
        if not os.path.exists(dir_feat):
            os.mkdir(dir_feat)
 
        #set variables from config yaml
        fact = var[area]['fact']
        path = var[area]['path']

        #create result files for each group of features with name of group
        for v_cat in var[area]['custom_feature_set']:
            if len(var[area]['custom_feature_set'][v_cat]) > 0:
                output_val_cat = {"type": "FeatureCollection", "features": []}
                with open(os.path.join(dir_feat, (v_cat +'.geojson')), 'w') as outfile:
                    json.dump(output_val_cat, outfile)

                # make request for each feature in each group
                for feature in var[area]['custom_feature_set'][v_cat]:
                    MapillaryFeaturesFromStudyArea(path, fact, feature, client_id, token, v_cat, dir_feat)

                    # open request.geojson
                    with open(os.path.join(dir_feat, (feature + '.geojson'))) as r:
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
                    os.remove(os.path.join(dir_feat, (feature + '.geojson')))

                #remove features located outside the study area with geopandas
                #open files with features and shapefile
                categ_gjson = geopandas.read_file(os.path.join(dir_feat, (v_cat +'.geojson')))
                st_area = geopandas.read_file(path + '.shp')
                #create mask for intersected features and filter them
                categ_mask = categ_gjson.within(st_area.loc[0,'geometry'])
                categ_cut = categ_gjson[categ_mask]
                #remove initial geojson file and save cut one
                if categ_cut.empty:
                    pass
                else:
                    os.remove(os.path.join(dir_feat, (v_cat +'.geojson')))
                    categ_cut.to_file(os.path.join(dir_feat, (v_cat +'.geojson')), driver='GeoJSON')

