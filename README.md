# MovieSDK documentation
## A experimental generic API to SDK class for Python with an implementation for Movies API

The APItoSDK class provides a way to quickly create SKD based on a configuration file.
YOu can find the code for the class in core.py, and the implementation of the MoveSQK is in movie_sdk.py and resources.py.


## Requirements
```Python >=3.7```

## Installation
The package is available only in pypi test environment 

``` 
pip install requests
pip install --index-url https://test.pypi.org/simple/ --no-deps mauro-sdk
```

## Run Tests
```
git clone https://github.com/
cd mauro-sdk
pipenv install
python -m unittest tests.tests
```

## Usage

Basic usage

```
from mauro_sdk.movie_sdk import MovieSDK
movie_sdk = MovieSDK(api_key="test")

movie_sdk.get_all_movies()

```

### Available Methods


See the movie_sdk.py example for usage of the APItoSDK Class, the api resources are defined in resources.py, for API authentication, the API key can be an env variable or be defined in config.py.

## Limitations

- The resource paths that can be added in resources.py support just one dynamic value {id}, a possible improvement would be to use a dictionary for resource paths that requires multiple dynamic values.
- There are no validations for the input data at the SDK level, if the validation is implemented at API level, it's probably acceptable, but it would be a nice addition.
- The only HTTP methods supported are GET, POST, PUT, DELETE
- Batch processing is not supported
- The only authentications supported is Bearer token.
- "resources" is a python file, it could be a JSON document instead so it can be reused for other SDKs.

NOTE: **for this example, I'm using mockapi.io for tests**
mockapi has some limitations in the way you defined the endpoints, and is unreliable, so if you get errors during tests is probably mockapi.io that failed. In a real word implementation I would mock the API in python using https://requests-mock.readthedocs.io/en/latest/ or similar.

