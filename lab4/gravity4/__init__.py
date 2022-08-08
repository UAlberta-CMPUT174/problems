import check50 as cs50


SCRIPT_NAME = "gravity4.py"

TEST_ONE_OUTPUT = """
Let's try all the methods we have:
Caesar cipher: 4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6
Atbash cipher: 4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6
Combined: 1) Caesar; 2) Atbash cipher: 4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6
Combined: 1) Atbash; 2) Caesar cipher: 4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6
A1Z26 cipher: DPS KWJ TIAJEDWOFE OE BSFY ULSBSF
Combined: 1) A1Z26; 2) Caesar cipher: AMP HTG QFXGBATLCB LB YPCV RIPYPC
Combined: 1) A1Z26; 2) Atbash cipher: WKH PDQ GRZQVWDLUV LV YHUB FOHYHU
Combined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: THE MAN DOWNSTAIRS IS VERY CLEVER
Combined: 1) A1Z26; 2) Caesar; 3) Atbash cipher: ZNK SGT JUCTYZGOXY OY BKXE IRKBKX
"""

TEST_TWO_OUTPUT = """
Let's try all the methods we have:
Caesar cipher: 19-2-23-11-18-17 12-22 9-24-17!
Atbash cipher: 19-2-23-11-18-17 12-22 9-24-17!
Combined: 1) Caesar; 2) Atbash cipher: 19-2-23-11-18-17 12-22 9-24-17!
Combined: 1) Atbash; 2) Caesar cipher: 19-2-23-11-18-17 12-22 9-24-17!
A1Z26 cipher: SBWKRQ LV IXQ!
Combined: 1) A1Z26; 2) Caesar cipher: PYTHON IS FUN!
Combined: 1) A1Z26; 2) Atbash cipher: HYDPIJ OE RCJ!
Combined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: EVAMFG LB OZG!
Combined: 1) A1Z26; 2) Caesar; 3) Atbash cipher: KBGSLM RH UFM!
"""

@cs50.check()
def exists():
    """gravity4.py exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_one():
    """Correct: The Secret Message Is, 'THE MAN DOWNSTAIRS IS VERY CLEVER'"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6").stdout()
    if TEST_ONE_OUTPUT.lstrip().rstrip() != output.rstrip():
        raise cs50.Mismatch(TEST_ONE_OUTPUT.lstrip().rstrip(), output.rstrip())


@cs50.check(exists)
def test_two():
    """Correct: The Secret Message Is, 'PYTHON IS FUN!'"""
    output = cs50.run(f"python3 {SCRIPT_NAME}").stdin("19-2-23-11-18-17 12-22 9-24-17!").stdout()
    if TEST_ONE_OUTPUT.lstrip().rstrip() != output.rstrip():
        raise cs50.Mismatch(TEST_ONE_OUTPUT.lstrip().rstrip(), output.rstrip())
