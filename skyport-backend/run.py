from app import create_app
from app.seed.seed_roles_and_users import seed_roles_and_users

app = create_app()


# Add CLI command after app is created
@app.cli.command("seed")
def seed():
    """Seed the database with roles and users."""
    seed_roles_and_users()

if __name__ == '__main__':
    app.run(debug=True)
