# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

__all__ = [
    "AdditionalFieldsV1",
    "AftershipEstimatedDeliveryDateTracking",
    "CarbonEmissionsTracking",
    "Checkpoint",
    "CoordinateCheckpoint",
    "Courier",
    "CourierResponseV1",
    "CustomEstimatedDeliveryDateTracking",
    "CustomFieldsTrackingUpdateTrackingBySlugTrackingNumberRequest",
    "DataCourierResponseV1",
    "DataNotificationResponseV1",
    "DataTrackingDeleteResponseV1",
    "DataTrackingResponseGetMultipleV1",
    "DataTrackingResponseV1",
    "DestinationAddressEstimatedDeliveryDateRequest",
    "DestinationAddressEstimatedDeliveryDateResponse",
    "DetectCourierResponse",
    "EstimatedDeliveryDateRequest",
    "EstimatedDeliveryDateResponse",
    "EstimatedPickupEstimatedDeliveryDateRequest",
    "EstimatedPickupEstimatedDeliveryDateResponse",
    "EventsCheckpoint",
    "FirstEstimatedDeliveryTracking",
    "GetAllCouriersResponse",
    "GetCheckpointBySlugTrackingNumberResponse",
    "GetCheckpointByTrackingIdResponse",
    "GetTrackingsResponse",
    "GetUserCouriersResponse",
    "LatestEstimatedDeliveryTracking",
    "MarkTrackingCompletedByIdRequest",
    "MarkTrackingCompletedBySlugTrackingNumberRequest",
    "MetaV1",
    "NextCouriersTracking",
    "NextCouriersTrackingCreateTrackingRequest",
    "Notification",
    "NotificationRequestV1",
    "NotificationResponseV1",
    "OrderProcessingTimeEstimatedPickupEstimatedDeliveryDateRequest",
    "OrderProcessingTimeEstimatedPickupEstimatedDeliveryDateResponse",
    "OriginAddressEstimatedDeliveryDateRequest",
    "OriginAddressEstimatedDeliveryDateResponse",
    "Pagination",
    "PartialDeleteTracking",
    "PartialUpdateTracking",
    "PredictBatchRequest",
    "PredictBatchResponse",
    "ReasonEventsCheckpoint",
    "SlugGroupV1",
    "TagV1",
    "Tracking",
    "TrackingCreateTrackingRequest",
    "TrackingDeleteResponseV1",
    "TrackingDetectCourierRequest",
    "TrackingResponseGetMultipleV1",
    "TrackingResponseV1",
    "TrackingUpdateTrackingByIdRequest",
    "TrackingUpdateTrackingBySlugTrackingNumberRequest",
    "WeightEstimatedDeliveryDateRequest",
    "WeightEstimatedDeliveryDateResponse",
]

from .additional_fields_v1 import AdditionalFieldsV1
from .aftership_estimated_delivery_date_tracking import AftershipEstimatedDeliveryDateTracking
from .carbon_emissions_tracking import CarbonEmissionsTracking
from .checkpoint import Checkpoint
from .coordinate_checkpoint import CoordinateCheckpoint
from .courier import Courier
from .courier_response_v1 import CourierResponseV1
from .custom_estimated_delivery_date_tracking import CustomEstimatedDeliveryDateTracking
from .custom_fields_tracking_update_tracking_by_slug_tracking_number_request import (
    CustomFieldsTrackingUpdateTrackingBySlugTrackingNumberRequest,
)
from .data_courier_response_v1 import DataCourierResponseV1
from .data_notification_response_v1 import DataNotificationResponseV1
from .data_tracking_delete_response_v1 import DataTrackingDeleteResponseV1
from .data_tracking_response_get_multiple_v1 import DataTrackingResponseGetMultipleV1
from .data_tracking_response_v1 import DataTrackingResponseV1
from .destination_address_estimated_delivery_date_request import (
    DestinationAddressEstimatedDeliveryDateRequest,
)
from .destination_address_estimated_delivery_date_response import (
    DestinationAddressEstimatedDeliveryDateResponse,
)
from .detect_courier_response import DetectCourierResponse
from .estimated_delivery_date_request import EstimatedDeliveryDateRequest
from .estimated_delivery_date_response import EstimatedDeliveryDateResponse
from .estimated_pickup_estimated_delivery_date_request import (
    EstimatedPickupEstimatedDeliveryDateRequest,
)
from .estimated_pickup_estimated_delivery_date_response import (
    EstimatedPickupEstimatedDeliveryDateResponse,
)
from .events_checkpoint import EventsCheckpoint
from .first_estimated_delivery_tracking import FirstEstimatedDeliveryTracking
from .get_all_couriers_response import GetAllCouriersResponse
from .get_checkpoint_by_slug_tracking_number_response import (
    GetCheckpointBySlugTrackingNumberResponse,
)
from .get_checkpoint_by_tracking_id_response import GetCheckpointByTrackingIdResponse
from .get_trackings_response import GetTrackingsResponse
from .get_user_couriers_response import GetUserCouriersResponse
from .latest_estimated_delivery_tracking import LatestEstimatedDeliveryTracking
from .mark_tracking_completed_by_id_request import MarkTrackingCompletedByIdRequest
from .mark_tracking_completed_by_slug_tracking_number_request import (
    MarkTrackingCompletedBySlugTrackingNumberRequest,
)
from .meta_v1 import MetaV1
from .next_couriers_tracking import NextCouriersTracking
from .next_couriers_tracking_create_tracking_request import (
    NextCouriersTrackingCreateTrackingRequest,
)
from .notification import Notification
from .notification_request_v1 import NotificationRequestV1
from .notification_response_v1 import NotificationResponseV1
from .order_processing_time_estimated_pickup_estimated_delivery_date_request import (
    OrderProcessingTimeEstimatedPickupEstimatedDeliveryDateRequest,
)
from .order_processing_time_estimated_pickup_estimated_delivery_date_response import (
    OrderProcessingTimeEstimatedPickupEstimatedDeliveryDateResponse,
)
from .origin_address_estimated_delivery_date_request import (
    OriginAddressEstimatedDeliveryDateRequest,
)
from .origin_address_estimated_delivery_date_response import (
    OriginAddressEstimatedDeliveryDateResponse,
)
from .pagination import Pagination
from .partial_delete_tracking import PartialDeleteTracking
from .partial_update_tracking import PartialUpdateTracking
from .predict_batch_request import PredictBatchRequest
from .predict_batch_response import PredictBatchResponse
from .reason_events_checkpoint import ReasonEventsCheckpoint
from .slug_group_v1 import SlugGroupV1
from .tag_v1 import TagV1
from .tracking import Tracking
from .tracking_create_tracking_request import TrackingCreateTrackingRequest
from .tracking_delete_response_v1 import TrackingDeleteResponseV1
from .tracking_detect_courier_request import TrackingDetectCourierRequest
from .tracking_response_get_multiple_v1 import TrackingResponseGetMultipleV1
from .tracking_response_v1 import TrackingResponseV1
from .tracking_update_tracking_by_id_request import TrackingUpdateTrackingByIdRequest
from .tracking_update_tracking_by_slug_tracking_number_request import (
    TrackingUpdateTrackingBySlugTrackingNumberRequest,
)
from .weight_estimated_delivery_date_request import WeightEstimatedDeliveryDateRequest
from .weight_estimated_delivery_date_response import WeightEstimatedDeliveryDateResponse
