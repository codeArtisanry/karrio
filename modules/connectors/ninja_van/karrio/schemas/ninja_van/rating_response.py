from attr import s
from typing import Optional

@s(auto_attribs=True)
class Data:
    total_fee: int

@s(auto_attribs=True)
class RatingResponseType:
    data: Optional[Data] = None
