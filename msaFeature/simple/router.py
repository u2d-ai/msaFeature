from fastapi import APIRouter
from starlette.responses import JSONResponse

from . import MSASimpleFeatureFlags
from .model import (MSASimpleFeature, MSASimpleFeatureList,
                    MSASimpleFeatureListReload)

router = APIRouter(prefix="/feature", tags=["feature"], include_in_schema=True)


@router.get("/all", response_model=MSASimpleFeatureList, response_class=JSONResponse)
def show_feature_flags() -> MSASimpleFeatureList:
    """
    Return all defined feature flags
    Returns:
        dict
    """
    features: MSASimpleFeatureList = MSASimpleFeatureList(
        feature_flags=MSASimpleFeatureFlags.get_features()
    )
    return features


@router.get(
    "/enable/{feature_flag}",
    response_model=MSASimpleFeature,
    response_class=JSONResponse,
)
def enable_feature_flag(feature_flag: str) -> MSASimpleFeature:
    """Enable a feature flag

    Args:
        feature_flag: the flag to disable

    Returns:
        MSASimpleFeature
    """
    feature_status = MSASimpleFeatureFlags.enable_feature(feature_flag)
    feature: MSASimpleFeature = MSASimpleFeature(
        feature_flag=feature_flag, feature_status=feature_status
    )
    return feature


@router.get(
    "/disable/{feature_flag}",
    response_model=MSASimpleFeature,
    response_class=JSONResponse,
)
def disable_feature_flag(feature_flag: str) -> MSASimpleFeature:
    """Disable a feature flag

    Args:
        feature_flag: the flag to disable

    Returns:
        MSASimpleFeature
    """
    feature_status = MSASimpleFeatureFlags.disable_feature(feature_flag)
    feature: MSASimpleFeature = MSASimpleFeature(
        feature_flag=feature_flag, feature_status=feature_status
    )
    return feature


@router.get("/reload")
def reload_feature_flags() -> MSASimpleFeatureListReload:
    """Reload feature flags from loaded configuration

    Returns:
        MSASimpleFeatureList
    """
    reload_status = MSASimpleFeatureFlags.reload_feature_flags()
    features: MSASimpleFeatureListReload = MSASimpleFeatureListReload(
        feature_flags=MSASimpleFeatureFlags.get_features(), reloaded=reload_status
    )
    return features
