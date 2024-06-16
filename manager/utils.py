from app.app import ALLOWED_EXTENSIONS
import random


def allowed_file(filename):
    if filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
       return '.'
  
def generate_random():
    string = '12345678910#$%^&*()_+-=!,."abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = ''
    for i in range(8):
        total += random.choice(string)
    return total