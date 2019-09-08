import math


def deg2rad(deg):
    return float(deg) * (math.pi/180)


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


def sort_customers(cust_invite):

    return sorted(cust_invite, key=lambda x: x["user_id"])