from flask import Flask
from flask import render_template
from flask import request
import requests
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/vista')
def homepage():
  artista = request.args.get('artista')

  if artista is None:
    return render_template('vista.html', albums=[])

  params = {
    'api_key': '5c1016ab26ab5b2f6ad21c3d873785bc',
    'format' : 'json',
    'artist': artista
  }
  r = requests.get(
      'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums',
      params=params)

  return render_template('vista.html',
               albums=r.json()['topalbums']['album'])


if __name__ == "__main__":
    app.run (host = '127.0.0.1', port = 5000, threaded=True)