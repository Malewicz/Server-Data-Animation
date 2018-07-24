from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class new_variable(FlaskForm):
    def glob():
        return render_template('global.html')

    def variable():
        return render_template('parameter.html')

    def result():
        if request.method == 'POST':
            result = request.form
            return render_template('parameter.html', result=result)
