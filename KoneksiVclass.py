import requests
from bs4 import BeautifulSoup
import os


def login_credentials(token,username,password):
    return {
        'logintoken': token,
        'username': username,
        'password': password
     }

def get_sesskey(MoodleSession,url):
    session = requests.Session()
    sess_key_url = f'https://{url}/calendar/export.php?'
    form_key = MoodleSession.get(sess_key_url, verify=False)
    soup = BeautifulSoup(form_key.content, 'lxml')
    return soup.find('input', attrs={'name': 'sesskey'})['value']


def get_cookie_key(username,password,urls):
    headers = {'Connection': "keep-alive"}
    with requests.Session() as s:
        url = f'https://{urls}/login/index.php'
        secure = f'https://{urls}/my/'
        if not os.path.isfile('./somefile') or os.path.isfile('./somefile'):
            f = s.get(url, verify=False)
            soup = BeautifulSoup(f.content, 'lxml')
            data = login_credentials(soup.find('input', attrs={'name': 'logintoken'})['value'],username,password)
            x = s.post(url, data=data, headers=headers, cookies=s.cookies, verify=False)
            r = s.get(secure, verify=False)
            return [s.cookies,get_sesskey(s,urls)]
