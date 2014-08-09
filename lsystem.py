from itertools import islice
import unittest

class LSystemI:
    def __init__(self, pieces='', rules={}):
        self.pieces = pieces
        self.rules = rules

    def __iter__(self):
        return self

    def next(self):
        pieces = []
        for v in self.pieces:
            try:
                pieces.append(self.rules[v])
            except KeyError:
                pieces.append(v)
        old = self.pieces
        self.pieces = ''.join(pieces)
        #self.rules = self.rules
        # we could trasform them too
        return old

class LSystem(object):
    """Container for an L-System
    
    """
    def __init__(self, variables=[], axiom='', consts=[], rules={}):
        super(LSystem, self).__init__()
        self.variables = variables,
        self.axiom = axiom
        self.consts = consts
        self.rules = rules

    def __getitem__(self, n):
        "Returns the nth item or the axiom"
        iterable = LSystemI(self.axiom, self.rules)
        return next(islice(iterable, n, None), self.axiom)


class TestLSystem(unittest.TestCase):
    def test_algae(self):
        algae = dict(
                variables=['A', 'B'], 
                axiom='A', 
                rules={ 'A':'AB', 'B': 'A'})
        algaeL = LSystem(**algae)
        self.assertEqual('ABAABABAABAAB', algaeL[5])

    def test_ex2(self):
        ex2 = LSystem(['0', '1'], '0', rules={'1': '11', '0': '1[0]0'})
        self.assertEqual('1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0', ex2[3])

    def test_koch_curve(self):
        koch_curve = dict(
                variables = ['F'],
                consts = ['+', '-'],
                axiom = 'F',
                rules = {'F': 'F+F-F-F+F'})
        koch_curveL = LSystem(**koch_curve)
        self.assertEqual('F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F', koch_curveL[2])

    def test_sierpinski_triangle(self):
        sierpinski_triangle = dict(
                variables = ['A', 'B'],
                consts = ['+', '-'],
                axiom = 'A',
                rules = {'A': 'B-A-B', 'B': 'A+B+A'})
        sierpinski_triangleL = LSystem(**sierpinski_triangle)
        self.assertEqual('B-A-B+A+B+A+B-A-B-A+B+A-B-A-B-A+B+A-B-A-B+A+B+A+B-A-B', 
                sierpinski_triangleL[3])

if __name__ == '__main__':
    unittest.main()

