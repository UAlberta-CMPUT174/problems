import check50 as cs50


SCRIPT_NAME = "age3.py"

@cs50.check()
def exists():
    """age3.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_eowyn():
    """Eowyn is younger than Arwen, Gollum, Frodo, Pippin."""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Eowyn") \
        .stdin("24") \
        .stdout("Eowyn is 24 years old, and they are younger than Arwen, Gollum, Frodo, Pippin.") \
        .exit()


@cs50.check(exists)
def test_bilbo():
    """Bilbo is older than Frodo and Pippin and younder than Arwen and Gollum."""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Bilbo") \
        .stdin("129") \
        .stdout("Bilbo is 129 years old, and they are older than Frodo, Pippin.\nBilbo is 129 years old, and they are younger than Arwen, Gollum.") \
        .exit()


@cs50.check(exists)
def test_galadriel():
    """Galadriel is older than Arwen, Gollum, Frodo, Pippin."""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Galadriel") \
        .stdin("7000") \
        .stdout("Galadriel is 7000 years old, and they are older than Arwen, Gollum, Frodo, Pippin.") \
        .exit()


@cs50.check(exists)
def test_invalid():
    """Ages Cannot Be Negative"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Foo") \
        .stdin("-1") \
        .stdout("Invalid age.") \
        .exit()
