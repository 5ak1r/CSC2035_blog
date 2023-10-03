from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Length, DataRequired, EqualTo, NoneOf, Regexp


class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(),
                                       Email(message="Invalid email address"),
                                       NoneOf(['<', '&', '%'])
                                       ])
    password = PasswordField(validators=[DataRequired(),
                                         NoneOf(['<', '&', '%']),
                                         Length(min=8, max=15),
                             Regexp(r'(?=.*\d)(?=.*[a-z])',
                                    message="Password must contain one digit and one lowercase letter")
                                         ])
    confirm_password = PasswordField(validators=[DataRequired(),
                                                 EqualTo('password',
                                                         message="Passwords must match")
                                                 ])

    submit = SubmitField()
