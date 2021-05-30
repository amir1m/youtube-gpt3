from flask import Flask, render_template,jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, URL
from main import get_video_text, create_summary

app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY']='LongAndRandomSecretKey'

class InputForm(FlaskForm):
    yturl = StringField(label=('Enter YouTube Video URL:'), validators=[DataRequired(),URL()])
    submit = SubmitField(label=('Submit'))

@app.route('/')
def home():
    form = InputForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('summarize'))

@app.route('/summarize/', methods=(['GET', 'POST']))
def summarize():
    # form = InputForm()
    # if form.validate_on_submit():
        # text = get_video_text(form.yturl.data)
        # summary = create_summary(text)
        # s_summary = create_summary(text)
        # return jsonify(data={'first_summary':summary, 'second_summary':s_summary})
    return jsonify(data={'first_summary':"summry1", 'second_summary':"summary2"})
    return jsonify(data=form.errors)

if __name__ == '__main__':
    app.run(debug=True)
