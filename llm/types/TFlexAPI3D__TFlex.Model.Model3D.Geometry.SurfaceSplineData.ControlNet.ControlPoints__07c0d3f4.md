# TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ControlPoints

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet`

## Summary

Упорядоченное множество контрольных точек по V для изопараметрической кривой по U - координаты точки и вес, если используется

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Methods

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ControlPoints.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ControlPoints.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ControlPoints.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ControlPoints.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ControlPoints.Length`

Количество контрольных точек

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ControlPoints.default(System.UInt32)`

Контрольная точку по номеру

Parameters:
- `index`: Номер контрольной точки

Remarks: Контрольные точки нумеруются от нуля. Если индекс отрицательный или превышает количество контрольных точек, то результат не определён
