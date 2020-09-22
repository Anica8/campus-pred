
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.validators import ValidationError

class registrationForm(FlaskForm):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(), EqualTo('pass_confirm', message='Password did not match!!')])
    pass_confirm = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_username_stud(self, field):
        if student.query.filter_by(username=field.data).first():
            raise ValidationError("Password already there !!!")

    def check_username_rec(self, field):
        if recruiter.query.filter_by(username=field.data).first():
            raise ValidationError("Password already there !!!")

    def check_username_comp(self, field):
        if company.query.filter_by(username=field.data).first():
            raise ValidationError("Password already there !!!")


class loginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('LogIn')

class companyappr(FlaskForm):
    companyname = StringField('company name',validators=[DataRequired()])
    companyinfo = TextAreaField('Type the company info',validators=[DataRequired()])
    submit =SubmitField('requst approval')

class predicform(FlaskForm):
    label1 = StringField('label1', Validators=[DataRequired()])
    label2 = StringField('label2', Validators=[DataRequired()])
    label3 = StringField('label3', Validators=[DataRequired()])
    label4 = StringField('label4', Validators=[DataRequired()])
    label5 = StringField('label5', Validators=[DataRequired()])
    label6 = StringField('label6', Validators=[DataRequired()])
    label7 = StringField('label7', Validators=[DataRequired()])
    label8 = StringField('label8', Validators=[DataRequired()])
    label9 = StringField('label9', Validators=[DataRequired()])
