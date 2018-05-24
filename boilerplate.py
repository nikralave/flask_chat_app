from flask import Flask, request, render_template
import os


app = Flask(__name__)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

