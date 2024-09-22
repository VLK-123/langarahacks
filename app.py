from flask import Flask, request, render_template, redirect, url_for, flash, session as flask_session, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.secret_key = '2024hacks'

url_list = {
    'site1' : '/get-url/1',
    'site2' : '/get-url/2',
    'site3' : '/get-url/3',
    'site4' : '/get-url/4',
    'site5' : '/get-url/5',
    'site6' : '/get-url/6'
}

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/todo_task')
@cross_origin()
def todo_task():
    return render_template('todo.html')

@app.route('/calender')
@cross_origin()
def calender():
    return render_template('calender.html')

@app.route('/clock')
@cross_origin()
def clock():
    return render_template('clock.html')

@app.route('/stopwatch')
@cross_origin()
def stopwatch():
    return render_template('stopwatch.html')

@app.route('/weather')
@cross_origin()
def weather():
    return render_template('weather.html')

@app.route('/get_url/<int:id>', methods=['POST', 'GET'])
@cross_origin()
def get_url(id):
    if request.method == 'POST':
        url = request.form.get('url')
        return redirect(url)
    return render_template('url.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)
