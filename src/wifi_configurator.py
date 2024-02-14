# wifi_configurator.py
import subprocess

def configure_wifi(ssid, password):
        # Use subprocess to execute commands to configure Wi-Fi

    try:
        subprocess.run(['sudo', 'wpa_passphrase', ssid, password], check=True, capture_output=True)
        subprocess.run(['sudo', 'wpa_cli', '-i', 'wlan0', 'reconfigure'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Wi-Fi configuration failed: {e}")
        return False
