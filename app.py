from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/result', methods=['POST'])
def result():
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    location = request.form['location']
    attendees = request.form['attendees']
    description = request.form['description']

    return render_template(
        'result.html',
        event_name=event_name,
        event_date=event_date,
        location=location,
        attendees=attendees,
        description=description
    )

if __name__ == '__main__':
    app.run(debug=True)
