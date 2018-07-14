from flask_wtf import FlaskForm
import wtforms


class LoginForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[wtforms.validators.data_required()])
    password = wtforms.PasswordField('Password', validators=[wtforms.validators.data_required()])
    remember_me = wtforms.BooleanField('Remember Me')
    login = wtforms.SubmitField('Log In')



