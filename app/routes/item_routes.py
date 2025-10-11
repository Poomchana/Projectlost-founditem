from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Item, User, Claim
from app.extensions import db
from app.utils import add_log  # ฟังก์ชันบันทึก log

item_bp = Blueprint("item_bp", __name__)

# 🟢 ดูของทั้งหมด (ไม่ต้อง login)
@item_bp.route("/", methods=["GET"])
def get_all_items():
    items = Item.query.order_by(Item.date_reported.desc()).all()
    result = [
        {
            "id": i.id,
            "title": i.title,
            "description": i.description,
            "item_type": i.item_type,
            "status": i.status,
            "location": i.location,
            "date_reported": i.date_reported.strftime("%Y-%m-%d %H:%M"),
            "user_id": i.user_id,
        }
        for i in items
    ]
    return jsonify(result), 200


# 🔍 ค้นหาของหาย / ของพบ (ไม่ต้อง login)
@item_bp.route("/search", methods=["GET"])
def search_items():
    keyword = request.args.get("keyword", "").strip()
    item_type = request.args.get("type")  # lost / found
    location = request.args.get("location", "")

    query = Item.query

    if keyword:
        query = query.filter(
            (Item.title.ilike(f"%{keyword}%")) |
            (Item.description.ilike(f"%{keyword}%"))
        )

    if item_type:
        query = query.filter_by(item_type=item_type)

    if location:
        query = query.filter(Item.location.ilike(f"%{location}%"))

    items = query.order_by(Item.date_reported.desc()).all()

    return jsonify([
        {
            "id": i.id,
            "title": i.title,
            "description": i.description,
            "item_type": i.item_type,
            "status": i.status,
            "location": i.location,
            "date_reported": i.date_reported.strftime("%Y-%m-%d %H:%M"),
        }
        for i in items
    ]), 200


# 🟣 เพิ่มของ (ต้อง login)
@item_bp.route("/", methods=["POST"])
@jwt_required()
def create_item():
    data = request.get_json()
    current_user_id = int(get_jwt_identity())

    item = Item(
        title=data.get("title"),
        description=data.get("description"),
        item_type=data.get("item_type"),
        location=data.get("location"),
        user_id=current_user_id
    )

    db.session.add(item)
    db.session.commit()

    add_log(f"User {current_user_id} created item '{item.title}'")

    return jsonify({"message": "Item created successfully"}), 201


# 🟡 แก้ไขข้อมูลของตัวเอง (ต้อง login)
@item_bp.route("/<int:item_id>", methods=["PUT"])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    current_user_id = int(get_jwt_identity())
    item = Item.query.get(item_id)

    if not item:
        return jsonify({"error": "Item not found"}), 404
    if item.user_id != current_user_id:
        return jsonify({"error": "Unauthorized"}), 403

    item.title = data.get("title", item.title)
    item.description = data.get("description", item.description)
    item.status = data.get("status", item.status)
    item.location = data.get("location", item.location)
    db.session.commit()

    add_log(f"User {current_user_id} updated item '{item.title}'")

    return jsonify({"message": "Item updated successfully"}), 200


# 🔴 ลบของตัวเอง (ต้อง login)
@item_bp.route("/<int:item_id>", methods=["DELETE"])
@jwt_required()
def delete_item(item_id):
    current_user_id = int(get_jwt_identity())
    item = Item.query.get(item_id)

    if not item:
        return jsonify({"error": "Item not found"}), 404
    if item.user_id != current_user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(item)
    db.session.commit()

    add_log(f"User {current_user_id} deleted item '{item.title}'")

    return jsonify({"message": "Item deleted successfully"}), 200


# 🟢 ดูเฉพาะของของตัวเอง (ต้อง login)
@item_bp.route("/my", methods=["GET"])
@jwt_required()
def get_my_items():
    current_user_id = int(get_jwt_identity())
    items = Item.query.filter_by(user_id=current_user_id).order_by(Item.date_reported.desc()).all()

    if not items:
        return jsonify({"message": "No items found for this user"}), 200

    result = [
        {
            "id": i.id,
            "title": i.title,
            "description": i.description,
            "item_type": i.item_type,
            "status": i.status,
            "location": i.location,
            "date_reported": i.date_reported.strftime("%Y-%m-%d %H:%M"),
        }
        for i in items
    ]

    return jsonify(result), 200


# 📬 ติดต่อเจ้าของของหาย
@item_bp.route("/<int:item_id>/claim", methods=["POST"])
def claim_item(item_id):
    data = request.get_json()
    item = Item.query.get_or_404(item_id)

    new_claim = Claim(
        item_id=item_id,
        sender_name=data.get("name"),
        sender_email=data.get("email"),
        message=data.get("message")
    )

    db.session.add(new_claim)
    db.session.commit()

    add_log(f"Claim created for item '{item.title}' by {data.get('name')}")

    return jsonify({
        "message": "Claim submitted successfully",
        "item": item.title,
        "from": data.get("name")
    }), 201
