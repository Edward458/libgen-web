from flask import Blueprint
import requests

views = Blueprint(__name__,'views')

@views.route('/')
def home():
    request = requests.get('http://62.182.86.140/main/1450000/5390a7bbc43507a05d35a487804e5b80/J.%20D.%20Salinger%20-%20The%20Catcher%20In%20The%20Rye-Random%20House%2C%20Inc.%20%281991%29.epub')
    return request.content