import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_rahan_ottaminen(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_ottaminen_palauttaa_true(self):
        otettu = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(otettu, True)

    def test_rahan_ottaminen_palautta_false(self):
        otettu = self.maksukortti.ota_rahaa(2000)
        self.assertEqual(otettu, False)
