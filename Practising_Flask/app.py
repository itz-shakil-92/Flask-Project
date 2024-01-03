from flask import Flask

##wsgi application
app=Flask(__name__)

#decorater---takes two parameter---binding with function
@app.route('/')
def welcome():
    return "Welcome to my my jundagi!!"

@app.route('/members')
def members():
    return "Welcome to  jundagi!!"



if __name__=='__main__':
    app.run()  #two parameter