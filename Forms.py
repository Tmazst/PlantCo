from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField,BooleanField, SelectField,DateField, URLField
from wtforms.validators import DataRequired,Length,Email, EqualTo, ValidationError
from flask_login import current_user
from flask_wtf.file import FileField , FileAllowed
# from wtforms.fields.html5 import DateField,DateTimeField


class Register(FlaskForm):

    name = StringField('name', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=64)])
    confirm = PasswordField('confirm', validators=[DataRequired(),EqualTo('password'), Length(min=8, max=64)])
    contacts = StringField('Contact(s)', validators=[Length(min=8, max=64)])
    zip_code = StringField('Zip Code / Postal Code', validators=[Length(min=0, max=64)])
    address = StringField('Physical Address', validators=[DataRequired(), Length(min=8, max=100)])
    image_pfl = FileField('Profile Image', validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField('Create Account!')

    def validate_email(self,email):
        from app import db, User,app

        # with db.init_app(app):
        user_email = User.query.filter_by(email = self.email.data).first()
        if user_email:
            return ValidationError(f"Email already registered in this platform")

class Update_account_form(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])


class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=64)])
    submit = SubmitField('Login')


class Contact_Form(FlaskForm):

    name = StringField('name')
    email = StringField('email', validators=[DataRequired(),Email()])
    subject = StringField("subject")
    message = TextAreaField("Message",validators=[Length(min=8, max=2000)])
    submit = SubmitField("Sumbit")


class Reset_Request(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])

    reset = SubmitField('Submit')

    # def validate_email(self,email):
    #     user = user.query.filter_by