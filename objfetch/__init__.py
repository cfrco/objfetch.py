import types

__version__ = '0.1-beta'

class FetchFunction(object):
    def __init__(self,func):
        self.func = func

    def get_value(self,item):
        return self.func(item)

    @staticmethod
    def fetch_not_allow(not_allow=[]):
        def _func_(obj):
            out = {}
            for k,v in obj.__dict__.items():
                for na in not_allow:
                    if na(k,v): break
                else: out[k] = v
            return out
        return FetchFunction(_func_)

class FetchRecursive(object):
    def __init__(self,structure=None):
        self.structure = structure

class FetchCondition(object):
    def __init__(self,condition,structure=None):
        self.condition = condition
        self.structure = structure

allvalue_not_allow_list = [
    lambda k,v : isinstance(v,types.FunctionType),
    lambda k,v : hasattr(v,'__iter__')
]
allvalue = FetchFunction.fetch_not_allow(allvalue_not_allow_list)

def fetch(obj,structure):
    if isinstance(structure,FetchFunction):
        return structure.get_value(obj)

    elif hasattr(obj,'__iter__') and not isinstance(obj,str):
        out = []
        for o in obj:
            out += [fetch(o,structure)]
    else:
        out = {}
        for k,v in structure.items():
            if isinstance(v,FetchCondition):
                if v.condition(obj.__getattribute__(k)):
                    v = v.structure
                else: continue
                    
            if k == "__vars__":
                for name in v:
                    out[name] = obj.__getattribute__(name)
            elif v == None :
                out[k] = obj.__getattribute__(k)
            elif isinstance(v,FetchRecursive):
                if v.structure == None:
                    out[k] = fetch(obj.__getattribute__(k),structure)
                else:
                    out[k] = fetch(obj.__getattribute__(k),v.structure)
            else:
                out[k] = fetch(obj.__getattribute__(k),v)

    return out
