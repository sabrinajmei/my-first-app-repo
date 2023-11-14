#import functions from our application code into test so we can invoke it here
from app.my_mod import enlarge

# we have to wrap test assertions inside a test function
def test_enlarge():
    assert enlarge(10) == 1000


