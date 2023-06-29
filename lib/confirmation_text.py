import os
from twilio.rest import Client


class ConfirmationText():

    def __init__(self):
        pass

    def send_sms(self, time):
        # Download the helper library from https://www.twilio.com/docs/python/install


        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
                    .create(
                        body=f"Thank you! Your order was placed and will be delivered before {time}",
                        from_='+447479272892',
                        to='+447507366403'
                        )

        print(message.sid)
