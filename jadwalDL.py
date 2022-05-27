import requests
from bs4 import BeautifulSoup
from lxml import etree
import json

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def getJadwalDL(username,password):
    session = requests.Session()
    login_url = 'https://v-class.gunadarma.ac.id/login/index.php'

    get_halaman = session.get(login_url)

    html = BeautifulSoup(get_halaman.content, 'html.parser')


    logintoken = html.find('input', {'name':'logintoken'})['value']

    payload = {
        'logintoken':logintoken,
        'username': username,
        'password': password
    }

    login = session.post(login_url, data=payload)

    halaman_dashboard = session.get('https://v-class.gunadarma.ac.id/my')

    html_halaman_dashboard = BeautifulSoup(halaman_dashboard.content, features="lxml")

    hasil = html_halaman_dashboard.find_all('div', {'class':'event'})

    jadwal_deadline = []
    i = 0;
    for hasils in hasil:
        get_href = hasils.find('a',).get("href").split('&')[1]
        course_id = int(get_href.replace('course=',''))
        course_name = session.get('https://v-class.gunadarma.ac.id/course/view.php?id=' + str(course_id))
        html_coursename = BeautifulSoup(course_name.content, features="lxml")
        course_name = html_coursename.find('h1')

        jadwal_deadline.append( str(i+1) + '\n' +  (course_name.get_text() + "\n" + hasils.get_text()))
        i+=1
    return listToString(jadwal_deadline)


def main():
    print(getJadwalDL('masukkan email vclass kalian', 'masukkan password vclass kalian'))

if __name__ == '__main__':
    main()
