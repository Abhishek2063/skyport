from app.extensions import db, bcrypt
from app.models.role import Role
from app.models.user import User

def seed_roles_and_users():
    print("Seeding roles and users...")

    # Create roles if they don't exist
    admin_role = Role.query.filter_by(name='admin').first()
    if not admin_role:
        admin_role = Role(name='admin')
        db.session.add(admin_role)

    user_role = Role.query.filter_by(name='user').first()
    if not user_role:
        user_role = Role(name='user')
        db.session.add(user_role)

    db.session.commit()

    # Hash password
    password_hash = bcrypt.generate_password_hash("Test@1234").decode('utf-8')

    # Seed Admin User
    if not User.query.filter_by(email="admin@example.com").first():
        admin_user = User(
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            password_hash=password_hash,
            phone="1234567890",
            is_admin=True,
            role_id=admin_role.id
        )
        db.session.add(admin_user)

    db.session.commit()
    print("Seeding completed!")
