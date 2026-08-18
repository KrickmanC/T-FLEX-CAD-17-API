# TFlex.Model.Model3D.StandardWorkplane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Стандартная рабочая плоскость

## Constructors

### `StandardWorkplane(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType)`

ID: `M:TFlex.Model.Model3D.StandardWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType)`

Конструктор для создания стандартной рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `type`: Стандартный вид

Remarks: Рабочая плоскость создаётся на активной странице

### `StandardWorkplane(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.StandardWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType,TFlex.Model.Page)`

Конструктор для создания стандартной рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `type`: Стандартный вид
- `page`: Страница, на которой создаётся рабочая плоскость

### `StandardWorkplane(TFlex.Model.Model3D.Workplane,System.Double)`

ID: `M:TFlex.Model.Model3D.StandardWorkplane.#ctor(TFlex.Model.Model3D.Workplane,System.Double)`

Конструктор для создания стандартной рабочей плоскости, смещённой относительно другой рабочей плоскости

Parameters:
- `plane`: Родительская плоскость
- `offset`: Смещение

Remarks: Рабочая плоскость создаётся на активной странице

## Methods

### `StandardWorkplane(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType)`

ID: `M:TFlex.Model.Model3D.StandardWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType)`

Конструктор для создания стандартной рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `type`: Стандартный вид

Remarks: Рабочая плоскость создаётся на активной странице

### `StandardWorkplane(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.StandardWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.StandardWorkplane.StandardType,TFlex.Model.Page)`

Конструктор для создания стандартной рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `type`: Стандартный вид
- `page`: Страница, на которой создаётся рабочая плоскость

### `StandardWorkplane(TFlex.Model.Model3D.Workplane,System.Double)`

ID: `M:TFlex.Model.Model3D.StandardWorkplane.#ctor(TFlex.Model.Model3D.Workplane,System.Double)`

Конструктор для создания стандартной рабочей плоскости, смещённой относительно другой рабочей плоскости

Parameters:
- `plane`: Родительская плоскость
- `offset`: Смещение

Remarks: Рабочая плоскость создаётся на активной странице

### `SetPosition(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.StandardWorkplane.SetPosition(TFlex.Model.Model3D.Geometry.Point3D)`

Переместить рабочую плоскость до совпадения с точкой

## Propertys

### `Standard`

ID: `P:TFlex.Model.Model3D.StandardWorkplane.Standard`

Стандартный вид рабочей плоскости
