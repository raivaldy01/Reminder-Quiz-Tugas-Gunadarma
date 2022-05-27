import requests
from bs4 import BeautifulSoup
import json
from jadwalDL import listToString
from KoneksiVclass import get_cookie_key
import html

def runGetTugas(username,password,url):
    data = {
                "url": 'https://' + url + '/lib/ajax/service.php',
                "headers": {
                    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                    "Connection": "keep-alive"
                    },
                "body": [{
                    "index": 0,
                    "methodname": "core_calendar_get_action_events_by_timesort",
                    "args": {
                        "timesortfrom": 1649869200, 
                        "limittononsuspendedevents": True
                    }
                }]
            }

    credentials = get_cookie_key(username,password,url)
    calendar = requests.post(data['url'], params={'sesskey': credentials[1], 'info': 'core_calendar_get_action_events_by_timesort'}, headers=data['headers'], cookies=credentials[0], json=data['body']).json()
    

    i = 0
    link = []
    for tugas in calendar[0]['data']['events']:
        waktu_html = BeautifulSoup(tugas['formattedtime'],'html.parser')
        waktu = (' on ' + waktu_html.get_text())
        link.append(
            str(
                '\n' + str(i+1) + '\n' + tugas['course']['fullname'] +
                '\n\n' + tugas['name'] + waktu + '\n' +
                tugas['action']['name'] +
                ' ON ' +
                tugas['action']['url'] + '\n'
            )
        )
        i+=1

    print (listToString(link))
    if listToString(link) == '':
        return 'Tidak ada tugas dalam daftar'
    else:
        return listToString(link)
