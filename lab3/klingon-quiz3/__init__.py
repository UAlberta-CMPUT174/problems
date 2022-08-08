import check50 as cs50


SCRIPT_NAME = "klingon-quiz3.py"

"b, ch, D, gh, H, j, l, m, n, p, q, Q, r, S, t, v, w, y,"

@cs50.check()
def exists():
    """klingon-quiz3.py exists"""
    cs50.exists(SCRIPT_NAME)

x = """How do you translate necklace to Klingon? You have 2 attempts left.
Hint: g___h
> \0"""

@cs50.check(exists)
def noun_incorrect_3():
    """Incorrect: The Answer Is batlh"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdout("asdasd").stdin("ghighi").stdout("asdasd").stdin("ghighi").stdout("asdasd").exit()