import check50 as cs50


SCRIPT_NAME = "chalkboard.py"

@cs50.check()
def exists():
    """chalkboard.py Exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_one():
    """Test Passed For Negative Input"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("Garlic gum is not funny.") \
        .stdin("3") \
        .stdout("Garlic gum is not funny. Garlic gum is not funny. Garlic gum is not funny. ") \
        .exit()