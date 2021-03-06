from django.test import TestCase
from seed.tasks import _normalize_address_str


class NormalizeStreetAddressTest(TestCase):
    def setUp(self):
        pass

    def test_normalize_simple_address(self):
        normalized_addr = _normalize_address_str("123 Test St.")
        self.assertEqual(normalized_addr, "123 test st")

    def test_empty_address(self):
        """
        Test what happens when we try & normalize a non-existent address.
        """
        normalized_addr = _normalize_address_str(None)
        self.assertEqual(None, normalized_addr)

        normalized_addr = _normalize_address_str('')
        self.assertEqual(None, normalized_addr)

    def test_missing_number(self):
        normalized_addr = _normalize_address_str("Test St.")
        self.assertEqual(normalized_addr, "test st")

    def test_missing_street_name(self):
        normalized_addr = _normalize_address_str("123")
        self.assertEqual(normalized_addr, "123")

    def test_integer_address(self):
        normalized_addr = _normalize_address_str(123)
        self.assertEqual('123', normalized_addr)
    
    def test_strip_leading_zeros(self):
        """
        Some of the addresses we receive have leading zeros.
        E.G. 240102 N Hazel Alley might be 0000240102 N Hazel Alley
        This tests the change to _normaliz
        """
        normalized_addr = _normalize_address_str("0000123")
        self.assertEqual(normalized_addr, "123")
        
        
    def test_abbrev_street_types(self):
        """
	Catches the spelled out street types e.g., "Street" == "St"  
	"""

	normalized_addr = _normalize_address_str("STREET")
        self.assertEqual(normalized_addr, "st")
	
        normalized_addr = _normalize_address_str("Street")
        self.assertEqual(normalized_addr, "st")

	normalized_addr = _normalize_address_str("Boulevard")
        self.assertEqual(normalized_addr, "blvd")
	
        normalized_addr = _normalize_address_str("avenue")
        self.assertEqual(normalized_addr, "ave")
