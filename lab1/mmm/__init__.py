import check50 as cs50


SCRIPT_NAME = "mmm.py"

@cs50.check()
def exists():
    """mmm.py Exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_space():
    """Test Passed For Food Containing Space"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("ice cream") \
        .stdout("Mmm... ice cream!") \
        .exit()


@cs50.check(exists)
def test_popcorn():
    """Test Passed For Popcorn"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("popcorn") \
        .stdout("Mmm... popcorn!") \
        .exit()


@cs50.check(exists)
def test_empty():
    """Test Passed For Emoty Input"""
    output = \
        cs50.run(f"python3 {SCRIPT_NAME}") \
            .stdin("") \
            .stdout()
    if not any(output.rstrip() == correct_output for correct_output in ["Mmm...", "Mmm... !"] ):
        raise cs50.Failure(f"Expected 'Mmm...' or 'Mmm... !', Got {output}")
