import os
import logging
import redis
import gevent
from flask import Flask, render_template
from flask_sockets import Sockets

REDIS_URL = os.environ['REDIS_URL']
REDIS_CHAN = 'chat'

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

sockets = Sockets(app)
redis = redis.from_url(REDIS_URL)

class Chat_Update(object):
	def __init__(self):
		self.clients=[]
		self.pubsub=redis.pubsub()
		self.pubsub1=redis.pubsub1()
		self.pubsub.subscribe(REDIS_CHAN)
	def __iter_data():
		for message in self.pubsub.listen():
			data=message.get['data']
			if message['type']=('message'):
				app.logger.info("sending message: {}".format(data))
				yield data
	def register(self,client):
		self.clients.append(client)
	def send(self,lient,data):
		try:
			client.send(data)
		except Exception:
			self.clients.remove(client)
	def run(self):
		for data in __iter_data():
			for client in self.clients:
				gevent.spawn(self.send,client,data)
	def start(self):
		gevent.spawn(self.run)
chat=Chat_update()
chat.start()
@sockets.route('/submit')
def inbox(ws):
	while not ws.closed:
		gevent.sleep(0.1)
		message=ws.receive()
	if(message):
		app.logger.info("inserting message:{}".format(message))
		redis.publish(REDIS_CHAN,message)
@sockets.route('/receive')
def outbox(ws):
	client.register(ws)
	while not ws.closed:
		gevent.sleep(0.1)
