import check50 as cs50


SCRIPT_NAME = "gravity2.py"

@cs50.check()
def exists():
    """gravity2.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_uppercase_and_space():
    """Correct: The Sectret Message Is 'SORRY, DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE.'"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.").stdout()
    correct_output = "Let's try all the methods we have:\nCaesar cipher: EIFFY, TOHHSF, VCD YICF ASJTY OE OJ WJIDPSF UWEDLS.\nAtbash cipher: SORRY, DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE."
    if correct_output != output.rstrip():
        raise cs50.Mismatch(correct_output, output.rstrip())


@cs50.check(exists)
def test_lowercase_and_symbols():
    """Correct: The Sectret Message Is 'Python is fun! :-)'"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("Sbwkrq lv ixq! :-)").stdout()
    correct_output = "Let's try all the methods we have:\nCaesar cipher: Python is fun! :-)\nAtbash cipher: Hydpij oe rcj! :-)"
    if correct_output != output.rstrip():
        raise cs50.Mismatch(correct_output, output.rstrip())
