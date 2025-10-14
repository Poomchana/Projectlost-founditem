from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os

# --- ตั้งค่า Flask ---
app = Flask(__name__, template_folder='frontend', static_folder='frontend/static')
app.secret_key = 'super_secret_key'  # จำเป็นสำหรับ session

# --- ฟังก์ชันเชื่อม Database ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="รหัสผ่านของคุณ",  # แก้ตามรหัสผ่าน MySQL ของคุณ
        database="mydatabase"
    )
# --- หน้า Homepage ---
@app.route('/')
def homepage():
    if 'username' not in session:
        return redirect(url_for('login'))  # ถ้าไม่ login ให้กลับหน้า login

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()

    return render_template('homepage/indexmore.html', products=products)

# --- หน้า Login ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = email  # เก็บ session
            return redirect(url_for('homepage'))
        else:
            message = "Login failed!"

    return render_template('login/loginuser.html', message=message)

# --- Logout ---
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# --- รัน Flask ---
if __name__ == '__main__':
    app.run(debug=True)
