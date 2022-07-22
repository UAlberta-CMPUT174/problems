import check50 as cs50


SCRIPT_NAME = "klingon-quiz1.py"

@cs50.check()
def exists():
    """klingon-quiz1.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_correct():
    """Correct, Computer is De'wI' in Klingon"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("De'wI'") \
        .stdout("Correct!") \
        .exit()


@cs50.check(exists)
def test_incorrect():
    """Sorry, Computer is De'wI' in Klingon"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Baz") \
        .stdout("Sorry, the correct answer is De'wI'.") \
        .exit()
