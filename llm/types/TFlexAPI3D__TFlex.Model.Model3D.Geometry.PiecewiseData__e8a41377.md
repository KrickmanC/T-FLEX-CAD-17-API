# TFlex.Model.Model3D.Geometry.PiecewiseData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Класс для задания и определения свойств сплайна по набору сегментов

## Constructors

### `PiecewiseData`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.#ctor`

Конструктор

## Methods

### `PiecewiseData`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.#ctor`

Конструктор

### `Dispose`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

## Propertys

### `Degree`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.Degree`

Степень сплайна

Remarks: При уменьшении степени информация о лишних точках теряется. При увеличении степени координаты добавленных точек нулевые. Если степень не меняется, то информация о точках также не меняется

### `Rational`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.Rational`

Признак рациональности сплайна

Remarks: При изменении типа на нерациональный информация о весах теряется. При изменении типа на рациональный все веса равны 1.0. Если тип не меняется, то информация о весах также не меняется

### `Representation`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.Representation`

Представление сплайна

### `Segments`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.Segments`

Получить сегменты
