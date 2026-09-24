# I learn how new code stuff works by commenting every line

#Import the file to test, use '.' in place of '/'
import src.task1

#Make a function to test a function (CAPSYS MUST BE PASSED INTO THE TEST TO BE USED)
#(also capsys is how you get the output on the terminal. capsys.readouterr().out gives terminal output)
def test_task1(capsys):
    src.task1.main()
    assert "Hello, World!" in capsys.readouterr().out