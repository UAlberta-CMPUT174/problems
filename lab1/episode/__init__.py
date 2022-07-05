import check50 as cs50


SCRIPT_NAME = "episode.py"


def unreadable(season, episode, name):
    """Given a season, episode, and name, returns the unreadable formatted string"""
    return f"S{season}_E{episode}_{name}"


def readable(season, episode, name):
    """Given a season, episode, and name, returns the readable formatted string"""
    return f"Season {season}, Episode {episode}: {name} (The Simpsons)"


@cs50.check()
def exists():
    """episode.py Exists"""
    cs50.exists(SCRIPT_NAME)


@cs50.check(exists)
def test_one():
    """Test Passed For Test One"""
    output = \
        cs50.run(f"python3 {SCRIPT_NAME}") \
            .stdin(unreadable(18, 7, "Fatzcarraldo")) \
            .stdout()
    if readable(18, 7, "Fatzcarraldo") != output.rstrip():
        raise cs50.Mismatch(readable(18, 7, "Fatzcarraldo"), output.rstrip())


@cs50.check(exists)
def test_two():
    """Test Passed For Test Two"""
    output = \
        cs50.run(f"python3 {SCRIPT_NAME}") \
            .stdin(unreadable(8, 17, "Life on Fast Lane")) \
            .stdout()
    if readable(8, 17, "Life on Fast Lane") != output.rstrip():
        raise cs50.Mismatch(readable(8, 17, "Life on Fast Lane"), output.rstrip())


@cs50.check(exists)
def test_three():
    """Test Passed For Test Three"""
    output = \
        cs50.run(f"python3 {SCRIPT_NAME}") \
            .stdin(unreadable(4, 9, "Last Exit to Springfield")) \
            .stdout()
    if readable(4, 9, "Last Exit to Springfield") != output.rstrip():
        raise cs50.Mismatch(readable(4, 9, "Last Exit to Springfield"), output.rstrip())
