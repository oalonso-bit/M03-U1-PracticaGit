# test_security.py
import unittest
from security import validar_password 

class TestPasswordValidator(unittest.TestCase):
    def test_short_password_fails(self):
        self.assertFalse(validar_password("curta"), "La contrasenya de 5 caràcters hauria de fallar")

    def test_long_password_passes(self):
        # Nou test per a una contrasenya de més de 8 caràcters
        self.assertTrue(validar_password("moltsegura123"), "La contrasenya llarga hauria de passar") # [cite: 112]

if __name__ == '__main__':
    unittest.main()