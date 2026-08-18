# RGPlatform.Geometry.Curve2DSelfIntersectionData

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry`

## Summary

Данные для поиска точек самопересечения двумерной кривой

## Constructors

### `Curve2DSelfIntersectionData(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGPlatform.Geometry.Curve2DSelfIntersectionData.#ctor(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор

Parameters:
- `iCurve`: Кривая
- `iInterval`: Параметрический интервал кривой, на котором выполняется поиск точек самопересечения
- `iTolerance`: Точность поиска точек самопересечения

## Methods

### `Curve2DSelfIntersectionData(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGPlatform.Geometry.Curve2DSelfIntersectionData.#ctor(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор

Parameters:
- `iCurve`: Кривая
- `iInterval`: Параметрический интервал кривой, на котором выполняется поиск точек самопересечения
- `iTolerance`: Точность поиска точек самопересечения

### `Check(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Curve2DSelfIntersectionData.Check(RGPlatform.Geometry.Context*)`

Проверить корректность данных

Parameters:
- `iContext`: Контекст геометрии

Returns: RGK::Common::Success - если данные корректны, код ошибки - иначе

### `Dispose`

ID: `M:RGPlatform.Geometry.Curve2DSelfIntersectionData.Dispose`

Деструктор

### `GetCurve`

ID: `M:RGPlatform.Geometry.Curve2DSelfIntersectionData.GetCurve`

Получить кривую

Returns: Кривая

### `GetInterval`

ID: `M:RGPlatform.Geometry.Curve2DSelfIntersectionData.GetInterval`

Получить параметрический интервал кривой, на котором выполняется поиск точек самопересечения

Returns: Параметрический интервал кривой, на котором выполняется поиск точек самопересечения

### `GetTolerance`

ID: `M:RGPlatform.Geometry.Curve2DSelfIntersectionData.GetTolerance`

Получить точность поиска точек самопересечения

Returns: Точность поиска точек самопересечения
