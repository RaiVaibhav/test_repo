import unittest
from io import StringIO
from MultiplyDivide.Debugfunc import debug_func, db

class DebugModeTest(unittest.TestCase):

    def test_debug_mode_function(self):
        args = {}
        kwargs = {}

        def fun(*args, **kwargs):
          yield 1
          yield 2

        input = StringIO("q\nq\nq")
        output = StringIO()
        dbg = db(stdin=input ,stdout=output)
        dbg.do_q = dbg.do_continue
        self.assertEqual(debug_func(fun, dbg, *args, **kwargs), [1,2])
        output = output.getvalue()
        self.assertEqual(output.split('\n')[1], '-> yield 1')
        self.assertEqual(output.split('\n')[3], '-> yield 2')
