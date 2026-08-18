# TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet`

## Summary

Упорядоченное множество контрольных точек в сегменте - координаты точки и вес, если используется

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Constructors

### `Segment(System.UInt32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.#ctor(System.UInt32,System.Boolean)`

Конструктор для сегмента с указанием степени сплайна, его рациональности

Parameters:
- `degree`: Степень сплайна
- `rational`: Рациональность сплайна

## Methods

### `Segment(System.UInt32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.#ctor(System.UInt32,System.Boolean)`

Конструктор для сегмента с указанием степени сплайна, его рациональности

Parameters:
- `degree`: Степень сплайна
- `rational`: Рациональность сплайна

### `Clone`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.Clone`

Метод создает неполную копию объекта

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.Length`

Количество контрольных точек (на единицу больше степени сплайна)

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment.default(System.UInt32)`

Контрольная точка по номеру

Parameters:
- `index`: Номер контрольной точки

Remarks: Контрольные точки нумеруются от нуля. Если индекс отрицательный или превышает количество контрольных точек, то результат не определён
