# TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.SegmentRow

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment`

## Summary

Упорядоченное по V множество точек в строке - координаты точки и вес, если используется

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Methods

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.SegmentRow.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.SegmentRow.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.SegmentRow.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.SegmentRow.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.SegmentRow.Length`

Количество контрольных точек

Remarks: Значение на единицу больше степени по U

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.SegmentRow.default(System.UInt32)`

Контрольная точку по номеру

Parameters:
- `index`: Номер контрольной точки

Remarks: Контрольные точки нумеруются от нуля. Если индекс отрицательный или превышает количество контрольных точек, то результат не определён
