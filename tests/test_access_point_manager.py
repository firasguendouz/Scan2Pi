# tests/test_access_point_manager.py
import subprocess
import unittest
from unittest.mock import patch, MagicMock
from src import access_point_manager

class TestAccessPointManager(unittest.TestCase):

    @patch('subprocess.run')
    def test_start_access_point_success(self, mock_run):
        # Mock subprocess.run to simulate a successful execution
        mock_run.return_value = MagicMock()

        # Call the function
        result = access_point_manager.start_access_point()

        # Assert that subprocess.run was called with the expected parameters
        mock_run.assert_called_once_with(['sudo', 'systemctl', 'start', 'hostapd'], check=True)
        self.assertTrue(result)

    @patch('subprocess.run', side_effect=subprocess.CalledProcessError)
    def test_start_access_point_failure(self, mock_run):
        # Mock subprocess.run to simulate a failure
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd="")

        # Call the function
        result = access_point_manager.start_access_point()

        # Assert that subprocess.run was called with the expected parameters
        mock_run.assert_called_once_with(['sudo', 'systemctl', 'start', 'hostapd'], check=True)
        self.assertFalse(result)

    @patch('subprocess.run')
    def test_stop_access_point_success(self, mock_run):
        # Mock subprocess.run to simulate a successful execution
        mock_run.return_value = MagicMock()

        # Call the function
        result = access_point_manager.stop_access_point()

        # Assert that subprocess.run was called with the expected parameters
        mock_run.assert_called_once_with(['sudo', 'systemctl', 'stop', 'hostapd'], check=True)
        self.assertTrue(result)

    @patch('subprocess.run', side_effect=subprocess.CalledProcessError)
    def test_stop_access_point_failure(self, mock_run):
        # Mock subprocess.run to simulate a failure
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd="")

        # Call the function
        result = access_point_manager.stop_access_point()

        # Assert that subprocess.run was called with the expected parameters
        mock_run.assert_called_once_with(['sudo', 'systemctl', 'stop', 'hostapd'], check=True)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
