import pdb
import collections

class db(pdb.Pdb):
    def do_continue(self,arg):
        self.clear_all_breaks()
        super().do_continue(arg)
        return(1) # pragma: no cover

dbg = db()
dbg.do_q = dbg.do_continue

def debug_func(func, dbg, *args,**kwargs):
    results = []
    bear_results = dbg.runcall(func, *args, **kwargs)
    if isinstance(bear_results, collections.Iterable):
        try:
            iterator = iter(bear_results)
            while True:
                result = dbg.runcall(next, iterator)
                results.append(result)
        except StopIteration:
            return results
    else:
        return results
