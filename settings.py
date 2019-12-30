# DEFINE APIS FIRST HERE BY STRING NAME
#DUMMY = "Holland"
FEDEX_FREIGHT = "Fedex_Freight"

# PUT THE API HERE TO ACTIVATE IT
ACTIVE_APIS = {
#    DUMMY: "DUMMY API",
    FEDEX_FREIGHT: "FEDEX_FREIGHT API"
}

# GIVE ALL INFORMATION NEEDED FOR THE API TO WORK
# Note that "name" needs to be the same string representation that will occour in orders list.
# API_dict = {
#  "LTL1": “Averitt”,
#  "LTL2": “Estes”,
#  "LTL3": “Fedex_Freight”,
#  "LTL4": “Holland”,
#  "LTL5": “ODFL”,
#  "LTL6": “Pitt_Ohio”,
#  "LTL7": “Southeastern”,
#  "LTL8": “UPS_Freight”,
# }


FREIGHTER_APIS = {

    # DUMMY: {
    #     "module": "Freighters.gateway.dummy",
    #     "name": "DUMMY",
    #     "coneection_params": {
    #         "public_key": "monkey",
    #         "secret_key": "secret_monkey"
    #     }
    # }
    FEDEX_FREIGHT: {
        "module": "Freighters.gateway.fedex_freight",
        "name": "FEDEX_FREIGHT",
        "connection_params": {
            "key": "cpZUxVy3iTW8TG8q",
            "password": "6iFcXc8xEyRCbNQs2jtrDeS9e",
            "account_number": "510087100",
            "meter_number": "114011186",
            "use_test_server": True
        }
    }
}
