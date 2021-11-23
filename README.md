lsystem
=======

A Python module for L-systems

Example use:

```python
>>> from lsystem import LSystem

>>> algae = LSystem(axiom='a', productions={'a':'ab', 'b':'a'})
>>> print(algae[5])
abaababaabaab
```

Requires Python3 or Python>=2.2

Another example is given as a script `example-plant.py`.
Running the script 

```shell
python example-plant.py
```

results in the following picture: ![plant image](imgs/plant6.png)
