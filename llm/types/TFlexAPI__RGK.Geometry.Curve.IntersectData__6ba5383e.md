# RGK.Geometry.Curve.IntersectData

Assembly: `TFlexAPI`
Namespace: `RGK.Geometry.Curve`

## Constructors

### `IntersectData(std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Geometry.Curve.IntersectData.#ctor(std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iCurve1`: Первая пересекаемая кривая
- `iInterval`: Параметрический интервал первой кривой, на котором выполняется поиск пересечений
- `iCurve2`: Вторая пересекаемая кривая
- `iInterva2`: Параметрический интервал второй кривой, на котором выполняется поиск пересечений
- `iTolerance`: Точность вычисления пересечения

## Methods

### `IntersectData(std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Geometry.Curve.IntersectData.#ctor(std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iCurve1`: Первая пересекаемая кривая
- `iInterval`: Параметрический интервал первой кривой, на котором выполняется поиск пересечений
- `iCurve2`: Вторая пересекаемая кривая
- `iInterva2`: Параметрический интервал второй кривой, на котором выполняется поиск пересечений
- `iTolerance`: Точность вычисления пересечения

### `Dispose`

ID: `M:RGK.Geometry.Curve.IntersectData.Dispose`

### `SetBox(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.IntersectData.SetBox(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iBox`: Ограничения на область поиска пересечений

### `SetSurface(std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.IntersectData.SetSurface(std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iSurface`: Поверхность, на которой лежат обе кривые
