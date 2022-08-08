import check50 as cs50


SCRIPT_NAME = "klingon-quiz3.py"

"b, ch, D, gh, H, j, l, m, n, p, q, Q, r, S, t, v, w, y,"

@cs50.check()
def exists():
    """klingon-quiz3.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def noun_incorrect_3():
    """The Script Terminates And Reveals The Correct Answer After 3 Incorrect Guesses"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdin("ghighi").stdin("ghighi").stdout()
    if "Sorry, you're wrong!\nThe correct answer was ghIgh." != output.rstrip():
        raise cs50.Mismatch("Sorry, you're wrong!\nThe correct answer was ghIgh.", output.rstrip())
    

@cs50.check(exists)
def noun_incorrect_2():
    """The Script Terminates And Reveals The Correct Answer After 3 Incorrect Guesses"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdin("ghighi").stdin("ghIgh").stdout()
    if "Sorry, you're wrong!\nThe correct answer was ghIgh." != output.rstrip():
        raise cs50.Mismatch("Sorry, you're wrong!\nThe correct answer was ghIgh.", output.rstrip())
    

@cs50.check(exists)
def noun_incorrect_1():
    """The Script Terminates And Reveals The Correct Answer After 3 Incorrect Guesses"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdin("ghighi").stdin("ghighi").stdout()
    if "Sorry, you're wrong!\nThe correct answer was ghIgh." != output.rstrip():
        raise cs50.Mismatch("Sorry, you're wrong!\nThe correct answer was ghIgh.", output.rstrip())
    

@cs50.check(exists)
def noun_correct():
    """The Script Terminates And Reveals The Correct Answer After 3 Incorrect Guesses"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("n").stdin("gh").stdin("ghighi").stdin("ghighi").stdin("ghighi").stdout()
    if "Sorry, you're wrong!\nThe correct answer was ghIgh." != output.rstrip():
        raise cs50.Mismatch("Sorry, you're wrong!\nThe correct answer was ghIgh.", output.rstrip())