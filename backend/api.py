import requests
import sys
from flask_cors import CORS, cross_origin
from flask import Flask, Response
from urllib.parse import urlencode

# print(sys.path, file=sys.stdout)
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

KEY = 'lvU0XCdkvH2M64CG1aTBczcIdmK4TC9umrNYqLupIYEwf5rlUbH0v93zCEFl2v4R'
SECRET = 'AhAcdUh7TM1KUx6ggkytfa7UWLeuaQkLwUAd9uec9toEo68AfPVLcw2LunDs1e6r'
# BASE_URL = 'https://api.binance.com' # production base url
BASE_URL = 'https://testnet.binance.vision'  # testnet base url


def dispatch_request(http_method):
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json;charset=utf-8',
        'X-MBX-APIKEY': KEY
    })
    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')


def send_public_request(url_path, payload={}):
    query_string = urlencode(payload, True)
    url = BASE_URL + url_path
    if query_string:
        url = url + '?' + query_string
    print("{}".format(url))
    response = dispatch_request('GET')(url=url)
    return response.json()


@app.route('/ticker')
@cross_origin()
def get_btc_usd():
    r = send_public_request('/api/v3/ticker/price', {'symbol': 'BTCUSDT'})
    print(r, file=sys.stdout)
    return {'response': r}
