from flask import *
from database import *
user=Blueprint('user',__name__)


@user.route('/userhome',methods=['get','post'])
def userhome():
	return render_template('userhome.html')

@user.route('/user_feedback',methods=['get','post'])
def user_feedback():
	ids = session['login_id']
	if 'submit' in request.form:
		fb = request.form['feedback']
		q = "insert into feedback values(null,(select user_id from users where login_id='%s'),'%s','pending',Curdate())" % (ids,fb)
		insert(q)
		flash("Feedback Added")
	return render_template('user_feedback.html')

@user.route('/user_viewreply',methods=['get','post'])
def user_viewreply():
	data={}
	ids = session['login_id']
	q="select * from feedback inner join users using(user_id)"
	res=select(q)
	data['fb']=res
	return render_template('user_viewreply.html',data=data)

@user.route('/user_viewprofile',methods=['get','post'])
def user_viewprofile():
	data = {}
	ids = session['login_id']
	q = "SELECT * FROM `users` WHERE login_id='%s'" % (ids)
	res = select(q)
	data['my'] = res
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None
	if action == 'update':
		q = "select * from users where login_id='%s'" % (ids)
		res = select(q)
		data['updatecat'] = res

	if 'update' in request.form:
		mobile = request.form['mobile']
		q = "update users set phone='%s' where login_id='%s'" % (mobile, ids)
		update(q)
		return redirect(url_for('user.user_viewprofile'))
	return render_template('user_viewprofile.html',data=data)

@user.route('/user_fuelrequest',methods=['get','post'])
def user_fuelrequest():
	data = {}
	if 'submit' in request.form:
		name = request.form['place']
		q = "select * from fuel inner join fuel_categorys using(category_id) WHERE  fuel.district LIKE '%s' or fuel.city LIKE '%s' and fuel.available='yes' " % (name,name)
		res = select(q)
		data['viewsearch'] = res
	return render_template('user_fuelrequest.html',data=data)


@user.route('/add_fuelrequest',methods=['get','post'])
def add_fuelrequest():
	id = request.args['id']
	ids = session['login_id']
	if 'submit' in request.form:
		name = request.form['name']
		quantity = request.form['quantity']
		location = request.form['location']
		num = request.form['number']
		q = "select amount from fuel where fuel_id='%s'" % (id)
		res = select(q)
		total = int(res[0]['amount']) * int(quantity)
		q = "insert into request values(null,'%s',(select user_id from users where login_id='%s'),'%s','%s','%s','%s',Curdate(),'Pending' ,'Pending','%s', '0')" % (id, ids, name, num, quantity, location, total)
		insert(q)
		flash("Added Successfully")
		return redirect(url_for('user.view_fuelrequest'))
	return render_template('useradd_fuelrequest.html')


@user.route('/view_fuelrequest',methods=['get','post'])
def view_fuelrequest():
	data={}
	ids = session['login_id']
	q = "SELECT * FROM  request INNER JOIN fuel USING(fuel_id) INNER JOIN fuelstations USING (fuelstation_id) INNER JOIN fuel_categorys USING(category_id) WHERE request.user_id=(select user_id from users where login_id='%s') and request.pay_status!='Paid' " % (ids)
	res=select(q)
	data['req']=res
	return render_template('userview_fuelrequest.html',data=data)

@user.route('/view_orders',methods=['get','post'])
def view_orders():
	data={}
	ids = session['login_id']
	q = "SELECT * FROM  request INNER JOIN fuel USING(fuel_id) INNER JOIN fuelstations USING (fuelstation_id) INNER JOIN fuel_categorys USING(category_id) left join employees using(employee_id) left join works using(request_id) WHERE request.user_id=(select user_id from users where login_id='%s') and request.pay_status='Paid' " % (ids)
	res=select(q)
	data['req']=res
	if 'id' in request.args:
		id = request.args['id']
		q = "update works set  work_status='Received'  where work_id='%s' " % (id)
		update(q)
		return redirect(url_for('user.view_orders'))
	return render_template('userview_orders.html',data=data)

@user.route('/fuel_payment',methods=['get','post'])
def fuel_payment():
	data = {}
	ids = session['login_id']
	id = request.args['id']
	q = "select * from request where request_id='%s'" % (id)
	res = select(q)
	data['amd'] = res
	if 'submit' in request.form:
		cnum = request.form['cnum']
		cname = request.form['cname']
		total_amount = request.form['total']
		q = "insert into payment values(null,(select user_id from users where login_id='%s'),'%s','%s','%s','%s','online')" % (ids, id,cnum,cname,total_amount)
		insert(q)
		q = "update request set pay_status='Paid' where request_id='%s'" % (id)
		update(q)
		flash("Payment Successfully Completed..")
		return redirect(url_for('user.view_fuelrequest'))

	return render_template('usermakefuel_payment.html',data=data)

