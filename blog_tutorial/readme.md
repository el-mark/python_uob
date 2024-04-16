# Flask Blog
from Corey Schafer youtube tutorial

https://www.youtube.com/watch?v=44PvX0Yv368&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=5&ab_channel=CoreySchafer

## Bcrypt commands (to test)

bcrypt = Bcrypt()
hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')

bcrypt.check_password_hash(hashed_pw, 'password')
>>> False

bcrypt.check_password_hash(hashed_pw, 'testing')
>>> True
