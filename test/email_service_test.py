# import from app
from app.email_service import send_email

# test function
def test_email_sending():
    assert send_email() == 200
