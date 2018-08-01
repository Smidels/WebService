from flask_wtf import FlaskFrom
from wtform import StringField, PasswordField, BooleanField, SubmitField
from wtform.validators import DataRequired


class LoginForm(FlaskFrom):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	rememder_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')