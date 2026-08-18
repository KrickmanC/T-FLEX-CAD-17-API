# TFlex.Model.Model3D.Model3DWorkplane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Рабочая плоскость, построенная по 3D

## Constructors

### `Model3DWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Model3DWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `Model3DWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Model3DWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Methods

### `Model3DWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Model3DWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `Model3DWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Model3DWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Propertys

### `Location`

ID: `P:TFlex.Model.Model3D.Model3DWorkplane.Location`

Точка, задающая начало координат рабочей плоскости

### `ReferenceDirection`

ID: `P:TFlex.Model.Model3D.Model3DWorkplane.ReferenceDirection`

Точка, задающая направление оси X рабочей плоскости

Remarks: Если не задано начало координат рабочей плоскости, то точка, задающая направление оси X рабочей плоскости, не используется
