
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, length

app = Flask(__name__)

import os
SECRET_KEY = "abcd"
app.config['SECRET_KEY'] = SECRET_KEY

import part1





#index page greeting and Form Code
class MyForm(FlaskForm):
    """Contact form."""
    username = StringField(
        'Username',
        [DataRequired()]
    )
    
    body = TextField(
        'Location',
        [
            DataRequired()
        ]
    )
    
    submit = SubmitField('Submit')



@app.route('/')
def hello():
    # return render_template ('hello.html')
    form = MyForm() 
    if request.method == 'POST' and form.validate():   
        return redirect(url_for('login')) 
    return render_template('signup.html', form=form) 




#POST submission
# os.system('python part1.py')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        print()
    # if request.method == 'POST':
        # form_data = request.form
        return print("it is a post ")

app.run(host='localhost', port=5000)


os.system('python part1.py')



# data page
# @app.route('/mbta_station')


# ''' THe Flask backend withll dandle the request to POST/nearest_mbta. 
# Then app will render a mbta_station page fo rthe user"
# presenting nearest MBTA stop and whether it is wheelchair accesble. This step requires you to use code from part 1
# '''


# if __name__ == "__main__":
#     app.run()






# def post_request():
#     url = 
#     myobj = {'somekey': 'somevalue'}

#     x = request.ost(url, data = myobj)

