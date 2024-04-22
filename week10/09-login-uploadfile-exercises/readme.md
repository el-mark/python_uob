# Content

All util week 9. Plus:
1. login
2. upload file for students
3. upload file for users
4. loans list (with user info inside)
5. toggle damage property on loans list
6. search feature on students list


# create first User (flask shell)(python)
from werkzeug.security import generate_password_hash
password_hash = password_hash=generate_password_hash('123', salt_length=32)
new_user = User(username='mark', email='m@g.com', password_hash=password_hash)

db.session.add(new_user)
db.session.commit()