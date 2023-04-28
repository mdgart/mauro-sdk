# MovieSDK documentation
## An experimental generic API to SDK class for Python with an implementation for Movies API

This package contains two classes:
The APItoSDK class provides a way to quickly create SKD based on a configuration file, the code is in core.py.
MoveSQK in an implementation for the movie API and lives is movie_sdk.


## Requirements
```Python >=3.7```

## Installation
NOTE: The package is available only in pypi test environment 

``` 
pip install requests
pip install -i https://test.pypi.org/simple/ mauro-sdk
```

## Run Tests
```
git clone git@github.com:mdgart/mauro-sdk.git
cd mauro-sdk
pipenv install
python -m unittest tests.tests
```

## Usage

Basic usage

```
from mauro_sdk.movie_sdk import MovieSDK
from mauro_sdk import resources
movie_sdk = MovieSDK("test", resources)

movie_sdk.get_all_movies()

```

### Available Methods


See the movie_sdk.py example for usage of the APItoSDK Class, the api resources are defined in resources.py, for API authentication, the API key can be an env variable or be defined in config.py.

## Limitations

- The resource paths that can be added in resources.py support just one dynamic value {id}, a possible improvement would be to use a dictionary for resource paths that allows for multiple dynamic values.
- There are no validations for the input data at the SDK level. The validation is implemented at API level, but it would be a nice addition to have custom validation at SDK level.
- The HTTP methods properly handled are GET, POST, PUT, DELETE, but the APItoSDK class can be extended to add additional methods.
- Batch processing is not supported
- The only authentications supported is Bearer token.
- "resources" is a python file, it could be a JSON document instead so it can be reused for other SDKs.

NOTE: **for this example, I'm using mockapi.io for tests**
mockapi has some limitations in the way you defined the endpoints, and is unreliable, so if you get errors during tests is probably mockapi.io that failed. In a real word implementation I would mock the API in python using https://requests-mock.readthedocs.io/en/latest/ or similar.

