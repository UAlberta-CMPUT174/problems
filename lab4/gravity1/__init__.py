import check50 as cs50


SCRIPT_NAME = "gravity1.py"

@cs50.check()
def exists():
    """gravity1.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_uppercase_and_space():
    """Correct: The Secret Message Is, 'STAN IS NOT WHAT HE SEEMS.'"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("VWDQ LV QRW ZKDW KH VHHPV.") \
        .stdout("STAN IS NOT WHAT HE SEEMS.") \
        .exit()


@cs50.check(exists)
def test_lowercase_and_symbols():
    """Correct: The Secret Message Is 'Python is fun! :-)'"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("Sbwkrq lv ixq! :-)").stdout()
    if "Python is fun! :-)" != output.rstrip():
        raise cs50.Mismatch("Python is fun! :-)", output.rstrip())
