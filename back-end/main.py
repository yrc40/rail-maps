from app import create_app
 
app = create_app('development')

'''from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"
    
@app.route("/yrc")
def yrc():
    return "I am a dog!"

if __name__ == "__main__":
    app.run()'''
