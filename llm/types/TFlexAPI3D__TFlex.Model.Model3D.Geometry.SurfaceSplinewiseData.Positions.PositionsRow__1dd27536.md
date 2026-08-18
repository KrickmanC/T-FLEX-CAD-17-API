# TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.PositionsRow

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions`

## Summary

Упорядоченное множество интерполяционных точек по V для изопараметрической кривой по U : координаты точки и параметр по V, если используется

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Methods

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.PositionsRow.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.PositionsRow.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.PositionsRow.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.PositionsRow.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.PositionsRow.Length`

Количество интерполяционных точек

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.PositionsRow.default(System.UInt32)`

Интерполяционная точку по номеру

Parameters:
- `index`: Номер интерполяционную точки

Remarks: Интерполяционные точки нумеруются от нуля. Если индекс отрицательный или превышает количество интерполяционных точек, то результат не определён
