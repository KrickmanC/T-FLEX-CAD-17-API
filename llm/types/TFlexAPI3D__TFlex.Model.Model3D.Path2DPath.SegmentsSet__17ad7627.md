# TFlex.Model.Model3D.Path2DPath.SegmentsSet

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Path2DPath`

## Summary

Упорядоченное множество сегментов 3D пути: 2D путь и рабочая поверхность

## Remarks

Возможно перечисление сегментов с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Path2DPath.SegmentsSet.Segment)`

ID: `M:TFlex.Model.Model3D.Path2DPath.SegmentsSet.Add(TFlex.Model.Model3D.Path2DPath.SegmentsSet.Segment)`

Добавить сегмент в конец списка

Parameters:
- `segment`: Добавляемый сегмент

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.Path2DPath.SegmentsSet.Delete(System.Int32)`

Удалить сегмент по номеру

Parameters:
- `Index`: Номер сегмента

Remarks: Сегменты нумеруются от нуля. Если индекс отрицательный или превышает количество сегментов, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Path2DPath.SegmentsSet.DeleteAll`

Удалить все сегменты

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Path2DPath.SegmentsSet.GetEnumerator`

Получить перечислитель

### `Insert(System.Int32,TFlex.Model.Model3D.Path2DPath.SegmentsSet.Segment)`

ID: `M:TFlex.Model.Model3D.Path2DPath.SegmentsSet.Insert(System.Int32,TFlex.Model.Model3D.Path2DPath.SegmentsSet.Segment)`

Вставить сегмент перед номером

Parameters:
- `Index`: Номер сегмента
- `segment`: Вставляемый сегмент

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Path2DPath.SegmentsSet.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Path2DPath.SegmentsSet.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Path2DPath.SegmentsSet.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Path2DPath.SegmentsSet.Length`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.Path2DPath.SegmentsSet.default(System.Int32)`

Сегмент по номеру

Parameters:
- `index`: Номер сегмента

Remarks: Сегменты нумеруются от нуля. Если индекс отрицательный или превышает количество сегментов, то результат не определён
