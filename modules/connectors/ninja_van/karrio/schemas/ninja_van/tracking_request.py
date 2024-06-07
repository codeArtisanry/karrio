from attr import s
from typing import Optional, List


@s(auto_attribs=True)
class TrackingRequestType:
    tracking_number: Optional[str] = None
