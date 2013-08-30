import objfetch
import pprint

class Node(object):
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.parent = None
        self.child = []
        self.nothing = lambda x : x

    def add(self,c):
        self.child += [c]
        c.parent = self

        return c

n = Node("root",10)
n.add(Node("A",5)).add(Node("a",3))
n.add(Node("B",2)).add(Node("b",4))

structure = {
    "__vars__":["name","value"],
    "child" : objfetch.FetchCondition(lambda x:len(x)>0,objfetch.FetchRecursive())
}

pprint.pprint(objfetch.fetch(n,structure))
pprint.pprint(objfetch.fetch(n,objfetch.allvalue))
