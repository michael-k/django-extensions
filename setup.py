# -*- coding: utf-8 -*-
"""
Based entirely on Django's own ``setup.py``.
"""
import sys
from setuptools import setup

try:
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        user_options = TestCommand.user_options[:] + [
            ('pytest-args=', 'a', "Arguments to pass into py.test"),
            ('exitfirst', 'x', "exit instantly on first error or failed test."),
            ('no-cov', 'C', "Disable coverage report completely"),
        ]
        exitfirst = False
        no_cov = False

        def initialize_options(self):
            TestCommand.initialize_options(self)
            self.pytest_args = 'tests django_extensions --ds=tests.testapp.settings --cov=django_extensions --cov-report html --cov-report term'

        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True
            if self.exitfirst:
                self.pytest_args += " -x"
            if self.no_cov:
                self.pytest_args += " --no-cov"

        def run_tests(self):
            import shlex
            import pytest
            errno = pytest.main(shlex.split(self.pytest_args))
            sys.exit(errno)
except ImportError:
    PyTest = None

if PyTest:
    cmdclasses = {"test": PyTest}
else:
    cmdclasses = {}


setup(
    cmdclass=cmdclasses,
)
