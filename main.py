from flask import Flask, render_template, request, redirect, url_for
import base64
from backups import backup_list
from clients import client_list


app = Flask(__name__)
user = ""
password = ""
credentials = ""


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home',methods=['GET','POST'])
def home():
    # Check if user and password are not 0 length string
    global user, password, credentials
    if request.method == "POST":
        user = request.form.get('login')
        password = request.form.get('password')
        message = user+":"+password
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        credentials = base64_bytes.decode('ascii')
        return redirect("/backups", code=302)
    else:
        print("This "+credentials+" -")
        if len(credentials) == 0:
            return redirect("/", code=302)
        return "Home Page "

# Route to get the list of all Backups
@app.route('/backups',methods=['GET'])
def backups():
    if len(credentials) == 0:
        return redirect("/", code=302)
    return backup_list(credentials, request)

# Route to get the list of clients configured
@app.route('/clients',methods=['GET'])
def client():
    if len(credentials) == 0:
        return redirect("/", code=302)
    return client_list(credentials, request)

@app.route('/log_out', methods=['GET'])
def log_out():
    global credentials
    credentials = ""
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run()
