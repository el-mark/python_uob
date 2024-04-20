# create first user
from werkzeug.security import generate_password_hash
new_user = User(
            username='mark', email='m@g.com',password_hash=generate_password_hash('123', salt_length=32)
        )

db.session.add(new_user)
db.session.commit()