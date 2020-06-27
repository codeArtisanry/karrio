from enum import Enum, Flag


class PackagingType(Flag):
    eshipper_envelope = "Envelope"
    eshipper_courier_pak = "Courier Pak"
    eshipper_package = "Package"
    eshipper_pallet = "Pallet"

    """ Unified Packaging type mapping """
    envelope = eshipper_envelope
    pak = eshipper_courier_pak
    tube = eshipper_package
    pallet = eshipper_pallet
    small_box = eshipper_package
    medium_box = eshipper_package
    your_packaging = eshipper_package


class PaymentType(Flag):
    check = "Check"
    receiver = "Receiver"
    shipper = "Shipper"
    third_party = "3rd Party"

    """ Unified payment type mapping """
    sender = shipper
    recipient = receiver


class Service(Enum):
    eshipper_fedex_priority = "1" 
    eshipper_fedex_first_overnight = "2" 
    eshipper_fedex_ground = "3" 
    eshipper_fedex_standard_overnight = "28"
    eshipper_fedex_2nd_day = "29"
    eshipper_fedex_express_saver = "30"
    eshipper_purolator_air = "4" 
    eshipper_purolator_air_9_am = "5" 
    eshipper_purolator_air_10_30 = "6" 
    eshipper_puroletter = "7" 
    eshipper_puroletter_9_am = "8" 
    eshipper_puroletter_10_30 = "9" 
    eshipper_puro_pak = "10"
    eshipper_puro_pak_9_am = "11"
    eshipper_puro_pak_10_30 = "12"
    eshipper_purolator_ground = "13"
    eshipper_purolator_ground_9_am = "19"
    eshipper_purolator_ground_10_30 = "20"
    eshipper_canada_worldwide_same_day = "14"
    eshipper_canada_worldwide_next_flight_out = "15"
    eshipper_canada_worldwide_air_freight = "16"
    eshipper_canada_worldwide_ltl = "17"
    eshipper_dhl_international_express = "106" 
    eshipper_ups_express_next_day_air = "600" 
    eshipper_ups_expedited_second_day_air = "601" 
    eshipper_ups_worldwide_express = "602" 
    eshipper_ups_worldwide_expedited = "603" 
    eshipper_ups_standard_ground = "604" 
    eshipper_ups_express_early_am_next_day_air_early_am = "605" 
    eshipper_ups_three_day_select = "606" 
    eshipper_ups_saver = "607" 
    eshipper_ups_ground = "608" 
    eshipper_next_day_saver = "609" 
    eshipper_worldwide_express_plus = "610" 
    eshipper_second_day_air_am = "611" 
    eshipper_canada_post_priority = "500" 
    eshipper_canada_post_xpress_post = "501" 
    eshipper_canada_post_expedited = "502" 
    eshipper_canada_post_regular = "503" 
    eshipper_canada_post_xpress_post_usa = "504" 
    eshipper_canada_post_xpress_post_intl = "505" 
    eshipper_canada_post_air_parcel_intl = "506" 
    eshipper_canada_post_surface_parcel_intl = "507" 
    eshipper_canada_post_expedited_parcel_usa = "508" 
    eshipper_tst_ltl = "1100"
    eshipper_ltl_chicago_suburban_express = "1500"
    eshipper_ltl_fedex_freight_east = "1501"
    eshipper_ltl_fedex_freight_west = "1502"
    eshipper_ltl_mid_states_express = "1503"
    eshipper_ltl_new_england_motor_freight = "1504"
    eshipper_ltl_new_penn = "1505"
    eshipper_ltl_oak_harbor = "1506"
    eshipper_ltl_pitt_ohio = "1507"
    eshipper_ltl_r_l_carriers = "1508"
    eshipper_ltl_saia = "1509"
    eshipper_ltl_usf_reddaway = "1510"
    eshipper_ltl_vitran_express = "1511"
    eshipper_ltl_wilson_trucking = "1512"
    eshipper_ltl_yellow_transportation = "1513"
    eshipper_ltl_roadway = "1514"
    eshipper_ltl_fedex_national = "1515"
    eshipper_wilson_trucking_tfc = "1800"
    eshipper_aaa_cooper_transportation = "1801"
    eshipper_roadrunner_dawes = "1802"
    eshipper_new_england_motor_freight = "1803"
    eshipper_new_penn_motor_express = "1804"
    eshipper_dayton_freight = "1805"
    eshipper_southeastern_freightway = "1806"
    eshipper_saia_inc = "1807"
    eshipper_conway = "1808"
    eshipper_roadway = "1809"
    eshipper_usf_reddaway = "1810"
    eshipper_usf_holland = "1811"
    eshipper_dependable_highway_express = "1812"
    eshipper_day_and_ross = "1813"
    eshipper_day_and_ross_r_and_l = "1814"
    eshipper_ups = "1815"
    eshipper_aaa_cooper = "1816"
    eshipper_ama_transportation = "1817"
    eshipper_averitt_express = "1818"
    eshipper_central_freight = "1819"
    eshipper_conway_us = "1820"
    eshipper_dayton = "1821"
    eshipper_drug_transport = "1822"
    eshipper_estes = "1823"
    eshipper_land_air_express = "1824"
    eshipper_fedex_west = "1825"
    eshipper_fedex_national = "1826"
    eshipper_usf_holland_us = "1827"
    eshipper_lakeville_m_express = "1828"
    eshipper_milan_express = "1829"
    eshipper_nebraska_transport = "1830"
    eshipper_new_england = "1831"
    eshipper_new_penn = "1832"
    eshipper_a_duie_pyle = "1833"
    eshipper_roadway_us = "1834"
    eshipper_usf_reddaway_us = "1835"
    eshipper_rhody_transportation = "1836"
    eshipper_saia_motor_freight = "1837"
    eshipper_southeastern_frgt = "1838"
    eshipper_pitt_ohio = "1839"
    eshipper_ward = "1840"
    eshipper_wilson = "1841"
    eshipper_chi_cargo = "1842"
    eshipper_tax_air = "1843"
    eshipper_fedex_east = "1844"
    eshipper_central_transport = "1845"
    eshipper_roadrunner = "1846"
    eshipper_r_and_l_carriers = "1847"
    eshipper_estes_us = "1848"
    eshipper_yrc_roadway = "1849"
    eshipper_central_transport_us = "1850"
    eshipper_absolute_transportation_services = "1851"
    eshipper_blue_sky_express = "1852"
    eshipper_galasso_trucking = "1853"
    eshipper_griley_air_freight = "1854"
    eshipper_jet_transportation = "1855"
    eshipper_metro_transportation_logistics = "1856"
    eshipper_oak_harbor = "1857"
    eshipper_stream_links_express = "1858"
    eshipper_tiffany_trucking = "1859"
    eshipper_ups_freight = "1860"
    eshipper_roadrunner_us = "1861"
    eshipper_global_mail_parcel_priority = "3500"
    eshipper_global_mail_parcel_standard = "3501"
    eshipper_global_mail_packet_plus_priority = "3502"
    eshipper_global_mail_packet_priority = "3503"
    eshipper_global_mail_packet_standard = "3504"
    eshipper_global_mail_business_priority = "3505"
    eshipper_global_mail_business_standard = "3506"
    eshipper_global_mail_parcel_direct_priority = "3507"
    eshipper_global_mail_parcel_direct_standard = "3508"


class Option(Flag):
    eshipper_saturday_pickup_required = "saturdayPickupRequired"
    eshipper_homeland_security = "homelandSecurity"
    eshipper_exhibition_convention_site = "exhibitionConventionSite"
    eshipper_military_base_delivery = "militaryBaseDelivery"
    eshipper_customs_in_bond_freight = "customsIn_bondFreight"
    eshipper_limited_access = "limitedAccess"
    eshipper_excess_length = "excessLength"
    eshipper_tailgate_pickup = "tailgatePickup"
    eshipper_residential_pickup = "residentialPickup"
    eshipper_cross_border_fee = "crossBorderFee"
    eshipper_notify_recipient = "notifyRecipient"
    eshipper_single_shipment = "singleShipment"
    eshipper_tailgate_delivery = "tailgateDelivery"
    eshipper_residential_delivery = "residentialDelivery"
    eshipper_insurance_type = "insuranceType"
    eshipper_inside_delivery = "insideDelivery"
    eshipper_is_saturday_service = "isSaturdayService"
    eshipper_dangerous_goods_type = "dangerousGoodsType"
    eshipper_stackable = "stackable"


class FreightClass(Enum):
    eshipper_freight_class_50 = 50
    eshipper_freight_class_55 = 55
    eshipper_freight_class_60 = 60
    eshipper_freight_class_65 = 65
    eshipper_freight_class_70 = 70
    eshipper_freight_class_77 = 77
    eshipper_freight_class_77_5 = 77.5
    eshipper_freight_class_85 = 85
    eshipper_freight_class_92_5 = 92.5
    eshipper_freight_class_100 = 100
    eshipper_freight_class_110 = 110
    eshipper_freight_class_125 = 125
    eshipper_freight_class_150 = 150
    eshipper_freight_class_175 = 175
    eshipper_freight_class_200 = 200
    eshipper_freight_class_250 = 250
    eshipper_freight_class_300 = 300
    eshipper_freight_class_400 = 400
