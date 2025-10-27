
def user_to_dict(user):
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,
        'address_line1': user.address_line1,
        'city': user.city,
        'state': user.state,
        'pincode': user.pincode,
        'created_at': user.created_at.isoformat() if user.created_at else None,
        'employment': [
            {
                'id': e.id,
                'company_name': e.company_name,
                'designation': e.designation,
                'start_date': e.start_date.isoformat() if e.start_date else None,
                'end_date': e.end_date.isoformat() if e.end_date else None,
                'is_current': e.is_current,
            } for e in user.employments
        ],
        'banks': [
            {
                'id': b.id,
                'bank_name': b.bank_name,
                'account_number': b.account_number,
                'ifsc': b.ifsc,
                'account_type': b.account_type,
            } for b in user.banks
        ]
    }
