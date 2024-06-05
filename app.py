from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    '''show madlib form on home page'''
    prompts = story.prompts
    return render_template('home.html', prompts=prompts) 


