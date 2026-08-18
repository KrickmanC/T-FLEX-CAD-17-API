# TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow`

## Summary

Сетка контрольных точек в сегменте. Упорядоченное по U множество строк точек

## Remarks

Возможно перечисление строк с использованием конструкции foreach

## Methods

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.Length`

Количество строк

Remarks: Значение на единицу больше степени по V

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Segment.default(System.UInt32)`

Получить строку по номеру

Parameters:
- `index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён
