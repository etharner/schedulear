import re, parser
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

def schedule_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('schedule', key=key),
        'text': parser.parse(key)
    }

def number_error(key):
	return {
		'url': request.host_url.rstrip('/') + url_for('schedule', key=key),
		'text': "{}" 
	}    

@app.route("/<string:key>/", methods=['GET', 'PUT', 'DELETE'])
def schedule(key):
	if (re.search('^[a-zA-Z]\d{3,4}$', key)):
		return schedule_repr(key)
	else:
		return number_error(key)

if __name__ == "__main__":
    app.run(debug=True)