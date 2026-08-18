# PreciseGeometryUtils.InterPointData

Assembly: `TFlexAPI`
Namespace: `PreciseGeometryUtils`

## Constructors

### `InterPointData`

ID: `M:PreciseGeometryUtils.InterPointData.#ctor`

### `InterPointData(RGPlatform.Geometry.Curve2DIntersectionPointData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:PreciseGeometryUtils.InterPointData.#ctor(RGPlatform.Geometry.Curve2DIntersectionPointData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор по данным RGP

### `InterPointData(System.Double,System.Double,System.Int32,System.Int32,<unknown type>)`

ID: `M:PreciseGeometryUtils.InterPointData.#ctor(System.Double,System.Double,System.Int32,System.Int32,<unknown type>)`

Конструктор общего вида

Parameters:
- `iX`: X-координата точки пересечения
- `iY`: Y-координата точки пересечения
- `iNDraw1`: Индекс первой пересекаемой кривой
- `iNDraw2`: Индекс второй пересекаемой кривой
- `iType`: Тип точки пересечения

## Methods

### `InterPointData`

ID: `M:PreciseGeometryUtils.InterPointData.#ctor`

### `InterPointData(RGPlatform.Geometry.Curve2DIntersectionPointData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:PreciseGeometryUtils.InterPointData.#ctor(RGPlatform.Geometry.Curve2DIntersectionPointData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор по данным RGP

### `InterPointData(System.Double,System.Double,System.Int32,System.Int32,<unknown type>)`

ID: `M:PreciseGeometryUtils.InterPointData.#ctor(System.Double,System.Double,System.Int32,System.Int32,<unknown type>)`

Конструктор общего вида

Parameters:
- `iX`: X-координата точки пересечения
- `iY`: Y-координата точки пересечения
- `iNDraw1`: Индекс первой пересекаемой кривой
- `iNDraw2`: Индекс второй пересекаемой кривой
- `iType`: Тип точки пересечения

### `GetParameter1`

ID: `M:PreciseGeometryUtils.InterPointData.GetParameter1`

Получить параметер на кривой соответствующий точке пересечения

Returns: Параметер пересесения

### `GetPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:PreciseGeometryUtils.InterPointData.GetPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Создать точку пересечения

Parameters:
- `oPoint`: Точка пересесения
- `iToModelSpaceScale`: Коэффициент преобразования в координаты модели

### `GetPoint(System.Double)`

ID: `M:PreciseGeometryUtils.InterPointData.GetPoint(System.Double)`

Создать точку пересечения

Parameters:
- `iToModelSpaceScale`: Коэффициент преобразования в координаты модели

Returns: Точка пересесения

### `GetTFPoint(System.Double)`

ID: `M:PreciseGeometryUtils.InterPointData.GetTFPoint(System.Double)`

Создать точку пересечения типа TFPoint

Parameters:
- `iToModelSpaceScale`: Коэффициент преобразования в координаты модели

Returns: Точка пересесения

### `IsTouchPoint`

ID: `M:PreciseGeometryUtils.InterPointData.IsTouchPoint`

Является ли точка касательной

Returns: true - если точка пересечения - касательная точка

## Fields

### `_nDraw1`

ID: `F:PreciseGeometryUtils.InterPointData._nDraw1`

### `_nDraw2`

ID: `F:PreciseGeometryUtils.InterPointData._nDraw2`

### `_parameter1`

ID: `F:PreciseGeometryUtils.InterPointData._parameter1`

### `_type`

ID: `F:PreciseGeometryUtils.InterPointData._type`

### `_x`

ID: `F:PreciseGeometryUtils.InterPointData._x`

### `_y`

ID: `F:PreciseGeometryUtils.InterPointData._y`
