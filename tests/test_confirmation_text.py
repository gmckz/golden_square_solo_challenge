from lib.confirmation_text import *
from datetime import datetime
from datetime import timedelta

def test_send_sms_prints_message():
    text = ConfirmationText()
    assert text.send_sms(datetime.now()) == f"Thank you! Your order was placed and will be delivered before {datetime.now() + timedelta(minutes=30)}"