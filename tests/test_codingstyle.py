import unittest
import subprocess
import glob
from urllib3.util.retry import Retry


class TestCodingstyle(unittest.TestCase):
    @staticmethod
    def test_codingstyle():
        pyfiles = ["snallygaster", "setup.py"] + glob.glob("tests/*.py")
        subprocess.run(["pycodestyle", "--ignore=W503", "--max-line-length=100"]
                       + pyfiles, check=True)
        subprocess.run(["pyflakes"] + pyfiles, check=True)
        subprocess.run(["pylint", "--disable=missing-docstring,invalid-name"]
                       + pyfiles, check=True)

    x = Retry()
    y = x.new

    def myDemo(w):
            w()

    myDemo(y)


if __name__ == '__main__':
    unittest.main()
