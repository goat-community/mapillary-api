
"""
Created on Tue Oct 27 11:50:33 2020

@author: Santiago
"""
def GetFeatures(bbox,values, client_id, token, layers, filename):

    import json, requests
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
    with open(finalfile, 'w') as outfile:
        print('DONE')
        json.dump(output, outfile)
    

