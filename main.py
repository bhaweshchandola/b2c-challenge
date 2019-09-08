import json
import math
cust = open("Customers _Assignment_Coding Challenge.txt", 'r')
fir = cust.readline()
jfir = json.loads(fir)
print(type(fir))
print(type(jfir))
import pprint
pprint.pprint(jfir)
print(jfir["user_id"])


def deg2rad(deg):
    return deg * (math.pi/180)

def distanceCal(lat1, lon1, lat2, lon2):
    R = 6371 # radius of earth
    dlat = deg2rad(lat2-lat1)
    dlon = deg2rad(lon2-lon1)

    a = math.sin(dlat/2) * math.sin(dlat/2) + \
        math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
        math.sin(dlon/2) * math.sin(dlon/2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

print(distanceCal(53.339428, -6.257664, 52.986375, -6.043701))
