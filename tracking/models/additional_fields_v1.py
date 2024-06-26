# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

from enum import Enum, unique


@unique
class AdditionalFieldsV1(Enum):
    """
    All available additional fields

    allowed enum values
    """

    TRACKING_ACCOUNT_NUMBER = "tracking_account_number"
    TRACKING_POSTAL_CODE = "tracking_postal_code"
    TRACKING_SHIP_DATE = "tracking_ship_date"
    TRACKING_KEY = "tracking_key"
    TRACKING_ORIGIN_COUNTRY = "tracking_origin_country"
    TRACKING_DESTINATION_COUNTRY = "tracking_destination_country"
    TRACKING_STATE = "tracking_state"
