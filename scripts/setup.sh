#!/bin/bash

# This script sets up the necessary environment for the Raspberry Pi Wi-Fi Setup

# Install required packages
sudo apt update
sudo apt install -y dnsmasq hostapd

# Set up static IP for wlan0
echo "interface wlan0" | sudo tee -a /etc/dhcpcd.conf
echo "    static ip_address=192.168.4.1/24" | sudo tee -a /etc/dhcpcd.conf
echo "    nohook wpa_supplicant" | sudo tee -a /etc/dhcpcd.conf

# Configure hostapd
sudo cp src/config/hostapd.conf /etc/hostapd/

# Configure dnsmasq
sudo cp src/config/dnsmasq.conf /etc/dnsmasq.conf

# Enable routing and NAT
sudo sysctl net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

# Start services
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl restart dnsmasq
