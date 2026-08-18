# TFlex.Model.Model3D.ViewSection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Сечение по 3D узлам и экранной плоскости

## Constructors

### `ViewSection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ViewSection.#ctor(TFlex.Model.Document)`

Конструктор для создания сечения по 3D узлам и экранной плоскости

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `ViewSection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ViewSection.#ctor(TFlex.Model.Document)`

Конструктор для создания сечения по 3D узлам и экранной плоскости

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `Normal`

ID: `P:TFlex.Model.Model3D.ViewSection.Normal`

Получить вектор номали к экранной плоскости

### `Origin`

ID: `P:TFlex.Model.Model3D.ViewSection.Origin`

Получить точку, лежащую на экранной плоскости

### `Points`

ID: `P:TFlex.Model.Model3D.ViewSection.Points`

Множество точек. Ломанная, построенная на последовательности проекций этих точек на плоскость сечения образуют контур сечения

Remarks: В настоящей версии в качестве точки можно выбирать только 3D узлы и вершины. В остальных случаях сечение строится не будет
