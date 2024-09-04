from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_client_country(ip):
    try:
        response = requests.get(f'http://ipinfo.io/{ip}/json')
        data = response.json()
        return data.get('country')
    except Exception as e:
        print(f"Error getting location: {e}")
        return None

@app.route('/')
def index():
    client_ip = request.remote_addr
    client_country = get_client_country(client_ip)
    return render_template('index.html', country=client_country)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)