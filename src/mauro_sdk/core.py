import os
import requests
from . import config

##########################################################################################
# The APItoSDK class is a generic wrapper, that can be configured for any REST APIs
# using the data in resources.py and config.py
#
# It provides methods for interacting with the API.
# The constructor takes an optional API key as an argument.
# If the API key is not provided, it will look for it in the environment variables.
##########################################################################################

class APItoSDK:
    """
    APItoSDK: A class that provides a simple interface for accessing a RESTful API using an API key. It supports the standard CRUD operations (Create, Read, Update, and Delete) for a set of resources defined by the API. 

    Usage:
        - Instantiate the APItoSDK class with an API key, which can be passed as an argument or read from the environment variable "API_KEY". The base URL and the list of resources are hardcoded in the config file, but they can be made configurable by passing them as arguments to the constructor or setting them as environment variables.
        - Use the provided methods to interact with the API:
            - get_all: returns all resources of a given type.
            - get_by_id: returns a single resource of a given type by ID.
            - create: creates a new resource of a given type.
            - update: updates an existing resource of a given type by ID.
            - delete: deletes an existing resource of a given type by ID.

    Attributes:
        - api_key: a string representing the API key used to authenticate requests.
        - base_url: a string representing the base URL of the API.
        - resources: a dictionary mapping resource names to resource metadata. The metadata includes the path to the resource and an optional list of required fields for POST.

    Methods:
        - _send_request: a private helper method that sends an HTTP request to the API.
        - _build_url: a private helper method that builds the URL for a resource.
        - _get_required_fields: a private helper method that returns the list of required fields for a resource.
        - _get_http_methods: a private helper method that returns the list of allowed HTTP methods for a resource.
        - _check_http_method: a private helper method that checks if a given HTTP method is allowed for a resource.
        - get_all: a public method that returns all resources of a given type.
        - get_by_id: a public method that returns a single resource of a given type by ID.
        - create: a public method that creates a new resource of a given type.
        - update: a public method that updates an existing resource of a given type by ID.
        - delete: a public method that deletes an existing resource of a given type by ID.

    """
    def __init__(self, api_key=None, resources=None):
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if not api_key:
            api_key = config.API_KEY
        if not api_key:
            # the API key is required
            raise ValueError("API key not provided")
        self.api_key = api_key

        # The base URL is hardcoded in the config file for this example,
        # but we could make it configurable
        # by passing it in as an argument to the constructor
        # or by setting it as an environment variable.
        self.base_url = resources.BASE_URL

        # The resources dictionary maps resource names to resource metadata.
        # The metadata includes the path to the resource and an optional list of required fields for POST.
        # It also includes the HTTP method that should be used for each operation.
        # This is not strictly necessary, but it makes the code a little easier to read.
        self.resources = resources.RESOURCES

    # The _send_request method is a helper method that sends an HTTP request to the API.
    def _send_request(self, method, url, data=None):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        if data is not None:
            headers["Content-Type"] = "application/json"
        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    # The _build_url method is a helper method that builds the URL for a resource.
    def _build_url(self, resource_name, resource_id=None):
        resource = self.resources[resource_name]
        path = resource["path"]
        if resource_id is not None:
            path = path.format(id=resource_id)
        return f"{self.base_url}{path}"

    # The _get_required_fields method is a helper method that returns the list of required fields for a resource.
    def _get_required_fields(self, resource_name):
        return self.resources[resource_name].get("required_fields", [])

    # The _get_http_methods method is a helper method that returns the list of allowed HTTP methods for a resource.
    def _get_http_methods(self, resource_name):
        return self.resources[resource_name].get("http_methods", [])

    # The _check_http_method method is a helper method that checks if a given HTTP method is allowed for a resource.
    def _check_http_method(self, resource_name, method):
        if not method in self._get_http_methods(resource_name):
            raise ValueError(
                f"HTTP method {method} not allowed for {resource_name}")

    # The get_all method returns all resources of a given type.      
    def get_all(self, resource_name):
        self._check_http_method(resource_name, "GET")
        url = self._build_url(resource_name)
        return self._send_request("GET", url)

    # The get_by_id method returns a single resource of a given type by ID.
    def get_by_id(self, resource_name, resource_id):
        self._check_http_method(resource_name, "GET")
        url = self._build_url(resource_name, resource_id)
        return self._send_request("GET", url)

    # The create method creates a new resource of a given type.
    # required_fields is a optional list of required fields for POST.
    def create(self, resource_name, fields, resource_id=None):
        self._check_http_method(resource_name, "POST")
        required_fields = self._get_required_fields(resource_name)
        if not all(field in fields for field in required_fields):
            raise ValueError(
                f"Missing required fields: {', '.join(required_fields)}")
        url = self._build_url(resource_name, resource_id)
        data = fields
        response = self._send_request("POST", url, data)
        return response

    # The update method updates an existing resource of a given type by ID.
    def update(self, resource_name, resource_id, fields):
        self._check_http_method(resource_name, "PUT")
        url = self._build_url(resource_name, resource_id)
        data = fields
        return self._send_request("PUT", url, data)
    
    # The delete method deletes an existing resource of a given type by ID.
    def delete(self, resource_name, resource_id):
        self._check_http_method(resource_name, "DELETE")
        url = self._build_url(resource_name, resource_id)
        return self._send_request("DELETE", url)
