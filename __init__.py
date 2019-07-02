from flask import Flask, render_template,redirect, url_for, request
import pymysql.cursors
app = Flask(__name__)
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root123',
                             db='erp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


print ("connect successful!!")


@app.route('/')
def default():
    return redirect(url_for('static', filename='index.html'))


def db_failures():
    return redirect(url_for('static', filename='index.html'))


@app.route('/add_item',methods=['POST', 'GET'])
def add_item():
    flag = ''
    if request.method == 'POST':
        item = request.form['itemname']
        status = request.form['in_out']
        color = request.form['itemcolor']

        with connection.cursor() as cursor:
            try:
                sql = "INSERT INTO Items (item_name,in_out_flag,color) VALUES (%s, %s,%s)"
                a = cursor.execute(sql, (item, status, color))
                print(a)
                connection.commit()
                flag = 'Success'
            except Exception as e:
                flag = "Failure with %s" % e
            finally:
                connection.close()
    if flag == 'Success':
        return redirect(url_for('default'))
    else:
        return render_template("failure.html")


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