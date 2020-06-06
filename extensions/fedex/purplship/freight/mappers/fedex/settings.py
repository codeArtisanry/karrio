"""PurplShip FedEx client settings."""

import attr
from purplship.carriers.fedex.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """FedEx connection settings."""

    user_key: str
    password: str
    meter_number: str
    account_number: str = None
    id: str = None
    test: bool = False
    carrier_id: str = "fedex_freight"
