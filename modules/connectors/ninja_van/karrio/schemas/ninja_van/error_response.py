from attr import s
from typing import Optional, List


@s(auto_attribs=True)
class ErrorType:
    code: Optional[str] = None
    message: Optional[str] = None


@s(auto_attribs=True)
class DetailErrorType:
    reason: Optional[str] = None
    field: Optional[str] = None
    message: Optional[str] = None


@s(auto_attribs=True)
class ErrorType:
    code: Optional[str] = None
    request_id: Optional[str] = None
    title: Optional[str] = None
    message: Optional[str] = None
    details: Optional[List[DetailErrorType]] = None


@s(auto_attribs=True)
class ErrorResponseType:
    error: Optional[ErrorType] = None
