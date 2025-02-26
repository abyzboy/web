from app.models.user import User

def get_all_users():
    return User.query.all()

def get_user_by_id(id):
    return User.query.get(id)

def delete_user(id):
    user : User = User.query.get(id)
    user.delete()