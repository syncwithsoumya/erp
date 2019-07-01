from flask import Flask,render_template,request
import datetime
import pymysql.cursors


app=Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")



# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root123',
                             db='erp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


print ("connect successful!!")



@app.route('/add_item',methods=['POST', 'GET'])
def add_item():

    if request.method == 'POST':
        item = request.form['itemname']
        status = request.form['in_out']
        color = request.form['color']

        with connection.cursor() as cursor:
            sql = "INSERT INTO Items (item_name,in_out_flag,color) VALUES (%s, %s,%s)"
            cursor.execute(sql, (item, status,color))
            connection.commit()
            connection.close()

    return render_template("add_item.html")




@app.route('/add_ledger',methods=['POST', 'GET'])
def add_ledger():

    if request.method == 'POST':
        ledname = request.form['ledgername']


        with connection.cursor() as cursor:
            sql = "INSERT INTO persons (ledger_name) VALUES (%s)"
            cursor.execute(sql, (ledname))
            connection.commit()
            connection.close()

    return render_template("add_ledger.html")









if __name__ == '__main__':
    app.run(debug=True)

