# TFlex.Model.Model3D.SpatialWorkSurface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех типов специальных координатных поверхностей

## Constructors

### `SpatialWorkSurface(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SpatialWorkSurface.#ctor(TFlex.Model.Document)`

Конструктор для создания нового пути

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

Remarks: Параметрическая область рабочей поверхности создаётся на активной странице

### `SpatialWorkSurface(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.SpatialWorkSurface.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания нового пути

Parameters:
- `Doc`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся параметрическая область рабочей поверхности

## Methods

### `SpatialWorkSurface(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SpatialWorkSurface.#ctor(TFlex.Model.Document)`

Конструктор для создания нового пути

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

Remarks: Параметрическая область рабочей поверхности создаётся на активной странице

### `SpatialWorkSurface(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.SpatialWorkSurface.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания нового пути

Parameters:
- `Doc`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся параметрическая область рабочей поверхности

## Propertys

### `BoundQuadrant`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.BoundQuadrant`

Квадрант границы рабочей поверхности, если границы задаются одним узлом и границами листа

Remarks: Квадранты нумеруются от 1 до 4. По умолчанию первый угол задаётся точкой привязки

### `FirstBoundCorner`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.FirstBoundCorner`

Первый угол границы

Remarks: По умолчанию первый угол задаётся точкой привязки

### `FirstUVBoxCorner`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.FirstUVBoxCorner`

Начало координат параметрической области

### `Geometry`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.Geometry`

Получить геометрические данные специальных координатных поверхностей

### `LCS`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.LCS`

Локальная система координат, в которой задаётся рабочая поверхость

### `Orientation`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.Orientation`

Соответствие координатных осей и параметров

### `SecondBoundCorner`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.SecondBoundCorner`

Второй угол границы

### `SecondUVBoxCorner`

ID: `P:TFlex.Model.Model3D.SpatialWorkSurface.SecondUVBoxCorner`

Вторая граница области
