# RGPlatform.Geometry.Spline2D.CharPointsReport

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry.Spline2D`

## Summary

Отчёт по результатам поиска характеристических точек на двумерной сплайн-кривой

## Constructors

### `CharPointsReport`

ID: `M:RGPlatform.Geometry.Spline2D.CharPointsReport.#ctor`

Конструктор

## Methods

### `CharPointsReport`

ID: `M:RGPlatform.Geometry.Spline2D.CharPointsReport.#ctor`

Конструктор

### `DetectG1DiscontinuityPoint(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Spline2D.CharPointsReport.DetectG1DiscontinuityPoint(System.Double,System.Double)`

Определение наличия точки разрыва непрерывности по G1

Parameters:
- `iParam`: Параметр точки на кривой, для которой проводится анализ
- `iTolerance`: Точность вычислений

Returns: true - в случае успеха, false - иначе

### `Dispose`

ID: `M:RGPlatform.Geometry.Spline2D.CharPointsReport.Dispose`

Деструктор

### `GetCharPoint(System.UInt64)`

ID: `M:RGPlatform.Geometry.Spline2D.CharPointsReport.GetCharPoint(System.UInt64)`

Получить характеристическую точку

Parameters:
- `iIndex`: Индекс характеристической точки

Returns: Характеристическая точка

### `GetCharPointsCount`

ID: `M:RGPlatform.Geometry.Spline2D.CharPointsReport.GetCharPointsCount`

Получить количество характеристических точек

Returns: Количество характеристических точек

### `GetCharPointsCount(RGK.Geometry.NURBSCurve.CharPointsReport.CharPoint.CharPointType)`

ID: `M:RGPlatform.Geometry.Spline2D.CharPointsReport.GetCharPointsCount(RGK.Geometry.NURBSCurve.CharPointsReport.CharPoint.CharPointType)`

Получить количество характеристических точек указанного типа

Parameters:
- `iType`: Тип характеристической точки

Returns: Количество характеристических точек
