from flask import Flask, request, render_template, redirect
import os


app = Flask(__name__)

messages = []

@app.route("/")
def get_index():
    return render_template("index.html") 

@app.route("/login")
def do_login():
    username = request.args['username']
    return redirect(username)

@app.route("/<username>")
def get_userpage(username):
    return render_template("chat.html", logged_in_as=username, all_the_messages=messages)
    
@app.route("/new", methods=["POST"])
def add_message():
    username = request.form['username']
    text = request.form['message']
    # message = "<strong>{0}:</strong> {1}".format(username, text)
    message = {
        'sender': username,
        'body': text
    }
    
    
    messages.append(message)
    return redirect(username)
    
   

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

