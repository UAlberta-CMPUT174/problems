import check50 as cs50


SCRIPT_NAME = "age2.py"

@cs50.check()
def exists():
    """age2.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_samwise():
    """Samwise is younger than Frodo and Gollum"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Samwise") \
        .stdin("39") \
        .stdout("Samwise is 39 years old, and they are younger than Frodo and Gollum.") \
        .exit()


@cs50.check(exists)
def test_bilbo():
    """Bilbo is older than Frodo but younger than Gollum"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Bilbo") \
        .stdin("129") \
        .stdout("Bilbo is 129 years old, and they are older than Frodo but younger than Gollum.") \
        .exit()


@cs50.check(exists)
def test_legolas():
    """Legolas is older than both Gollum and Frodo"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Legolas") \
        .stdin("2931") \
        .stdout("Legolas is 2931 years old, and they are older than Gollum and Frodo.") \
        .exit()
