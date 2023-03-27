import unittest
import requests


class TestTwo(unittest.TestCase):
    url = "http://universities.hipolabs.com"

    def test_get_all_universities(self):
        endpoint = "/search"
        query_params = {"country": "Turkey"}
        response = requests.get(self.url + endpoint, params=query_params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)

    def test_filter_by_name_and_country(self):
        endpoint = "/search"
        query_params = {"name": "Middle", "country": "Turkey"}
        response = requests.get(self.url + endpoint, params=query_params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)


if __name__ == '__main__':
    unittest.main()





