from flask import redirect, render_template, request
from app.app import app
from flask_login import login_required
from manager.forms import DecryptForm, EncryptForm


@app.route("/crypto", methods=["GET", "POST"])
@login_required
def crypto():
    form_encrypt = EncryptForm()
    form_decrypt = DecryptForm()
    return render_template("user/main/crypto.html", form_encrypt=form_encrypt, form_decrypt=form_decrypt)

