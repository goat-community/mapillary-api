from MapFeatures import GetFeatures
from MapSegmentations import Object_Detection
from CredentialsApi import *

bbox = '11.5486908, 48.1582993, 11.5747833, 48.1404324' #minlon, maxlat, maxlon, minlat
values = 'object--vehicle--car' # reference values you'd like here, separate multiple by comma, leave empty quotes to get all values
max_score = '0.1' #Filter detections with the maximal score (Percentage of value within the image).
min_score = '0' #Filter detections with the minimal score.
layers = 'segmentations' # choose trafficsigns or segmentations or instances
filename = 'car-0to100' #filename without extension (extension will be geojosn)

#filename = 'TUM-trash-can'

GetFeatures(bbox,values,client_id,token,layers,filename)
Object_Detection(bbox, values, client_id, max_score, min_score, token, layers,filename)
