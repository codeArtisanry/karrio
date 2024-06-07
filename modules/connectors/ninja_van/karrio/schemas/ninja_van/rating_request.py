from attr import s
from typing import Optional

@s(auto_attribs=True)
class LocationType:
    l1_tier_code: str
    l2_tier_code: str

@s(auto_attribs=True)
class RatingRequestType:
    weight: int
    service_level: Optional[str] = None
    from_location: Optional[LocationType] = None
    to_location: Optional[LocationType] = None
