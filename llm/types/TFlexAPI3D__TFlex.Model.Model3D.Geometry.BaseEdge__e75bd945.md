# TFlex.Model.Model3D.Geometry.BaseEdge

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый интерфейс для геометрических и модельных рёбер

## Methods

### `GetPolyline`

ID: `M:TFlex.Model.Model3D.Geometry.BaseEdge.GetPolyline`

Полилиния

### `GetPolyline(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseEdge.GetPolyline(System.Double,System.Double,System.Double)`

Полилиния

## Propertys

### `Curve`

ID: `P:TFlex.Model.Model3D.Geometry.BaseEdge.Curve`

Получить кривую, на которой лежит ребро

### `Faces`

ID: `P:TFlex.Model.Model3D.Geometry.BaseEdge.Faces`

Множество смежных граней

Remarks: Обычно смежных граней не больше двух

### `Interval`

ID: `P:TFlex.Model.Model3D.Geometry.BaseEdge.Interval`

Получить интервал кривой на котором лежит ребро

### `Loops`

ID: `P:TFlex.Model.Model3D.Geometry.BaseEdge.Loops`

Множество смежных циклов

Remarks: Обычно смежных циклов не больше двух

### `Sense`

ID: `P:TFlex.Model.Model3D.Geometry.BaseEdge.Sense`

Получить признак совпадения ориентации кривой и ребра

### `Vertices`

ID: `P:TFlex.Model.Model3D.Geometry.BaseEdge.Vertices`

Множество вершин, смежных ребру
