from datetime import datetime
from app.extensions import db


# 🧍 ตารางผู้ใช้
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="user")  # user / admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # ความสัมพันธ์
    items = db.relationship("Item", backref="owner", lazy=True)
    logs = db.relationship("Log", backref="user", lazy=True)
    requests = db.relationship("Request", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.name} ({self.role})>"


# 📦 ตารางสิ่งของ (ของหาย / ของพบ)
class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    item_type = db.Column(db.String(10), nullable=False)   # lost / found
    status = db.Column(db.String(20), default="open")      # open / closed
    location = db.Column(db.String(200))
    image_url = db.Column(db.String(255))                  # 🔹 รูปภาพ (เผื่ออัปโหลด)
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)

    # เชื่อมกับ User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # เชื่อมกับ Claim (มีคนติดต่อเข้ามา)
    claims = db.relationship("Claim", backref="item", lazy=True)

    def __repr__(self):
        return f"<Item {self.title} ({self.item_type})>"


# 📬 ตาราง Claim (ติดต่อเจ้าของของหาย)
class Claim(db.Model):
    __tablename__ = "claim"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    sender_name = db.Column(db.String(100), nullable=False)
    sender_email = db.Column(db.String(120))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Claim from {self.sender_name} on item {self.item_id}>"


# 🕒 ตาราง Logs (บันทึกกิจกรรม)
class Log(db.Model):
    __tablename__ = "log"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    action = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Log {self.action} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})>"


# 📩 ตาราง Request (คำขอถึงแอดมิน)
class Request(db.Model):
    __tablename__ = "request"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    subject = db.Column(db.String(120), nullable=False)    # หัวข้อคำขอ เช่น "แจ้งของหาย"
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default="pending")   # pending / resolved
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Request {self.subject} (from user {self.user_id})>"
