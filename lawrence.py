#get the ids
from secret import ClientID, ClientSecret

import foursquare
client = foursquare.Foursquare(
    client_id=ClientID(), 
    client_secret=ClientSecret()
)


# 38.96001 -95.23603
# 38d 57m 46s

# 38.97265 -95.23603
# 38d 58m 22s

second =  0.00027 # just about 100 feet
min_lat =38.96001
max_lat =38.97265 
min_lon =-95.23603
max_lon =-95.23603

pos = min_lat
while pos < max_lat :
    pos = pos + second

    result = client.venues.search(
        params = {
            'll' : "%s,%s" % (pos,min_lon),
            'radius' : 100,
            'llAcc'  : 30,
        }
        )

    print result

#venues.search() ll	44.3,37.2
