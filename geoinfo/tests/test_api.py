import geoip2.database
from django.test import TestCase
from ddt import ddt, data, unpack
from django.conf import settings

from geoinfo.api import country_code_from_ip


@ddt
class GeoIPTest(TestCase):

    @data(
        ("8.8.8.8", "US"),  # Google Public DNS (USA)
        ("1.1.1.1", "AU"),  # Cloudflare (Australia)
    )
    @unpack
    def test_geoip_lookup(self, ip_addr, expected_country):
        country_code = country_code_from_ip(ip_addr)
        self.assertEqual(country_code, expected_country)
