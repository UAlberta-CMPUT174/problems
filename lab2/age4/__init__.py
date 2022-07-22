import check50 as cs50


SCRIPT_NAME = "age4.py"

@cs50.check()
def exists():
    """age4.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_eowyn():
    """Eowyn is younger than Frodo, Samwise, Gandalf, Legolas, Gimli, Aragorn, Boromir, Merry, Pippin."""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Eowyn") \
        .stdin("24") \
        .stdout("Eowyn is 24 years old, and they are younger than Frodo, Samwise, Gandalf, Legolas, Gimli, Aragorn, Boromir, Merry, Pippin.") \
        .exit()


@cs50.check(exists)
def test_bilbo():
    """Bilbo is older than Frodo, Samwise, Aragorn, Boromir, Merry, Pippin and younger than Gandalf, Legolas, Gimli."""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Bilbo") \
        .stdin("129") \
        .stdout("Bilbo is 129 years old, and they are older than Frodo, Samwise, Aragorn, Boromir, Merry, Pippin.\nBilbo is 129 years old, and they are younger than Gandalf, Legolas, Gimli.") \
        .exit()


@cs50.check(exists)
def test_galadriel():
    """Galadriel is older than Frodo, Samwise, Gandalf, Legolas, Gimli, Aragorn, Boromir, Merry, Pippin."""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Galadriel") \
        .stdin("7000") \
        .stdout("Galadriel is 7000 years old, and they are older than Frodo, Samwise, Gandalf, Legolas, Gimli, Aragorn, Boromir, Merry, Pippin.") \
        .exit()


@cs50.check(exists)
def test_invalid():
    """Ages Cannot Be Negative"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Foo") \
        .stdin("-1") \
        .stdout("Invalid age.") \
        .exit()
