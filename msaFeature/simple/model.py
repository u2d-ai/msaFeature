from pydantic import BaseModel


class MSASimpleFeature(BaseModel):
    feature_flag: str
    enabled: bool


class MSASimpleFeatureList(BaseModel):
    feature_flags: dict


class MSASimpleFeatureListReload(MSASimpleFeatureList):
    reloaded: bool
