import sys
import io
import multiprocessing
import pyttsx3
import linecache


def store_output(code):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    exec(code)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output


def sayFunc(phrase, speed ):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("rate", speed)
    engine.setProperty("voice",voices[16].id)
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()

def read_program(file):
    f = open(file)
    x = f.readlines()
    for i in range(len(x)):
        sayFunc("\nLine " + str(i + 1) + ". " + x[i], 120)

def build_trycatch(file):
    f = open(file)
    l = ["\t\t" + line for line in f.readlines()]
    l.insert(0, "\ttry:\n")
    l.insert(0, "def test():\n")
    l.insert(0, "import sys\n")
    l.insert(0, "import traceback\n")
    l.append("\n\t\treturn 1")
    l.append("\n\texcept:\n")
    l.append("\n\t\tname, h, tb = sys.exc_info()")
    l.append("\n\t\ttraceback.print_tb(tb)")
    l.append("\n\t\ttb_info = traceback.extract_tb(tb)")
    l.append("\n\t\tfilename, line, func, text = tb_info[-1]")
    l.append("\n\t\treturn line,text,name , h")
    f = open("test.py", "w")
    f.write("".join(l))
    f.close()
