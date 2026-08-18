# TFlex.Model.Model3D.Workplane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех типов рабочих плоскостей

## Constructors

### `Workplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Workplane.#ctor(TFlex.Model.Document)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `Workplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Workplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Methods

### `Workplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Workplane.#ctor(TFlex.Model.Document)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `Workplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Workplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

### `Project(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Workplane.Project(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Проекция точки на рабочую плоскость

## Propertys

### `AddOffset`

ID: `P:TFlex.Model.Model3D.Workplane.AddOffset`

Смещение рабочей плоскости вдоль нормали

### `Bottom`

ID: `P:TFlex.Model.Model3D.Workplane.Bottom`

Нижняя Y-координата границ бумаги

### `Geometry`

ID: `P:TFlex.Model.Model3D.Workplane.Geometry`

Получить геометрические данные рабочей плоскости

### `GroupType`

ID: `P:TFlex.Model.Model3D.Workplane.GroupType`

Получить тип объекта

### `Left`

ID: `P:TFlex.Model.Model3D.Workplane.Left`

Левая X-координата границ бумаги

### `Right`

ID: `P:TFlex.Model.Model3D.Workplane.Right`

Правая X-координата границ бумаги

### `ShowElements2DInView3D`

ID: `P:TFlex.Model.Model3D.Workplane.ShowElements2DInView3D`

Показать 2D элементы на 3D виде

### `Top`

ID: `P:TFlex.Model.Model3D.Workplane.Top`

Верхняя Y-координата границ бумаги
