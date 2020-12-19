# Function takes path of shp file and minimal length of small bbox side in grad
# returns bbox coordinates in string data format readable in Mapillary API
def Shp2Bbox(path, fact):
    import shapefile as sf
    import math

    # Function create subbboxes out of large bbox
    def sub_bboxes(fact_lon, fact_lat, wlim, slim, elim, nlim):
        bbox_list = list()
        # Divide the difference between the limits by the factor
        lat_adj_factor = (nlim - slim) / fact_lat
        lon_adj_factor = (elim - wlim) / fact_lon
        # Create longitude and latitude lists
        lat_list = []
        lon_list = []
        for i in range(fact_lon + 1):
            lon_list.append(wlim)
            wlim += lon_adj_factor
        for i in range(fact_lat + 1):
            lat_list.append(slim)
            slim += lat_adj_factor
        # Build a list of longitude and latitude pairs
        for i in range(0, len(lon_list) - 1):
            for j in range(0, len(lat_list) - 1):
                bbox_list.append(
                    [lon_list[i], lat_list[j], lon_list[i + 1], lat_list[j + 1]])
        return bbox_list

    #create return bboxes list
    bboxes = []
    #minimal area of desired small bbox
    bb_ar_fact = fact * fact
    # getting shapefile
    shpf = sf.Reader(path)
    # getting bbox
    shp_bb = shpf.bbox.tolist()
    #bbox area calculation
    bb_ar = (shp_bb[2] - shp_bb[0]) * (shp_bb[3] - shp_bb[1])
    #split bbox to smaller equal boxes
    if bb_ar > bb_ar_fact:
        fact_lat = math.ceil((shp_bb[2] - shp_bb[0]) / fact)
        fact_lon = math.ceil((shp_bb[3] - shp_bb[1]) / fact)
        bboxes_coords = sub_bboxes(fact_lon, fact_lat, shp_bb[0], shp_bb[1], shp_bb[2], shp_bb[3])
        for bb in bboxes_coords:
            bboxes.append(', '.join(str(b) for b in bb))
    else:
        bboxes.append(', '.join(str(b) for b in shp_bb))

    return bboxes