import check50 as cs50


@cs50.check()
def exists():
    """temperature.py exists"""
    cs50.exists("temperature.py")


@cs50.check(exists)
def test_negative():
    """Samwise is younger than Frodo"""
    cs50.run("python3 temperature.py") \
        .stdin("-30") \
        .stdout("-30 degrees in Canada would be -22 degrees in Springfield. D'oh!") \
        .exit()


@cs50.check(exists)
def test_positive():
    """Samwise is younger than Frodo"""
    cs50.run("python3 temperature.py") \
        .stdin("30") \
        .stdout("30 degrees in Canada would be 86 degrees in Springfield. D'oh!") \
        .exit()


@cs50.check(exists)
def test_zero():
    """Samwise is younger than Frodo"""
    cs50.run("python3 temperature.py") \
        .stdin("0") \
        .stdout("0 degrees in Canada would be 32 degrees in Springfield. D'oh!") \
        .exit()
