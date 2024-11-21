from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Get Web3Forms API Key
web3forms_access_key = os.getenv('WEB3FORMS_ACCESS_KEY', 'default_dummy_key')
if web3forms_access_key == 'default_dummy_key':
  print("Warning: WEB3FORMS_ACCESS_KEY is not set!")


@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route('/aboutme')
def aboutme():
  return render_template('aboutme.html')


@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html')


@app.route('/resume')
def resume():
  return render_template('resume.html')


@app.route('/contact')
def contact():
  return render_template('contact.html',
                         web3forms_access_key=web3forms_access_key)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
