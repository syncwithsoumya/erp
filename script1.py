from flask import Flask,render_template,request
import pymysql.cursors


app=Flask(__name__)



@app.route('/')
def home():
    return render_template("home.html")


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root123',
                             db='erp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


print ("connect successful!!")

@app.route('/add',methods=['POST', 'GET'])
def about():

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




if __name__ == '__main__':
    app.run(debug=True)
