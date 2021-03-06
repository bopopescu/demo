from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sqlite3
 
conn = sqlite3.connect("myapp1.db") 
 
cursor = conn.cursor()
 
cursor.execute("""CREATE TABLE form12(Name varchar(25), email varchar(25), password varchar(25))""")

cursor.execute()

 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
     name = TextField('Name:', validators=[validators.required()])
     email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
     password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
 
@app.route("/register", methods=['GET', 'POST'])
def hello():
     form = ReusableForm(request.form)

     # print form.errors
     print(form.errors)
     if request.method == 'POST':
         name=request.form['name']
         password=request.form['password']
         email=request.form['email']
         print(name, " ", email, " ", password)
 
         if form.validate():
             # Save the comment here.
                 flash('Thanks for registration ' + name)
         else:
             flash('Error: All the form fields are required. ')
     else:
         return render_template('hello.html',form=form)
 
if __name__ == "__main__":
    app.run()
