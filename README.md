# AfterShip Tracking API library for Python

This library allows you to quickly and easily use the AfterShip Tracking API via Python.

For updates to this library, see our [GitHub release page](https://github.com/AfterShip/tracking-sdk-python/releases).

If you need support using AfterShip products, please contact support@aftership.com.

## Table of Contents

- [AfterShip Tracking API library for Python](#aftership-tracking-api-library-for-python)
  - [Table of Contents](#table-of-contents)
  - [Before you begin](#before-you-begin)
    - [API and SDK Version](#api-and-sdk-version)
  - [Quick Start](#quick-start)
    - [Installation](#installation)
  - [Constructor](#constructor)
    - [Example](#example)
  - [Rate Limiter](#rate-limiter)
  - [Error Handling](#error-handling)
    - [Error List](#error-list)
  - [Endpoints](#endpoints)
    - [/courier-connections](#courier-connections)
    - [/estimated-delivery-date](#estimated-delivery-date)
    - [/trackings](#trackings)
    - [/couriers](#couriers)
  - [Help](#help)
  - [License](#license)


## Before you begin

Before you begin to integrate:

- [Create an AfterShip account](https://admin.aftership.com/).
- [Create an API key](https://organization.automizely.com/api-keys).
- [Install Python](https://www.python.org/downloads/) version 3.8 or later.

### API and SDK Version

- SDK Version: 
- API Version: 2025-07

## Quick Start

### Installation
```bash
pip install aftership-tracking-sdk
```


## Constructor

Create AfterShip instance with options

| Name       | Type   | Required | Description                                                                                                                       |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| api_key    | string | ✔        | Your AfterShip API key                                                                                                            |
| auth_type  | enum   |          | Default value: `ApiKey` <br > AES authentication: `Aes` <br > RSA authentication: `Rsa`               |
| api_secret | string |          | Required if the authentication type is `auth.Aes` or `auth.Rsa`                                                           |
| domain     | string |          | AfterShip API domain. Default value: https://api.aftership.com                                                                    |
| user_agent | string |          | User-defined user-agent string, please follow [RFC9110](https://www.rfc-editor.org/rfc/rfc9110#field.user-agent) format standard. |
| proxy      | string |          | HTTP proxy URL to use for requests. <br > Default value: `null` <br > Example: `http://192.168.0.100:8888`                        |
| max_retry  | number |          | Number of retries for each request. Default value: 2. Min is 0, Max is 10.                                                        |
| timeout    | number |          | Timeout for each request in milliseconds.                                                                                         |

### Example

```python
import tracking
from tracking import exceptions, auth

try:
    sdk = tracking.Client(
        tracking.Configuration(
            api_key="YOUR_API_KEY",
            authentication_type=auth.ApiKey,
        )
    )


    result = sdk.tracking.get_tracking_by_id(
        'valid_value',
        
        
    )
    print(result)

except exceptions.InvalidOptionError:
    pass
except exceptions.InvalidApiKeyError:
    pass
except exceptions.RateLimitExceedError:
    pass
```

## Rate Limiter

See the [Rate Limit](https://www.aftership.com/docs/tracking/quickstart/rate-limit) to understand the AfterShip rate limit policy.

## Error Handling

The SDK will return an error object when there is any error during the request, with the following specification:

| Name            | Type   | Description                    |
| --------------- | ------ | ------------------------------ |
| message         | string | Detail message of the error    |
| code            | enum   | Error code enum for API Error. |
| meta_code       | number | API response meta code.        |
| status_code     | number | HTTP status code.              |
| response_body   | string | API response body.             |
| response_header | object | API response header.           |

### Error List

| code                              | meta_code       | status_code     | message |
| --------------------------------- | --------------- | --------------- | ------- |
| INVALID_REQUEST | 400 | 400 | The request was invalid or cannot be otherwise served. |
| INVALID_JSON | 4001 | 400 | Invalid JSON data. |
| TRACKING_ALREADY_EXIST | 4003 | 400 | Tracking already exists. |
| TRACKING_DOES_NOT_EXIST | 4004 | 404 | Tracking does not exist. |
| TRACKING_NUMBER_INVALID | 4005 | 400 | The value of tracking_number is invalid. |
| TRACKING_REQUIRED | 4006 | 400 | tracking object is required. |
| TRACKING_NUMBER_REQUIRED | 4007 | 400 | tracking_number is required. |
| VALUE_INVALID | 4008 | 400 | The value of [field_name] is invalid. |
| VALUE_REQUIRED | 4009 | 400 | [field_name] is required. |
| SLUG_INVALID | 4010 | 400 | The value of slug is invalid. |
| MISSING_OR_INVALID_REQUIRED_FIELD | 4011 | 400 | Missing or invalid value of the required fields for this courier. Besides tracking_number, also required: [field_name] |
| BAD_COURIER | 4012 | 400 | The error message will be one of the following:1. Unable to import shipment as the carrier is not on your approved list for carrier auto-detection. Add the carrier here: https://admin.aftership.com/settings/couriers2. Unable to import shipment as we don&#39;t recognize the carrier from this tracking number.3. Unable to import shipment as the tracking number has an invalid format.4. Unable to import shipment as this carrier is no longer supported.5. Unable to import shipment as the tracking number does not belong to a carrier in that group. |
| INACTIVE_RETRACK_NOT_ALLOWED | 4013 | 400 | Retrack is not allowed. You can only retrack an inactive tracking. |
| NOTIFICATION_REQUIRED | 4014 | 400 | notification object is required. |
| ID_INVALID | 4015 | 400 | The value of id is invalid. |
| RETRACK_ONCE_ALLOWED | 4016 | 400 | Retrack is not allowed. You can only retrack each shipment once. |
| TRACKING_NUMBER_FORMAT_INVALID | 4017 | 400 | The format of tracking_number is invalid. |
| API_KEY_INVALID | 401 | 401 | The API Key is invalid. |
| REQUEST_NOT_ALLOWED | 403 | 403 | The request is understood, but it has been refused or access is not allowed. |
| NOT_FOUND | 404 | 404 | The URI requested is invalid or the resource requested does not exist. |
| TOO_MANY_REQUEST | 429 | 429 | You have exceeded the API call rate limit. The default limit is 10 requests per second. |
| INTERNAL_ERROR | 500 | 500 | Something went wrong on AfterShip&#39;s end. |
| INTERNAL_ERROR | 502 | 502 | Something went wrong on AfterShip&#39;s end. |
| INTERNAL_ERROR | 503 | 503 | Something went wrong on AfterShip&#39;s end. |
| INTERNAL_ERROR | 504 | 504 | Something went wrong on AfterShip&#39;s end. |

## Endpoints

The AfterShip instance has the following properties which are exactly the same as the API endpoints:

- courier_connection
  - Get courier connections
  - Create courier connections
  - Get courier connection by id
  - Update courier connection by id
  - Delete courier connection by id
- estimated_delivery_date
  - Prediction for the Estimated Delivery Date
  - Batch prediction for the Estimated Delivery Date
- tracking
  - Get trackings
  - Create a tracking
  - Get a tracking by ID
  - Update a tracking by ID
  - Delete a tracking by ID
  - Retrack an expired tracking by ID
  - Mark tracking as completed by ID
- courier
  - Get couriers
  - Detect courier

### /courier-connections
**GET** /courier-connections

```python

result = sdk.courier_connection.get_courier_connections(
    
    
    
)
print(result)
```

**POST** /courier-connections

```python
req = tracking.PostCourierConnectionsRequest()


req.courier_slug = 'valid_value'


req.credentials = {}


result = sdk.courier_connection.post_courier_connections(
    
    req,
    
)
print(result)
```

**GET** /courier-connections/{id}

```python

result = sdk.courier_connection.get_courier_connections_by_id(
    'valid_value',
    
    
)
print(result)
```

**PATCH** /courier-connections/{id}

```python
req = tracking.PutCourierConnectionsByIdRequest()


req.credentials = {}


result = sdk.courier_connection.put_courier_connections_by_id(
    'valid_value',
    req,
    
)
print(result)
```

**DELETE** /courier-connections/{id}

```python

result = sdk.courier_connection.delete_courier_connections_by_id(
    'valid_value',
    
    
)
print(result)
```

### /estimated-delivery-date
**POST** /estimated-delivery-date/predict

```python
req = tracking.EstimatedDeliveryDateRequest()


req.slug = 'valid_value'


req.origin_address = tracking.EstimatedDeliveryDateRequestOriginAddress()


req.destination_address = tracking.EstimatedDeliveryDateRequestDestinationAddress()


result = sdk.estimated_delivery_date.predict(
    
    req,
    
)
print(result)
```

**POST** /estimated-delivery-date/predict-batch

```python
req = tracking.PredictBatchRequest()



result = sdk.estimated_delivery_date.predict_batch(
    
    req,
    
)
print(result)
```

### /trackings
**GET** /trackings

```python

result = sdk.tracking.get_trackings(
    
    
    
)
print(result)
```

**POST** /trackings

```python
req = tracking.CreateTrackingRequest()


req.tracking_number = 'valid_value'


result = sdk.tracking.create_tracking(
    
    req,
    
)
print(result)
```

**GET** /trackings/{id}

```python

result = sdk.tracking.get_tracking_by_id(
    'valid_value',
    
    
)
print(result)
```

**PUT** /trackings/{id}

```python
req = tracking.UpdateTrackingByIdRequest()


result = sdk.tracking.update_tracking_by_id(
    'valid_value',
    req,
    
)
print(result)
```

**DELETE** /trackings/{id}

```python

result = sdk.tracking.delete_tracking_by_id(
    'valid_value',
    
    
)
print(result)
```

**POST** /trackings/{id}/retrack

```python

result = sdk.tracking.retrack_tracking_by_id(
    'valid_value',
    
    
)
print(result)
```

**POST** /trackings/{id}/mark-as-completed

```python
req = tracking.MarkTrackingCompletedByIdRequest()



result = sdk.tracking.mark_tracking_completed_by_id(
    'valid_value',
    req,
    
)
print(result)
```

### /couriers
**GET** /couriers

```python

result = sdk.courier.get_couriers(
    
    
    
)
print(result)
```

**POST** /couriers/detect

```python
req = tracking.DetectCourierRequest()


req.tracking_number = 'valid_value'


result = sdk.courier.detect_courier(
    
    req,
    
)
print(result)
```


## Help

If you get stuck, we're here to help:

- [Issue Tracker](https://github.com/AfterShip/tracking-sdk-python/issues) for questions, feature requests, bug reports and general discussion related to this package. Try searching before you create a new issue.
- Contact AfterShip official support via support@aftership.com

## License
Copyright (c) 2025 AfterShip

Licensed under the MIT license.