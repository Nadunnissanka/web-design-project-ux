import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)

github_credentials = {
    'username': 'Nadunnissanka',
    'password': 'Nadun@123'
}


@app.route('/')
def home():
    authentication = HTTPBasicAuth(github_credentials['username'], github_credentials['password'])
    git_data = requests.get('https://api.github.com/users/' + github_credentials['username'], auth=authentication)
    git_stats = git_data.json()
    return render_template('index.html', github=git_stats)


@app.route('/download')
def download():
    return send_from_directory('static', filename="files/service_letter_one.pdf", path="static")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
