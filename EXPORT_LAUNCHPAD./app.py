from flask import Flask, render_template, request, redirect, session
import pymysql

app = Flask(__name__)
app.secret_key = "export_launchpad_secret"

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root123",
    database="export_launchpad",
    cursorclass=pymysql.cursors.DictCursor
)

# ---------------- SIGNUP ----------------
@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        db.commit()

        return redirect("/login")

    return render_template("signup.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # For hackathon demo, just redirect to home
        return redirect("/home")

    return render_template("login.html")


#-------------------HOME---------------------
@app.route("/home")
def home():
    return render_template("home.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard(): 
    return render_template("dashboard.html")


# ---------------- CLICKABLE BOX PAGES ----------------
@app.route("/niche_products")
def niche_products():
    return render_template("niche_products.html")

@app.route("/profit_snapshot")
def profit_snapshot():
    return render_template("profit_snapshot.html")

@app.route("/risk_radar")
def risk_radar():
    return render_template("risk_radar.html")

@app.route("/smart_docs")
def smart_docs():
    return render_template("smart_docs.html")

#----------------smart docs---------------
@app.route("/iec")
def iec():
    return render_template("iec.html")

@app.route("/proforma_invoice")
def proforma_invoice():
    return render_template("proforma_invoice.html")

@app.route("/packing_list")
def packing_list():
    return render_template("packing_list.html")

@app.route("/bill_of_lading")
def bill_of_lading():
    return render_template("bill_of_lading.html")

@app.route("/coo")
def coo():
    return render_template("coo.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

