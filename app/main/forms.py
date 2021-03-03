from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User
from flask import request


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class ResourceForm(FlaskForm):
    nom = TextAreaField(_l('Nom o títol del recurs:'), validators=[DataRequired()])
    tipus = SelectField(_l('Tipus de recurs:'),
                        choices=[
                            ('Blog d\'activitats', 'Blog d\'activitats'),
                            ('Activitat', 'Activitat'),
                            ('Concepte', 'Il·lustració de conceptes'),
                            ('Lloc d\interès', 'Lloc d\'interès'),
                            ('Altres', 'Altres')
                        ],
                        validators=[DataRequired()])
    descripcio = TextAreaField(_l('Descripció:'), validators=[DataRequired()])
    idioma = SelectField(_l('Idioma:'),
                         choices=[('Català', 'Català'), ('Castellà', 'Castellà'), ('Anglès', 'Anglès'), ('Altres', 'Altres')],
                         validators=[DataRequired()])
    link = TextAreaField(_l('Enllaç:'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

