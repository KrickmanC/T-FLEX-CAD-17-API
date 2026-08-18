# TFlex.Model.Model3D.Geometry.SplineData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Класс для задания и определения свойств сплайна по набору контрольных точек, весов и последовательности узлов параметризации

## Constructors

### `SplineData`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.#ctor`

Конструктор

## Methods

### `SplineData`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.#ctor`

Конструктор

### `Dispose`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

## Propertys

### `Closed`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.Closed`

Признак замкнутости сплайна

### `Degree`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.Degree`

Степень сплайна

### `KnotSequenceType`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.KnotSequenceType`

Тип последовательности узлов

### `Knots`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.Knots`

Получить последовательность узлов

### `Periodic`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.Periodic`

Признак периодичности сплайна

### `Points`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.Points`

Получить контрольные точки

### `Rational`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.Rational`

Установить признак рациональности сплайна

Remarks: При изменении типа на нерациональный информация о весах теряется. При изменении типа на рациональный все веса равны 1.0. Если тип не меняется, то информация о весах также не меняется

### `SelfIntersecting`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.SelfIntersecting`

Признак наличия самопересечения

Remarks: Если этот признак не определён, то сплайн считается не самопересекающимся

### `Shape`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.Shape`

Форма кривой
