from flask import Flask

# สร้างอินสแตนซ์ของ Flask แอปพลิเคชัน
app = Flask(__name__)

# กำหนดเส้นทาง URL "/" ให้เชื่อมโยงกับฟังก์ชัน home()
@app.route('/')
def home():
    return "Hello, Flask!"

# ตรวจสอบว่าไฟล์ถูกรันโดยตรงหรือไม่ แล้วรันแอปพลิเคชัน
if __name__ == '__main__':
    app.run(debug=True) # โหมด debug จะช่วยรีสตาร์ทเซิร์ฟเวอร์อัตโนมัติเมื่อโค้ดมีการเปลี่ยนแปลง
