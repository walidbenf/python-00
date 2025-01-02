Les variables en python s'écrivent en Camel case exemple:
```
hero_health = 100
```

On peut afficher la valeur d'une variable en mettant un f dans notre print et en encapsulant la variable:
```
print(f"Walid a {hero_health} points de vie")
```
On peut utiliser le type None si jamais on a une variable qui n'a pas encore de valeur définie(par exemple la on peut définir age sur None et plus tard demander l'age à notre utilisateur:
```
age = None
age = input("How old are you? ")
```
Python est typé dynamiquement, ce qui signifie qu’une variable peut stocker n’importe quel type et que ce type peut changer.
Toutes les fonctions doivent être définies avant d'être utilisées.
La plupart des développeurs Python résolvent ce problème en définissant d'abord toutes les fonctions de leur programme, puis en dernier
, ils appellent une fonction "point d'entrée". De cette façon, toutes les fonctions ont été lues par l'interpréteur Python avant que la première ne soit appelée.
