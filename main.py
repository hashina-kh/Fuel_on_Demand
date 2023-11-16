from flask import Flask
from public import public
from admin import admin
from user import user
from fuelstation import fuel
from employee import employee

app=Flask(__name__)
app.secret_key="Hai"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(fuel,url_prefix='/fuel')
app.register_blueprint(employee,url_prefix='/employee')
app.run(debug=True,port=5000)