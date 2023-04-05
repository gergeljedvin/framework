import sys
import unittest
from tests.something import Something


def suite():
    suite_x = unittest.TestSuite()
    suite_x.addTest(unittest.makeSuite(Something))

    return suite_x


def run():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == '__main__':
    run()
