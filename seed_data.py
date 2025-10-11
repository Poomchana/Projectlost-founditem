from app import create_app
from app.extensions import db
from app.models import User, Item

app = create_app()

with app.app_context():
    # ล้างข้อมูลเดิม (ไม่บังคับ)
    db.drop_all()
    db.create_all()

    # เพิ่มผู้ใช้
    u1 = User(name="Alice", email="alice@example.com", password="1234")
    u2 = User(name="Bob", email="bob@example.com", password="5678")

    db.session.add_all([u1, u2])
    db.session.commit()

    # เพิ่มของหาย/ของพบ
    i1 = Item(title="กระเป๋าสตางค์สีดำ", description="ลืมไว้ที่ BTS อโศก", item_type="lost", user_id=u1.id)
    i2 = Item(title="พวงกุญแจรูปหมี", description="เก็บได้หน้าร้านกาแฟ", item_type="found", user_id=u2.id)

    db.session.add_all([i1, i2])
    db.session.commit()

    print("✅ Sample data inserted successfully!")
