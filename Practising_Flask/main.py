
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my jundagi!!"

#you can add Html----

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and marks are " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and marks are " + str(score)

# result checker
@app.route('/results/<int:score>')
def results(score):
    if score < 50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result, score=score))

if __name__ == '__main__':
    app.run(debug=True)
