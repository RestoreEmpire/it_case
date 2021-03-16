from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Required
from application.models import Users, Positions


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя',validators=[DataRequired()])
    password = PasswordField('Пароль',validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя',validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Имя пользователя занято, выберете другое')

    def validate_email(self, email):
        email = Users.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Укажите другую электронную почту')


class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя',validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    position = SelectField('Должность', validators=[DataRequired()],coerce=int)
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    patronym = StringField('Отчество',  validators=[DataRequired()])
    submit = SubmitField('Подтвердить')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = Users.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Используйте другое имя пользователя')