import check50 as cs50


SCRIPT_NAME = "klingon-quiz3.py"

"b, ch, D, gh, H, j, l, m, n, p, q, Q, r, S, t, v, w, y,"

@cs50.check()
def exists():
    """klingon-quiz3.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def noun_incorrect_3():
    """Incorrect: The Answer Is batlh"""
    attempt_1 = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdout()

    print(attempt_1.rstrip())
    if "How do you translate necklace to Klingon? You have 2 attempts left.\nHint: g___h\n>" != attempt_1.rstrip():
        raise cs50.Mismatch("How do you translate necklace to Klingon? You have 2 attempts left.\nHint: g___h\n>", attempt_1.rstrip())

        """
        .stdout("How do you translate necklace to Klingon? You have 2 attempts left.\nHint: g___h\n> ") \
        .stdin("ghighi") \
        .stdout("Sorry, you're wrong!\nHow do you translate necklace to Klingon?\nYou have 1 attempts left.\nHint: g___h\n> ") \
        .stdin("ghighi") \
        .stdout("Sorry, you're wrong!\nThe correct answer was ghIgh.") \
        .exit()
        """