#!/usr/bin/env python3
import sys

from IPython.core.ultratb import VerboseTB
import nose
from nose.plugins import Plugin


class NoseVTB(Plugin):
    """Formats nosetests traceback with VerboseTB from IPython.  """
    name = 'vtb'
    formatter = VerboseTB()

    def _print_exception(self, err):
        stdout, sys.stdout = sys.stdout, sys.__stdout__
        print(self.formatter.text(*err))
        sys.stdout = stdout

    def addError(self, test, err):
        self._print_exception(err)

    def addFailure(self, test, err):
        self._print_exception(err)


if __name__ == '__main__':
    nose.main(addplugins=[NoseVTB()])
