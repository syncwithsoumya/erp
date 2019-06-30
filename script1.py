from flask import Flask,render_template,request
import pyodbc
conn= pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=LAPTOP-GQVL76QU\SQLEXPRESS;'
    r'DATABASE=Dberp;'
    r'Trusted_Connection=yes;'
)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/add/',methods=['GET','POST'])
def about():
    if request.method == 'POST':
        userDetails=request.form
        item=userDetails['itemname']
        status=userDetails['in_out']
        color=userDetails['color']
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Dberp.dbo.Erpadd(Itemname,Status,Color) VALUES(?,?,?)',(item,status,color))
        conn.commit()
        cursor.close()
        return ('success')
    return render_template("add_item.html")



if __name__ == '__main__':
    app.run(debug=True)