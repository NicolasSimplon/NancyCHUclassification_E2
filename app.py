import os
from pydoc import classname

from flask import Flask, render_template, request, redirect

from inference import get_prediction
from commons import format_class_name                                            #for the print 33 et 34

import sys

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'                                         #direct files to the folder uploads which was created


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        print(request.files)                                                    # print to view request file
        if 'files[]' not in request.files:                                      # change from one file to a list
            print("redirection")
            return redirect(request.url)
        
        files = request.files.getlist('files[]')                                # request the list
        if not files:
            return
        resultats_prediction=[]                                                 # return empty list
        for file in files:                                                      # from the loop
            img_bytes = file.read()
            class_id, class_name=get_prediction(image_bytes=img_bytes) 
            print(class_name, class_id)                                         # print the result of each class
            resultats_prediction.append((class_name, class_id))                 # add the result in the list
            print("control1 : ", app.config['UPLOAD_FOLDER'], file=sys.stderr)
            print("control2 : ", class_name, file=sys.stdout)
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], class_name) # create the variable output_path to make code below more readable
            if not os.path.isdir(output_path):                                  # if there is no folder with the output name, create one  
                os.mkdir(output_path)
            file.stream.seek(0)
            file.save(os.path.join(output_path, file.filename))                 # save to the created folder upload
        return render_template('result.html', resultats=resultats_prediction)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

