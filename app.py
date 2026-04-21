#basic flask app 
# containerize it 
# we will automate the build (using git)
# we will deploy it to cloud aws ec2 

from flask import Flask 

app = flask(__name__)

@app.route('/')
def home():
    return "<h1> devops successfull</h1> <p> pthon + docker + git + aws running .. created by akshat </p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',  port = 5000)