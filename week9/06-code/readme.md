# imports
from werkzeug.security import generate_password_hash, check_password_hash
# commands
hash = generate_password_hash('123')
check_password_hash(hash, '123')
