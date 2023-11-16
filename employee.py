from flask import *
from database import *
employee=Blueprint('employee',__name__)

@employee.route('/employeehome',methods=['get','post'])
def employeehome():
	return render_template('employeehome.html')

@employee.route('/empworks',methods=['get','post'])
def empworks():
	data={}
	ids = session['login_id']
	q = "SELECT * FROM works INNER JOIN request USING(request_id) INNER JOIN fuel USING (fuel_id) INNER JOIN fuel_categorys USING(category_id) INNER JOIN fuelstations USING(fuelstation_id) INNER JOIN users USING(user_id) where work_status!='Completed' and works.employee_id=(select employee_id from employees where login_id='%s') "%(ids)
	res = select(q)
	data['work'] = res
	if 'id' in request.args:
		id = request.args['id']
		q = "update works set  work_status='Completed'  where work_id='%s' " % (id)
		update(q)
		return redirect(url_for('employee.empworks'))
	return render_template('employee_viewassignedworks.html',data=data)

@employee.route('/empcompworks',methods=['get','post'])
def empcompworks():
	data={}
	ids = session['login_id']
	q = "SELECT * FROM works INNER JOIN request USING(request_id) INNER JOIN fuel USING (fuel_id) INNER JOIN fuel_categorys USING(category_id) INNER JOIN fuelstations USING(fuelstation_id) INNER JOIN users USING(user_id) where work_status!='Pending' and works.employee_id=(select employee_id from employees where login_id='%s') "%(ids)
	res = select(q)
	data['work'] = res
	return render_template('employee_viewcompleatedworks.html',data=data)

@employee.route('/empprofile',methods=['get','post'])
def empprofile():
	data = {}
	ids = session['login_id']
	q = "SELECT * FROM `employees`inner join fuelstations using(fuelstation_id) WHERE employees.login_id='%s' " % (ids)
	# inner join fuelstations using(fuelstation_id)
	res = select(q)
	data['my'] = res
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None
	if action == 'update':
		q = "select * from employees where login_id='%s'" % (ids)
		res = select(q)
		data['updatecat'] = res

	if 'update' in request.form:
		mobile = request.form['mobile']
		q = "update employees set contact='%s' where login_id='%s'" % (mobile, ids)
		update(q)
		return redirect(url_for('employee.empprofile'))
	return render_template('employee_viewprofile.html',data=data)

@employee.route('/empfeedback',methods=['get','post'])
def empfeedback():
	data = {}
	q = "select * from feedback inner join users using(user_id) "
	res = select(q)
	data['fb'] = res
	return render_template('employee_viewfeedbacks.html',data=data)

@employee.route('/empchpsw',methods=['get','post'])
def empchpsw():
	ids = session['login_id']
	if 'submit' in request.form:
		psw1= request.form['psw1']
		psw2 = request.form['psw2']
		psw3 = request.form['psw3']
		if psw2==psw3:
			q = "update login set password='%s' where login_id='%s' and password='%s'" % (psw2, ids,psw1)
			update(q)
			flash("Password Updated")
		else:
			flash("Please Try Again.")
			return redirect(url_for('employee.empchpsw'))

	return render_template('employee_changepassword.html')

