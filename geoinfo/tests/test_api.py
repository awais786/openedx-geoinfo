"""Unit tests checking method directly for the given ip"""

from django.test import TestCase
from ddt import ddt, data, unpack

from geoinfo.api import country_code_from_ip


@ddt
class GeoIPTest(TestCase):

    @data(
        ("8.8.8.8", "US"),
        ("116.58.86.0", "PK")
    )
    @unpack
    def test_country_code_from_ip(self, ip_addr, expected_country):
        country_code = country_code_from_ip(ip_addr)
        self.assertEqual(country_code, expected_country)
