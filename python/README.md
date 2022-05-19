
Collection of Kannada language specific tools.

Install by running the following command.

```
pip3 install kannada
```

```python
from kannada import utils as knutils

print(knutils.letters("ನನ್ನಂತೆ")) # ["ನ", "ನ್ನಂ", "ತೆ"]
```



## Letters

Split the given Kannada text into letters. It handles the
complex letters including Vattaksharas.

```python
from kannada import knutils

print(knutils.letters("ನನ್ನಂತೆ")) # ["ನ", "ನ್ನಂ", "ತೆ"]
```

