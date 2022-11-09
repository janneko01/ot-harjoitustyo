import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_oikea_edullisten_lounaiden_maara(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_oikea_maukkaiden_lounaiden_maara(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_kateisella(self):
        osto = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(osto, 0)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaan_lounaan_osto_kateisella(self):
        osto = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(osto, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullisen_lounaan_osto_kateisella_liian_vahan_rahaa(self):
        osto = self.kassapaate.syo_edullisesti_kateisella(40)
        self.assertEqual(osto, 40)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_osto_kateisella_liian_vahan_rahaa(self):
        osto = self.kassapaate.syo_maukkaasti_kateisella(40)
        self.assertEqual(osto, 40)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_lounaan_osto_kateisella_liian_vahan_rahaa(self):
        osto = self.kassapaate.syo_edullisesti_kateisella(40)
        self.assertEqual(osto, 40)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



    def test_edullisen_lounaan_osto_kortilla(self):
        maksukortti = Maksukortti(1000)
        kassapaate = Kassapaate()
        self.assertEqual(kassapaate.syo_edullisesti_kortilla(maksukortti), True)
        self.assertEqual(maksukortti.saldo, 760)
        self.assertEqual(kassapaate.edulliset, 1)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_osto_kortilla(self):
        maksukortti = Maksukortti(1000)
        kassapaate = Kassapaate()
        self.assertEqual(kassapaate.syo_maukkaasti_kortilla(maksukortti), True)
        self.assertEqual(maksukortti.saldo, 600)
        self.assertEqual(kassapaate.maukkaat, 1)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)


    def test_edullisen_lounaan_osto_kortilla_liian_vahan_rahaa(self):
        maksukortti = Maksukortti(100)
        kassapaate = Kassapaate()
        self.assertEqual(kassapaate.syo_edullisesti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(kassapaate.edulliset, 0)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_osto_kortilla_liian_vahan_rahaa(self):
        maksukortti = Maksukortti(100)
        kassapaate = Kassapaate()
        self.assertEqual(kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(kassapaate.maukkaat, 0)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataus_maksukortille(self):
        maksukortti = Maksukortti(100)
        kassapaate = Kassapaate()
        kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(kassapaate.kassassa_rahaa, 100100)

    def test_rahan_lataus_maksukortille_negatiivisella_arvolla(self):
        maksukortti = Maksukortti(100)
        kassapaate = Kassapaate()
        kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    

