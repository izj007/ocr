import requests
from flask import Flask,request,jsonify
from base64 import b64decode

app = Flask(__name__)
@app.route('/', methods=['POST'])
def ocrindex():
	if request.method=='POST':
		import ddddocr
		ocr = ddddocr.DdddOcr()
		data = request.form['image']
		print(data)
		res = ocr.classification(b64decode(data)) 
		return res

if __name__ == "__main__":
	app.run()