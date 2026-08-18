# TFlex.Model.Model3D.Geometry.BaseAxis

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для оси

## Constructors

### `BaseAxis(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection)`

Конструктор для геометрической оси

### `BaseAxis(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной оси

## Methods

### `BaseAxis(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection)`

Конструктор для геометрической оси

### `BaseAxis(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной оси

### `LineIntersection(TFlex.Model.Model3D.Geometry.Axis)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.LineIntersection(TFlex.Model.Model3D.Geometry.Axis)`

Получить пересечение двух прямых

Parameters:
- `line`: Геометрическая ось, с которой пересекается данная ось

Remarks: Если оси не пересекаются, то результат нулевой

### `LineNearPoints(TFlex.Model.Model3D.Geometry.Axis)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.LineNearPoints(TFlex.Model.Model3D.Geometry.Axis)`

Получить точку на прямой, ближайшую к другой прямой

Parameters:
- `line`: Ближайшая к данной прямой прямая

Remarks: Если прямые параллельны, то результат нулевой

### `PointProjection(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.PointProjection(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Получить ортогональную проекцию точки на прямую

Parameters:
- `point`: Точка

### `Update`

ID: `M:TFlex.Model.Model3D.Geometry.BaseAxis.Update`

Обновить геометрию для каждого конкретного порождённого типа

## Propertys

### `Direction`

ID: `P:TFlex.Model.Model3D.Geometry.BaseAxis.Direction`

Вектор направления оси

### `Origin`

ID: `P:TFlex.Model.Model3D.Geometry.BaseAxis.Origin`

Точка, через которую проходит ось
