import check50 as cs50


SCRIPT_NAME = "gravity3.py"

@cs50.check()
def exists():
    """gravity3.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_a1z26():
    """Correct: The Secret Message Is: 'VIVAN LOS PATOS DE LA PISCINA.'"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.").stdout()
    correct_output = "Let's try all the methods we have:\nCaesar cipher: 22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.\nAtbash cipher: 22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.\nA1Z26 cipher: VIVAN LOS PATOS DE LA PISCINA."
    if correct_output != output.rstrip():
        raise cs50.Mismatch(correct_output, output.rstrip())
