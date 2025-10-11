from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Item, Claim, Log, Request
from app.utils import is_admin
from app.extensions import db

admin_bp = Blueprint("admin", __name__)

# 🟣 ดึงข้อมูลผู้ใช้ทั้งหมด (Admin เท่านั้น)
@admin_bp.get("/users")
@jwt_required()
def list_users():
    """ดึงข้อมูลผู้ใช้ทั้งหมด (เฉพาะแอดมิน)"""
    if not is_admin():
        return jsonify({"error": "Permission denied"}), 403

    users = User.query.order_by(User.id).all()
    data = [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "role": u.role,
            "created_at": u.created_at.strftime("%Y-%m-%d %H:%M"),
        }
        for u in users
    ]
    return jsonify({
        "total_users": len(data),
        "users": data
    }), 200


# 🟣 ดูรายการของทั้งหมด (รวมทุก user)
@admin_bp.get("/items")
@jwt_required()
def list_all_items():
    """ดูรายการของหาย/ของพบทั้งหมด (เฉพาะแอดมิน)"""
    if not is_admin():
        return jsonify({"error": "Permission denied"}), 403

    items = Item.query.order_by(Item.date_reported.desc()).all()
    data = [
        {
            "id": i.id,
            "title": i.title,
            "description": i.description,
            "item_type": i.item_type,
            "status": i.status,
            "location": i.location,
            "owner": i.owner.name if i.owner else "N/A",
            "date_reported": i.date_reported.strftime("%Y-%m-%d %H:%M"),
        }
        for i in items
    ]
    return jsonify({
        "total_items": len(data),
        "items": data
    }), 200


# 📩 ดูคำขอ (Request) ทั้งหมด
@admin_bp.get("/requests")
@jwt_required()
def list_all_requests():
    """ดูคำขอจากผู้ใช้ (เฉพาะแอดมิน)"""
    if not is_admin():
        return jsonify({"error": "Permission denied"}), 403

    requests = Request.query.order_by(Request.created_at.desc()).all()
    data = [
        {
            "id": r.id,
            "user": r.user.name if r.user else "N/A",
            "subject": r.subject,
            "message": r.message,
            "status": r.status,
            "created_at": r.created_at.strftime("%Y-%m-%d %H:%M"),
        }
        for r in requests
    ]
    return jsonify({
        "total_requests": len(data),
        "requests": data
    }), 200


# 📊 Dashboard Admin (รวมสถิติทั้งหมด)
@admin_bp.get("/dashboard")
@jwt_required()
def admin_dashboard():
    """สรุปภาพรวมระบบ (เฉพาะแอดมิน)"""
    if not is_admin():
        return jsonify({"error": "Permission denied"}), 403

    total_users = User.query.count()
    total_items = Item.query.count()
    lost_items = Item.query.filter_by(item_type="lost").count()
    found_items = Item.query.filter_by(item_type="found").count()
    closed_items = Item.query.filter_by(status="closed").count()
    total_claims = Claim.query.count()
    total_requests = Request.query.count()

    # ดึง Log ล่าสุด 5 รายการ
    logs = Log.query.order_by(Log.timestamp.desc()).limit(5).all()
    recent_logs = [
        {
            "user": log.user.name if log.user else "System",
            "action": log.action,
            "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M"),
        }
        for log in logs
    ]

    summary = {
        "total_users": total_users,
        "total_items": total_items,
        "lost_items": lost_items,
        "found_items": found_items,
        "closed_items": closed_items,
        "total_claims": total_claims,
        "total_requests": total_requests,
        "recent_logs": recent_logs,
    }

    return jsonify(summary), 200
