lsystem
=======

A Python module for L-systems

Example use:
    ```python
    >>> from lsystem import LSytem

    >>> algae = LSytem(axiom='a', rules={'a':'ab', 'b':'a'})
    >>> print algae[5]
    abaababaabaab
    ```

