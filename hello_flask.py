import flask
import os
from Scriptor import Scriptor

app = flask.Flask(__name__)
app.secret_key = "online survey"

@app.route('/', methods=['GET'])
def index():
	return flask.render_template("onlinesurvey.html")

@app.route('/uploadSurveyModel',methods=["POST"])
def uploadModel():
	print flask.request.json['data'];
	script =Scriptor(flask.request.json['data']).scriptRender()
	print script
	return flask.json.dumps({'success':True,'script':script}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
	app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))