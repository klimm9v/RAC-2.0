from app.app import ALLOWED_EXTENSIONS

def allowed_file(filename):
    if filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return '.'
  
  
  