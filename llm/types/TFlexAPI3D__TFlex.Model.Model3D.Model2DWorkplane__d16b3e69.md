# TFlex.Model.Model3D.Model2DWorkplane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Рабочая плоскость, построенная по 2D

## Constructors

### `Model2DWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Model2DWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `Model2DWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Model2DWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Methods

### `Model2DWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Model2DWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `Model2DWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Model2DWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Propertys

### `BaseNode`

ID: `P:TFlex.Model.Model3D.Model2DWorkplane.BaseNode`

Точка привязки

Remarks: Для рабочей плоскости по проекции точка привязки не используется

### `BoundQuadrant`

ID: `P:TFlex.Model.Model3D.Model2DWorkplane.BoundQuadrant`

Квадрант границы рабочей плоскости, если границы задаются одним узлом и границами листа

Remarks: Квадранты нумеруются от 1 до 4. По умолчанию первый угол задаётся точкой привязки.

### `FirstBoundCorner`

ID: `P:TFlex.Model.Model3D.Model2DWorkplane.FirstBoundCorner`

Первый угол границы

Remarks: По умолчанию первый угол задаётся точкой привязки

### `SecondBoundCorner`

ID: `P:TFlex.Model.Model3D.Model2DWorkplane.SecondBoundCorner`

Второй угол границы

### `TargetNode`

ID: `P:TFlex.Model.Model3D.Model2DWorkplane.TargetNode`

Связь с 3D-узлом

Remarks: Для рабочей плоскости по проекции и рабочей плоскости по системе координат связь с 3D-узлом не используется
