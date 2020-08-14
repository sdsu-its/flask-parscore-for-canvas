

from app import app
from flask import Flask, request,Response, redirect,session, url_for, render_template, send_from_directory
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
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
#app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.csv'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
app.config.update(
    # Flask-Dropzone config:
    DROPZONE_MAX_FILE_SIZE=8,
    DROPZONE_MAX_FILES=50,
    DROPZONE_PARALLEL_UPLOADS=20,  # set parallel amount
    DROPZONE_UPLOAD_MULTIPLE=True,  # enable upload multiple
)
dropzone = Dropzone(app)

def process_file(path, filename):
    pandasParscoreParser.parscoreParser(path)
    #print(filename)
import thread
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    if os.path.exists('/tmp/'+filename):
        thread.start_new_thread( delay_delete, (filename, ) )
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], filename=filename, as_attachment=True)

def delay_delete(path):
    print "started"
    time.sleep(10)
    print "trying to delete"
    os.remove('/tmp/'+path)
    print "done"
    return
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/results',methods=['GET','POST'])
def results():
    if 'filenames' not in session:
        session['filenames']=[]
    if request.method == 'POST':
       session.clear()
       session['filenames']=[]
       for key, f in request.files.items():
           if key.startswith('file'):
               f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
               process_file(os.path.join(app.config['UPLOAD_FOLDER'], f.filename), f.filename)
               session['filenames'].append(f.filename)
    #session['filenames'].append('impossible')
    if session['filenames'] == []:
        a='a'
    elif len(session['filenames'])==1:
        for files in session['filenames']:
            if not files=='impossible':
                return redirect(url_for('uploaded_file',filename=files))
  
    else:
        os.chdir('/tmp/')
        zipf = zipfile.ZipFile('results.zip','w', zipfile.ZIP_DEFLATED)
        for files in session['filenames']:
            if not files=='impossible':
                zipf.write(files)
        zipf.close()
        return redirect(url_for('uploaded_file',filename='results.zip'))
    session.clear()
    session['filenames']=[]

    #files=find_csv_filenames(path_to_dir=app.config['UPLOAD_FOLDER'])
    #for file in files:
         #return redirect(url_for('uploaded_file', filename=file))
    #return render_template('index.html')
    return render_template('results.html')
