# RGPlatform.Geometry.Curve2DIntersectionData

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry`

## Summary

Данные для пересечения двумерных кривых

## Constructors

### `Curve2DIntersectionData(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.#ctor(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор

Parameters:
- `iCurve1`: Первая пересекаемая кривая
- `iInterval`: Параметрический интервал первой кривой, на котором выполняется поиск пересечений
- `iCurve2`: Вторая пересекаемая кривая
- `iInterva2`: Параметрический интервал второй кривой, на котором выполняется поиск пересечений
- `iTolerance`: Точность вычисления пересечения

## Methods

### `Curve2DIntersectionData(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.#ctor(RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор

Parameters:
- `iCurve1`: Первая пересекаемая кривая
- `iInterval`: Параметрический интервал первой кривой, на котором выполняется поиск пересечений
- `iCurve2`: Вторая пересекаемая кривая
- `iInterva2`: Параметрический интервал второй кривой, на котором выполняется поиск пересечений
- `iTolerance`: Точность вычисления пересечения

### `Check(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.Check(RGPlatform.Geometry.Context*)`

Проверить корректность данных

Parameters:
- `iContext`: Контекст геометрии

Returns: RGK::Common::Success - если данные корректны, код ошибки - иначе

### `Dispose`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.Dispose`

Деструктор

### `GetCurve1`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.GetCurve1`

Получить первую пересекаемую кривую

Returns: Первая пересекаемая кривая

### `GetCurve2`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.GetCurve2`

Получить первую пересекаемую кривую

Returns: Первая пересекаемая кривая

### `GetInterval1`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.GetInterval1`

Получить параметрический интервал первой кривой

Returns: Параметрический интервал первой кривой

### `GetInterval2`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.GetInterval2`

Получить параметрический интервал второй кривой

Returns: Параметрический интервал второй кривой

### `GetSelectingPoint`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.GetSelectingPoint`

Получить точку, по которой будет выбран ответ

Returns: Точка, по которой будет выбран ответ

### `GetTolerance`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.GetTolerance`

Получить точность вычисления пересечения

Returns: Точность вычисления пересечения

### `SetSelectingPoint(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DIntersectionData.SetSelectingPoint(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Задать точку, по которой будет выбран ответ

Parameters:
- `iPoint`: Точка, по которой будет выбран ответ
