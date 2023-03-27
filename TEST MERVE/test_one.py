import unittest
import requests


class TestOne(unittest.TestCase):
    url = "http://universities.hipolabs.com"

    def test_get_request(self):
        endpoint = "/search"
        query_params = {"country": "United States"}  # Optional filter by country
        response = requests.get(self.url + endpoint, params=query_params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)


if __name__ == '__main__':
    unittest.main()