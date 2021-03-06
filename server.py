import re
from sparser import parse
import json
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)
rd = parse()

def schedule_repr(key, action):
	text = "{}"

	if (action == 'schedule'):
		if (key in rd):
			text = rd[key]
	if (action == 'near'):
		if (key == 'D734'):
			text = 	"{'near': Мастер-класс\nперенесен в аудиторию D733\n⇦}"
		if (key == 'D733'):
			text = "{'near': Мастер-класс\n13:30-15:00}"
	if (action == 'work'):
		if (key == 'D951'):
			text = "{'work': РЕЖИМ РАБОТЫ\n09:00-17:00}"		
	if (action == 'history'):
		if (key == 'A941'):
			text = "{'history': Этот кабинет посетил\nПрезидент Российской Федерации\nВ.В. Путин}"	
	if (action == 'food'):
		if (key == 'A841'):
			text = "{'food': 🍲Здесь можно поесть🍲}"			
	if (action == 'event'):
		if (key == 'A841'):
			text = "{'event': Событие: Хакатон}"			
	if (action == 'rate'):
		if (key == 'A941'):
			p = {'photo': 'https://i.imgur.com/l1RuzcX.png', 'rate': '☆☆☆☆☆', 'name': 'Анисимов Никита Юрьевич'}
			text = p

	return {
		'url': request.host_url.rstrip('/') + url_for('schedule', key=key, action=action),
		'text': json.loads(json.dumps(text, ensure_ascii=False).encode('utf8').decode('utf8'))
	}

def number_error(key):
	return {
		'url': request.host_url.rstrip('/') + url_for('schedule', key=key),
		'text': "{}" 
	} 

@app.route("/<string:key>/<string:action>", methods=['GET', 'PUT', 'DELETE'])
def schedule(key, action):
	if (re.search('^[a-zA-Z]\d{3,4}$', key)):
		return schedule_repr(key, action)
	else:
		return number_error(key)
