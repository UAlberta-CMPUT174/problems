import check50


@check50.check()
def exists():
    """age1.py exists"""
    check50.exists("age1.py")


@check50.check(exists)
def test_samwise():
    """input of 39 yields output of 4"""
    check50.run("python3 age1.py").stdin("Samwise").stdin("39").stdout(
        "Samwise is 39 years old, and they are younger than Frodo.\n"
    ).exit()
