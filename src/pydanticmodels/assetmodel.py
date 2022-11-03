from pydantic import BaseModel, Required, Field


class AssetModel(BaseModel):
    asset_name: str = Field(Required, alias='ticker', min_length=6)
