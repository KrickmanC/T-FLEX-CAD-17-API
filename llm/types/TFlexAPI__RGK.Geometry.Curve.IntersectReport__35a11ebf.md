# RGK.Geometry.Curve.IntersectReport

Assembly: `TFlexAPI`
Namespace: `RGK.Geometry.Curve`

## Summary

Результат поиска пересечений

## Constructors

### `IntersectReport`

ID: `M:RGK.Geometry.Curve.IntersectReport.#ctor`

## Methods

### `IntersectReport`

ID: `M:RGK.Geometry.Curve.IntersectReport.#ctor`

### `Dispose`

ID: `M:RGK.Geometry.Curve.IntersectReport.Dispose`

### `GetIntersectionCount`

ID: `M:RGK.Geometry.Curve.IntersectReport.GetIntersectionCount`

Returns: Количество пересечений

### `GetIntersectionPoint(System.UInt32)`

ID: `M:RGK.Geometry.Curve.IntersectReport.GetIntersectionPoint(System.UInt32)`

Parameters:
- `iIndex`: Номер точки пересечения

Returns: Точка пересечения

### `GetParametersOnCurve1(System.UInt32)`

ID: `M:RGK.Geometry.Curve.IntersectReport.GetParametersOnCurve1(System.UInt32)`

Parameters:
- `iIndex`: Номер точки пересечения

Returns: Параметр в точке пересечения для первой кривой

### `GetParametersOnCurve2(System.UInt32)`

ID: `M:RGK.Geometry.Curve.IntersectReport.GetParametersOnCurve2(System.UInt32)`

Parameters:
- `iIndex`: Номер точки пересечения

Returns: Параметр в точке пересечения для второй кривой

### `GetSolutionTolerance`

ID: `M:RGK.Geometry.Curve.IntersectReport.GetSolutionTolerance`

Returns: Точность пересечения

### `GetTypeOfIntersection(System.UInt32)`

ID: `M:RGK.Geometry.Curve.IntersectReport.GetTypeOfIntersection(System.UInt32)`

Parameters:
- `iIndex`: Номер точки пересечения

Returns: Тип точки пересечения
