import pytesseract as pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from flask import Flask,render_template,request

import pytesseract
from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = '/static/imgs/'
ocr_app=Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ocr(file):

    # Open image using PIL
    image = Image.open(file)
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)
    # Get the current size of the image
    #width, height = image.size
    # Resize the image
    #new_size = (int(width/2), int(height/2))
    image = image.resize((250,250))
    # Save the image
    image.save('static/imgs/temp.png')
    # Return extracted text
    return text

@ocr_app.route('/',methods=['GET','POST'])
def upload_img():
    if request.method == "POST":
        if 'file' not in request.files:

            return render_template('upload_img.html',msg='Select a file')
        file = request.files['file']
        if file.filename == '':

            return render_template('upload_img.html',msg='Select a file')
        if file and allowed_file(file.filename):
            extracted_text = ocr(file)
            return render_template('upload_img.html', msg='Successfully processed',
                                   extracted_text=extracted_text,img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload_img.html')


if __name__=='__main__':
    ocr_app.run(debug=True)
