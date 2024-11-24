from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
class UploadForm(FlaskForm):
    image = FileField('Image', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Upload')
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    
    if form.validate_on_submit():
        file = form.image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Here, you might want to save the comment in a database or a file
        # For simplicity, we won't persist comments in this example
        
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form, images=images)

if __name__ == '__main__':
    app.run(debug=True)
