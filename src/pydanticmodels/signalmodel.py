from datetime import datetime

from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Required, Field, validator, PositiveInt


class SignalModel(BaseModel):
    asset_name: str = Field(Required, alias='ticker')
    signal: int = Field(Required)
    close: Decimal = Field(Required)
    open: Decimal = Field(Required)
    high: Decimal = Field(Required)
    low: Decimal = Field(Required)
    time: datetime
    timenow: datetime
    interval: PositiveInt
    plot_0: Optional[Decimal] = Field(default=None)
    plot_1: Optional[Decimal] = Field(default=None)
    plot_2: Optional[Decimal] = Field(default=None)
    plot_3: Optional[Decimal] = Field(default=None)
    plot_4: Optional[Decimal] = Field(default=None)
    plot_5: Optional[Decimal] = Field(default=None)
    plot_6: Optional[Decimal] = Field(default=None)
    plot_7: Optional[Decimal] = Field(default=None)
    plot_8: Optional[Decimal] = Field(default=None)
    plot_9: Optional[Decimal] = Field(default=None)
    plot_10: Optional[Decimal] = Field(default=None)
    plot_11: Optional[Decimal] = Field(default=None)
    plot_12: Optional[Decimal] = Field(default=None)
    plot_13: Optional[Decimal] = Field(default=None)
    plot_14: Optional[Decimal] = Field(default=None)
    plot_15: Optional[Decimal] = Field(default=None)
    plot_16: Optional[Decimal] = Field(default=None)
    plot_17: Optional[Decimal] = Field(default=None)
    plot_18: Optional[Decimal] = Field(default=None)
    plot_19: Optional[Decimal] = Field(default=None)

    @validator('signal')
    def validate_signal(value: int) -> int:
        correct_range: list[int] = [1, -1]
        if value not in correct_range:
            raise ValueError('Error! signal must be 1 or -1')
        return value

    @validator(*[f'plot_{i}' for i in range(20)], pre=True)
    def validate_plot(value):
        if value == 'NULL':
            return None
        return value
