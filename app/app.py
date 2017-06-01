from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm

class LambdaButton(FlaskForm):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reallybadpassword'

@app.route('/', methods=('GET','POST'))
def index():
    form = LambdaButton()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

