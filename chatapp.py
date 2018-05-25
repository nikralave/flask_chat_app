from flask import Flask, request, render_template, redirect
import os


app = Flask(__name__)
messages = []
bannedwords = ['sugar', 'poop']

# @app.route('rooms/add')
# def add_room():
#     roomname = request.form['roomname']
#     rooms[rooomname]=[]
#     return redirect(...)

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
  
  #--------------------------------------------------------  
    # for banned_word in bannedwords:
    #     text = text.replace(" " + banned_word + " ", "*"*len(banned_word))
        
    #------------------------------------------------------
    
    
        
    words = text.split()
    words = [ "*" * len(word) if word.lower() in bannedwords else word for word in words]
    
    text = " ".join(map(str,words))
    #------------------------------------------------------
    
    message = {
        'sender': username,
        'body': text
    }
    
    
    messages.append(message)
    return redirect(username)
    
   
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
