from flask import Flask
from flask import request
import base64

app = Flask('ownerotifier')

@app.route('/', methods = ['POST'])
def home():
    image = request.form.get('image')
    print(type(image))
    return 'hello'



app.run(debug=True)