import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
length = 50
print ''.join([random.choice(chars) for i in range(length)])
