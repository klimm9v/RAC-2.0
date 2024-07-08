from app.app import ALLOWED_EXTENSIONS
import random

def allowed_file(filename: str) -> str:
    if filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
       return '.'
  
def generate_random() -> str:
    string = '12345678910#$%&()_+-=!"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = ''
    for i in range(8):
        total += random.choice(string)
    return total