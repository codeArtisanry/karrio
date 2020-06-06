from typing import List
from pypurolator.estimate_service_2_1_2 import Error
from pysoap.envelope import Fault
from purplship.core.models import Message
from purplship.core.utils.xml import Element
from .utils import Settings


def parse_error_response(response: Element, settings: Settings) -> List[Message]:
    errors = response.xpath(".//*[local-name() = $name]", name="Error")
    faults = response.xpath(".//*[local-name() = $name]", name="Fault")
    return (
        [_extract_error(node, settings) for node in errors] +
        [_extract_fault(node, settings) for node in faults]
    )


def _extract_error(error_node: Element, settings: Settings) -> Message:
    error = Error()
    error.build(error_node)
    return Message(
        code=error.Code,
        message=error.Description,
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        details=dict(AdditionalInformation=error.AdditionalInformation)
        if error.AdditionalInformation is not None
        else None,
    )


def _extract_fault(fault_node: Element, settings: Settings) -> Message:
    error = Fault()
    error.build(fault_node)
    return Message(
        code=error.faultcode,
        message=error.faultstring,
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id
    )
