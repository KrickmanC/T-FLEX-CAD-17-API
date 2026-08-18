# RGK.Geometry.Curve

Assembly: `TFlexAPI`
Namespace: `RGK.Geometry`

## Methods

### `Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

В базовом классе метод реализован на основе сплайн-представления

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляется производная
- `iDerivOrder`: Порядок производной (>=0)
- `oDerivative`: Значение вычисленной производной

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*)`

ID: `M:RGK.Geometry.Curve.Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных (массив векторов размера не менее iMaxDerivOrder+1)

Returns: - Result::Success в случае успешного выполнения - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `Evaluate(RGK.Common.Context*,System.Double,System.UInt32,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.Evaluate(RGK.Common.Context*,System.Double,System.UInt32,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных

Returns: - Result::Success в случае успешного выполнения - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `EvaluateCurvature(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.EvaluateCurvature(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляется кривизна
- `oCurvature`: Значение вычисленной кривизны

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::ZeroVector значение первой производной меньше системной точности - Result::NullPointer недопустимая передача нулевого указателя

### `EvaluateNormal(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.EvaluateNormal(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляется нормаль
- `oDerivative`: Значение вычисленной нормали

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NormalIsNotSignificant очень маленькая кривизна в точке. Радиус кривизны не определяется - Result::NullPointer недопустимая передача нулевого указателя

### `EvaluatePoint(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.EvaluatePoint(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляются координаты точки на кривой
- `oPoint`: Значение вычисленной точки

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `EvaluatePoints(RGK.Common.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.EvaluatePoints(RGK.Common.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметры на кривой, в которых вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных

Returns: - Result::Success в случае успешного выполнения - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `EvaluateTangent(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.EvaluateTangent(RGK.Common.Context*,System.Double,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляется касательная
- `oDerivative`: Значение вычисленной касательной

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `FindBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*,System.Boolean)`

ID: `M:RGK.Geometry.Curve.FindBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*,System.Boolean)`

Получить ограничивающий параллелепипед для кривой на интервале в заданной или глобальной системе координат

Parameters:
- `iContext`: Указатель на контекст вычисления
- `iInterval`: Интервал параметров, для которого выполняется расчёт ограничивающего параллелепипеда
- `oBox`: Результирующий ограничивающий параллелепипед для кривой
- `ipLCS`: Система координат для поиска ограничивающего параллелепипеда
- `iEstimate`: Выполнить быструю приблизительную оценку

Returns: - Result::NotSupported данный тип интервала не поддерживается - Result::Success в случае успешного выполнения

### `FindInterval(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.FindInterval(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint1`: Первая точка
- `iPoint2`: Вторая точка
- `iTolerance`: Точность положения точки на кривой
- `oInterval`: Найденный интервал

Returns: - Result::Success в случае успешного выполнения

### `FindLength(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,System.Int32)`

ID: `M:RGK.Geometry.Curve.FindLength(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,System.Int32)`

Parameters:
- `iContext`: Контекст вычисления
- `iInterval`: Параметрический интервал кривой, на котором считается длина
- `iTolerance`: Запрашиваемая точность вычисления длины
- `oLength`: Найденная длина

Returns: - Result::Success в случае успешного выполнения

### `FindMinRadius(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.FindMinRadius(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iInterval`: Интервал
- `iTolerance`: Точность поиска
- `oRadius`: Радиус
- `oParams`: Параметр

Returns: - Result::Success в случае успешного выполнения

### `FindMinimalBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

ID: `M:RGK.Geometry.Curve.FindMinimalBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

Получить наименьший (ориентированный) ограничивающий параллелепипед для кривой на интервале в заданной (или текущей) системе координат

Parameters:
- `iContext`: Указатель на контекст вычисления
- `iInterval`: Интервал параметров, для которого выполняется расчёт ограничивающего параллелепипеда
- `oBox`: Результирующий ограничивающий параллелепипед для кривой
- `oLCS`: Система координат ограничивающего параллелепипеда
- `iEstimate`: Выполнить быструю приблизительную оценку

Returns: - Result::NotSupported данный тип интервала не поддерживается - Result::Success в случае успешного выполнения

### `FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка, для которой ищется ближайшая точка на кривой
- `iTolerance`: Точность, с которой ищется ближайшая точка
- `oParam`: Найденный параметр ближайшей точки на кривой

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована

### `FindSelfIntersections(RGK.Common.Context*,RGK.Geometry.Curve.SelfIntersectionData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IntersectReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.FindSelfIntersections(RGK.Common.Context*,RGK.Geometry.Curve.SelfIntersectionData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IntersectReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iData`: Данные для пересечения кривых
- `oReport`: Результат поиска самопересечений

Returns: - Result::Success в случае успешного выполнения

### `GetInterval(RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.GetInterval(RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

В базовом классе метод реализован на основе сплайн-представления

Parameters:
- `oInterval`: Интервал

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported - для данного класса кривой функциональность не реализована

### `IntersectCurve(RGK.Common.Context*,RGK.Geometry.Curve.IntersectData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IntersectReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.IntersectCurve(RGK.Common.Context*,RGK.Geometry.Curve.IntersectData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IntersectReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iData`: Данные для пересечения кривых
- `oReport`: Результат поиска пересечений

Returns: - Result::Success в случае успешного выполнения

### `IsCurve`

ID: `M:RGK.Geometry.Curve.IsCurve`

Returns: true если объект является кривой

### `IsPlanar(RGK.Common.Context*,RGK.Geometry.Curve.IsPlanarData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IsPlanarReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.IsPlanar(RGK.Common.Context*,RGK.Geometry.Curve.IsPlanarData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IsPlanarReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Проверка, что кривая или её участок является плоской

Parameters:
- `iData`: Параметры проверки
- `oReport`: Результаты проверки

Returns: - Result::Success в случае успешного выполнения

### `IterateToNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.IterateToNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка, для которой ищется ближайшая точка на поверхности
- `iLinearTolerance`: Точность, с которой ищется ближайшая точка
- `oApproximationParam`: Первое приближение
- `oParam`: Найденный параметр ближайшей точки на поверхности

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса поверхности функциональность не реализована

### `MakeEquidistantOnSurface(RGK.Common.Context*,RGK.Geometry.Curve.EquidistantOnSurfaceData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.MakeEquidistantOnSurface(RGK.Common.Context*,RGK.Geometry.Curve.EquidistantOnSurfaceData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iData`: Параметры построения эквидистантной поверхности
- `oReport`: Результат построения

Returns: - Result::Success в случае успешного выполнения

### `MakeNURBSCurve(RGK.Common.Context*,RGK.Geometry.MakeNURBSCurveData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.MakeNURBSCurveReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.MakeNURBSCurve(RGK.Common.Context*,RGK.Geometry.MakeNURBSCurveData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.MakeNURBSCurveReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iData`: Данные для интерполяции
- `oReport`: Результат построения

Returns: - Result::Success в случае успешного выполнения

### `MakeNormalOffset(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.MakeNormalOffset(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,std.shared_ptr<RGK.Geometry.Curve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iInterval`: Входной интервал
- `iSurface`: Входная поверхность
- `iOffset`: Величина сдвига
- `iTolerance`: Входная точность
- `oCurve`: Выходная кривая

Returns: - Result::Success в случае успешного выполнения

### `OutputPoints(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.OutputPointsOptions!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.OutputPoints(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.OutputPointsOptions!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iInterval`: Интервал, на котором выполняется расчёт точек
- `iOptions`: Параметры разбиения
- `oPoints`: Массив насчитанных точек
- `oParams`: Массив параметров, в которых насчитаны точки

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя - Result::NotConverged ошибка сходимости алгоритма (вероятна ошибка в реализации функции Evaluate)

### `Parameterise(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

ID: `M:RGK.Geometry.Curve.Parameterise(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка на кривой
- `ioParam`: Найденный параметр на кривой (на входе может содержать начальное приближение)
- `iUseGuess`: Использовать ли начальное приближение

Returns: - Result::Success в случае успешного выполнения - Result::NotOnCurve точка не лежит на кривой - Result::NotSupported для данного класса кривой функциональность не реализована

### `Transform(RGK.Common.Context*,RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve.Transform(RGK.Common.Context*,RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания линии
- `iMap`: Аффинное преобразование
- `iTolerance`: Допустимая точность преобразований
- `oCopy`: Возвращается трансформированная геометрия
- `oExact`: Возвращается true-для точного преобразования

Returns: - Result::Success в случае успешного выполнения

### `_FindBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*,System.Boolean)`

ID: `M:RGK.Geometry.Curve._FindBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*,System.Boolean)`

Получить ограничивающий параллелепипед для кривой на интервале в заданной или глобальной системе координат

Parameters:
- `iContext`: Указатель на контекст вычисления
- `iInterval`: Интервал параметров, для которого выполняется расчёт ограничивающего параллелепипеда
- `oBox`: Результирующий ограничивающий параллелепипед для кривой
- `ipLCS`: Система координат для поиска ограничивающего параллелепипеда
- `iEstimate`: Выполнить быструю приблизительную оценку

Returns: - Result::NotSupported данный тип интервала не поддерживается - Result::Success в случае успешного выполнения

### `_FindMinimalBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

ID: `M:RGK.Geometry.Curve._FindMinimalBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

Получить наименьший (ориентированный) ограничивающий параллелепипед для кривой на интервале в заданной (или текущей) системе координат

Parameters:
- `iContext`: Указатель на контекст вычисления
- `iInterval`: Интервал параметров, для которого выполняется расчёт ограничивающего параллелепипеда
- `oBox`: Результирующий ограничивающий параллелепипед для кривой
- `oLCS`: Система координат ограничивающего параллелепипеда
- `iEstimate`: Выполнить быструю приблизительную оценку

Returns: - Result::NotSupported данный тип интервала не поддерживается - Result::Success в случае успешного выполнения

### `_FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve._FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка, для которой ищется ближайшая точка на кривой
- `iTolerance`: Точность, с которой ищется ближайшая точка
- `oParam`: Найденный параметр ближайшей точки на кривой

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована

### `_MakeNURBSCurve(RGK.Common.Context*,RGK.Geometry.MakeNURBSCurveData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.MakeNURBSCurveReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Curve._MakeNURBSCurve(RGK.Common.Context*,RGK.Geometry.MakeNURBSCurveData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.MakeNURBSCurveReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iData`: Данные для интерполяции
- `oReport`: Результат построения

Returns: - Result::Success в случае успешного выполнения

### `_Parameterise(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

ID: `M:RGK.Geometry.Curve._Parameterise(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка на кривой
- `ioParam`: Найденный параметр на кривой (на входе может содержать начальное приближение)
- `iUseGuess`: Использовать ли начальное приближение

Returns: - Result::Success в случае успешного выполнения - Result::NotOnCurve точка не лежит на кривой - Result::NotSupported для данного класса кривой функциональность не реализована
