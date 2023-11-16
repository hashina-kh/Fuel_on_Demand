from flask import *
from database import *
public=Blueprint('public',__name__)


@public.route('/',methods=['get','post'])
def index():
	return render_template('index.html')

@public.route('/fuel_register',methods=['get','post'])
def fuel_register():
	if 'submit' in request.form:
		name=request.form['fname']
		lnum=request.form['lnum']
		dist=request.form['district']
		city=request.form['city']
		pin=request.form['pincode']
		email=request.form['email']
		mob=request.form['mobile']
		loc=request.form['location']
		psw=request.form['password']

		q = "select * from login where username='%s'" % (email)
		res = select(q)
		if len(res) > 0:
			flash("Email ID Already Exists")
		else:
			q = "insert into login values(null,'%s','%s','fuelstation','pending')" % (email,psw)
			result = insert(q)
			q = "insert into fuelstations values(null,'%s','%s','%s','%s','%s','%s','%s','%s')" % (result, name, lnum, dist,city,pin,mob,loc)
			insert(q)
			flash("Fuelstation Registration Successfully Completed")

	return render_template('fuelstation_register.html')

@public.route('/user_register',methods=['get','post'])
def user_register():
	if 'submit' in request.form:
		name=request.form['name']
		dob=request.form['dob']
		dist=request.form['district']
		city=request.form['city']
		str = request.form['street']
		pin=request.form['pincode']
		email=request.form['email']
		mob=request.form['mobile']
		psw=request.form['password']
		q = "select * from login where username='%s'" % (email)
		res = select(q)
		if len(res) > 0:
			flash("Your Email ID Already Exists ")
		else:
			q = "insert into login values(null,'%s','%s','user',null)" % (email, psw)
			result = insert(q)
			q = "insert into users values(null,'%s','%s','%s','%s','%s','%s','%s','%s')" % (result, name, dob, dist,city,str,pin,mob)
			insert(q)
			flash("User Registration Successfully Completed")
	return render_template('user_register.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['email']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)

		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=="user":
				return redirect(url_for('user.userhome'))
			if res[0]['usertype']=="employee":
				return redirect(url_for('employee.employeehome'))
			if res[0]['usertype']=="fuelstation":
				if res[0]['status'] == "Accept":
					return redirect(url_for('fuel.fuelhome'))
				elif res[0]['status'] == "Reject":
					flash("Your are Rejected by Admin.")
				else:
					flash("You are not Approved by Admin... Wait for the confirmation")
		else:
			flash("Incorrect email or password.")
	return render_template('login.html')