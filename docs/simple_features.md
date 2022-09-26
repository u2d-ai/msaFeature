# msaFeature.simple

Simple implementation of feature flags for FastAPI. Configuration can be loaded from a json file, dict or an url/json.

## Usage
Example of msaFeature.simple:
```python
from msaFeature.simple import MSASimpleFeatureFlags, feature_flag, feature_enabled

MSASimpleFeatureFlags(conf_source="https://YOUR_URL_TO_JSON_CONFIG")
print("Enabled Features:", MSASimpleFeatureFlags.get_features())


@feature_flag("myflag_A")
def myflag_A_function():
    print("This feature should be enabled: myflag_A")

myflag_A_function()

if feature_enabled("myflag_B"):
    print("Something is wrong, this feature should be disabled: myflag_B")
else:
    print("This feature is disabled: myflag_B")
```

MSASimpleFeatureFlags can be configured and loaded from a **File with a JSON str inside**, **URL**, **Dictionary or ENV Variables**:
```python
from msaFeature.simple import MSASimpleFeatureFlags
MSASimpleFeatureFlags.load_config("https://YOUR_URL_TO_JSON_CONFIG")
MSASimpleFeatureFlags.load_config("configsfolder/my_features.json")
MSASimpleFeatureFlags.load_config({"myflag_A": True, "myflag_A": False})

MSASimpleFeatureFlags.reload_feature_flags()
```

There is also a `@feature_flag` handler to build features at runtime, defaults to False.

Function `get_features` returns a dict of all defined MSASimpleFeatureFlags. 
You can enable or disable features with `enable_feature` or `enable_feature`  

You can reload all configuration with `reload_feature_flags`, 
this clears all current features and reloads the configuration. 

There is a simple `FastAPI.router` available:
```python
from msaFeature.simple import router as simple_feature_router
from fastapi import FastAPI
app = FastAPI()
app.include_router(simple_feature_router)
```