from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from flask import Flask, request, render_template
from rasa_core.agent import Agent
from rasa_core.utils import read_endpoint_config
from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter

import argparse
import warnings



endpoint = read_endpoint_config('endpoints.yml', 'action_endpoint')

app = Flask(__name__)

agent = Agent.load('models/current/dialogue', interpreter='models/current/nlu', action_endpoint=endpoint)

@app.route('/')
def load_webpage():
	hello = "Hello! you can ask me question in this window. Type 'stop' to end the conversation."
	return render_template('bot_input.html', message=hello)
	

@app.route('/bot_input', methods = ['POST'])
def bot_input():
	if request.method.lower() == 'post':
		msg = request.form['msg']

	if msg.lower() != "stop":
		# responses is a list of dicts
		responses = agent.handle_message(msg)
		print (len(responses))
		for r in responses:
			print (r)
			resp = r.get("text")
			if resp:
				output = resp
	else:
		output = "talk to you some other time"

	return render_template('human_output.html', response=output)


if __name__ == '__main__':
	app.run(debug=True)
	# app.run(host='0.0.0.0', debug = True, port=5000)