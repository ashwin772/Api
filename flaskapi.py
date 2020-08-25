from flask import Flask, render_template, url_for, request, jsonify
from flask_restful import Api , Resource, reqparse, abort
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db2'
db2=SQLAchemy(app)

api= Api(app)


class Userdata(db.Model):
	username= db.Column(db.String(100), primary_key=True)
	password= db.Column(db.String(100), nullable=False)


	def __repr__(self):
		return f"User(username= {username} , password = {password})"



class UserVal(db2.Model):
	username= db2.Column(db.String(100))
	site_name= db2.Column(db2.String(100))
	site_username= db2.Column(db2.String(100))
	site_password= db2.Column(db2.String(100), nullable=False)

	def __repr__(self):
		return f"User_val(username= {username} ,site_name = {site_name}, site_username= {site_username}, site_password={site_password})"

#db.create_all()
#db2.create_all()
class Hellow(Resource):
	def get(self):
		return {"adta":"hj"}


api.add_resource(Hellow, "/Hellow")

if __name__ == '__main__':
      app.run(debug=True)  