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
    - [/trackings](#trackings)
    - [/couriers](#couriers)
    - [/courier-connections](#courier-connections)
    - [/estimated-delivery-date](#estimated-delivery-date)
  - [Help](#help)
  - [License](#license)


## Before you begin

Before you begin to integrate:

- [Create an AfterShip account](https://admin.aftership.com/).
- [Create an API key](https://organization.automizely.com/api-keys).
- [Install Python](https://www.python.org/downloads/) version 3.8 or later.

### API and SDK Version

Each SDK version is designed to work with a specific API version. Please refer to the table below to identify the supported API versions for each SDK version, ensuring you select the appropriate SDK version for the API version you intend to use.

| SDK Version | Supported API Version | Branch                                                        |
| ----------- | --------------------- | ------------------------------------------------------------- |
| 6.x.x      | 2025-04               | https://github.com/AfterShip/tracking-sdk-python/tree/2025-04 |
| 5.x.x      | 2025-01               | https://github.com/AfterShip/tracking-sdk-python/tree/2025-01 |
| 4.x.x      | 2024-10               | https://github.com/AfterShip/tracking-sdk-python/tree/2024-10 |
| 3.x.x      | 2024-07               | https://github.com/AfterShip/tracking-sdk-python/tree/2024-07 |
| 2.x.x       | 2024-04               | https://github.com/AfterShip/tracking-sdk-python/tree/2024-04 |
| <=1.x.x     | Legacy API            | https://github.com/AfterShip/aftership-sdk-python             |

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
| auth_type  | enum   |          | Default value: `auth.ApiKey` <br > AES authentication: `auth.Aes` <br > RSA authentication: `auth.Rsa`               |
| api_secret | string |          | Required if the authentication type is `auth.Aes` or `auth.Rsa`                                                           |
| domain     | string |          | AfterShip API domain. Default value: https://api.aftership.com                                                                    |
| user_agent | string |          | User-defined user-agent string, please follow [RFC9110](https://www.rfc-editor.org/rfc/rfc9110#field.user-agent) format standard. |
| proxy      | string |          | HTTP proxy URL to use for requests. <br > Default value: `null` <br > Example: `http://192.168.0.100:8888`                        |
| max_retry  | number |          | Number of retries for each request. Default value: 2. Min is 0, Max is 10.                                                        |
| timeout    | number |          | Timeout for each request in milliseconds.                                                                                         |

### Example

```python
import tracking
from tracking import exceptions
from tracking import auth

try:
    sdk = tracking.Client(
        tracking.Configuration(
            api_key="YOUR_API_KEY",
            authentication_type=auth.ApiKey,
        )
    )
    result = sdk.tracking.get_tracking_by_id("<tracking_id>")
    print(result)
except exceptions.InvalidOptionError:
    pass
except exceptions.InvalidApiKeyError:
    pass
except exceptions.RateLimitExceedError:
    pass
```

## Rate Limiter

See the [Rate Limit](https://www.aftership.com/docs/tracking/2025-04/quickstart/api-quick-start) to understand the AfterShip rate limit policy.

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

| code                              | meta_code       | status_code     | message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | --------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INVALID_REQUEST                   | 400             | 400             | The request was invalid or cannot be otherwise served.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| INVALID_JSON                      | 4001            | 400             | Invalid JSON data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| TRACKING_ALREADY_EXIST            | 4003            | 400             | Tracking already exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TRACKING_DOES_NOT_EXIST           | 4004            | 404             | Tracking does not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TRACKING_NUMBER_INVALID           | 4005            | 400             | The value of tracking_number is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TRACKING_REQUIRED                 | 4006            | 400             | tracking object is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TRACKING_NUMBER_REQUIRED          | 4007            | 400             | tracking_number is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VALUE_INVALID                     | 4008            | 400             | The value of [field_name] is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VALUE_REQUIRED                    | 4009            | 400             | [field_name] is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SLUG_INVALID                      | 4010            | 400             | The value of slug is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MISSING_OR_INVALID_REQUIRED_FIELD | 4011            | 400             | Missing or invalid value of the required fields for this courier. Besides tracking_number, also required: [field_name]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| BAD_COURIER                       | 4012            | 400             | The error message will be one of the following:<br/>1. Unable to import shipment as the carrier is not on your approved list for carrier auto-detection. Add the carrier here: https://admin.aftership.com/settings/couriers<br/>2. Unable to import shipment as we don’t recognize the carrier from this tracking number.<br/>3. Unable to import shipment as the tracking number has an invalid format.<br/>4. Unable to import shipment as this carrier is no longer supported.<br/>5. Unable to import shipment as the tracking number does not belong to a carrier in that group. |
| INACTIVE_RETRACK_NOT_ALLOWED      | 4013            | 400             | Retrack is not allowed. You can only retrack an inactive tracking.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| NOTIFICATION_REUQIRED             | 4014            | 400             | notification object is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ID_INVALID                        | 4015            | 400             | The value of id is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RETRACK_ONCE_ALLOWED              | 4016            | 400             | Retrack is not allowed. You can only retrack each shipment once.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TRACKING_NUMBER_FORMAT_INVALID    | 4017            | 400             | The format of tracking_number is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| API_KEY_INVALID                   | 401             | 401             | The API key is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| REQUEST_NOT_ALLOWED               | 403             | 403             | The request is understood, but it has been refused or access is not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| NOT_FOUND                         | 404             | 404             | The URI requested is invalid or the resource requested does not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TOO_MANY_REQUEST                  | 429             | 429             | You have exceeded the API call rate limit. The default limit is 10 requests per second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| INTERNAL_ERROR                    | 500 502 503 504 | 500 502 503 504 | Something went wrong on AfterShip's end.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Endpoints

The AfterShip instance has the following properties which are exactly the same as the API endpoints:

- courier - Get a list of our supported couriers.
- tracking - Create trackings, update trackings, and get tracking results.
- courier-connection - Create courier connections, update courier connections, and get courier connections results.
- estimated-delivery-date - Get estimated delivery date for your order.


### /trackings

**POST** /trackings

```python
import tracking
from tracking import (
    auth,
    exceptions
)

try:
    sdk = tracking.Client(
        tracking.Configuration(
            api_key="YOUR_API_KEY",
            api_secret="YOUR_API_SECRET",
            authentication_type=auth.Aes,
        )
    )
    data = tracking.CreateTrackingRequest()
    data.tracking_number = "<tracking_number>"
    data.slug = "<slug>"
    result = sdk.tracking.create_tracking(data)
    print(result)
except exceptions.InvalidOptionError:
    pass
```

**DELETE** /trackings/:id

```python
sdk.tracking.delete_tracking_by_id("<tracking_id>")
```

**GET** /trackings

```python
result = sdk.tracking.get_trackings(keyword="1234")
print(result)
```

**GET** /trackings/:id

```python
result = sdk.tracking.get_tracking_by_id("<tracking_id>")
print(result)
```

**PUT** /trackings/:id

```python
data = tracking.UpdateTrackingByIdRequest()
data.note = "test"
result = sdk.tracking.update_tracking_by_id("<tracking_id>", data)
print(result)
```

**POST** /trackings/:id/retrack

```python
result = sdk.tracking.retrack_tracking_by_id("<tracking_id>")
print(result)
```

**POST** /trackings/:id/mark-as-completed

```python
data = tracking.MarkTrackingCompletedByIdRequest()
data.reason = "DELIVERED"
result = sdk.tracking.mark_tracking_completed_by_id("<tracking_id>", data)
print(result)
```

### /couriers
**GET** /couriers

```python
result = sdk.courier.get_couriers()
print(result)
```

**POST** /couriers/detect

```python
data = tracking.DetectCourierRequest()
data.tracking_number = "<tracking_number>"
result = sdk.courier.detect_courier(data)
print(result)
```

### /courier-connections
**GET** /courier-connections

```python
result = sdk.courier_connection.get_courier_connections()
print(result)
```

**POST** /courier-connections

```python
data = tracking.PostCourierConnectionsRequest()
data.courier_slug = "dhl-api"
data.credentials = {"api_key": "<api_key>"}
result = sdk.courier_connection.post_courier_connections(data)
print(result)
```

**GET** /courier-connections/:id

```python
result = sdk.courier_connection.get_courier_connections_by_id("<courier_connection_id>")
print(result)
```

**PATCH** /courier-connections/:id

```python
data = PutCourierConnectionsByIdRequest()
data.credentials={"api_key": "<api_key>"}
result = sdk.courier_connection.put_courier_connections_by_id("<courier_connection_id>", data)
print(result)
```

**DELETE** /courier-connections/:id

```python
result = sdk.courier_connection.delete_courier_connections_by_id("<courier_connection_id>")
print(result)
```

### /estimated-delivery-date

**POST** /estimated-delivery-date/predict-batch

```python
req = tracking.PredictBatchRequest()
date = tracking.EstimatedDeliveryDateRequest()
date.slug = '<slug>'
req.estimated_delivery_dates = [date]
result = sdk.estimated_delivery_date.predict_batch(req)
print(result)
```

## Help

If you get stuck, we're here to help:

- [Issue Tracker](https://github.com/AfterShip/tracking-sdk-python/issues) for questions, feature requests, bug reports and general discussion related to this package. Try searching before you create a new issue.
- Contact AfterShip official support via support@aftership.com

## License
Copyright (c) 2025 AfterShip

Licensed under the MIT license.