'''
Unit tests for the Eddington API using FastAPI and TestClient.

'''
import unittest
from fastapi.testclient import TestClient
from app.api_eddington import app

client = TestClient(app)

class TestEddingtonAPI(unittest.TestCase):

    def test_single_star(self):
        payload = {
            "luminosity": 1,
            "mass": 1
        }
        response = client.post("/eddington_ratio", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("eddington_ratio", data)
        self.assertTrue(isinstance(data["eddington_ratio"], float))

    def test_batch_star_valid_csv(self):
        csv_content = "luminosity,mass,temperature,metallicity\n1e38,10,20000,0.02\n2e38,20,25000,0.01"
        files = {
            "file": ("stars.csv", csv_content, "text/csv")
        }
        response = client.post("/eddington_ratio_batch", files=files)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertIn("eddington_ratio", data[0])

    def test_batch_star_missing_columns(self):
        csv_content = "luminosity,temperature\n1e38,20000"
        files = {
            "file": ("bad.csv", csv_content, "text/csv")
        }
        response = client.post("/eddington_ratio_batch", files=files)
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.json())

if __name__ == "__main__":
    unittest.main()
