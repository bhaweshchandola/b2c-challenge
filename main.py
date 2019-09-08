import json
from func import distanceCal, sort_customers


dub_lat, dub_lon = (53.339428, -6.257664)
filename = "Customers _Assignment_Coding Challenge.txt"  # file with customers list
cust = open(filename, 'r')  # open file in readable format
fir = cust.readlines()  # read the content of the file into a iterable variable

customers_to_invite = []
# iterate over the customers in the file
for x in fir:
    # convert string to json
    x = json.loads(x)
    # calculate the distance between the customer and dublin
    dist = round(distanceCal(dub_lat, dub_lon, x["latitude"], x["longitude"]),2)
    if dist <= 100:
        customers_to_invite.append({"user_id": x["user_id"], "name": x["name"]})
    # print("user_id: {}, distance: {}".format(x["user_id"], dist))


pprint.pprint(sort_customers(customers_to_invite))