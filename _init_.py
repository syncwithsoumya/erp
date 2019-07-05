from flask import Flask,render_template,request
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


@app.route('/add_purchase',methods=['POST', 'GET'])
def add_purchase():
    if request.method == 'POST':
        da=request.form['pdate']
        vendor = request.form['vendors']
        iteminkgs = request.form['iteminkg']
        amount = request.form['iteminkgamount']
        iteminnos = request.form['iteminno']


        with connection.cursor() as cursor:
            sql = "INSERT INTO purchase (purchase_date,person,quantity_in_kg,total_amount,item_in_no) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql,(da,vendor,int(iteminkgs),int(amount),int(iteminnos)))
            connection.commit()
            connection.close()

    return render_template("add_purchase.html")



@app.route('/add_new_sell',methods=['POST', 'GET'])
def add_new_sell():
    if request.method == 'POST':
        customer = request.form['cust_name']
        commoditys = request.form['commodity']
        itemqtys = request.form['itemqty']
        itemrates = request.form['itemrate']
        itemamts = request.form['itemamt']

        with connection.cursor() as cursor:
            sql = "INSERT INTO sell (Person,item,quantity,rate,amount) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, (customer, commoditys, int(itemqtys), int(itemrates), int(itemamts)))
            connection.commit()
            connection.close()

    return render_template("add_sell.html")



@app.route('/build',methods=['POST', 'GET'])
def build():
    if request.method == 'POST':
        pois = request.form['poi']
        itemname = request.form['materials']
        itemqtys = request.form['itemqty']
        itemcolorr = request.form['itemcolor']
        itemratee = request.form['itemrate']
        itemamtt = request.form['itemamt']


        with connection.cursor() as cursor:
            sql = "INSERT INTO buildout (build_date,raw_materials,quantity,color,rate,amount) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (pois, itemname, int(itemqtys),itemcolorr,int(itemratee), int(itemamtt)))
            connection.commit()
            connection.close()

    return render_template("build.html")


@app.route('/delete_item',methods=['POST', 'GET'])
def delete_item():
    if request.method == 'POST':
        item = request.form['itemname']

        with connection.cursor() as cursor:
            sql = "DELETE FROM items WHERE item_name = %s"
            cursor.execute(sql,item)
            connection.commit()
            connection.close()


    return render_template("delete_item.html")



@app.route('/delete_ledger',methods=['POST', 'GET'])
def delete_ledger():
    if request.method == 'POST':
        name = request.form['ledgername']

        with connection.cursor() as cursor:
            sql = "DELETE FROM persons WHERE ledger_name = %s"
            cursor.execute(sql,name)
            connection.commit()
            connection.close()


    return render_template("delete_ledger.html")



@app.route('/material_proc_del',methods=['POST', 'GET'])
def material_proc_del():
    if request.method == 'POST':
        qqdate = request.form['qwe']
        vendor = request.form['vendors']

        with connection.cursor() as cursor:
            sql = "DELETE FROM purchase WHERE purchase_date = %s and person = %s"
            cursor.execute(sql, (qqdate,vendor))
            connection.commit()
            connection.close()

    return render_template("del_purchase.html")



@app.route('/del_new_sell',methods=['POST', 'GET'])
def del_new_sell():
    if request.method == 'POST':
        cust_names = request.form['cust_name']
        commoditys = request.form['commodity']


        with connection.cursor() as cursor:
            sql = "DELETE FROM sell WHERE Person = %s and item = %s"
            cursor.execute(sql, (cust_names,commoditys))
            connection.commit()
            connection.close()

    return render_template("del_sell.html")



@app.route('/modify_item',methods=['POST', 'GET'])
def modify_item():
    if request.method == 'POST':
        oldname = request.form['itemname']
        newname = request.form['newitemname']


        with connection.cursor() as cursor:
            sql = "UPDATE items set item_name=%s where item_name=%s"
            cursor.execute(sql,(newname,oldname))
            connection.commit()
            connection.close()

    return render_template("modify_item.html")


@app.route('/modify_ledger',methods=['POST', 'GET'])
def modify_ledger():
    if request.method == 'POST':
        oldname = request.form['ledgername']
        newname = request.form['newledgername']


        with connection.cursor() as cursor:
            sql = "UPDATE persons set ledger_name=%s where ledger_name=%s"
            cursor.execute(sql,(newname,oldname))
            connection.commit()
            connection.close()

    return render_template("modify_ledger.html")













if __name__ == '__main__':
    app.run(debug=True)

