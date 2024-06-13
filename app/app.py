from flask import Flask
import datetime


app = Flask(__name__)

from manager.config import *
from user.session import *
from user.login import *
from user.crypto import *
from user.forum import *