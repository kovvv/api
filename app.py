from flask import Flask, request, json
import datetime
app = Flask(__name__)

@app.route('/date', methods=['POST'])
def service():
    try:
        data = json.loads(request.data)
        date_time_obj = datetime.datetime.strptime(data['date'], '%b %d %Y %I:%M%p')
        res = str(date_time_obj)
        return{'message': 'success', 'date': res}
    except Exception:
        return{'message': 'not correct date/time format, must be %b %d %Y at %I:%M%p'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
