"""
A command line interface for running python programs and getting audio output
"""
import sys
from helpers import (
    store_output,
    sayFunc,
    read_program,
    build_trycatch,
)
import io

# pylint: disable=no-value-for-parameter
# pylint: disable=broad-except
# pylint: disable=import-outside-toplevel


def main(file):
    """
    Cli for running python programs
    """
    try:
        assert file[-3:] == ".py"
    except AssertionError:
        sayFunc("File not ending in .py", 120)
        sys.exit(1)
    try:
        with open(file, "rb") as source_file:
            code = compile(source_file.read(), file, "exec")
        print(code)
        try:
            exec(code)
            output = 1
            return output
        except Exception as e:
            print(e)
            build_trycatch(file)
            from test import test

            line, text, name, error = test()
            name = str(name).split("'")[1]
            line -= 4
            repeat = "R"
            while repeat in ("r", "R"):
                sayFunc(
                    "There is a error in your program. "
                    + file
                    + "The error is as follows. "
                    + name
                    + str(error),
                    100,
                )
                sayFunc("Line" + str(line) + "is. " + text, 130)
                repeat = "l"
            return error
    except SyntaxError as err:
        _, error, _ = sys.exc_info()
        repeat = "R"
        while repeat in ("r", "R"):
            sayFunc(
                "There is a error in your program. "
                + file
                + "The error is as follows. "
                + str(err),
                100,
            )
            repeat = "l"
            sayFunc(
                "Line" + str(line) + "is. " + file_name.readlines()[err.lineno - 1], 130
            )
        return error


if __name__ == "__main__":
    main("x.py")
