while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (Its is a fish.)')
    password = input()
    if password == 'a fish':
        break
print('Access granted')
