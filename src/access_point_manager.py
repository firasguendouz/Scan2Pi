# access_point_manager.py
import subprocess

def start_access_point():
    try:
        # Start the hostapd service to enable the Wi-Fi access point
        subprocess.run(['sudo', 'systemctl', 'start', 'hostapd'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to start access point: {e}")
        return False

def stop_access_point():
    try:
        # Stop the hostapd service to disable the Wi-Fi access point
        subprocess.run(['sudo', 'systemctl', 'stop', 'hostapd'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop access point: {e}")
        return False
