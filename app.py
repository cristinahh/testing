from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  #when this path is accessed, show whatever is after return
def hello_world():
  return render_template('home.html')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) #starts the app on hose 0.0.0.0

#deleted comment
