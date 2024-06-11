from flask import Flask

app = Flask(__name__)


@app.route('/')  #when this path is accessed, show whatever is after return
def hello_world():
  return "Hello, Cristy"


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
#this is just a comment line
