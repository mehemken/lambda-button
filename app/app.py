from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from message import ping_lambda

class LambdaButton(FlaskForm):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reallybadpassword'

@app.route('/', methods=('GET','POST'))
def index():
    form = LambdaButton()
    if form.validate_on_submit():
        new_value = ping_lambda()
        return redirect(f'/{new_value}')
    return render_template('index.html', form=form)

@app.route('/<value>', methods=('GET','POST'))
def new(value):
    form = LambdaButton()
    if form.validate_on_submit():
        new_value = ping_lambda()
        return redirect(f'/{new_value}')
    return render_template('index.html', form=form, value=value)

if __name__ == '__main__':
    app.run(debug=True)

