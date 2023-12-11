from flask import Flask, request, jsonify, redirect, render_template
import requests

app = Flask(__name__)

ACCESS_KEY = "f6346584fb341af6496d9b3701ddc59d"


@app.route('/')
def home():
    return redirect('/welcome')


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    endpoint = "http://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "access_key": ACCESS_KEY
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        return render_template('convert.html', data=data)
    else:
        return f"Failed to convert currency. Status code: {response.status_code}"


