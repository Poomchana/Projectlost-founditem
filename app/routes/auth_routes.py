from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..extensions import db
from ..models import User

auth_bp = Blueprint("auth", __name__)

# 🟢 สมัครสมาชิก
@auth_bp.post("/register")
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(
        name=data.get("name"),
        email=email,
        password=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

# 🟠 ล็อกอิน
@auth_bp.post("/login")
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()

    if not user or not check_password_hash(user.password, data.get("password")):
        return jsonify({"error": "Invalid credentials"}), 401

    # ✅ ต้องแปลง user.id เป็น string
    token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": token})

# 🔵 ข้อมูลผู้ใช้ (ต้อง login)
@auth_bp.get("/me")
@jwt_required()
def me():
    # ✅ แปลงกลับเป็น int
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })
