import check50 as cs50


SCRIPT_NAME = "gravity2.py"

@cs50.check()
def exists():
    """gravity2.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_uppercase_and_space():
    """Correct: The Secret Message Is: 'STAN IS NOT WHAT HE SEEMS.'"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.").stdout()
    correct_output = "Let's try all the methods we have:\nCaesar cipher: EIFFY, TOHHSF, VCD YICF ASJTY OE OJ WJIDPSF UWEDLS.\nAtbash cipher: SORRY, DIPPER, BUT YOUR WENDY IS IN ANOTHER CASTLE."
    if correct_output != output.rstrip():
        raise cs50.Mismatch(correct_output, output.rstrip())
