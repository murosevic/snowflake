from flask import Flask
from flask import render_template
from flask import request
import main

app = Flask(__name__)


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def home():

    return render_template('index.html', title="Snowflake")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='499')
