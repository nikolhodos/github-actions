import unittest
from unittest.mock import patch
from app.main import fetch_match_data, process_matches, motivational_quote


class TestMain(unittest.TestCase):

    @patch('app.main.requests.get')
    def test_fetch_match_data(self, mock_get):
        mock_get.return_value.json.return_value = {
            "response": [
                {
                    "teams": {
                        "home": {
                            "name": "Real Madrid"}, "away": {
                            "name": "Barcelona"}}, "goals": {
                        "home": 2, "away": 1}}, {
                    "teams": {
                        "home": {
                            "name": "Real Madrid"}, "away": {
                            "name": "Atletico Madrid"}}, "goals": {
                        "home": 3, "away": 0}}, {
                    "teams": {
                        "home": {
                            "name": "Real Madrid"}, "away": {
                            "name": "Sevilla"}}, "goals": {
                        "home": 1, "away": 1}}, ]}
        mock_get.return_value.status_code = 200
        mock_get.return_value.raise_for_status = lambda: None

        data = fetch_match_data("fake_api_key")
        matches = process_matches(data, 3)
        expected = [
            "Real Madrid 2 - 1 Barcelona",
            "Real Madrid 3 - 0 Atletico Madrid",
            "Real Madrid 1 - 1 Sevilla"
        ]
        self.assertEqual(matches, expected)

    def test_motivational_quote(self):
        self.assertEqual(motivational_quote(),
                         "Dream big!")


if __name__ == '__main__':
    unittest.main()
