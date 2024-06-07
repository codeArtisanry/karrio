"""Karrio Ninja Van error parser."""
import karrio.schemas.ninja_van.error_responses as ninja_van
import typing
import karrio.lib as lib
import karrio.core.models as models
import karrio.providers.ninja_van.utils as provider_utils


def parse_error_response(
    response: dict,
    settings: provider_utils.Settings,
    **kwargs,
) -> typing.List[models.Message]:
    responses = response if isinstance(response, list) else [response]
    errors: typing.List[ninja_van.ErrorResponseType] = [
        lib.to_object(ninja_van.ErrorResponseType, error)
        for error in responses
        if isinstance(error, dict) and error.get("error")
    ]

    return [
        models.Message(
            carrier_id=settings.carrier_id,
            carrier_name=settings.carrier_name,
            code=error.code,
            message=error.message,
            details={
                **kwargs,
                "details": error.details,
                "request_id": error.request_id,
                "title": error.title
            },
        )
        for error in errors
    ]
