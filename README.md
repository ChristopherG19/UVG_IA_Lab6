# UVG_IA_Lab6

## Task 1.1 (LOL)
- ¿Qué métrica usaron para seleccionar los features?

  - Se utiliza el coeficiente de correlación de Pearson y los gráficos de caja y bigotes para determinar que variables aportaban menos valor al modelo.
- Los features más importantes son:

  -  Blue Wins
  - Blue kills
  - Red Deaths
  - Blue Total Experience
  - Blue Total Minions Killed

- Para manejar el overfitting, ya que se normalizaron algunos datos y se buscó el balanceo de datos, se trabajó con cross-validation.

- En cuanto al tunning de variables, esto se trabajó principalmente en la evaluación de los modelos, dónde se modificó la profundidad del árbol y la cantidad de intentos para buscar el mejor split de los datos al momento de construir el árbol, para el cross_validation se modificaron datos como el número de trabajos a realizar y la cantidad de "folds" que se realizarían.

## Task 1.2 (FIFA)
