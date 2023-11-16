from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/adminview_user',methods=['get','post'])
def adminview_user():
	data = {}
	q = "select * from Users"
	res = select(q)
	data['users'] = res
	return render_template('adminview_user.html',data=data)

@admin.route('/adminview_fuelstations',methods=['get','post'])
def adminview_fuelstations():
	data = {}
	q = "select * from fuelstations inner join login ON fuelstations.login_id = login.login_id where status!='Accept';"
	res = select(q)
	data['fuel'] = res
	data['count'] = len(res)
	if 'id' in request.args:
		id=request.args['id']
		q="update login set  status='Accept'  where login_id='%s' "%(id)
		update(q)
		return redirect(url_for('admin.adminview_fuelstations'))
	elif 'id1' in request.args:
		id1=request.args['id1']
		q="update login set  status='Reject'  where login_id='%s' "%(id1)
		update(q)
		return redirect(url_for('admin.adminview_fuelstations'))
	return render_template('adminview_fuelstations.html',data=data)

@admin.route('/adview_appr_fuelstations',methods=['get','post'])
def adview_appr_fuelstations():
	data = {}
	q = "select * from fuelstations inner join login ON fuelstations.login_id = login.login_id where status='Accept';"
	res = select(q)
	data['Afuel'] = res
	return render_template('adview_appr_fuelstations.html',data=data)

@admin.route('/adminadd_fuelcateg',methods=['get','post'])
def adminadd_fuelcateg():
	if 'submit' in request.form:
		categoryname=request.form['cname']
		q="select * from fuel_categorys where categoryname='%s'"%(categoryname)
		res=select(q)
		if len(res)>0:
			flash("The Fuel Category Is Already Exists")
		else:
			q="insert into fuel_categorys  values(null,'%s')"%(categoryname)
			insert(q)
			flash("Category Added")
			return redirect(url_for('admin.adminview_fuelcateg'))

	return render_template('adminadd_fuelcategory.html')

@admin.route('/adminview_fuelcateg',methods=['get','post'])
def adminview_fuelcateg():
	data = {}
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None

	if action == 'delete':
		q = "delete from fuel_categorys where category_id='%s'" % (id)
		delete(q)
		return redirect(url_for('admin.adminview_fuelcateg'))

	if action == 'update':
		q = "select * from fuel_categorys where category_id='%s'" % (id)
		res = select(q)
		data['updatecat'] = res

	if 'update' in request.form:
		categoryname = request.form['cname']
		q = "update fuel_categorys set categoryname='%s' where category_id='%s'" % (categoryname, id)
		update(q)
		return redirect(url_for('admin.adminview_fuelcateg'))

	q = "select * from fuel_categorys"
	res = select(q)
	data['Cat'] = res
	return render_template('adminview_fuelcategorys.html',data=data)


@admin.route('/adminview_newfb',methods=['get','post'])
def adminview_newfb():
	data = {}
	q = "select * from feedback inner join users using(user_id)"
	res = select(q)
	data['fb'] = res
	j = 0
	for i in range(1, len(res) + 1):
		if 'submit' + str(i) in request.form:
			reply = request.form['reply' + str(i)]
			q = "UPDATE feedback SET reply='%s' WHERE feedback_id='%s'" % (reply, res[j]['feedback_id'])
			update(q)
			flash("send message")
			return redirect(url_for('admin.adminview_newfb'))

		j = j + 1

	return render_template('adminview_newfeedback.html',data=data)

@admin.route('/adminview_repliedfb',methods=['get','post'])
def adminview_repliedfb():
	data = {}
	q = "select * from feedback inner join users using(user_id) "
	res = select(q)
	data['fb'] = res
	return render_template('adminview_repliedfeedback.html',data=data)











