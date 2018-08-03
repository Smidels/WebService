from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, DeleteForm
from app.models import User



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
	users = User.query.all()
	register_form = RegistrationForm()
	delete_form = DeleteForm()

	if register_form.validate_on_submit():
		username = register_form.username.data
		email = register_form.email.data
		password = register_form.password.data
		new_user = User(username=username,
					email=email,
					password_hash=User.set_password(password))
		db.session.add(new_user)
		db.session.commit()
		flash('You register new user: "{}".'.format(username))
		return redirect(url_for('index'))

	elif delete_form.validate_on_submit():
		user = User.query.filter_by(username=delete_form.name_del_user.data).first()
		if user is None:
			flash('Invalid username or password')
			redirect(url_for('index'))
		elif user.username == 'admin':
			flash("You can't delete the admin page!")
			redirect(url_for('index'))
		else:
			db.session.delete(user)
			db.session.commit()
			flash('You delete user: "{}".'.format(user.username))
			return redirect(url_for('index'))
	return render_template(
						'index.html', title='User Page',
						users=users, form1=register_form, 
						form2=delete_form
						)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		form = LoginForm()
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not User.check_password(form.password.data, user.password_hash):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))