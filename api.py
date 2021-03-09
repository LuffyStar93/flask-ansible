from flask import *
from db import *


app = Flask(__name__)

@app.route('/')
def welcome(): 
    return redirect(url_for('home'))  

@app.route('/home')
def home(): 
    return render_template("index.html")


@app.route('/inc')
def increment(): 
    cur.execute("UPDATE mytable SET id = id + 1")
    conn.commit()
    wait_time = 2000
    return f"<html><body><p>ID succesfully increase </br> You will be redirected in 2 seconds</p><script>var timer = setTimeout(function() {{window.location='/home'}}, { wait_time });</script></body></html>"


@app.route('/id')
def showId(): 
    cur.execute("SELECT id FROM mytable")
    result = cur.fetchall()
    return str(result[0][0]) 

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3000, debug = True)
