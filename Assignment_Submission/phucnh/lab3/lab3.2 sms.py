from twilio.rest import TwilioRestClient

account_sid = "ACc0aa18c224fa2d295957d2dbd5c0ceaa"
auth_token = "4a0f9c6bf82500bb816b04738f00e7b5"

client = TwilioRestClient(account_sid, auth_token)


def gui(number):
    while True:
        #number = input('number')
        input('OK')
        message= client.messages.create(body="Phuc",to="+84%s"%number,from_="+12015286688")
        print(message.sid)

#975626296
#967286259
        
gui(123563116)
    
