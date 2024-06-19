# AfterShip Tracking API library for Python

This library allows you to quickly and easily use the AfterShip Tracking API via Python.

For updates to this library, see our GitHub release page.

If you need support using AfterShip products, please contact support@aftership.com.

## Table of Contents

- [AfterShip Tracking API library for Python](#aftership-tracking-api-library-for-python)
  - [Table of Contents](#table-of-contents)
  - [Before you begin](#before-you-begin)
  - [Quick Start](#quick-start)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Constructor](#constructor)
    - [Example](#example)
  - [Rate Limiter](#rate-limiter)
  - [Error Handling](#error-handling)
    - [Error List](#error-list)
  - [Endpoints](#endpoints)
    - [/trackings](#trackings)
    - [/couriers](#couriers)
    - [/last\_checkpoint](#last_checkpoint)
    - [/notifications](#notifications)
  - [Help](#help)
  - [License](#license)


## Before you begin

Before you begin to integrate:

- [Create an AfterShip account](https://admin.aftership.com/).
- [Create an API key](https://organization.automizely.com/api-keys).
- [Install Python](https://www.python.org/downloads/) version 3.8 or later.

## Quick Start

### Installation
```bash
pip install aftership-tracking-sdk
```

### Usage
```python
import tracking
from tracking import exceptions

try:
    sdk = tracking.Client(
        tracking.Configuration(
            api_key="YOUR_API_KEY",
            authentication_type=tracking.ApiKey,
        )
    )
    result = sdk.tracking.get_tracking_by_id("qshqj7p2ugqhclxlg4ef3004")
    print(result)
except exceptions.InvalidOptionError:
    pass
except exceptions.InvalidApiKeyError:
    pass
except exceptions.RateLimitExceedError:
    pass
```


## Constructor

Create AfterShip instance with options

| Name       | Type   | Required | Description                                                                                                                       |
|------------|--------|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| api_key    | string | ✔        | Your AfterShip API key                                                                                                            |
| auth_type  | enum   |          | Default value: `AuthType.API_KEY` <br > AES authentication: `AuthType.AES` <br > RSA authentication: `AuthType.RSA`               |
| api_secret | string |          | Required if the authentication type is `AuthType.AES` or `AuthType.RSA`                                                           |
| domain     | string |          | AfterShip API domain. Default value: https://api.aftership.com                                                                    |
| user_agent | string |          | User-defined user-agent string, please follow [RFC9110](https://www.rfc-editor.org/rfc/rfc9110#field.user-agent) format standard. |
| proxy      | string |          | HTTP proxy URL to use for requests. <br > Default value: `null` <br > Example: `http://192.168.0.100:8888`                        |
| max_retry  | number |          | Number of retries for each request. Default value: 2. Min is 0, Max is 10.                                                        |
| timeout    | number |          | Timeout for each request in milliseconds.                                                                                         |

### Example

```javascript
import tracking

sdk = tracking.Client(
    tracking.Configuration(
        api_key="YOUR_API_KEY",
        api_secret="YOUR_API_SECRET",
        authentication_type=tracking.Aes,
    )
)
```

## Rate Limiter

See the [Rate Limit](https://www.aftership.com/docs/aftership/quickstart/rate-limit) to understand the AfterShip rate limit policy.

## Error Handling

The SDK will return an error object when there is any error during the request, with the following specification:

| Name          | Type   | Description                    |
|---------------|--------|--------------------------------|
| message       | string | Detail message of the error    |
| code          | enum   | Error code enum for API Error. |
| meta_code     | number | API response meta code.        |
| status_code   | number | HTTP status code.              |
| response_body | string | API response body.             |


### Error List

| code                              | meta_code        | status_code     | message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 
|-----------------------------------|------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INVALID_REQUEST                   | 	400             | 	400	           | The request was invalid or cannot be otherwise served.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| INVALID_JSON                      | 	4001            | 	400	           | Invalid JSON data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| TRACKING_ALREADY_EXIST            | 	4003            | 	400	           | Tracking already exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TRACKING_DOES_NOT_EXIST           | 	4004            | 	404	           | Tracking does not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                             
| TRACKING_NUMBER_INVALID           | 	4005            | 	400	           | The value of tracking_number is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TRACKING_REQUIRED                 | 	4006            | 	400	           | tracking object is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TRACKING_NUMBER_REQUIRED          | 	4007            | 	400	           | tracking_number is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VALUE_INVALID                     | 	4008            | 	400	           | The value of [field_name] is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VALUE_REQUIRED                    | 	4009            | 	400	           | [field_name] is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SLUG_INVALID                      | 	4010            | 	400	           | The value of slug is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MISSING_OR_INVALID_REQUIRED_FIELD | 	4011            | 	400	           | Missing or invalid value of the required fields for this courier. Besides tracking_number, also required: [field_name]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| BAD_COURIER                       | 	4012            | 	400	           | The error message will be one of the following:<br/>1. Unable to import shipment as the carrier is not on your approved list for carrier auto-detection. Add the carrier here: https://admin.aftership.com/settings/couriers<br/>2. Unable to import shipment as we don’t recognize the carrier from this tracking number.<br/>3. Unable to import shipment as the tracking number has an invalid format.<br/>4. Unable to import shipment as this carrier is no longer supported.<br/>5. Unable to import shipment as the tracking number does not belong to a carrier in that group. |
| INACTIVE_RETRACK_NOT_ALLOWED      | 	4013            | 	400	           | Retrack is not allowed. You can only retrack an inactive tracking.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| NOTIFICATION_REUQIRED             | 	4014            | 	400	           | notification object is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ID_INVALID                        | 	4015            | 	400	           | The value of id is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RETRACK_ONCE_ALLOWED              | 	4016            | 	400	           | Retrack is not allowed. You can only retrack each shipment once.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TRACKING_NUMBER_FORMAT_INVALID    | 	4017            | 	400	           | The format of tracking_number is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| API_KEY_INVALID                   | 	401             | 	401	           | The API key is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| REQUEST_NOT_ALLOWED               | 	403             | 	403            | The request is understood, but it has been refused or access is not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| NOT_FOUND                         | 	404             | 	404	           | The URI requested is invalid or the resource requested does not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TOO_MANY_REQUEST                  | 	429             | 	429            | You have exceeded the API call rate limit. The default limit is 10 requests per second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| INTERNAL_ERROR	                   | 500 502 503 504	 | 500 502 503 504 | Something went wrong on AfterShip's end.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Endpoints

The AfterShip instance has the following properties which are exactly the same as the API endpoints:

courier - Get a list of our supported couriers.
tracking - Create trackings, update trackings, and get tracking results.
last_checkpoint - Get tracking information of the last checkpoint of a tracking.
notification - Get, add or remove contacts (sms or email) to be notified when the status of a tracking has changed.


### /trackings

**POST** /trackings

```python
import tracking
from tracking import exceptions

try:
    sdk = tracking.Client(
        tracking.Configuration(
            api_key="asak_da8a673f24ff4475a44defe7bd3d2de7",
            api_secret="assk_33532102503846b28e879455d0e0122e",
            authentication_type=tracking.Aes,
        )
    )
    data = tracking.TrackingCreateTrackingRequest()
    data.tracking_number = "9505513461174170617209"
    data.slug = "usps"
    result = sdk.tracking.create_tracking(data)
    print(result)
except exceptions.InvalidOptionError:
    pass
```

**DELETE** /trackings/:id

```python
sdk.tracking.delete_tracking_by_id("pugd4lue1oxtjlxlphas600f")
```

**GET** /trackings

```python
result = sdk.tracking.get_trackings(keyword="1234")
print(result)
```

**GET** /trackings/:id

```python
result = sdk.tracking.get_tracking_by_id("rft4xu2rs1um1lwhm8j1p02r")
print(result)
```

```python
# GET /trackings/:slug/:tracking_number?tracking_postal_code=:postal_code&tracking_ship_date=:ship_date
result = sdk.tracking.get_tracking_by_slug_tracking_number(slug="usps", tracking_number="9434609105464265845274")
print(result)
```


> Pro Tip: You can always use /:id to replace /:slug/:tracking_number.
```python
# GET /trackings/:id
result = sdk.tracking.get_tracking_by_id("rft4xu2rs1um1lwhm8j1p02r")
print(result)
```

**PUT** /trackings/:id

```python
data = tracking.TrackingUpdateTrackingByIdRequest()
data.note = "test"
result = sdk.tracking.update_tracking_by_id("hqhyzb21sm0colweuats7001", data)
print(result)
```

**POST** /trackings/:id/retrack

```python
result = sdk.tracking.retrack_tracking_by_id("hqhyzb21sm0colweuats7001")
print(result)
```

**POST** /trackings/:id/mark-as-completed

```python
data = tracking.MarkTrackingCompletedByIdRequest()
data.reason = "DELIVERED"
result = sdk.tracking.mark_tracking_completed_by_id("hqhyzb21sm0colweuats7001", data)
print(result)
```

### /couriers
**GET** /couriers

```python
result = sdk.courier.get_user_couriers()
print(result)
```

**GET** /couriers/all

```python
result = sdk.courier.get_all_couriers()
print(result)
```

**POST** /couriers/detect

```python
data = tracking.TrackingDetectCourierRequest()
data.tracking_number = "9434609105464265845274"
result = sdk.courier.detect_courier(data)
print(result)
```

### /last_checkpoint

**GET** /last_checkpoint/:id

```python
result = sdk.last_checkpoint.get_checkpoint_by_tracking_id("qshqj7p2ugqhclxlg4ef3004")
print(result)
```

### /notifications

**GET** /notifications/:id

```python
result = sdk.notification.get_notification_by_tracking_id("qshqj7p2ugqhclxlg4ef3004")
print(result)
```

**POST** /notifications/:id/add

```python
data = tracking.NotificationRequestV1()
data.emails = ["test@gmail.com"]
result = sdk.notification.add_notification_by_tracking_id("qshqj7p2ugqhclxlg4ef3004", data)
print(result)
```

**POST** /notifications/:id/remove

```python
data = tracking.NotificationRequestV1()
data.emails = ["123@gmail.com"]
result = sdk.notification.delete_notification_by_tracking_id("kponlnb1w64fmlxlakyln00l", data)
print(result)
```

## Help

If you get stuck, we're here to help:

- [Issue Tracker](https://github.com/AfterShip/tracking-sdk-python/issues) for questions, feature requests, bug reports and general discussion related to this package. Try searching before you create a new issue.
- Contact AfterShip official support via support@aftership.com

## License
Copyright (c) 2024 AfterShip

Licensed under the MIT license.