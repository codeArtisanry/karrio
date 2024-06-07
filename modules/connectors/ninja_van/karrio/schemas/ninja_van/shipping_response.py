from attr import s
from typing import Optional, List, Dict

@s(auto_attribs=True)
class Event:
    shipper_id: int
    tracking_number: str
    shipper_order_ref_no: str
    timestamp: str
    status: str
    is_parcel_on_rts_leg: bool
    comments: Optional[str] = None
    arrived_at_origin_hub_information: Optional[Dict[str, str]] = None

@s(auto_attribs=True)
class TrackingData:
    tracking_number: str
    is_full_history_available: bool
    events: List[Event]

@s(auto_attribs=True)
class ShippingResponseType:
    data: List[TrackingData]
