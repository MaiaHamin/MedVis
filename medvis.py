from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os
import json
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


medcos = ["WaPo", "NYT", "CNN", "WSJ", "Buzzfeed", "OccupyDems", "UpWorthy", "NowThis", "FFA", "ForAmerica", "Fox"]
like_paths = []
share_paths = []
com_paths = []
like_dic = {}
share_dic = {}
com_dic = {}

def eprint(*s):
	print(*s, file=sys.stderr)

@app.before_request
def before_request():
	for mc in medcos:
		likename = mc + "_likes.json"
		likepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", likename))
		sharename = mc + "_shares.json"
		sharepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", sharename))
		comname = mc + "_comments.json"
		compath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", comname))
		like_paths.append(likepath)
		share_paths.append(sharepath)
		com_paths.append(compath)

	for i in range(len(medcos)):
		like_d=open(like_paths[i]).read()
		like_p = json.loads(like_d)
		share_d=open(share_paths[i]).read()
		share_p = json.loads(share_d)
		com_d=open(com_paths[i]).read()
		com_p = json.loads(com_d)
		like_stories = []
		share_stories = []
		com_stories = []
		for story in like_p[:10]:
			like_stories.append(story)
			share_stories.append(story)
			
		for story in com_p[:10]:
			com_stories.append(story)
		like_dic[medcos[i]]ke_stories
		share_dic[medcos[i]] = share_stories
		com_dic[medcos[i]] = com_stories


@app.route('/')
def homepage():
	return render_template("homepage.html")


@app.route('/engagementchart')
def engagement_chart():
	return render_template("template.html")

@app.route('/fbsim')
def facebook_sim(medco="NYT"):
	return render_template("facebooksim.html", medcos=medcos, likes=like_dic[medco], coms=com_dic[medco])

@app.route('/fbsim/<medco>')
def facebook_sim_wco(medco="NYT"):
	return render_template("facebooksim.html", medcos=medcos, likes=like_dic[medco], coms=com_dic[medco])

if __name__ == '__main__':
    app.run()
