import os
from twilio.rest import Client
from datetime import timedelta


class ConfirmationText():

    def __init__(self):
        self.format_delivery_time = None

    def time_formatter(self, time):
        delivery_time = time + timedelta(minutes=30)
        self.format_delivery_time = delivery_time.strftime("%H:%M")

    def send_sms(self, time):
        # Download the helper library from https://www.twilio.com/docs/python/install


        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
                    .create(
                        body=f"Thank you! Your order was placed and will be delivered before {time_formatter(time)}",
                        from_='+447479272892',
                        to='+447507366403'
                        )

        print(message.sid)
