"""
placemaster index view.

URLs include:
/
"""
import flask
import placemaster


@placemaster.app.route('/', methods=['GET', 'POST'])
def index():
  return "Hey there."