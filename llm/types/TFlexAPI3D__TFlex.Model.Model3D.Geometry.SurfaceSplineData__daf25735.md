# TFlex.Model.Model3D.Geometry.SurfaceSplineData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Класс для задания и определения свойств сплайновой поверхности по набору контрольных точек, весов и последовательности узлов параметризации

## Constructors

### `SurfaceSplineData`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.#ctor`

Конструктор

## Methods

### `SurfaceSplineData`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.#ctor`

Конструктор

### `Dispose`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

## Propertys

### `Convexity`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.Convexity`

Выпуклость поверхности

### `Points`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.Points`

Получить контрольные точки

### `Rational`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.Rational`

Признак рациональности сплайна

Remarks: При изменении типа на нерациональный информация о весах теряется. При изменении типа на рациональный все веса равны 1.0. Если тип не меняется, то информация о весах также не меняется

### `SelfIntersecting`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.SelfIntersecting`

Признак самопересечения сплайна

Remarks: Если этот признак не определён, то сплайновая поверхность считается не самопересекающейся

### `Shape`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.Shape`

Форма поверхности

### `UClosed`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.UClosed`

Признак замкнутости сплайна по U

### `UDegree`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.UDegree`

Степень сплайна по U

### `UKnotSequenceType`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.UKnotSequenceType`

Тип последовательности узлов по U

### `UKnots`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.UKnots`

Получить последовательность узлов по U

### `UPeriodic`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.UPeriodic`

Признак периодичности сплайна по U

### `VClosed`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.VClosed`

Признак замкнутости сплайна по V

### `VDegree`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.VDegree`

Степень сплайна по V

### `VKnotSequenceType`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.VKnotSequenceType`

Тип последовательности узлов по V

### `VKnots`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.VKnots`

Получить последовательность узлов по V

### `VPeriodic`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.VPeriodic`

Признак периодичности сплайна по V
