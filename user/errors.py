from app.app import app
from flask import redirect, url_for, request, flash, session

@app.errorhandler(404)
def error404(e):
    return "Error 404"

@app.errorhandler(401)
def error401(e):
    return 'Error 401'

@app.errorhandler(403)
def error404(e):
    return 'Error 403'