from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
user = ""
password = ""

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home',methods=['GET','POST'])
def home():
    # Check if user and password are not 0 length string
    global user
    if request.method == "POST":
        user = request.form.get('login')
        password = request.form.get('password')
        return redirect("/home", code=302)
    else:
        print("This"+user+"-")
        if len(user) == 0:
            return redirect("/", code=302)
        return "Home Page "

@app.route('/client',methods=['GET'])
def client():
    return user


if __name__ == '__main__':
    app.run()
