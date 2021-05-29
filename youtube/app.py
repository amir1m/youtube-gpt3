from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, URL


app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY']='LongAndRandomSecretKey'

class InputForm(FlaskForm):
    yturl = StringField(label=('Enter YouTube Video URL:'), validators=[DataRequired(),URL()])
    submit = SubmitField(label=('Submit'))

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = InputForm()
        if form.validate_on_submit():
            return f'''<h1> Summary for {form.yturl.data} </h1>'''
        return render_template('index.html', form=form)
