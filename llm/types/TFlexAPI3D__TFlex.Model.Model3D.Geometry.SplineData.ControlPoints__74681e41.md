# TFlex.Model.Model3D.Geometry.SplineData.ControlPoints

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SplineData`

## Summary

Класс представляет упорядоченное множество контрольных точек - координат точки и вес, если используется

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.ControlPoint)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.Add(TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.ControlPoint)`

Добавить контрольную точку в конец списка

Parameters:
- `point`: Контрольная точка

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.Delete(System.UInt32)`

Удалить контрольную точку по номеру

Parameters:
- `index`: Номер контрольной точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.DeleteAll`

Удалить все контрольные точки

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.GetEnumerator`

Получить перечислитель

### `Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.ControlPoint)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.ControlPoint)`

Вставить контрольную точку перед номером

Parameters:
- `Index`: Номер контрольной точки
- `point`: Контрольная точка

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.Length`

Количество контрольных точек

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.ControlPoints.default(System.UInt32)`

Контрольная точка по номеру

Parameters:
- `index`: Номер контрольной точки

Remarks: Контрольные точки нумеруются от нуля. Если индекс отрицательный или превышает количество контрольных точек, то результат не определён
