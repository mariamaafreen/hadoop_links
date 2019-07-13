from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('links.db', check_same_thread=False)

@app.route('/')
def home():
    c = conn.execute("select * from hadoop")

    return render_template('view.html', datas = c.fetchall())

if __name__ =='__main__':
    app.run(debug=True)
