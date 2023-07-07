# Break and fix this program -> what if numOfGuests is false ( blank space, or not an int)?

name = ''
while not name:
    print('Enter your name:')
    name = input()

print('How many guests will you have?')
numOfGuests = int(input())

if numOfGuests:
    print('Be sure to have enough rom for all your guests.')
print('Done')
