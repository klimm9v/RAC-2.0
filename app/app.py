from flask import Flask

app = Flask(__name__)
from manager.config import *
from user.session import *
from user.login import *