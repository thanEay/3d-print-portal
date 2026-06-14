from flask import *
# from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "thisissupersecretandwillbechanged"

@app.get("/")
def home():
    return render_template("student.html")

@app.post("/")
def student_post():
    name = request.form.get("name")
    email = request.form.get("email")
    color = request.form.get("color")
    color2 = request.form.get("color2")
    session["name"] = name
    session["email"] = email
    session["color"] = color
    session["color2"] = color2
    # session[""] = 
    # TODO: SQL stuff here
    return redirect(url_for("submit"))
    
@app.get("/submit")
def submit():
    html = f'''<h1>Thank you for submitting</h1><ul>
    <li>{session["name"]}</li>
    <li>{session["email"]}</li>
    <li>{session["color"]}</li>
    <li>{session["color2"]}</li>
    </ul>'''
    return html

if __name__ == "__main__":
    app.run(debug=True)