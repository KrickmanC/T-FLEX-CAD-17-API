# RGK.Geometry.Interval

Assembly: `TFlexAPI`
Namespace: `RGK.Geometry`

## Constructors

### `Interval`

ID: `M:RGK.Geometry.Interval.#ctor`

### `Interval(System.Double,System.Double)`

ID: `M:RGK.Geometry.Interval.#ctor(System.Double,System.Double)`

Parameters:
- `iStart`: Начало интервала
- `iEnd`: Конец интервала

### `Interval(System.Double,System.Double,RGK.Geometry.Interval.Type)`

ID: `M:RGK.Geometry.Interval.#ctor(System.Double,System.Double,RGK.Geometry.Interval.Type)`

Parameters:
- `iStart`: Начало интервала
- `iEnd`: Конец интервала
- `iType`: Тип интервала

## Methods

### `Interval`

ID: `M:RGK.Geometry.Interval.#ctor`

### `Interval(System.Double,System.Double)`

ID: `M:RGK.Geometry.Interval.#ctor(System.Double,System.Double)`

Parameters:
- `iStart`: Начало интервала
- `iEnd`: Конец интервала

### `Interval(System.Double,System.Double,RGK.Geometry.Interval.Type)`

ID: `M:RGK.Geometry.Interval.#ctor(System.Double,System.Double,RGK.Geometry.Interval.Type)`

Parameters:
- `iStart`: Начало интервала
- `iEnd`: Конец интервала
- `iType`: Тип интервала

### `ContainParam(System.Double,System.Double)`

ID: `M:RGK.Geometry.Interval.ContainParam(System.Double,System.Double)`

Parameters:
- `iParam`: Параметр, для которого проверяется вложенность
- `iTolerance`: Точность, с которой сравнивается совпадение границ

Returns: >Common::Success - передаваемый параметр лежит внутри данного интервала

### `ContainParamOn0Period(System.Double,System.Double)`

ID: `M:RGK.Geometry.Interval.ContainParamOn0Period(System.Double,System.Double)`

Parameters:
- `iParam`: Параметр, для которого проверяется вложенность
- `iTolerance`: Точность, с которой сравнивается совпадение границ

Returns: Common::Success - в случае если параметр лежит в интервала

### `ConvertParamFromInterval1ToInterval2(System.Double,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Interval.ConvertParamFromInterval1ToInterval2(System.Double,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iParam`: Параметр на интервале 1
- `interval1`: Интервал 1
- `interval2`: Интервал 2

Returns: параметр на втором интервале

### `DrawParameterInInterval(System.Double)`

ID: `M:RGK.Geometry.Interval.DrawParameterInInterval(System.Double)`

Parameters:
- `iParameter`: Параметр

Returns: Новое значение параметра

### `EndPoints`

ID: `M:RGK.Geometry.Interval.EndPoints`

Returns: Конечные точки интервала в виде массива

### `FindPeriod(System.Double)`

ID: `M:RGK.Geometry.Interval.FindPeriod(System.Double)`

Parameters:
- `iParam`: Заданный параметр

Returns: Значение периода, если интервал периодичный, ноль в противном случае

### `GetCenter`

ID: `M:RGK.Geometry.Interval.GetCenter`

### `GetEnd`

ID: `M:RGK.Geometry.Interval.GetEnd`

Returns: Конец интервала

### `GetLength`

ID: `M:RGK.Geometry.Interval.GetLength`

Returns: Длина интервала

### `GetLinearPrecision(RGK.Common.Context*)`

ID: `M:RGK.Geometry.Interval.GetLinearPrecision(RGK.Common.Context*)`

Parameters:
- `iContext`: Контекст вычисления, из которого берётся относительная точность

Returns: Точность

### `GetParameter(System.Double)`

ID: `M:RGK.Geometry.Interval.GetParameter(System.Double)`

Parameters:
- `iInterval`: Относительная длина интервала

Returns: Параметр

### `GetStart`

ID: `M:RGK.Geometry.Interval.GetStart`

Returns: Начало интервала

### `GetType`

ID: `M:RGK.Geometry.Interval.GetType`

Returns: Тип интервала

### `Intersect(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Interval.Intersect(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iInterval`: Интервал, с которым выполняется пересечение
- `iTolerance`: Точность, с которой сравнивается совпадение границ
- `oIntersection`: Пересечение интервалов

Returns: true - интервалы пересекаются false - интервалы не пересекаются

### `IsEqualInterval(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Geometry.Interval.IsEqualInterval(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iInterval`: Интервал
- `iTolerance`: Точность, с которой сравнивается совпадение границ

Returns: true - интервал oInterval совпадает с интервалом

### `IsEqualIntervalWithoutType(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Geometry.Interval.IsEqualIntervalWithoutType(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iInterval`: Интервал
- `iTolerance`: Точность, с которой сравнивается совпадение границ

Returns: true - интервал oInterval совпадает с интервалом

### `IsNestedInterval(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Geometry.Interval.IsNestedInterval(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iInterval`: Интервал, для которого проверяется вложенность
- `iTolerance`: Точность, с которой сравнивается совпадение границ

Returns: true - интервал oInterval совпадает с интервалом или вложен в него

### `ParametersOnOnePeriod(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Interval.ParametersOnOnePeriod(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iParam1`: Параметр
- `iParam2`: Параметр

### `Revert`

ID: `M:RGK.Geometry.Interval.Revert`

Returns: Интервал, у которого начало и конец наоборот по отношению к исходному

### `Set(System.Double,System.Double,RGK.Geometry.Interval.Type)`

ID: `M:RGK.Geometry.Interval.Set(System.Double,System.Double,RGK.Geometry.Interval.Type)`

Parameters:
- `iStart`: Начало интервала
- `iEnd`: Конец интервала
- `iType`: Тип интервала

### `SetEnd(System.Double)`

ID: `M:RGK.Geometry.Interval.SetEnd(System.Double)`

Parameters:
- `iEnd`: Конец интервала

### `SetStart(System.Double)`

ID: `M:RGK.Geometry.Interval.SetStart(System.Double)`

Parameters:
- `iStart`: Начало интервала

### `SetType(RGK.Geometry.Interval.Type)`

ID: `M:RGK.Geometry.Interval.SetType(RGK.Geometry.Interval.Type)`

Parameters:
- `iType`: Тип интервала

### `Trace(std.basic_ostream<System.Char,std.char_traits{System.Char}>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Interval.Trace(std.basic_ostream<System.Char,std.char_traits{System.Char}>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `Unite(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Interval.Unite(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iInterval`: Интервал, с которым выполняется объединение
- `iPeriod`: Период
- `iTolerance`: Точность, с которой сравнивается совпадение границ
- `oIntersection`: Объединение интервалов

Returns: true - интервалы пересекаются false - интервалы не пересекаются

### `_DrawParameterInInterval(System.Double)`

ID: `M:RGK.Geometry.Interval._DrawParameterInInterval(System.Double)`

### `op_AdditionAssignment(System.Double)`

ID: `M:RGK.Geometry.Interval.op_AdditionAssignment(System.Double)`

### `op_MultiplicationAssignment(System.Double)`

ID: `M:RGK.Geometry.Interval.op_MultiplicationAssignment(System.Double)`

### `op_Subscript(System.Int32)`

ID: `M:RGK.Geometry.Interval.op_Subscript(System.Int32)`

Returns: Начало интервала если end == 0, конец если end == 1
