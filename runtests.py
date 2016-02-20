import sys
sys.path.append('E:/Software/FreeCAD_0.16.5958_x86_dev_bin/bin')
from tests import *
import cadquery
import unittest

#if you are on python 2.7, you can use -m uniitest discover.
#but this is required for python 2.6.6 on windows. FreeCAD0.12 will not load
#on py 2.7.x on win
suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCadObjects.TestCadObjects))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestWorkplanes.TestWorkplanes))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCQSelectors.TestCQSelectors))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCadQuery.TestCadQuery))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestExporters.TestExporters))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestImporters.TestImporters))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCQGI.TestCQGI))
unittest.TextTestRunner().run(suite)
