from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, URL
from main import get_video_text, create_summary

app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY']='LongAndRandomSecretKey'

class InputForm(FlaskForm):
    yturl = StringField(label=('Enter YouTube Video URL:'), validators=[DataRequired(),URL()])
    submit = SubmitField(label=('Submit'))

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = InputForm()
        if form.validate_on_submit():
            text = get_video_text(form.yturl.data)
            summary = create_summary(text)
            s_summary = create_summary(text)
            return f'''<h1> First summary</h1>{summary}
                            <p><h2>Second summary</h2>{s_summary}'''
        return render_template('index.html', form=form)
