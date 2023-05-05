from flask import Flask,render_template,request
import requests
import string
from bs4 import BeautifulSoup
from collections import defaultdict
import re
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/receiveFormData',methods=['POST'])
def extract_Data():
    url = request.form['url']
    page= requests.get(url)
    #if(page.status_code==2000):
    htmlContent = page.content
    soup= BeautifulSoup(htmlContent, 'html.parser')
    text= str(soup.get_text())
    counts = defaultdict(int)
    for word in re.findall('\w+', text):
        counts[word] += 1
    
    data = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return render_template('extractData.html',data=data)

    
        
if __name__== "__main__":
    app.run(debug=True)