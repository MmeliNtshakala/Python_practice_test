import unittest
from unittest.mock import patch, mock_open
import csv

# This is the function you're testing.
from src.transact.transact_impl import get_user_data

class TestGetUserData(unittest.TestCase):
    # Sample CSV data
    sample_csv_data = """username,password,cheque_account_balance,savings_account_balance,investment_account_balance
johndoe,secure123,1500,3000,5000
janedoe,secure456,2000,4000,6000
"""

    @patch('builtins.open', new_callable=mock_open, read_data=sample_csv_data)
    def test_get_user_data_positive(self, mock_file):
        """ Test that get_user_data correctly retrieves a user's data. """
        # Here, 'johndoe' is expected to be in the CSV file.
        user_data = get_user_data('johndoe')
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data['username'], 'johndoe')
        self.assertEqual(user_data['password'], 'secure123')
        self.assertEqual(user_data['cheque_account_balance'], '1500')
        self.assertEqual(user_data['savings_account_balance'], '3000')
        self.assertEqual(user_data['investment_account_balance'], '5000')

    @patch('builtins.open', new_callable=mock_open, read_data=sample_csv_data)
    def test_get_user_data_user_not_found(self, mock_file):
        """ Test that get_user_data returns None when the user is not found. """
        # Here, 'nonexistentuser' is not expected to be in the CSV file.
        user_data = get_user_data('nonexistentuser')
        self.assertIsNone(user_data)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_get_user_data_file_not_found(self, mock_file):
        """ Test that get_user_data handles a FileNotFoundError correctly. """
        user_data = get_user_data('johndoe')
        self.assertIsNone(user_data)

if __name__ == '__main__':
    unittest.main()
