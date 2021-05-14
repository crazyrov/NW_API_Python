from flask import render_template, redirect
import requests as re
import json
#
# m = 'ndzY3JpcHQ6VDFtZXNuMHdAMTIzNDU2Nw=='
# headers = {
#          'Authorization': 'Basic ' + m + ''
# }
# r = re.get('https://10.3.128.37:9095/nwrestapi/v2/global/alerts', headers=headers, verify=False)
# print(r.content)


def backup_list(creds, request):
    headers = {
             'Authorization': 'Basic ' + creds + ''
    }

    r = re.get('https://192.168.31.50:9090/nwrestapi/v2/global/backups', headers=headers, verify=False)
    #incase of any errors redirect to the default page of the app
    if r.status_code >= 400:
        return redirect("/")

    # Sort the list based on the clieants hostname and savetime of the client
    content = sorted(json.loads(r.content)['backups'], key = lambda i: (i['clientHostname'],  i['creationTime']), reverse=True)
    return render_template('backups.html', content=content)
