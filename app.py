from flask import Flask, render_template, url_for, request
import ibm_db

app = Flask (__name__)

conn = ibm_db.connect("database=bludb; hostname = 98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud; PORT=30875;UID=kzk97177; PWD=NeEs6NtGALgvcyyK ; SECURITY= ssl; SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt", "","" )
print(ibm_db.active(conn))





@app.route("/")
def index():
        return render_template("index.html")

@app.route("/contact")
def contact():
        return render_template("contact.html")
        
@app.route("/index")
def s():
        return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
        if request.method == "POST":
               uname = request.form['username']
               pword = request.form['password']
               print (uname, pword)
               sql = 'SELECT * FROM REGISTER_FDP WHERE USERNAME =? AND PASSWORD=? '
               stmt=ibm_db.prepare(conn,sql)
               ibm_db.bind_param(stmt,1,uname)
               ibm_db.bind_param(stmt,2,pword)
               ibm_db.execute(stmt)
               out= ibm_db.fetch_assoc(stmt)
               print(out)
               if out:
                      role = out['ROLE']
                      if role == 0:
                        return render_template("admin.html")
                      elif role == 1:
                             return render_template("student.html")
                      elif role ==2:
                             return render_template("faculty.html")
                      
               else:
                      msg = "INVALID Credentials"
                      return render_template("login.html", login_message = msg)
                        
        return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
       if request.method == "POST":
               name = request.form['name']
               uname = request.form['username']
               email = request.form['email']
               pword = request.form['password']
               role = request.form['role']
               print (name, pword)

if __name__=="__main__":
    app.run(debug= True, host="0.0.0.0")