from flask import Flask
import datetime


app = Flask(__name__)

from manager.config import *
from user.user import *
from user.crypto import *
from user.forum import *
from user.errors import *