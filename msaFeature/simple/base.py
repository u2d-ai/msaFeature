import json
from typing import Union
from urllib.parse import urlparse

import httpx


class MSASimpleFeatureFlags(object):
    conf_source = None
    features = {}

    @staticmethod
    def _load_items(param_of_items):
        """internal to load items from config params"""
        for k, v in param_of_items.items():
            MSASimpleFeatureFlags.features[k] = v

    @staticmethod
    def load_config(conf_source: Union[str, dict]) -> bool:
        """Load a config from json, dict or url

        Args:
            conf_source: the source of the config (json, dict or url)

        Returns:
            ret: if load was successful, True or False
        """
        ret: bool = True
        MSASimpleFeatureFlags.features.clear()
        MSASimpleFeatureFlags.conf_source = conf_source
        try:
            if isinstance(MSASimpleFeatureFlags.conf_source, str):  # json str or url
                try:
                    check_if_ur = urlparse(MSASimpleFeatureFlags.conf_source)
                    params = httpx.get(MSASimpleFeatureFlags.conf_source).json()
                    MSASimpleFeatureFlags._load_items(params)
                except:  # it is not an url or hhtpx failed, try json
                    with open(MSASimpleFeatureFlags.conf_source, "r") as f:
                        params = json.loads(f.read())
                        MSASimpleFeatureFlags._load_items(params)
            elif isinstance(MSASimpleFeatureFlags.conf_source, dict):
                MSASimpleFeatureFlags._load_items(conf_source)
        except Exception as e:
            ret = False

        return ret

    @staticmethod
    def reload_feature_flags() -> bool:
        """Reload from the last defined config source, if it was set"""
        MSASimpleFeatureFlags.features.clear()
        if MSASimpleFeatureFlags.conf_source:
            return MSASimpleFeatureFlags.load_config(MSASimpleFeatureFlags.conf_source)
        else:
            return False

    @classmethod
    def handle_feature(cls, feature_name: str):
        """Handle a single feature"""
        features = cls.features
        if features.get(feature_name, False) is False:
            features[feature_name] = False

    @classmethod
    def get_features(cls) -> dict:
        """Get all features as dict"""
        return cls.features

    @classmethod
    def is_enabled(cls, feature_name: str) -> bool:
        """Check if feature is enabled"""
        features = cls.features
        return features.get(feature_name, False)

    @classmethod
    def enable_feature(cls, feature_name: str) -> bool:
        """Enable a feature"""
        cls.features[feature_name] = True
        return cls.features[feature_name]

    @classmethod
    def disable_feature(cls, feature_name: str) -> bool:
        """Disable a feature"""
        cls.features[feature_name] = False
        return cls.features[feature_name]


def feature_flag(feature_name: str):
    """Simple Feature Decorator"""

    def decorator(function):
        def wrapper(*args, **kwargs):
            MSASimpleFeatureFlags.handle_feature(feature_name)
            if MSASimpleFeatureFlags.is_enabled(feature_name):
                return function(*args, **kwargs)
            else:
                return True

        return wrapper

    return decorator


def feature_enabled(feature_name: str) -> bool:
    MSASimpleFeatureFlags.handle_feature(feature_name)
    return MSASimpleFeatureFlags.is_enabled(feature_name)
