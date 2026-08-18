# RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry.Curve2DGeometry`

## Summary

Объект результата преобразования кривой в набор RGK-кривых

## Methods

### `AddPair(RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.RGKCurvePair!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.AddPair(RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.RGKCurvePair!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Добавить пару {кривая, интервал}

Parameters:
- `iPair`: Добавляемая пара

### `GetAt(System.UInt64,RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.RGKCurvePair*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.GetAt(System.UInt64,RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.RGKCurvePair*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить пару {кривая, интервал} по индексу

Parameters:
- `iIndex`: Индекс пары
- `oPair`: Пара

Returns: true - если пара с указанным индексом существует, false - иначе

### `GetCount`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.GetCount`

Получить число пар

Returns: Число пар

### `op_Subscript(System.UInt64)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult.op_Subscript(System.UInt64)`

Получить пару {кривая, интервал} по индексу

Returns: Пара {кривая, интервал}
