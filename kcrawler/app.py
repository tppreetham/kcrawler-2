from flask import Flask, request, render_template, Response
from flaskext import mysql
import mysql.connector

# global reciever

app = Flask(__name__)

# con = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = '',
#     database = 'kcrawler'
# )


# cursor = con.cursor()

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/submitkeyword/', methods = ['POST'])
def submitkeyword():
    from scrapy import cmdline
    import os 

    filename = 'response.json'
    if os.path.exists(filename):
	    os.remove(filename)

    name = request.form['name']
    if (" " in name):
        print("entered")
        name = name.replace(" ", "-")

    print("name ", name)
    
    cmd="scrapy crawl mainspider -a keyword="+name+" -o response.json"
    print(cmd)
    cmdline.execute(cmd.split())

    return "OK"
    
if __name__ == '__main__':
    app.run(debug=True)