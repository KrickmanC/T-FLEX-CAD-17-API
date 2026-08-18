# TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet`

## Summary

Упорядоченное по V множество сегментов в строке

## Remarks

Возможно перечисление сегментов с использованием конструкции foreach

## Methods

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.Length`

Количество сегментов

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SegmentsRow.default(System.UInt32)`

Получить сегмент по номеру

Parameters:
- `index`: Номер сегмента

Remarks: Сегменты нумеруются от нуля. Если индекс отрицательный или превышает количество сегментов, то результат не определён
