from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')  #when this path is accessed, show whatever is after return
def hello_world():
  return render_template('home.html')

@app.route(
    '/aboutme')  #when this path is accessed, show whatever is after return
def aboutme():
  return render_template('aboutme.html')


@app.route(
    '/portfolio')  #when this path is accessed, show whatever is after return
def portfolio():
  return render_template('portfolio.html')


@app.route(
    '/resume')  #when this path is accessed, show whatever is after return
def resume():
  return render_template('resume.html')


@app.route(
    '/contact')  #when this path is accessed, show whatever is after return
def contact():
  return render_template('contact.html')


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #starts the app on hose 0.0.0.0

#deleted comment
