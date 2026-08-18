# TFlex.Model.Model2D.PathConstruction

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Линия построения - путь

## Constructors

### `PathConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.PathConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `PathConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.PathConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `GetAngle(System.ValueType!TFlex.Drawing.Point!System.Runtime.CompilerServices.IsBoxed)`

ID: `M:TFlex.Model.Model2D.PathConstruction.GetAngle(System.ValueType!TFlex.Drawing.Point!System.Runtime.CompilerServices.IsBoxed)`

Получить угол наклона касательной в заданной точке пути

Parameters:
- `point`: Точка на пути

Returns: Угол относительно оси OX(в градусах)

### `GetCircleArcApproximation(System.Double)`

ID: `M:TFlex.Model.Model2D.PathConstruction.GetCircleArcApproximation(System.Double)`

Геометрия дуг окружностей

### `GetRelativePointToBegin(System.Double)`

ID: `M:TFlex.Model.Model2D.PathConstruction.GetRelativePointToBegin(System.Double)`

Получить точку на пути

Parameters:
- `distance`: Расстояние от начала пути

Returns: Точка на пути

Remarks: Параметр distance не должен превышать длину пути

## Propertys

### `ConstructionGeometry`

ID: `P:TFlex.Model.Model2D.PathConstruction.ConstructionGeometry`

Геометрия линии построения

### `Contour`

ID: `P:TFlex.Model.Model2D.PathConstruction.Contour`

Контур пути

### `GeometryType`

ID: `P:TFlex.Model.Model2D.PathConstruction.GeometryType`

Тип геометрии линии построения

### `Length`

ID: `P:TFlex.Model.Model2D.PathConstruction.Length`

Длина пути

### `PolylineConstructionGeometry`

ID: `P:TFlex.Model.Model2D.PathConstruction.PolylineConstructionGeometry`

Геометрия линии построения (полилиния)

Remarks: После использования рекомендуется удалить полученную геометрию, использую функцию Dispose().

### `SubType`

ID: `P:TFlex.Model.Model2D.PathConstruction.SubType`

Подтип линии построения
