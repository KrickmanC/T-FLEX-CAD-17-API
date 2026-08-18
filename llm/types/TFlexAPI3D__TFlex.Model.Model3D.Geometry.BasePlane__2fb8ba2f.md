# TFlex.Model.Model3D.Geometry.BasePlane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для плоскостей

## Constructors

### `BasePlane(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

Конструктор для геометрической плоскости

### `BasePlane(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной плоскости

## Methods

### `BasePlane(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

Конструктор для геометрической плоскости

### `BasePlane(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной плоскости

### `Equal(TFlex.Model.Model3D.Geometry.BasePlane)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.Equal(TFlex.Model.Model3D.Geometry.BasePlane)`

Проверка совпадения плоскостей

Parameters:
- `other`: Плоскость, с которой ищется пересечение данной плоскости

### `LineIntersection(TFlex.Model.Model3D.Geometry.Axis)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.LineIntersection(TFlex.Model.Model3D.Geometry.Axis)`

Получить пересечение плоскости с прямой

Parameters:
- `line`: Прямая, с которой ищется пересечение

Remarks: Если прямая не пересекает плоскость, то результат нулевой

### `PlaneIntersection(TFlex.Model.Model3D.Geometry.BasePlane)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.PlaneIntersection(TFlex.Model.Model3D.Geometry.BasePlane)`

Получить пересечение двух плоскостей

Parameters:
- `plane`: Плоскость, с которой ищется пересечение

Remarks: Если плоскости параллельны, то результат нулевой

### `PointProjection(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BasePlane.PointProjection(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Получить ортогональную проекцию точки на плоскость

Parameters:
- `point`: Точка, проецируемая на плоскость

## Propertys

### `Normal`

ID: `P:TFlex.Model.Model3D.Geometry.BasePlane.Normal`

Получить нормаль к плоскости

### `Origin`

ID: `P:TFlex.Model.Model3D.Geometry.BasePlane.Origin`

Получить нулевую точку плоскости

### `XAxis`

ID: `P:TFlex.Model.Model3D.Geometry.BasePlane.XAxis`

Получить направление оси X к плоскости
