# objfetch
A tool to translate Python Objects to dict&list.

### Motivation
Recently, I work with LeapMotion(Python SDK). When I try to record `frame`s and translate it to `JSON` or `pickle`, it cause Execption. So, I write this code to translate objects to dict&list that are easy to translate to `JSON` or `pickle`.

### Features
 * Use `dict` as structure to translate.
 * Can choose the fields we want.
 * Easy-use recursive structure.
 * Flexible and customizable action.

### Structure
#### An example for Leap.Frame
```python
import objfetch

vector2tuple = objfetch.FetchFunction(lambda v : (v[0],v[1],v[2]))
frame_structure = {
   	"hands":{
       	"fingers":{
           	"__vars__": ["id"],
           	"tip_position":vector2tuple,
       	}  
   	}        
}

import pprint
pprint.pprint(objfetch.fetch(frame,frame_structure))
```
Output:
```
{u'hands': [{u'fingers': [{u'id': 4,
                        u'tip_position': [-33.04090881347656,
                                          167.19410705566406,
                                          -65.78760528564453]},
                       {u'id': 1,
                        u'tip_position': [17.395418167114258,
                                          157.41246032714844,
                                          -63.4946403503418]},
                       {u'id': 2,
                        u'tip_position': [-61.48387908935547,
                                          185.1539306640625,
                                          -40.94517135620117]}]}]}
```

#### Conditional and Recursive
```python
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
```
Output:
```
{'child': [{'child': [{'name': 'a', 'value': 3}], 'name': 'A', 'value': 5},
           {'child': [{'name': 'b', 'value': 4}], 'name': 'B', 'value': 2}],
 'name': 'root',
 'value': 10}
{'name': 'root', 'parent': None, 'value': 10}
```

### Detail
#### Functions
 * objfetch.fetch(obj,structure)

#### Classes
 * objfetch.FetchFunction(func)
 * objfetch.FetchRecursive(structure=None)
 * objfetch.FetchCondition(condition,structure=None)

#### Useful Tool
 * objfetch.allvalue (objfetch.FetchFunction)
