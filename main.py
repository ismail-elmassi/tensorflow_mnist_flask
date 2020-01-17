import os
import json
from flask import Flask, render_template,request,redirect,url_for, send_from_directory    
from werkzeug.utils import secure_filename
from dpl_model.predict_mnist import predict_image as model_predict

UPLOAD_FOLDER = 'upload_files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		print("requestfiles", type(request.files))
		if 'file' not in request.files:
			return redirect("/error")

		file = request.files['file']
		
		if file.filename == '':
			return redirect('/error')

		if 'file' in request.files:
			file = request.files['file']
			filename = secure_filename(file.filename)
			file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(file_path)
			classe = model_predict(file_path)
			image_uploaded = {
                'file': 'uploads/' + filename,
                'classe': str(classe[0])}
			messages = json.dumps(image_uploaded)
			return redirect(url_for('image_predict', messages=messages))

	return render_template("hello.html")

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/predict')
def image_predict():
    messages = request.args['messages']
    messages = json.loads(messages)
    return render_template('predict.html', image=messages['file'], predicted_classe=messages['classe'])

# @app.route("/error")
# def error():
# 	return render_template('error.html')

@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)