from flask import *
from database import *
fuel=Blueprint('fuel',__name__)


@fuel.route('/fuelhome',methods=['get','post'])
def fuelhome():
	return render_template('fuelhome.html')

@fuel.route('/addfuel',methods=['get','post'])
def addfuel():
	data = {}
	ids = session['login_id']
	q = "select * from fuelstations where login_id='%s'" % (ids)
	res = select(q)
	data['fs']= res
	if 'submit' in request.form:
		categ = request.form['Category']
		district = request.form['district']
		city = request.form['city']
		amount = request.form['amount']
		mobile = request.form['mobile']
		available=request.form['available']
		q = "insert into fuel values(null,(select fuelstation_id from fuelstations where login_id='%s'),'%s','%s','%s','%s','%s','%s')" % (ids,categ, district, city, amount, mobile, available )
		insert(q)
		flash("Fuel Added")
	q = "select * from fuel_categorys"
	res1 = select(q)
	data['cat'] = res1
	return render_template('fuel_addfuel.html',data=data)

@fuel.route('/viewfuel',methods=['get','post'])
def viewfuel():
	data={}
	ids = session['login_id']
	q = "select * from fuel inner join fuelstations using(fuelstation_id) inner join fuel_categorys using(category_id) where fuelstation_id=(select fuelstation_id from fuelstations where login_id='%s') "%(ids)
	res1 = select(q)
	data['fuel'] = res1
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None

	if action == 'delete':
		q = "delete from fuel where fuel_id='%s'" % (id)
		delete(q)
		return redirect(url_for('fuel.viewfuel'))

	if action=='update':
		q="select * from fuel where fuel_id='%s'"%(id)
		res=select(q)
		data['updatefuel']=res

	if 'update' in request.form:
		avail=request.form['available']
		amount=request.form['amount']
		q="update fuel set available='%s',amount='%s' where fuel_id='%s'"%(avail,amount,id)
		update(q)
		return redirect(url_for('fuel.viewfuel'))
	return render_template('fuel_viewfuel.html',data=data)

@fuel.route('/fuelrequests',methods=['get','post'])
def fuelrequests():
	data = {}
	ids = session['login_id']
	q = "select * from request inner join fuel using(fuel_id) inner join fuelstations using(fuelstation_id) where req_status='Pending' and fuelstation_id=(select fuelstation_id from fuelstations where login_id='%s') "%(ids)
	res = select(q)
	data['req'] = res
	data['count']=len(res)
	if 'id' in request.args:
		id=request.args['id']
		q="update request set  req_status='Accepted'  where request_id='%s' "%(id)
		update(q)
		return redirect(url_for('fuel.fuelrequests'))
	return render_template('fuel_fuelrequests.html',data=data)

@fuel.route('/ap_fuelrequests',methods=['get','post'])
def ap_fuelrequests():
	data = {}
	ids = session['login_id']
	q =  "select * from request inner join fuel using(fuel_id) inner join fuelstations using(fuelstation_id) where req_status!='Pending' and fuelstation_id=(select fuelstation_id from fuelstations where login_id='%s') "%(ids)
	res = select(q)
	data['req'] = res
	return render_template('fuel_apr_fuelrequests.html',data=data)

@fuel.route('/fuel_profile',methods=['get','post'])
def fuel_profile():
	data = {}
	ids = session['login_id']
	q = "SELECT * FROM `fuelstations` WHERE login_id='%s'" % (ids)
	res = select(q)
	data['my'] = res
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None
	if action=='update':
		q="select * from fuelstations where login_id='%s'"%(ids)
		res=select(q)
		data['updatecat']=res

	if 'update' in request.form:
		mobile=request.form['mobile']
		q="update fuelstations set mobile='%s' where login_id='%s'"%(mobile,ids)
		update(q)
		return redirect(url_for('fuel.fuel_profile'))
	return render_template('fuel_profile.html',data=data)

@fuel.route('/fuel_addemployees',methods=['get','post'])
def fuel_addemployees():
	ids = session['login_id']
	if 'submit' in request.form:
		name=request.form['name']
		add=request.form['address']
		email=request.form['email']
		mob=request.form['mobile']
		psw=request.form['password']
		q = "select * from login where username='%s'" % (email)
		res = select(q)
		if len(res) > 0:
			flash("Your Email ID Already Exists ")
		else:
			q = "insert into login values(null,'%s','%s','employee',null)" % (email, psw)
			result = insert(q)
			q = "insert into employees values(null,'%s',(select fuelstation_id from fuelstations where login_id='%s'),'%s','%s','%s')" % (result,ids, name,add,mob)
			insert(q)
			flash("Employee Registration Successfully Completed")
	return render_template('fuel_addemployees.html')

@fuel.route('/fuel_viewemployees',methods=['get','post'])
def fuel_viewemployees():
	data={}
	ids = session['login_id']
	q = "select * from employees inner join login using(login_id) where fuelstation_id= (select fuelstation_id from fuelstations where login_id='%s') "%(ids)
	res1 = select(q)
	data['emp'] = res1
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None

	if action == 'delete':
		q = "delete from login where login_id='%s'" % (id)
		q1 = "delete from employees where login_id='%s'" % (id)
		delete(q)
		delete(q1)
		return redirect(url_for('fuel.fuel_viewemployees'))
	return render_template('fuel_viewemployees.html',data=data)

@fuel.route('/fuel_chpassword',methods=['get','post'])
def fuel_chpassword():
	return render_template('fuel_chpassword.html')

@fuel.route('/fuel_assignworks',methods=['get','post'])
def fuel_assignworks():
	data = {}
	ids = session['login_id']
	q="select * from request inner join fuel using(fuel_id) inner join fuelstations using(fuelstation_id) where fuelstation_id=(select fuelstation_id from fuelstations where login_id='%s')and request.pay_status='Paid' "% (ids)
	res = select(q)
	data['req'] = res

	q="select * from employees where fuelstation_id=(select fuelstation_id from fuelstations where login_id='%s')"%(ids)
	res1=select(q)
	data['emp']=res1

	j = 0
	for i in range(1, len(res) + 1):
		if 'submit' + str(i) in request.form:
			employee = request.form['employee']
			q = "UPDATE request SET employee_id='%s' WHERE request_id='%s'" % (employee, res[j]['request_id'])
			update(q)
			q = "insert into works values(null,'%s','%s','Pending')" % (res[j]['request_id'], employee)
			insert(q)
			flash("Work Assigned for the Employee")
			return redirect(url_for('fuel.fuel_assignworks'))
		j = j + 1

	return render_template('fuel_assignworks.html',data=data)

