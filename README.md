# ColorSky
Esta librería de Python te proporciona comodidad a la hora de crear scripts, permite dar color a cadenas y etiquetas
### Uso
Primero, importa la librería ColorSky
```python
from ColorSky import *
```

Imprime cadenas coloridas de la siguiente manera

```python
print(red('This string is red'))
```

Imprime cadenas con los distintos estilos

```python
print(italic('This string is in italic'))
```

Combina estilos con los colores

```python
print(bold(red('This string is bold and red')))
```

Si se produjo algún error en su programa o algo malo sucedió, no es necesario que imprima toda la línea en rojo. Con ColorSky, simplemente puede hacer esto 

```python 
print(bad('An error ocurred.'))
``` 

#### Lista de todos los colores

```python
white, grey, black, green, lightgreen, cyan, lightcyan, red, lightred,
blue, lightblue, purple, light purple, orange, yellow
```

#### Lista de todos los estilos

```python
bold, bg, under, strike, italic
```

#### Lista de etiquetas

```python
info, que, run, bad, good
``` 
