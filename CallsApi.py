import MapFeaturesFunctions
import MapObjectsFunctions
from CredentialsAPI import client_id, token
import os


fact = 0.035
min_score = 0.7

#path = 'F:\Hasenbergl\goat\\app\database\data\study_area'
path = 'data\\study_area\\test_st_ar'
#path = 'F:\Privat\Study\TUM\Environmental_Engineering_18.19\WiSe2021\MasterT\GOAT_SPGG\goat\\app\database\data\study_area'

#MapFeaturesFunctions.MapillaryMultiFeaturesRequest(path, fact, client_id, token)

MapObjectsFunctions.MapillaryMultiObjectsRequest(path, fact, client_id, min_score, token)
