# TFlex.Model.Model3D.OffsetPath

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Путь, построенный как смещение к плоской проволочной модели

## Constructors

### `OffsetPath(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OffsetPath.#ctor(TFlex.Model.Document)`

Конструктор для создания пути как смещения к плоской проволочной модели

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `OffsetPath(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OffsetPath.#ctor(TFlex.Model.Document)`

Конструктор для создания пути как смещения к плоской проволочной модели

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `BreakFillType`

ID: `P:TFlex.Model.Model3D.OffsetPath.BreakFillType`

Способ обработки разрывов

Remarks: Для границ контуров, состоящих из нескольких рёбер или имеющих изломы в вершинах, возможно возникновение разрывов между эквидистантами, построенными для каждого ребра. В этом случае задаётся способ обработки такого разрыва. По умолчанию используется метод продолжения по кривой

### `Offset`

ID: `P:TFlex.Model.Model3D.OffsetPath.Offset`

Значение смещения

Remarks: Значение смещения задаётся двумя взаимоисключающими способами: по точке или по значению

### `OffsetPoint`

ID: `P:TFlex.Model.Model3D.OffsetPath.OffsetPoint`

Точка, определяющая значение смещения

Remarks: В настоящей версии в качестве точки можно выбирать только 3D узел. В остальных случаях путь строится не будет. Значение смещения задаётся двумя взаимоисключающими способами: по точке или по значению

### `PlanarWire`

ID: `P:TFlex.Model.Model3D.OffsetPath.PlanarWire`

Проволочная модель

Remarks: В настоящей версии в качестве проволочной модели можно выбирать только плоский 3D путь. В остальных случаях путь строится не будет

### `RemoveLoops`

ID: `P:TFlex.Model.Model3D.OffsetPath.RemoveLoops`

Удалять петли
