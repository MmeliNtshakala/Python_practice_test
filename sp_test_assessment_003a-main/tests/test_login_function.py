import unittest
from unittest.mock import mock_open, patch

# Assume the login function is in a module named bank
import src.login_signup.bankLoginService as bls

class TestLoginFunction(unittest.TestCase):

    def setUp(self):
        self.sample_data = 'username,password\njohndoe,secure123\njanedoe,abc123\n'

    def test_login_success(self):
        """ Test login with correct username and password """
        with patch('builtins.open', mock_open(read_data=self.sample_data)):
            self.assertTrue(bls.login('johndoe', 'secure123')[0])

    def test_login_wrong_password(self):
        """ Test login with correct username but incorrect password """
        with patch('builtins.open', mock_open(read_data=self.sample_data)):
            self.assertFalse(bls.login('johndoe', 'wrongpassword')[0])

    def test_login_nonexistent_user(self):
        """ Test login with a username that doesn't exist """
        with patch('builtins.open', mock_open(read_data=self.sample_data)):
            self.assertFalse(bls.login('nonexistent', 'any_password')[0])

    def test_login_empty_username(self):
        """ Test login with an empty username """
        with patch('builtins.open', mock_open(read_data=self.sample_data)):
            self.assertFalse(bls.login('', 'secure123')[0])

    def test_login_empty_password(self):
        """ Test login with an empty password """
        with patch('builtins.open', mock_open(read_data=self.sample_data)):
            self.assertFalse(bls.login('johndoe', '')[0])

    def test_login_empty_username_and_password(self):
        """ Test login with both username and password empty """
        with patch('builtins.open', mock_open(read_data=self.sample_data)):
            self.assertFalse(bls.login('', '')[0])

# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()
