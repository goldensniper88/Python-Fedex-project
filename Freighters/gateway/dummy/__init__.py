import sys
sys.path.append('../../..')
from Freighters import FREIGHTER_APIS

def get_freight_cost_quotation(**kwargs):
    """
    IMPORTANT this is not a pickup request, its only for getting the price for shipping an item.
    :param kwargs:
        REQUIRED:
            Shipping: {
                DestCity -> String
                DestZip -> integer
                Shipdate -> utc date (YY-MM-DD) this might differ from api to api
                RequestedPickupDate -> datetime.datetime.now() -> format YY-MM-DD
            }
            Customer: {
                CustomerType
                PaymentType
            }
        OPTIONAL:
            NumPieces -> integer (is this units shipped?)
            HazMat -> Default to 0/False
            ArrivalNotify -> Bool
            Liftgate  -> Bool
            ResidentialDelivery -> Bool
            Non-CommercialPickupDelivery -> Bool
            StandardLTLGuarante -> Bool
            SecurityInspectio  -> bool
    :return integer (Price quatation):
    """
    return 25



def pickup_request(**kwargs):
    """
    :param kwargs:
            REQUIRED:
                Shipping: {
                    DestCity -> String
                    DestZip -> integer
                    Shipdate -> utc date (YY-MM-DD) this might differ from api to api
                    RequestedPickupDate -> datetime.datetime.now() -> format YY-MM-DD
                }
                Customer: {
                    CustomerType
                    PaymentType
                }
            OPTIONAL:
                NumPieces -> integer (is this units shipped?)
                HazMat -> Default to 0/False
                ArrivalNotify -> Bool
                Liftgate  -> Bool
                ResidentialDelivery -> Bool
                Non-CommercialPickupDelivery -> Bool
                StandardLTLGuarante -> Bool
                SecurityInspectio  -> bool
    :return: This should return Bill-of-Lading XOR Pro number -> String.
    """
    return "12345"



# request a copy of the shipping document
# from that company, per the Bill-of-Lading or PRO number that was received in the
# function return from the pickup request.
def get_shipping_document(get_by="BOL", number=None):
    """

    :param get_by: Should be either Bill-Of-Lading or Pro number
    :param number: The corrosponding number to get_by for an order item
    :return: Save document in some folder -> then return True
    """
    return "document"


# test the shipment tracking/tracing requests
def get_shipment_trace(get_by="BOL", number=None):
    """

    :param get_by: Should be either Bill-Of-Lading or Pro number
    :param number: The corrosponding number to get_by for an order item
    :return: sorted list element, posible use json to list conversion.
    """
    return [1,2,3]