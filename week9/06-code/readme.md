# imports
from werkzeug.security import generate_password_hash, check_password_hash
# commands
hash = generate_password_hash('123')
check_password_hash(hash, '123')


# imports2
from werkzeug.security import generate_password_hash

# commands2
u = User(username='mark', email='m@g.com', password_hash = generate_password_hash('abc', salt_length=32))
db.session.add(u)
db.session.commit()
