# TFlex.Model.Model3D.MeshPoint

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Узел на пересечении трёх плоскостей

## Remarks

Это временный объект. Узел нельзя явно создать и использовать как родителя для других объектов. Он возвращается при селекции на сетке точек пересечения рабочих плоскостей

## Methods

### `Create`

ID: `M:TFlex.Model.Model3D.MeshPoint.Create`

Создать или найти модельный узел на пересечении

### `Create(System.Collections.Generic.Dictionary`2{TFlex.Model.Model3D.Workplane,TFlex.Model.Model3D.Workplane})`

ID: `M:TFlex.Model.Model3D.MeshPoint.Create(System.Collections.Generic.Dictionary`2{TFlex.Model.Model3D.Workplane,TFlex.Model.Model3D.Workplane})`

Создать или найти модельный узел на пересечении с заменой рабочей плоскости

## Propertys

### `Coords`

ID: `P:TFlex.Model.Model3D.MeshPoint.Coords`

Получить координаты точки

### `GroupType`

ID: `P:TFlex.Model.Model3D.MeshPoint.GroupType`

Тип объекта

### `HandleForSelection`

ID: `P:TFlex.Model.Model3D.MeshPoint.HandleForSelection`

Для внутреннего использования

### `Plane1`

ID: `P:TFlex.Model.Model3D.MeshPoint.Plane1`

Первая плоскость

### `Plane2`

ID: `P:TFlex.Model.Model3D.MeshPoint.Plane2`

Вторая плоскость

### `Plane3`

ID: `P:TFlex.Model.Model3D.MeshPoint.Plane3`

Третья плоскость
