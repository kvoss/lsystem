lsystem
=======

A Python module for L-systems

Example use:

    >>> from lsystem import LSystem

    >>> algae = LSystem(axiom='a', rules={'a':'ab', 'b':'a'})
    >>> print algae[5]
    abaababaabaab


