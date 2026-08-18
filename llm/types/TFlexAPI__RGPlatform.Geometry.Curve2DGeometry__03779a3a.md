# RGPlatform.Geometry.Curve2DGeometry

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry`

## Summary

Базовый класс двумерной кривой

## Constructors

### `Curve2DGeometry`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.#ctor`

## Methods

### `Curve2DGeometry`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.#ctor`

### `ApproximateWithArcs(RGPlatform.Geometry.Context*,System.Double,std.vector<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.allocator<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ApproximateWithArcs(RGPlatform.Geometry.Context*,System.Double,std.vector<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.allocator<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст геометрии
- `iTolerance`: Максимальное отклонение от исходной кривой.
- `ioCurves`: Массив дуг или отрезков, аппроксимирующий исходную кривую.

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `AsCurve2DGeometry`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.AsCurve2DGeometry`

Получить геометрию как двумерную кривую

Returns: Указатель на данный объект двумерной кривой

### `ConvertArcLengthToParameter(RGPlatform.Geometry.Context*,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertArcLengthToParameter(RGPlatform.Geometry.Context*,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Вычислить параметр на кривой по длине дуги от указанного параметра

Parameters:
- `iContext`: Контекст геометрии
- `iStartParam`: Параметр, от которого отсчитывается расстояние по кривой
- `iLength`: Длина дуги
- `oParam`: Найденный параметр, соответствующий указанной длине дуги

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `ConvertRGKParamToRGP(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertRGKParamToRGP(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Curve2DGeometry!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `ConvertToPolyline(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertToPolyline(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Адаптивный алгоритм получения полилинии.

Parameters:
- `iRGKContext`: Контекст RGK
- `iInterval`: Интервал, на котором выполняется расчёт полилинии
- `iScale`: Условный масштаб преобразования в единицы измерения устройства
- `ioPolyline`: Результирующая полилиния

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Точки добавляются к уже имеющимся в ioPolyline.

### `ConvertToPolyline(RGK.Common.Context*,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertToPolyline(RGK.Common.Context*,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Адаптивный алгоритм получения полилинии.

Parameters:
- `iRGKContext`: Контекст RGK
- `iScale`: Условный масштаб преобразования в единицы измерения устройства
- `ioPolyline`: Результирующая полилиния

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Точки добавляются к уже имеющимся в ioPolyline.

### `ConvertToRGK(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.ConvertToRGK(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Преобразовать кривую в набор RGK-кривых

Parameters:
- `iContext`: Контекст геометрии
- `iInterval`: Интервал RGP-кривой
- `oResult`: Результат преобразования

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `CreateCropped(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.CreateCropped(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Построить кривую, совпадающую с данной на участке, ограниченном интервалом

Parameters:
- `iContext`: Контекст геометрии
- `iInterval`: Интервал
- `ioCurve`: Построенная кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `CreateCropped(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.CreateCropped(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Построить кривую, совпадающую с данной на участке, ограниченном двумя точками

Parameters:
- `iContext`: Контекст геометрии
- `iPoint1`: Начальная точка сегмента кривой
- `iPoint2`: Конечная точка сегмента кривой
- `iTolerance`: Погрешность, с которой точки лежат на кривой
- `iInsideCurveBounds`: true - учитывается только кривая в своих границах, точки сегмента должны лежать внутри этих границ false - учитывается носитель кривой целиком, точки сегмента должны лежать на носителе
- `ioCurve`: Построенная кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Направление роста параметра определяется порядком точек

### `CreateReversed(RGPlatform.Geometry.Context*,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.CreateReversed(RGPlatform.Geometry.Context*,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Построить кривую, совпадающую с данной, но с противоположной параметризацией

Parameters:
- `iContext`: Контекст геометрии
- `ioCurve`: Построенная кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Данная операция возможна не для всех типов кривых

### `Dispose`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.Dispose`

Деструктор

### `EstimateDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.EstimateDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оценка расстояния от точки до объекта

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `oExact`: Флаг, определяющий является ли вычисленное приближённое расстояние точным
- `oDistance`: Приближённое расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение производной (заданного порядка) кривой по заданному параметру

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляется производная
- `iDerivOrder`: Порядок производной (>=0)
- `oDerivative`: Значение вычисленной производной

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить координаты точки и все производные по параметру кривой. Пакетный расчёт производных.

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `EvaluateCurvature(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.EvaluateCurvature(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение вектора кривизны к кривой по параметру iU

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляется вектор кривизны
- `oCurvature`: Вычисленное значение вектора кривизны

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `EvaluateCurvatureDerivative(System.Double,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.EvaluateCurvatureDerivative(System.Double,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Вычислить производную кривизны

Parameters:
- `iTolerance`: Линейная точность
- `iDerivatives`: Производные, степень >=3
- `oCurvatureDerivative`: Производная

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `EvaluateNormal(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.EvaluateNormal(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение нормали к кривой по параметру iU

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляется нормаль
- `oNormal`: Вычисленное значение нормали

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Вектор нормали нормируется на 1.

### `EvaluatePoint(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.EvaluatePoint(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение кривой по параметру iU

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляется значение
- `oPoint`: Вычисленное значение

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `EvaluateTangent(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.EvaluateTangent(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение касательной к кривой по параметру iU

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляется касательная
- `oTangent`: Вычисленное значение касательной

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Вектор касательной нормируется на 1.

### `FindArea(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FindArea(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить площадь которую огрничивает кривая

Parameters:
- `iTolerance`: Точность вычисления

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindLength(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FindLength(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить длину кривой

Parameters:
- `iContext`: Контекст геометрии
- `iInterval`: Интервал, соответствующий участку кривой, длина которого ищется
- `iTolerance`: Точность вычисления длины кривой
- `oLength`: Вычисленная длина кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindLength(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FindLength(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить длину кривой

Parameters:
- `iContext`: Контекст геометрии
- `iTolerance`: Точность вычисления длины кривой
- `oLength`: Вычисленная длина кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindNearestPoint(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*,RGPlatform.Geometry.Point2D*)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FindNearestPoint(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*,RGPlatform.Geometry.Point2D*)`

Получить параметр точки на кривой, ближайшей к передаваемой точке

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, для которой ищется ближайшая точка на кривой
- `iTolerance`: Точность, с которой ищется ближайшая точка
- `oParam`: Найденный параметр ближайшей точки на кривой
- `oPoint`: Найденная точка на кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FitParamToInterval(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FitParamToInterval(RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

### `GetDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение расстояния от точки до объекта

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `oDistance`: Расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetDistanceWithClipping(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetDistanceWithClipping(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение расстояния от точки до кривой с заданной обрезкой

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `iClipInteval`: Интервал, задающий обрезку
- `oDistance`: Расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetEndParameter(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetEndParameter(RGPlatform.Geometry.Context*)`

Вычислить конечный параметр кривой

Parameters:
- `iContext`: Контекст геометрии

Returns: Конечный параметр кривой

### `GetEndPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetEndPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить конечную точку кривой

Parameters:
- `oPoint`: Конечная точка кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetInterval(RGPlatform.Geometry.Context*,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetInterval(RGPlatform.Geometry.Context*,RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить интервал кривой

Parameters:
- `oInterval`: Интервал кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetRectangleWithClipping(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetRectangleWithClipping(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить ограничивающий прямоугольник с заданной обрезкой

Parameters:
- `iContext`: Контекст геометрии
- `iClipInteval`: Интервал, задающий обрезку
- `oRect`: Вычисленный ограничивающий прямоугольник

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetStartParameter(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetStartParameter(RGPlatform.Geometry.Context*)`

Вычислить начальный параметр кривой

Parameters:
- `iContext`: Контекст геометрии

Returns: Начальный параметр кривой

### `GetStartPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.GetStartPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить начальную точку кривой

Parameters:
- `oPoint`: Начальная точка кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `IsClosed`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.IsClosed`

Проверить, является ли кривая замкнутой

Returns: true - кривая является замкнутой, false - кривая не является замкнутой

### `IsPeriodic`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.IsPeriodic`

Проверить, является ли кривая периодической

Returns: true - кривая является периодической, false - кривая не является периодической

### `MakeOffset(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Curve2DGeometry.MakeOffsetData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.MakeOffsetResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.MakeOffset(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Curve2DGeometry.MakeOffsetData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.MakeOffsetResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Построить эквидистантную кривую

### `OutputPoints(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.FacetParameters!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.OutputPoints(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.FacetParameters!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Адаптивный алгоритм расчёта точек на кривой с учётом параметров точности

Parameters:
- `iContext`: Контекст геометрии
- `iInterval`: Интервал, на котором выполняется расчёт точек
- `iOptions`: Параметры разбиения
- `oPoints`: Массив насчитанных точек
- `oParams`: Массив параметров, в которых насчитаны точки

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Точки добавляются к уже имеющимся в ioPoints, ioParams.

### `Parameterise(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.Parameterise(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

Определить параметр точки, лежащей на кривой

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка на кривой
- `ioParam`: Найденный параметр на кривой (на входе может содержать начальное приближение)
- `iUseGuess`: Использовать ли начальное приближение

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `_ConvertRGKParamToRGP(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry._ConvertRGKParamToRGP(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`
