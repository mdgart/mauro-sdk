
# Design Decisions for APItoSDK Class

The APItoSDK class is designed to create Python SDKs to map RESTful APIs functionalities. The class is intended to be flexible and extensible, allowing users to interact with different resources provided by the API.

## Constructor

The APItoSDK constructor takes an optional `api_key` parameter. If `api_key` is not provided, the class attempts to read the API key from the `API_KEY` environment variable. If the environment variable is not set, the class attempts to read the API key from a `config` module.

If no API key is found, the constructor raises a `ValueError` to ensure that users are required to provide a valid API key before they can use the SDK.

A future improvement would be to allow to use different authentication types. Currently only Bearer token is supported.

## Resource Metadata

The APItoSDK class uses a `resources` dictionary to store metadata for each resource provided by the API. The metadata includes the resource path, the required fields for POST requests, and the allowed HTTP methods.

This design decision was made to keep the class flexible and extensible. By storing metadata for each resource in a dictionary, users can easily add or modify resources without having to modify the class code.

Since "resources" is a python file, a future improvement could be to, instead, use a JSON document instead so it can be reused for other SDKs.

## HTTP Requests

The APItoSDK class uses the `requests` module to send HTTP requests to the API. The `_send_request` method is a helper method that sends an HTTP request with the appropriate headers and data based on the `resources` dictionary. If the request is successful, the method returns a JSON payload with the response. For now it supports GET, POST, PUT, and DELETE requests, but this design makes the class extensible for future HTTP methods implementation.

## Error Handling

The APItoSDK class raises a `ValueError` if a required field is missing or an invalid HTTP method is used for a resource. The class also raises an `HTTPError` if an HTTP request fails.

This ensure that users are aware of any errors that occur when using the class. By raising specific exceptions for common error conditions, users can more easily diagnose and fix problems.

## Extensibility

The APItoSDK class is designed to be extensible, allowing users to add or modify resources without having to modify the class code. The class also allows users to pass in a custom base URL in `resources` dictionary. This way, the class can be used with a wider range of APIs.