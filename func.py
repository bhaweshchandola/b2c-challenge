import math


'''
convert given latitude or longitude in decimal to radians

input params: deg

returns coordinates in radians
'''
def deg2rad(deg):
    return float(deg) * (math.pi/180)


'''
calculate the distance between dublin
and the customer

input params: lat1, lon1 (dublin coordinates), lat2, lon2 (customer coordinates)

returns: distance between two coordinates
'''
def distanceCal(lat1, lon1, lat2, lon2):

    lat2 = float(lat2)
    lon2 = float(lon2)
    R = 6371  # radius of earth
    dlat = deg2rad(lat2-lat1)
    dlon = deg2rad(lon2-lon1)

    a = math.sin(dlat/2) * math.sin(dlat/2) + \
        math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
        math.sin(dlon/2) * math.sin(dlon/2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d


'''
sort the customers to be invited by 
their user id

input params: list of dictionaries containing customer user id and name

returns: list of dictionaries sorted by user id in ascending
'''
def sort_customers(cust_invite):

    return sorted(cust_invite, key=lambda x: x["user_id"])