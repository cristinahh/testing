from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
web3forms_access_key = os.getenv('WEB3FORMS_ACCESS_KEY')


@app.route('/web3forms_api_key')
def home():
  return f"Your Web3Forms API Key is: {web3forms_access_key}"


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


print(
    web3forms_access_key
)  # This should print the value of the access key if it's loaded correctly.
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=False)

#deleted comment
