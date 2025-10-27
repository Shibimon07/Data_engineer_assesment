from flask import Flask, request, jsonify
from datetime import datetime
import os

from models import db, User, EmploymentInfo, UserBankInfo

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()


    # all routing
    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json() or {}
        if not data.get("email"):
            return jsonify({"error": "Email is required"}), 400

        user = User(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            phone=data.get("phone"),
            address_line1=data.get("address_line1"),
            city=data.get("city"),
            state=data.get("state"),
            pincode=data.get("pincode")
        )
        db.session.add(user)
        db.session.flush()  

        for emp in data.get("employment", []):
            emp_obj = EmploymentInfo(
                user_id=user.id,
                company_name=emp.get("company_name"),
                designation=emp.get("designation"),
                start_date=emp.get("start_date"),
                end_date=emp.get("end_date"),
                is_current=emp.get("is_current", False)
            )
            db.session.add(emp_obj)

        for b in data.get("banks", []):
            bank_obj = UserBankInfo(
                user_id=user.id,
                bank_name=b.get("bank_name"),
                account_number=b.get("account_number"),
                ifsc=b.get("ifsc"),
                account_type=b.get("account_type")
            )
            db.session.add(bank_obj)

        db.session.commit()
        return jsonify({"id": user.id, "email": user.email}), 201

    @app.route('/users', methods=['GET'])
    def list_users():
        users = User.query.all()
        results = []
        for u in users:
            results.append({
                "id": u.id,
                "name": f"{u.first_name} {u.last_name}",
                "email": u.email,
                "pincode": u.pincode,
                "employment_count": len(u.employments),
                "bank_count": len(u.banks)
            })
        return jsonify(results)

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "employment": [{"company_name": e.company_name} for e in user.employments],
            "banks": [{"bank_name": b.bank_name} for b in user.banks]
        })

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json() or {}

        for field in ['first_name', 'last_name', 'email', 'phone', 'address_line1', 'city', 'state', 'pincode']:
            if field in data:
                setattr(user, field, data[field])

        db.session.commit()
        return jsonify({"message": "User updated"}), 200

    @app.route('/users/<int:user_id>/employment', methods=['POST'])
    def add_employment(user_id):
        data = request.get_json() or {}
        emp = EmploymentInfo(user_id=user_id, **data)
        db.session.add(emp)
        db.session.commit()
        return jsonify({"message": "Employment added"}), 201

    @app.route('/users/<int:user_id>/bank', methods=['POST'])
    def add_bank(user_id):
        data = request.get_json() or {}
        bank = UserBankInfo(user_id=user_id, **data)
        db.session.add(bank)
        db.session.commit()
        return jsonify({"message": "Bank added"}), 201

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
