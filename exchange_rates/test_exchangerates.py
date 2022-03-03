import unittest
from unittest import TestCase
from unittest.mock import patch

import exchange_rate  # importing the program to get to the functions of the program and test


class TestExchangeRate(TestCase):

    @patch('exchange_rate.request_rates')  # 
    def test_dollars_to_target(self, mock_rates):  # test mthod
        mock_rate = 123.4567                       # mock rate to use for testing nt a real value from API 
        # api ptyhon dict data and then we use our mock_rate varabile in place of the data from the call.
        example_api_responce = {"rates":{"CAD": mock_rate}, "base": "USD","date":"2020-10-02"}  
        mock_rates.side_effect = [example_api_responce]  # tells function to use our mock example api.
        converted = exchange_rate.convert_dollars_to_target(100, 'CAD')  # value to use with with test run
        expected = 12345.67              # expected is the mock_rate * 100    
        self.assertEqual(expected, converted)  # two arguments to assert to eaqual.


    # todo - test error conditions 
    # Currency symbol is not found,
    # Dollar value is not a number,
    # Connection errors to exchange rate API, server is down
    # what else? assert raises


    # Alternative test - patch the requests's libraries json() method
    # Which one do you prefer? I don't think ther is much of a change here
    @patch('requests.Response.json')
    def test_dollars_to_target_2(self, mock_requests_json):
        mock_rate = 123.4567
        example_api_response = {"rates":{"CAD": mock_rate},"base":"USD","date":"2020-10-02"}
        mock_requests_json.return_value = example_api_response
        converted = exchange_rate.convert_dollars_to_target(100, 'CAD')
        expected = 12345.67
        self.assertEqual(expected, converted)

