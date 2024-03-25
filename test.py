#import unittest module for running tests
import unittest
#module that allows the sending of HTTP requests
import requests

class TestJWKS_Server(unittest.TestCase):


    def test_auth_endpoint(self):
        # Testoing the POST:/auth endpoint with a valid key
        response = requests.post('http://localhost:8080/auth')
        self.assertEqual(response.status_code, 200)


    def test_auth_expired_key(self):
        # Testing the POST:/auth endpoint with an expired key
        response = requests.post('http://localhost:8080/auth?expired=true')
        self.assertEqual(response.status_code, 200)


    def test_jwks_endpoint(self):
        # Testing the  GET:/.well-known/jwks.json endpoint that reads all valid keys from the DB and creates a JWKS response.
        response = requests.get('http://localhost:8080/.well-known/jwks.json')
        self.assertEqual(response.status_code, 200)


#calling the test
if __name__ == '__main__':
    unittest.main()
