from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Request as RequestModel, User
from app.extensions import db
from app.utils import add_log

request_bp = Blueprint("request", __name__)

# 📨 ผู้ใช้ส่งคำขอ
@request_bp.route("/", methods=["POST"])
@jwt_required()
def create_request():
    data = request.get_json()
    user_id = int(get_jwt_identity())

    new_req = RequestModel(
        user_id=user_id,
        subject=data.get("subject"),
        message=data.get("message")
    )
    db.session.add(new_req)
    db.session.commit()

    add_log(f"User {user_id} created request '{data.get('subject')}'")

    return jsonify({"message": "Request sent successfully"}), 201


# 🟢 ผู้ใช้ดูคำขอตัวเอง
@request_bp.route("/my", methods=["GET"])
@jwt_required()
def get_my_requests():
    user_id = int(get_jwt_identity())
    requests = RequestModel.query.filter_by(user_id=user_id).all()
    data = [
        {
            "id": r.id,
            "subject": r.subject,
            "message": r.message,
            "status": r.status,
            "created_at": r.created_at.strftime("%Y-%m-%d %H:%M")
        }
        for r in requests
    ]
    return jsonify(data), 200
