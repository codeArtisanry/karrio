
import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.ninja_van.error as error
import karrio.providers.ninja_van.utils as provider_utils
import karrio.providers.ninja_van.units as provider_units
import karrio.schemas.ninja_van.rating_response as rating
import karrio.schemas.ninja_van.rating_request as ninja_van



def parse_rate_response(
    _response: lib.Deserializable[dict],
    settings: provider_utils.Settings,
) -> typing.Tuple[typing.List[models.RateDetails], typing.List[models.Message]]:
    response = _response.deserialize()

    messages = error.parse_error_response(response, settings)
    rates = [_extract_details(rate, settings) for rate in response]

    return rates, messages


def _extract_details(
    data: dict,
    settings: provider_utils.Settings,
) -> models.RateDetails:
    rate = lib.to_object(rating.RatingResponseType, data)
    return models.RateDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        service="",  # extract service from rate
        total_charge=lib.to_money(rate.data.total_fee),  # extract the rate total rate cost
        currency="",  # extract the rate pricing currency
        transit_days=0,  # extract the rate transit days
        meta=dict(
            service_name="",  # extract the rate service human readable name
        ),
    )


def rate_request(
    payload: models.RateRequest,
    settings: provider_utils.Settings,
) -> lib.Serializable:
    shipper = lib.to_address(payload.shipper)
    recipient = lib.to_address(payload.recipient)
    packages = lib.to_packages(payload.parcels)
    services = lib.to_services(payload.services, provider_units.ShippingService)
    options = lib.to_shipping_options(
        payload.options,
        package_options=packages.options,
    )

    # map data to convert karrio model to ninja_van specific type
    request = ninja_van.RatingRequestType(
        weight=packages.weight,
        service_level=services.first,
        from_location=ninja_van.LocationType(
            l1_tier_code=shipper.state_code,
            l2_tier_code=shipper.postal_code,
        ),
        to_location=ninja_van.LocationType(
            l1_tier_code=recipient.state_code,
            l2_tier_code=recipient.postal_code,
        ),
    )

    return lib.Serializable(request, lib.to_dict)
