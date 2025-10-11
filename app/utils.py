from flask_jwt_extended import get_jwt_identity
from app.models import User

def is_admin():
    """ตรวจสอบว่า user ที่ล็อกอินเป็น admin ไหม"""
    current_user_id = int(get_jwt_identity())
    user = User.query.get(current_user_id)
    return user.role == "admin"
