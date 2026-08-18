# TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.PiecewiseData`

## Summary

Упорядоченное множество сегментов - координаты точки и вес, если используется

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment)`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Add(TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment)`

Добавить сегмент в конец списка

Parameters:
- `segment`: Добавляемый сегмент

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Delete(System.UInt32)`

Удалить сегмент по номеру

Parameters:
- `index`: Номер сегмента

Remarks: Сегменты нумеруются от нуля. Если индекс отрицательный или превышает количество сегментов, то результат неопределён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.DeleteAll`

Удалить все сегменты

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.GetEnumerator`

Получить перечислитель

### `Insert(System.UInt32,TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment)`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Insert(System.UInt32,TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Segment)`

Вставить сегмент перед номером

Parameters:
- `Index`: Номер сегмента
- `segment`: Сегмент

Remarks: Сегменты нумеруются от нуля. Если индекс отрицательный или превышает количество сегментов, то результат неопределён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.Length`

Количество сегментов

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.PiecewiseData.SegmentsSet.default(System.UInt32)`

Сегмент по номеру

Parameters:
- `index`: Номер сегмента

Remarks: Сегменты нумеруются от нуля. Если индекс отрицательный или превышает количество сегментов, то результат неопределён
