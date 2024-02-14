# main.py
from flask import Flask, render_template, request, redirect, url_for
import qrcode
import access_point_manager

app = Flask(__name__)

# Generate QR Code for accessing the Wi-Fi setup page
def generate_qr_code():
    access_point_ip = access_point_manager.get_access_point_ip()  # Dynamically retrieve the access point IP
    url = f"http://{access_point_ip}/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_path = 'static/qr_code.png'
    img.save(img_path)
    return img_path

@app.route('/')
def home():
    qr_code_path = generate_qr_code()
    return render_template('index.html', qr_code_path=qr_code_path)

@app.route('/submit', methods=['POST'])
def submit_wifi_credentials():
    ssid = request.form['ssid']
    password = request.form['password']
    # Here you would add logic to configure the Raspberry Pi Wi-Fi with these credentials
    return redirect(url_for('home'))

if __name__ == '__main__':
    access_point_manager.start_access_point()  # Start the access point
    app.run(host='0.0.0.0', port=80, debug=True)
