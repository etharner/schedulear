import re, parser
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)
rd = parser.parse()

def schedule_repr(key):
	text = "{}"
	if (key in rd):
		text = json.dumps(rd[key])	
	return {
		'url': request.host_url.rstrip('/') + url_for('schedule', key=key),
		'text': text
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