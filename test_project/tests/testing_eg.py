def test_testing_success_code():
    assert 10 / 2 == 5 #Test should pass

def test_testing_failure_code():
    assert 10 / 2 == 0 # Test should fail
    
def test_exception():
    if True : # If something does go wrong, output_you_got != desired_output
        raise ValueError("You got a value error!!")