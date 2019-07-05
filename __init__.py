from flask import Flask, render_template,redirect, url_for, request
import pymysql.cursors
app = Flask(__name__)
# Connect to the database

def connect_to_db():
    conn = pymysql.connect(host='localhost',
                             user='root',
                             password='root123',
                             db='erp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return conn


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
        connection = connect_to_db()
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


@app.route('/add_purchase')
def add_purchase():
    connection = connect_to_db()
    if connection.open == 1:
        # Populate ledger names from table
        try:
            with connection.cursor() as cursor:
                sql = "SELECT DISTINCT ledger_name FROM persons"
                cursor.execute(sql)
                data = cursor.fetchall()
        except Exception as e:
            return 'Exception'
        cursor.close()
        # Populate item names from table
        try:
            with connection.cursor() as cursor:
                get_items = "SELECT DISTINCT item_name FROM items"
                cursor.execute(get_items)
                items_data = cursor.fetchall()
                connection.close()
                return render_template('add_purchase.html', data=data, items_data=items_data)
        except Exception as e:
            return 'Exception'


@app.route('/add_ledger', methods=['POST', 'GET'])
def add_ledger():
    if request.method == 'POST':
        ledger_name = request.form['ledgername']
        connection = connect_to_db()
        with connection.cursor() as cursor:
            try:
                sql = "INSERT INTO persons (ledger_name) VALUES (%s)"
                cursor.execute(sql, ledger_name)
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


if __name__ == '__main__':
    app.run(debug=True)