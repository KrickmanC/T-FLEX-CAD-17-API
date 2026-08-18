# TFlex.Model.Model3D.MeshWorkPlane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Сетка из точек пересечения рабочих плоскостей

## Constructors

### `MeshWorkPlane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `MeshWorkPlane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `Build`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.Build`

Обновление сетки

### `FindBoundBox`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.FindBoundBox`

Границы множества точек пересечений рабочих плоскостей

### `FindByCoords(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.FindByCoords(TFlex.Model.Model3D.Geometry.Point3D)`

Найти точку по её координатам

Parameters:
- `point`: Точка

### `FindFar(TFlex.Model.Model3D.Geometry.Axis)`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.FindFar(TFlex.Model.Model3D.Geometry.Axis)`

Найти удалённую точку по направлению

### `FindMinMax(TFlex.Model.Model3D.Geometry.Axis,System.Boolean)`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.FindMinMax(TFlex.Model.Model3D.Geometry.Axis,System.Boolean)`

Найти минимальную или максимальную точку на луче

Parameters:
- `axis`: Геометрическая ось
- `max`: true, если ищется максимальная точка, в противном случае false

### `FindNear(TFlex.Model.Model3D.Geometry.Axis)`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.FindNear(TFlex.Model.Model3D.Geometry.Axis)`

Найти ближайшую точку по направлению

### `FindNearByLength(TFlex.Model.Model3D.Geometry.Axis,System.Double,System.Boolean)`

ID: `M:TFlex.Model.Model3D.MeshWorkPlane.FindNearByLength(TFlex.Model.Model3D.Geometry.Axis,System.Double,System.Boolean)`

Найти ближайшую точку с учётом длины вектора, задающего направление, включая точку на луче

## Propertys

### `ActiveWorkplane`

ID: `P:TFlex.Model.Model3D.MeshWorkPlane.ActiveWorkplane`

Активная рабочая плоскость

### `Enable`

ID: `P:TFlex.Model.Model3D.MeshWorkPlane.Enable`

Включение сетки рабочих плоскостей

### `FindNearPoint`

ID: `P:TFlex.Model.Model3D.MeshWorkPlane.FindNearPoint`

Режим выбора ближайших к лучу точек

### `Inverse`

ID: `P:TFlex.Model.Model3D.MeshWorkPlane.Inverse`

Инверсия порядка возвращаемых узлов сетки, от дальних к ближним
