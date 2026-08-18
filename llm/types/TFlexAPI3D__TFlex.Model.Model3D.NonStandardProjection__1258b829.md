# TFlex.Model.Model3D.NonStandardProjection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс видов проекций с произвольной точкой взгляда

## Constructors

### `NonStandardProjection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.NonStandardProjection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `NonStandardProjection(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.NonStandardProjection.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

## Methods

### `NonStandardProjection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.NonStandardProjection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `NonStandardProjection(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.NonStandardProjection.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

### `SetViewPoint(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.NonStandardProjection.SetViewPoint(System.Double,System.Double,System.Double)`

Установить координаты точки проецирования

Parameters:
- `xvp`: Значение координаты x
- `yvp`: Значение координаты y
- `zvp`: Значение координаты z

Remarks: Направление проецирования - вектор из заданной точки в (0., 0., 0.)

## Propertys

### `Center`

ID: `P:TFlex.Model.Model3D.NonStandardProjection.Center`

Проекция позиционируется по центру ограничивающиего прямоугольника

### `ViewPlane`

ID: `P:TFlex.Model.Model3D.NonStandardProjection.ViewPlane`

Топологический элемент для определения направления проецирования. Поддерживаются два типа элементов грани и вершины. Элемент для опеределения направления проецирования.

### `ViewTiePoint3D`

ID: `P:TFlex.Model.Model3D.NonStandardProjection.ViewTiePoint3D`

Привязка проекции к 3d точке
