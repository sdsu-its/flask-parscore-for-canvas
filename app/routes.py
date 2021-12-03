from app import app
from flask import Flask,flash, request,Response, redirect,session, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
from requests_toolbelt import MultipartEncoder
import requests
import zipfile
DOWNLOAD_FOLDER = '/tmp'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'4234mdfsjnfsd3342'
from app import pandasParscoreParser
from flask_dropzone import Dropzone
import time
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
#app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.csv'
app.config['DROPZONE_REDIRECT_VIEW'] = 'error'
app.config.update(
    # Flask-Dropzone config:
    DROPZONE_MAX_FILE_SIZE=8,
    DROPZONE_MAX_FILES=1,
    DROPZONE_PARALLEL_UPLOADS=20,  # set parallel amount
    DROPZONE_UPLOAD_MULTIPLE=False,  # enable upload multiple
)
dropzone = Dropzone(app)

def process_file(path, filename):
    pandasParscoreParser.parscoreParser(path)
import thread
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #session.clear()
    #session['filenames']=[]
    if os.path.exists('/tmp/'+filename):
        os.rename('/tmp/'+filename,'/tmp/converted-'+filename)
        thread.start_new_thread( delay_delete, (filename, ) )
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], filename='converted-'+filename, as_attachment=True)

def delay_delete(path):
    time.sleep(30)
    os.remove('/tmp/converted-'+path)
    return
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/results',methods=['GET','POST'])
def results():
     if 'filename' in session:
     	name=session['filename']
     	session.clear()
     	return render_template('results.html',file=name)
     else:
         return redirect(url_for('index'))
@app.route('/error',methods=['GET','POST'])
def error():
    if request.method == 'POST':
       for key, f in request.files.items():
           if key.startswith('file'):
               try:
                   f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
                   process_file(os.path.join(app.config['UPLOAD_FOLDER'], f.filename), f.filename)
               except:
                   os.remove(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
                   return render_template('error.html')
               session['filename']=f.filename
               return render_template('results.html')
    if 'filename' in session:
        #for files in session['filenames']:
        return redirect(url_for('results'))
    #return redirect(url_for('index'))
    return render_template('error.html')
