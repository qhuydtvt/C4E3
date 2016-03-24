from twilio.rest import TwilioRestClient
import time

account_sid = "ACc0aa18c224fa2d295957d2dbd5c0ceaa"
auth_token = "4a0f9c6bf82500bb816b04738f00e7b5"
client = TwilioRestClient(account_sid, auth_token)

while True:
##    number = input('number: ')
    time.sleep(5)
    message = client.messages.create(body="xin chao", to="+84%s"%1235631116, from_ ="+12015286688")
    print(message.sid)

