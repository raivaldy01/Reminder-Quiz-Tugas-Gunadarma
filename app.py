from flask import Flask, request
import GetTugasDL
from twilio.twiml.messaging_response import MessagingResponse

## Init Flask APp
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
  ## GEt user message
    user_msg = request.values.get('Body', '')
    lewat = 0
    username = ''
    password = ''
    validate = 'gunadarma.ac.id'
    ## Init bot response
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    # Applying bot logic
    if 'mulai' in user_msg.lower() :
        msg.body('BOT WHATSAPP JADWAL DEADLINE TUGAS UNIV.GUNADARMA\nkontak ke saya jika terdapat masalah dalam penggunaan bot, ke https://wa.me/+6281818475959 atau bisa join ke grup whatsapp untuk diskusi bersama ke link https://chat.whatsapp.com/J0z6x3dRDNRDhkPPK2HR3f' + '\nMENU\n' + 
        '1. Untuk mendapatkan jadwal deadline vclass ketik format \n "usernamev:usernamevclass + spasi + passwordv:passwordvclass" lalu kirim ke chat \n\n' + 
        '2. Untuk mendapatkan jadwal deadline praktikum ilab ketik format \n "usernamep:usernamepraktikum + spasi + passwordp:passwordpraktikum" lalu kirim ke chat' 
    )
    elif 'usernamev:' in user_msg:
        msg.body(GetTugasDL.runGetTugas(str(user_msg).split(' ')[0].replace('usernamev:', ''), str(user_msg).split(' ')[1].replace('passwordv:', ''),'v-class.gunadarma.ac.id')
    )
    elif 'usernamep:' in user_msg :
        msg.body(GetTugasDL.runGetTugas(str(user_msg).split(' ')[0].replace('usernamep:', ''), str(user_msg).split(' ')[1].replace('passwordp:', ''),'praktikum.gunadarma.ac.id')
    )
    elif 'usernameupn:' in user_msg:
        msg.body(GetTugasDL.runGetTugas(str(user_msg).split(' ')[0].replace('usernameupn:', ''), str(user_msg).split(' ')[1].replace('passwordupn:', ''),'leads.upnvj.ac.id')
    )
    else:
        msg.body(
        "Maaf Query yang anda ketikkan salah silahkan ulangi" + "\n\n" + 'untuk memulai ketik "mulai"'
    )

    # elif not 'mulai' in user_msg:
    #     msg.body(jadwalDL.getJadwalDL(username, password))
    #     concat_u_pw = str(user_msg).split(' ')
    #     username = concat_u_pw[0]
    #     password = concat_u_pw[1] 
    #     print(username + ' ' + password)
    # else:
    #     msg.body("Sorry, I didn't get what you have said!")

    
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)