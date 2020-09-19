from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('qwerqwerqwer')
print(hashed_pass)

check = check_password_hash(hashed_pass, 'tewajakearwe')
print(check)

check = check_password_hash(hashed_pass, 'qwerqwerqwer')
print(check)


pass1 = generate_password_hash('hola.mundo')
pass2 = generate_password_hash('hola.mundo')

print(pass1)
print(pass2)
