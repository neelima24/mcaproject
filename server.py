from flask import Flask, request, render_template, session, redirect, url_for, flash
from datetime import datetime
import pymysql
import os
import barcode

UPLOAD_FOLDER = '/home/neelima/Desktop/Stock_mng_main/static/barcodeimage/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','svg'}
barcode.PROVIDED_BARCODES= {'code39', 'code128', 'ean', 'ean13', 'ean8', 'gs1', 'gtin','isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca'}
app = Flask(__name__)

app.secret_key = 'some secret key'
#mysql=MySQL()
connection=pymysql.connect(
    host='localhost',
    user='testuser',
    password='test',
    db='sample_db',
    port=3307,
    use_unicode=True,
    charset="utf8"
)
 

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login/")
def login():
    return render_template('login.html')


@app.route("/login/",methods=['POST'])
def login_page():
    username=request.form['username']
    password=request.form['password']
    
    try:
        
          cursor=connection.cursor()
          res = cursor.execute("select * from login where username='"+username+"' and password='"+password+"'")
          if not res:
            error="incorrect username or password"
            flash("Invalid Login")
            return render_template("/login.html",error=error)
          else:
            data1=cursor.fetchall()
            for row in data1:
                utype=row[3]
                if utype=="admin":
                    session['logged in']=True
                    session['utype']="admin"
                    session['id']=row[0]
                    return render_template("admin_home_page.html")
                else:
                    session['logged in']=True
                    session['utype']="admin"
                    session['id']=row[0]
                    return render_template("guest_home.html")


    except Exception as e:
        return (str(e))




@app.route("/admin")
def admin():
    return render_template('admin_home_page.html')
    
@app.route("/forgot")
def forgot():
    return render_template('forgot_password.html')


@app.route("/stockin")
def stockin():
    return render_template('stock_inventory.html')


@app.route("/addstock")
def addstock():
    return render_template('add_stock.html')

@app.route("/addstock/",methods=['POST'])
def stockadd():
    stockname=request.form['stockname']
    num_items=request.form['noitems']
    stock_type=request.form['stocktype']
    date_time=str(datetime.now())
    dept=request.form['dept']
    room_no=request.form['roomno']
    particulars =request.form['particulars']
    bill_no=request.form['billno']
    total_amt=request.form['amount']
    warranty=request.form['warranty']
    status='working'
    '''number = 5901234123457 
    number = str(number)

    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(number, writer=ImageWriter())
    stock_code = ean.save('barcode')'''
    x=0
    while(x < int(num_items)):        
        
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN('5901234123457')
        #ean = barcode.get('ean13', '123456789102')
        cod=str(ean.get_fullcode())
        #stock_code = ean.save('ean13')
        stock_code=ean.save('ean13_barcode')
        barcodeimage = "barcodeimage/" + stock_code
        #insqry = "insert into dept_stock(stock_code,stock_name,stock_type,date_time,dept,room_no,particulars,bill_no,total_amt,warranty,barcodeimage,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        insqry = """INSERT INTO dept_stock (stock_code,stock_name,stock_type,date_time,dept,room_no,particulars,bill_no,total_amt,warranty,barcodeimage,status) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s) """
        recordTuple = (cod,stockname, stock_type, date_time, dept, room_no, particulars, bill_no,total_amt,warranty,barcodeimage,status)
        cursor=connection.cursor()
        res=cursor.execute(insqry,recordTuple)
        connection.commit()
        x=x+1

    if res==1:
        result="successfully inserted"
        return render_template("/add_stock.html",result=result)
    else:
        result="some error occured"
        return render_template("/add_stock.html",result=result)

@app.route("/upstock")
def upstock():
    return render_template('update_stock.html')

@app.route("/maintenance")
def maintenance():
    return render_template('maintenance.html')


@app.route("/report")
def report():
    return render_template('report.html')

@app.route("/report_all.html")
def reportall():
    cursor=connection.cursor()
    cursor.execute("select * from login")
    data1=cursor.fetchall()
    return render_template('report_all.html', data=data1)
   

@app.route("/report_serviced.html")
def reportserviced():
    cursor=connection.cursor()
    cursor.execute("select * from service")
    data1=cursor.fetchall()
    return render_template('report_serviced.html', data=data1)
   

@app.route("/report_damaged.html")
def reportdamaged():
    cursor=connection.cursor()
    cursor.execute("select * from dept_stock where status='not working'")
    data1=cursor.fetchall()
    return render_template('report_damaged.html', data=data1)
    
@app.route("/report_warranty.html")
def report_warranty():
    cursor=connection.cursor()
    cursor.execute("select * from dept_stock")
    data1=cursor.fetchall()
    return render_template('report_warranty.html', data=data1)

app.route("/pdff")
def pdff():
    return render_template('pdf_template.html')


if __name__ == '__main__':
    app.run(debug=True)
