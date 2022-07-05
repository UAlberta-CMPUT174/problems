import check50 as cs50


SCRIPT_NAME = "chalkboard.py"

@cs50.check()
def exists():
    """chalkboard.py Exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_garlic():
    """Test Passed For 'Garlic gum is not funny.'"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Garlic gum is not funny.") \
        .stdin("3") \
        .stdout("Garlic gum is not funny. Garlic gum is not funny. Garlic gum is not funny.") \
        .exit()


@cs50.check(exists)
def test_car():
    """Test Passed For 'I will not drive the principal's car.'"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("I will not drive the principal's car.") \
        .stdin("1") \
        .stdout("I will not drive the principal's car.") \
        .exit()


@cs50.check(exists)
def test_attitude():
    """Test Passed For 'I will not get very far with this attitude.'"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("I will not get very far with this attitude.") \
        .stdin("4") \
        .stdout("I will not get very far with this attitude. I will not get very far with this attitude. I will not get very far with this attitude. I will not get very far with this attitude.") \
        .exit()
