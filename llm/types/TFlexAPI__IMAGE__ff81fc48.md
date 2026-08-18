# IMAGE

Assembly: `TFlexAPI`

## Methods

### `EvaluatePoint(RGPlatform.Geometry.Context*,System.Double,TFPoint*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:IMAGE.EvaluatePoint(RGPlatform.Geometry.Context*,System.Double,TFPoint*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение кривой по параметру

Parameters:
- `iContext`: Контекст геометрии
- `iParameter`: Параметр на кривой, в котором вычисляется значение
- `oPointInPageCs`: Вычисленное значение с учётом масштаба страницы

Returns: true - в случае успеха, false - иначе

### `FindNearestPoint(RGPlatform.Geometry.Context*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:IMAGE.FindNearestPoint(RGPlatform.Geometry.Context*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Получить параметр точки на кривой, ближайшей к передаваемой точке

Parameters:
- `iContext`: Контекст геометрии
- `iPointInPageCs`: Точка с учётом масштаба страницы, для которой ищется ближайшая точка на кривой
- `oParameter`: Найденный параметр ближайшей точки на кривой
- `iTolerance`: Точность, с которой ищется ближайшая точка

Returns: true - в случае успеха, false - иначе

### `GetDistance(RGPlatform.Geometry.Context*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:IMAGE.GetDistance(RGPlatform.Geometry.Context*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить расстояние от точки до кривой

Parameters:
- `iContext`: Контекст геометрии
- `iPointInPageCs`: Точка с учётом масштаба страницы, от которой ищется расстояние
- `oDistance`: Найденное расстояние

Returns: true - в случае успеха, false - иначе

### `IsFixedForConstraint`

ID: `M:IMAGE.IsFixedForConstraint`

### `Parameterise(RGPlatform.Geometry.Context*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

ID: `M:IMAGE.Parameterise(RGPlatform.Geometry.Context*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

Определить параметр точки, лежащей на кривой

Parameters:
- `iContext`: Контекст геометрии
- `iPointInPageCs`: Точка на кривой с учётом масштаба страницы
- `ioParameter`: Найденный параметр на кривой (на входе может содержать начальное приближение)
- `iUseGuess`: Использовать ли начальное приближение

Returns: true - в случае успеха, false - иначе

### `SetConstraintPoint(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:IMAGE.SetConstraintPoint(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`
