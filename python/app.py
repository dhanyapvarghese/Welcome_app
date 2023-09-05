from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to 2023!"

if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=80)

# Why you should run it at 0.0.0.0
# https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues
