import check50 as cs50


SCRIPT_NAME = "age1.py"

@cs50.check()
def exists():
    """age1.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_samwise():
    """Samwise is younger than Frodo"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Samwise") \
        .stdin("39") \
        .stdout("Samwise is 39 years old, and they are younger than Frodo.\n") \
        .exit()


@cs50.check(exists)
def test_bilbo():
    """Bilbo is older than Frodo"""
    cs50.run("python3 age1.py") \
        .stdin("Bilbo") \
        .stdin("129") \
        .stdout("Bilbo is 129 years old, and they are older than Frodo.\n") \
        .exit()


@cs50.check(exists)
def test_frodo():
    """Frodo is of the same age as Frodo"""
    cs50.run("python3 age1.py") \
        .stdin("Frodo") \
        .stdin("51") \
        .stdout("Frodo is 51 years old, and they are of the same age as Frodo.\n") \
        .exit()
