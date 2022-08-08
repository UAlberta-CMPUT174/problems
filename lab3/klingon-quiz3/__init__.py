import check50 as cs50


SCRIPT_NAME = "klingon-quiz3.py"

"b, ch, D, gh, H, j, l, m, n, p, q, Q, r, S, t, v, w, y,"

@cs50.check()
def exists():
    """klingon-quiz3.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def noun_incorrect_3():
    """The Script Terminates And Reveals The Correct Noun After 3 Incorrect Nouns"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdin("ghighi").stdin("ghighi").stdout()
    if "Sorry, you're wrong!\nThe correct answer was ghIgh." != output.rstrip():
        raise cs50.Mismatch("Sorry, you're wrong!\nThe correct answer was ghIgh.", output.rstrip())
    

@cs50.check(exists)
def noun_incorrect_2():
    """The Script Accepts A Correct Noun After 2 Incorrect Nouns"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdin("ghighi").stdin("ghIgh").stdout()
    if "Correct!" != output.rstrip():
        raise cs50.Mismatch("Correct!", output.rstrip())
    

@cs50.check(exists)
def noun_incorrect_1():
    """The Script Accepts A Correct Noun After 1 Incorrect Nouns"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdin("ghIgh").stdout()
    if "Correct!" != output.rstrip():
        raise cs50.Mismatch("Correct!", output.rstrip())
    

@cs50.check(exists)
def noun_correct():
    """The Script Accepts A Correct Noun On The First Try"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghIgh").stdout()
    if "Correct!\nThe correct answer was ghIgh." != output.rstrip():
        raise cs50.Mismatch("Correct!\nThe correct answer was ghIgh.", output.rstrip())


@cs50.check(exists)
def verb_incorrect_3():
    """The Script Terminates And Reveals The Correct Verb After 3 Incorrect Verbs"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("v").stdin("Q").stdin("quche").stdin("quche").stdin("quche").stdout()
    if "Sorry, you're wrong!\nThe correct answer was Qochbe'." != output.rstrip():
        raise cs50.Mismatch("Sorry, you're wrong!\nThe correct answer was ghIgh.", output.rstrip())


@cs50.check(exists)
def verb_incorrect_2():
    """The Script Terminates And Reveals The Correct Verb After 3 Incorrect Verbs"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("v").stdin("Q").stdin("quche").stdin("quche").stdin("Qochbe'").stdout()
    if "Correct!" != output.rstrip():
        raise cs50.Mismatch("Correct!", output.rstrip())


@cs50.check(exists)
def verb_incorrect_1():
    """The Script Accepts A Correct Verb After 2 Incorrect Verbs"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("v").stdin("Q").stdin("quche").stdin("Qochbe'").stdout()
    if "Correct!" != output.rstrip():
        raise cs50.Mismatch("Correct!", output.rstrip())


@cs50.check(exists)
def verb_correct():
    """The Script Accepts A Correct Verb After 1 Incorrect Verbs"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("v").stdin("Q").stdin("Qochbe'").stdout()
    if "Correct!\nThe correct answer was Qochbe'." != output.rstrip():
        raise cs50.Mismatch("Correct!\nThe correct answer was Qochbe'.", output.rstrip())


@cs50.check(exists)
def case_sensitive():
    """The Script Correctly Detects Letter Case"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghigh").stdin("ghigh").stdin("ghigh").stdout()
    if "Sorry, you're wrong!\nThe correct answer was ghIgh." != output.rstrip():
        raise cs50.Mismatch("Sorry, you're wrong!\nThe correct answer was ghIgh.", output.rstrip())