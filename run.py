from app import create_app
from app.extensions import db
from app.models import User, Item

app = create_app()

if __name__ == "__main__":
    # ✅ สร้างตารางภายใน app context
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully!")

    # ✅ รันเซิร์ฟเวอร์ Flask
    app.run(debug=True)
