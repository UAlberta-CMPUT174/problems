import check50 as cs50


SCRIPT_NAME = "klingon-quiz2.py"

"b, ch, D, gh, H, j, l, m, n, p, q, Q, r, S, t, v, w, y,"

@cs50.check()
def exists():
    """klingon-quiz2.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_noun_incorrect():
    """Incorrect: The Answer Is batlh"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("n") \
        .stdin("b") \
        .stdin("bal") \
        .stdout("Sorry, the correct answer is batlh.") \
        .exit()


@cs50.check(exists)
def test_noun_correct():
    """Correct: The Answer Is ghIgh!"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("n") \
        .stdin("gh") \
        .stdin("ghIgh") \
        .stdout("Correct!") \
        .exit()


@cs50.check(exists)
def test_verb_incorrect():
    """Incorrect: The Answer Is Qochbe"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("v") \
        .stdin("m") \
        .stdin("mevil") \
        .stdout("Sorry, the correct answer is mIgh.") \
        .exit()


@cs50.check(exists)
def test_verb_correct():
    """Correct: The Answer Is Qochbe'!"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("v") \
        .stdin("Q") \
        .stdin("Qochbe'") \
        .stdout("Correct!") \
        .exit()


@cs50.check(exists)
def test_capitalization():
    """Incorrect: The Answer Is Qochbe', Not qochbe'"""
    cs50.run(f"python3 {SCRIPT_NAME}") \
        .stdin("v") \
        .stdin("Q") \
        .stdin("qochbe'") \
        .stdout("Sorry, the correct answer is Qochbe'.") \
        .exit()
