from flask import Flask, request, render_template, session, redirect, url_for, flash
from datetime import datetime
import pymysql
import os
import barcode

UPLOAD_FOLDER = './static/barcodeimage/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','svg'}
barcode.PROVIDED_BARCODES= {'code39', 'code128', 'ean', 'ean13', 'ean8', 'gs1', 'gtin','isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    stock_code=request.form['stockcode'] #code given by admin
    num_items=request.form['noitems']
    stock_type=request.form['stocktype']
    date_time=str(datetime.now().strftime("%d%m%Y%H%M%S"))
    dept=request.form['dept']
    room_no=request.form['roomno']
    particulars =request.form['particulars']
    bill_no=request.form['billno']
    total_amt=request.form['amount']
    warranty=request.form['warranty']
    status='working'
    command="""select stock_id from dept_stock ORDER BY stock_id DESC LIMIT 1"""
    cursor=connection.cursor()
    cursor.execute(command)
    row = cursor.fetchone()

    if len(res) >0:
        bvalue=row
    else:
        bvalue='01'


    x=0
    while(x < int(num_items)):        
        
        EAN = barcode.get_barcode_class('ean13')

        codevalue=str(datetime.now().strftime("%d%m%Y%H"))+bvalue
        ean = EAN(codevalue)
        #ean = barcode.get('ean13', '123456789102')
        bcod_value=str(ean.get_fullcode())
        stock_code=stock_code+bvalue
        #stock_code = ean.save('ean13')
        barcodeimage=ean.save(UPLOAD_FOLDER + (date_time + 'barcode'))
        #barcodeimage = "./static/barcodeimage/" + stock_code
        #insqry = "insert into dept_stock(stock_code,stock_name,stock_type,date_time,dept,room_no,particulars,bill_no,total_amt,warranty,barcodeimage,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        insqry = """INSERT INTO dept_stock (stock_code,stock_name,stock_type,date_time,dept,room_no,particulars,bill_no,total_amt,warranty,barcode_value,barcodeimage,status) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s) """
        recordTuple = (stock_code,stockname, stock_type, date_time, dept, room_no, particulars, bill_no,total_amt,warranty,bcod_value,barcodeimage,status)
        cursor=connection.cursor()
        res=cursor.execute(insqry,recordTuple)
        connection.commit()
        x=x+1
        bvalue=bvalue+1
       
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
