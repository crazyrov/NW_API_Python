from flask import render_template, redirect
import requests as re
import json
import numpy

def client_list(creds, request):
    print(creds)
    headers = {
             'Authorization': 'Basic ' + creds + ''
    }

    r = re.get('https://192.168.31.50:9090/nwrestapi/v3/global/clients', headers=headers, verify=False)
    if r.status_code >= 400:
        return redirect("/")
    content = sorted(json.loads(r.content)['clients'], key = lambda i: i['hostname'], reverse=True)
    return render_template('clients.html', content=content)
