# TFlex.Model.Model3D.OutlinePath

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс линии очерка

## Constructors

### `OutlinePath(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OutlinePath.#ctor(TFlex.Model.Document)`

Конструктор для создания линии очерка

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `OutlinePath(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OutlinePath.#ctor(TFlex.Model.Document)`

Конструктор для создания линии очерка

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `ChangeOutline`

ID: `M:TFlex.Model.Model3D.OutlinePath.ChangeOutline`

Выбрать другую линию очерка

Remarks: Функцию можно вызывать, когда все данные заданы, то есть построен первый очерк

## Propertys

### `Direction`

ID: `P:TFlex.Model.Model3D.OutlinePath.Direction`

Направление очерка

Remarks: Вектор очерка задаётся двумя взаимоисключающими методами: направлением или двумя точками

### `FirstPoint`

ID: `P:TFlex.Model.Model3D.OutlinePath.FirstPoint`

Первая точка, задающая направление очерка

Remarks: Вектор очерка задаётся двумя взаимоисключающими методами: направлением или двумя точками

### `Operation`

ID: `P:TFlex.Model.Model3D.OutlinePath.Operation`

Тело, для которого задаётся очерк

Remarks: В настоящей версии в качестве тела можно выбирать только 3D операцию. В остальных случаях путь строится не будет

### `SecondPoint`

ID: `P:TFlex.Model.Model3D.OutlinePath.SecondPoint`

Вторая точка, задающая направление очерка

Remarks: Вектор очерка задаётся двумя взаимоисключающими методами: направлением или двумя точками

### `VerticalFaces`

ID: `P:TFlex.Model.Model3D.OutlinePath.VerticalFaces`

Параметр обработки вертикальных граней
