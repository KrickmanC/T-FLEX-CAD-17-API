# TFlex.Model.Model3D.OnWirePoint

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Узел, построенный на проволочной модели (на пути)

## Constructors

### `OnWirePoint(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OnWirePoint.#ctor(TFlex.Model.Document)`

Конструктор для создания узла на проволочной модели (на пути)

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `OnWirePoint(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OnWirePoint.#ctor(TFlex.Model.Document)`

Конструктор для создания узла на проволочной модели (на пути)

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Propertys

### `Offset`

ID: `P:TFlex.Model.Model3D.OnWirePoint.Offset`

Смещение на пути

### `Param`

ID: `P:TFlex.Model.Model3D.OnWirePoint.Param`

Получить параметр на пути

### `Parameterization`

ID: `P:TFlex.Model.Model3D.OnWirePoint.Parameterization`

Тип параметризации

### `Path`

ID: `P:TFlex.Model.Model3D.OnWirePoint.Path`

Путь, на котором строится 3D узел

Remarks: В качестве пути можно задавать только профиль, путь, ребро. В остальных случаях узел строится не будет. При установке пути, все ранее установленные значения Offset или Param будут сброшены

### `Reference`

ID: `P:TFlex.Model.Model3D.OnWirePoint.Reference`

Тип точки отсчёта

### `ReferencePoint`

ID: `P:TFlex.Model.Model3D.OnWirePoint.ReferencePoint`

Точка отсчёта смещения
