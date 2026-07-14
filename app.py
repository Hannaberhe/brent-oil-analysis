from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_csv('data/BrentOilPrices.csv', parse_dates=['Date'])
events = pd.read_csv('data/events.csv')

@app.route('/api/prices')
def get_prices():
    data = df[['Date', 'Price']].tail(1000).to_dict('records')
    return jsonify([{'date': str(r['Date'])[:10], 'price': r['Price']} for r in data])

@app.route('/api/events')
def get_events():
    return jsonify(events.to_dict('records'))

@app.route('/api/stats')
def get_stats():
    return jsonify({
        'min': float(df['Price'].min()),
        'max': float(df['Price'].max()),
        'mean': float(df['Price'].mean()),
        'days': len(df)
    })

@app.route('/api/changepoints')
def get_changepoints():
    return jsonify({
        'count': 30,
        'key_dates': ['1990-08-03', '2008-09-02', '2020-03-06', '2022-02-03']
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
