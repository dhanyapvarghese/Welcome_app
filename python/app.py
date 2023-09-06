from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to 2023!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)

# Why you should run it at 0.0.0.0
# https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues
