import unittest
from unittest.mock import patch, mock_open, MagicMock

# Assume the sign_up function and user_exists are in a module named src.login_signup.bankSignUpService
from src.login_signup.bankSignUpService import sign_up

class TestSignUp(unittest.TestCase):
    
    @patch('src.login_signup.bankSignUpService.write_user_data')
    @patch('src.login_signup.bankSignUpService.user_exists', return_value=False)
    @patch('builtins.input', side_effect=['newuser', 'newpass', 'newpass'])
    def test_sign_up_success(self, input_mock, user_exists_mock, write_data_mock):
        """ Test sign up success when the user does not exist and passwords match """
        with patch('builtins.print') as mock_print:
            result = sign_up()
            mock_print.assert_called_with("Registration successful. You can now log in.")
        self.assertTrue(result)
        write_data_mock.assert_called_once_with('newuser', 'newpass')

    @patch('src.login_signup.bankSignUpService.user_exists', return_value=True)
    @patch('builtins.input', return_value='existinguser')
    def test_sign_up_user_exists(self, input_mock, user_exists_mock):
        """Test that sign up notifies user if username already exists."""
        with patch('builtins.print') as mock_print:
            result = sign_up()
            self.assertFalse(result)
            mock_print.assert_called_with("This username already exists. Please choose a different one.")

        input_mock.assert_called_once()
    
    @patch('src.login_signup.bankSignUpService.write_user_data')
    @patch('src.login_signup.bankSignUpService.user_exists', return_value=False)
    @patch('builtins.input', side_effect=['newuser', 'pass1', 'pass2'])
    def test_sign_up_password_mismatch(self, input_mock, user_exists_mock, write_data_mock):
        """ Test sign up failure when the passwords do not match """
        with patch('builtins.print') as mock_print:
            with self.assertRaises(StopIteration):
                sign_up()
            mock_print.assert_called_with("Passwords do not match. Please try again.")
        write_data_mock.assert_not_called()

# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()
