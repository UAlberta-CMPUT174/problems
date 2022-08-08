import check50 as cs50


SCRIPT_NAME = "klingon-quiz2.py"

"b, ch, D, gh, H, j, l, m, n, p, q, Q, r, S, t, v, w, y,"

@cs50.check()
def exists():
    """klingon-quiz2.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_noun_incorrect():
    """The Correct Answer Is batlh"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("n") \
        .stdin("b") \
        .stdin("bal") \
        .stdout("Sorry, the correct answer is batlh.") \
        .exit()
