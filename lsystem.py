from itertools import islice
import unittest

# TODO: try transforming productions just like words

class LSystemI:
    def __init__(self, word='', productions={}):
        self.word = word
        self.productions = productions

    def __iter__(self):
        return self

    def next(self):
        old = self.word
        self.word = ''.join(self.productions.get(c, c) for c in self.word)
        return old

class LSystem(object):
    """Container for an L-System
    
    """
    def __init__(self, variables=[], axiom='', consts=[], productions={}):
        super(LSystem, self).__init__()
        self.variables = variables,
        self.axiom = axiom
        self.consts = consts
        self.productions = productions

    def __getitem__(self, n):
        "Returns the nth generation or the axiom"
        iterable = LSystemI(self.axiom, self.productions)
        return next(islice(iterable, n, None), self.axiom)


class TestLSystem(unittest.TestCase):
    def test_algae(self):
        algae = dict(
                variables=['A', 'B'], 
                axiom='A', 
                productions={ 'A':'AB', 'B': 'A'})
        algaeL = LSystem(**algae)
        self.assertEqual('ABAABABAABAAB', algaeL[5])

    def test_ex2(self):
        ex2 = LSystem(['0', '1'], '0', productions={'1': '11', '0': '1[0]0'})
        self.assertEqual('1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0', ex2[3])

    def test_koch_curve(self):
        koch_curve = dict(
                variables = ['F'],
                consts = ['+', '-'],
                axiom = 'F',
                productions = {'F': 'F+F-F-F+F'})
        koch_curveL = LSystem(**koch_curve)
        self.assertEqual('F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F', koch_curveL[2])

    def test_sierpinski_triangle(self):
        sierpinski_triangle = dict(
                variables = ['A', 'B'],
                consts = ['+', '-'],
                axiom = 'A',
                productions = {'A': 'B-A-B', 'B': 'A+B+A'})
        sierpinski_triangleL = LSystem(**sierpinski_triangle)
        self.assertEqual('B-A-B+A+B+A+B-A-B-A+B+A-B-A-B-A+B+A-B-A-B+A+B+A+B-A-B', 
                sierpinski_triangleL[3])

if __name__ == '__main__':
    unittest.main()

