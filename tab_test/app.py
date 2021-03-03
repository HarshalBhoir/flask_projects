from flask import Flask, make_response, request, render_template,jsonify

import tablib
import os
import io
# from io import StringIO
import csv
import pandas as pd
import numpy as np
import re
import os
from werkzeug.utils import secure_filename
 
app = Flask (__name__)



@app.route('/')
def form():
    return render_template('index.html')

@app.route('/data', methods=['GET','POST'])    
def another_page():
    if request.method == 'POST':

        file = request.files['csvfile']
        if not file:
            return "No file"

        
        filename = secure_filename(file.filename)
        file_path2 = os.path.join("uploads", filename)
        file.save(file_path2)
        file_path22 = str(file_path2)

        # with open(filename) as csvfile: 
        #   csvfile = csv.reader(filename)
        #   data = []
        #   for row in csvfile:
        #       print(row)

        
        table = pd.read_csv(file_path22)
        return render_template("index.html", data=table.to_html())
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')


# @app.route('/')    
# def another_page():
#     table = pd.read_csv("email.csv")
#     return render_template("index.html", data=table.to_html())
 
# if __name__ == "__main__":
#     app.run()
