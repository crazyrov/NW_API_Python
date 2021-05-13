from flask import render_template
import requests as re
import json

m = 'ndzY3JpcHQ6VDFtZXNuMHdAMTIzNDU2Nw=='
headers = {
         'Authorization': 'Basic ' + m + ''
}
r = re.get('https://10.3.128.37:9095/nwrestapi/v2/global/alerts', headers=headers, verify=False)
print(r.content)


def client_list(user, pass, request):
    return render_template()


# https://hackersandslackers.com/flask-jinja-templates/

# @app.route('/')
# def home():
#     """Landing page."""
#     nav = [
#         {'name': 'Home', 'url': 'https://example.com/1'},
#         {'name': 'About', 'url': 'https://example.com/2'},
#         {'name': 'Pics', 'url': 'https://example.com/3'}
#     ]
#     return render_template(
#         'home.html',
#         nav=nav,
#         title="Jinja Demo Site",
#         description="Smarter page templates with Flask & Jinja."
#     )
#
# <header>
#    <nav>
#     {% for link in nav %}
#       <a href="{{ link.url }}">{{ link.name }}</a>
#     {% endfor %}
#   </nav>
# </header>
