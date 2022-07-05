import check50 as cs50


SCRIPT_NAME = "temperature.py"

@cs50.check()
def exists():
    """temperature.py Exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_negative():
    """Test Passed For Negative Input"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("-30") \
        .stdout("-30 degrees in Canada would be -22 degrees in Springfield. D'oh!") \
        .exit()


@cs50.check(exists)
def test_positive():
    """Test Passed For Positive Input"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("30") \
        .stdout("30 degrees in Canada would be 86 degrees in Springfield. D'oh!") \
        .exit()


@cs50.check(exists)
def test_zero():
    """Test Passed For Zero Input"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("0") \
        .stdout("0 degrees in Canada would be 32 degrees in Springfield. D'oh!") \
        .exit()
