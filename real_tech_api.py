from flask import Flask, request
from fitPLS_udf import fitPLS

app = Flask(__name__)

@app.route('/')
def index():
	return 'Greetings! Nothing to see here though.'

@app.route('/fitPLS', methods=['POST'])
def run_fitPLS():
	training = request.get_json()

	if training is not None:

		model = fitPLS(training)

		return model
	else:
		return 'no data was sent'

if __name__ == '__main__':
	app.run(host='0.0.0.0')