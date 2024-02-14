# tests/test_wifi_configurator.py
import subprocess
import unittest
from unittest.mock import patch, MagicMock
from src import wifi_configurator

class TestWifiConfigurator(unittest.TestCase):

    @patch('subprocess.run')
    def test_configure_wifi_success(self, mock_run):
        # Mock subprocess.run to simulate a successful execution
        mock_run.return_value = MagicMock()

        # Call the function with sample SSID and password
        result = wifi_configurator.configure_wifi("MyWiFi", "MyPassword")

        # Assert that subprocess.run was called with the expected parameters
        mock_run.assert_called_once_with(['sudo', 'wpa_passphrase', 'MyWiFi', 'MyPassword'],
        check=True, capture_output=True)
        self.assertTrue(result)

    @patch('subprocess.run', side_effect=subprocess.CalledProcessError)
    def test_configure_wifi_failure(self, mock_run):
        # Mock subprocess.run to simulate a failure
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd="")

        # Call the function with sample SSID and password
        result = wifi_configurator.configure_wifi("MyWiFi", "MyPassword")

        # Assert that subprocess.run was called with the expected parameters
        mock_run.assert_called_once_with(['sudo', 'wpa_passphrase', 'MyWiFi', 'MyPassword'],
        check=True, capture_output=True)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
