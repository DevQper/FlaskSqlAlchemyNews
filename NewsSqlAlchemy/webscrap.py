from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response, url_for
from flask import request
from flask.json import jsonify
from flask.templating import render_template
import jwt
from werkzeug.utils import redirect
from services import PutResults
from coin_market_news import news_scraper
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session

from services import GetResults

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0000@localhost/News'    
db = SQLAlchemy(app)

""" Start of the controller blocks """

@app.route('/coin', methods=['POST', 'GET'])
def coin():
    if request.method == "POST":
         result = request.form["cryptoname"]
         return redirect(url_for("result", cryptoname=result))
    else:
        return render_template('index.html')

@app.route('/<cryptoname>')
def result(cryptoname):
    PutResults(cryptoname)
    result = GetResults()
    for news in result:
        print(news.title)
    return render_template('result_page.html', content = result)

    # return '<p>Hello</p>'



if __name__ == '__main__':
    app.run(debug=True)


    