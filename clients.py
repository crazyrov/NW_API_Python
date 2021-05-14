from flask import render_template, redirect
import requests as re
import json
import numpy

def client_list(creds, request):
    headers = {
             'Authorization': 'Basic ' + creds + ''
    }

    r = re.get('https://192.168.31.50:9090/nwrestapi/v3/global/clients', headers=headers, verify=False)
    #incase of any errors redirect to the default page of the app
    if r.status_code >= 400:
        return redirect("/")
    # Sort the list based on the hostname 
    content = sorted(json.loads(r.content)['clients'], key = lambda i: i['hostname'], reverse=True)
    return render_template('clients.html', content=content)
