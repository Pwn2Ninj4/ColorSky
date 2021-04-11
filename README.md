# ColorSky
This Python library provides you with comfort when creating scripts, it allows you to color strings and labels

### Install
```
pip install ColorSky
```


### Usage
First, import the ColorSky library
```python
from ColorSky import *
```

Print colorful chains as follows

```python
print(red('This string is red'))
```

Print strings with the different styles

```python
print(italic('This string is in italic'))
```

Match styles with colors

```python
print(bold(red('This string is bold and red')))
```

If there was an error in your program or something bad happened, you do not need to print the entire line in red. With ColorSky, you can simply do this

```python 
print(bad('An error ocurred.'))
``` 

#### List of all colors

```python
white, grey, black, green, lightgreen, cyan, lightcyan, red, lightred,
blue, lightblue, purple, light purple, orange, yellow
```

#### Lista of all styles

```python
bold, bg, under, strike, italic
```

#### Label list

```python
info, que, run, bad, good
``` 
