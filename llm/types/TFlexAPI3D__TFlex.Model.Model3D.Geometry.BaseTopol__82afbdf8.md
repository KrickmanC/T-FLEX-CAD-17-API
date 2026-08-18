# TFlex.Model.Model3D.Geometry.BaseTopol

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для всех типов (модельных и геометрических) граней, циклов, рёбер и вершин

## Remarks

Для двух элементов поддерживается функция сравнения

## Methods

### `FindBoundBox`

ID: `M:TFlex.Model.Model3D.Geometry.BaseTopol.FindBoundBox`

Получить границы элемента

### `FindExtreme(TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseTopol.FindExtreme(TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

Найти экстремальную точку на элементе в заданном направлении

Parameters:
- `direction1`: Направление 1
- `direction2`: Направление 2
- `direction3`: Направление 3

Remarks: Экстремальная точка на элементе ищется в направлении 1. Если решение неоднозначное, то количество экстремальных точек последовательно редуцируется по направлениям 2 и 3

### `RangePoint(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseTopol.RangePoint(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Найти ближайшую точку на элементе к данной точке

Parameters:
- `point`: Точка

### `RangeTopol(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseTopol.RangeTopol(TFlex.Model.Model3D.Geometry.BaseTopol)`

Найти ближайшие расстояние между двумя топологическими элементами

Parameters:
- `rhs`: Топологический элемент

## Propertys

### `BaseBody`

ID: `P:TFlex.Model.Model3D.Geometry.BaseTopol.BaseBody`

Получить тело, в котором определён элемент

### `Identify`

ID: `P:TFlex.Model.Model3D.Geometry.BaseTopol.Identify`

Уникальный идентификатор элемента
