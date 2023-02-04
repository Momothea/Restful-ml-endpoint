import unittest
from Flask_api import app



class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_classify(self):
        response = self.app.get('/classify/0')
        self.assertEqual(response.status_code, 200)
        {"prediction": "T-shirt/top",
        "predicted_array": [[1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]
}
 

if __name__ == '__main__':
    unittest.main()