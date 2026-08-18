# SplineImageData

Assembly: `TFlexAPI`

## Methods

### `BuildMiddlePoints(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.BuildMiddlePoints(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Построить список промежуточных точек

### `BuildSpline(RGPlatform.Geometry.Context*,System.Int32,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double)`

ID: `M:SplineImageData.BuildSpline(RGPlatform.Geometry.Context*,System.Int32,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double)`

Создать сплайн и запомнить в кэше

Parameters:
- `iContext`: Контекст
- `iVersion`: Версия объекта
- `iDoc`: Документ
- `iToModelSpaceScale`: Масштаб

### `CloseContiniouslyRequired`

ID: `M:SplineImageData.CloseContiniouslyRequired`

Флаг, если TRUE тогда необходимы дополнительные модификации контрольного полигона для замкнутой кривой

Returns: True или False

### `ConvertToExtension(RGPlatform.Geometry.Context*,std.optional<System.Int32>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.ConvertToExtension(RGPlatform.Geometry.Context*,std.optional<System.Int32>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конвертировать вырезаемый интервал в отрицательно расширение

### `Copy`

ID: `M:SplineImageData.Copy`

Создать копию

### `Create(SPLINE_IMAGE*,System.Double,std.shared_ptr<RGPlatform.Geometry.Spline2D>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<SplineImageData>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.Create(SPLINE_IMAGE*,System.Double,std.shared_ptr<RGPlatform.Geometry.Spline2D>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<SplineImageData>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать по сплайну

Parameters:
- `iSpline`: Сплайн

### `DetachNode(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,TFDocument!System.Runtime.CompilerServices.IsConst*)`

ID: `M:SplineImageData.DetachNode(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,TFDocument!System.Runtime.CompilerServices.IsConst*)`

Отвязаться от узла (обновляет координаты из узла)

Parameters:
- `srcDoc`: Документ
- `setNodeCoords`: false, если не требуется обновление координат

Returns: true - если удалось получить узел, обновить координаты и отвязаться от него

### `EvaluateBaseDegree(System.Boolean,System.UInt64)`

ID: `M:SplineImageData.EvaluateBaseDegree(System.Boolean,System.UInt64)`

Основное правило вычисления степени

### `EvaluateDegree(System.Boolean,System.Boolean,System.Boolean,System.UInt64,System.UInt64,<unknown type>)`

ID: `M:SplineImageData.EvaluateDegree(System.Boolean,System.Boolean,System.Boolean,System.UInt64,System.UInt64,<unknown type>)`

Получить cтепень сплайна с учетом ограничения, метод реализует общее правило вычисления степени

### `FillDerivativeData(RGPlatform.Geometry.Context*,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double)`

ID: `M:SplineImageData.FillDerivativeData(RGPlatform.Geometry.Context*,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double)`

Получить данные о диф. геометрии кривой в кэше

Parameters:
- `iContext`: Контекст
- `iDoc`: Документ
- `iToModelSpaceScale`: Масштаб

### `GetCounter`

ID: `M:SplineImageData.GetCounter`

Получить значение счетчика уникальных точек

### `GetCroppedCurve(RGPlatform.Geometry.Context*)`

ID: `M:SplineImageData.GetCroppedCurve(RGPlatform.Geometry.Context*)`

Получить требуемую кривую с учетом: "-" расщирения, "+" расширения, интервала

### `GetCroppedEnd`

ID: `M:SplineImageData.GetCroppedEnd`

Получить конечный параметр сплайна

### `GetCroppedInterval`

ID: `M:SplineImageData.GetCroppedInterval`

Получить вырезаемый интервал

### `GetCroppedStart`

ID: `M:SplineImageData.GetCroppedStart`

Получить начальный параметр сплайна

### `GetCurve`

ID: `M:SplineImageData.GetCurve`

Получить кривую

### `GetDegree`

ID: `M:SplineImageData.GetDegree`

Получить cтепень сплайна с учетом ограничения

### `GetEndDerivative(TFModelDirection*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetEndDerivative(TFModelDirection*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить направление первой производной в последней точке

Parameters:
- `ioDirection`: Направление первой производной

### `GetEndPoint(RGPlatform.Geometry.Context*,System.Double)`

ID: `M:SplineImageData.GetEndPoint(RGPlatform.Geometry.Context*,System.Double)`

Получить точку конца кривой с учетом обрезки

### `GetErrorMessage(RGK.Common.Result)`

ID: `M:SplineImageData.GetErrorMessage(RGK.Common.Result)`

Получить строку для ошибки

### `GetExtendData(System.UInt64)`

ID: `M:SplineImageData.GetExtendData(System.UInt64)`

Получить расширение в конце кривой

### `GetHighExtension`

ID: `M:SplineImageData.GetHighExtension`

Получить расширение в конце кривой

### `GetKnotMethod`

ID: `M:SplineImageData.GetKnotMethod`

Метод построения узлов и параметров точек для интерполяции

Returns: Метод

### `GetKnots`

ID: `M:SplineImageData.GetKnots`

Получить список узлов сплайна, может быть не задан.

### `GetKnots(std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetKnots(std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить список узлов сплайна, может быть не задан.

Parameters:
- `oKnots`: Узлы

### `GetLowExtension`

ID: `M:SplineImageData.GetLowExtension`

Получить расширение в начале кривой

### `GetModelPoint(System.UInt64)`

ID: `M:SplineImageData.GetModelPoint(System.UInt64)`

Получить модельную точку сплайна по индексу

### `GetParameters`

ID: `M:SplineImageData.GetParameters`

Получить параметры интерполяции для точек

### `GetPointIndexByUID(System.UInt32)`

ID: `M:SplineImageData.GetPointIndexByUID(System.UInt32)`

Получить модельную точку сплайна по идентификатору

### `GetRawBackFirstDerivatives(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double!System.Runtime.CompilerServices.IsConst,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetRawBackFirstDerivatives(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double!System.Runtime.CompilerServices.IsConst,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить обратные производные в масштабе RGP

### `GetRawDegree`

ID: `M:SplineImageData.GetRawDegree`

Получить значение поля для cтепени

### `GetRawDerivatives(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetRawDerivatives(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить производные в масштабе RGP

### `GetRawPoint(System.UInt64,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double)`

ID: `M:SplineImageData.GetRawPoint(System.UInt64,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double)`

Получить точку в масштабе RGP

### `GetRawPoints(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetRawPoints(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить точки в масштабе RGP

### `GetStartDerivative(TFModelDirection*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetStartDerivative(TFModelDirection*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить направление первой производной в первой точке

Parameters:
- `ioDirection`: Направление первой производной

### `GetStartPoint(RGPlatform.Geometry.Context*,System.Double)`

ID: `M:SplineImageData.GetStartPoint(RGPlatform.Geometry.Context*,System.Double)`

Получить точку начала кривой, с учетом обрезки

### `GetSuppressedPointIndices`

ID: `M:SplineImageData.GetSuppressedPointIndices`

Получить индексы подавленных точке

Parameters:
- `oIndices`: Индексы

### `GetSuppressedPointsCount`

ID: `M:SplineImageData.GetSuppressedPointsCount`

Получить количество подавленных точке

Parameters:
- `oIndices`: Индексы

### `GetTFPoints(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst,TFPoints*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetTFPoints(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst,TFPoints*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить точки в масштабе модели

### `GetTolerantPointIndices(System.Boolean)`

ID: `M:SplineImageData.GetTolerantPointIndices(System.Boolean)`

Получить индексы толерантных точке

Parameters:
- `iAllowSuppressed`: Учитывать подавленные точки
- `oIndices`: Индексы

### `GetTolerantPointsCount(System.Boolean)`

ID: `M:SplineImageData.GetTolerantPointsCount(System.Boolean)`

Получить количество толерантных точке

Parameters:
- `iAllowSuppressed`: Учитывать подавленные точки (считать или не считать одновременно толерантные и подавденные точки)
- `oIndices`: Количество

### `GetUpperConstrainedDerivativeOrder`

ID: `M:SplineImageData.GetUpperConstrainedDerivativeOrder`

Получить макс. указанную степень производной в точке сплайна

### `GetWeights(std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.GetWeights(std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить веса точек

### `HasTolerantPoints`

ID: `M:SplineImageData.HasTolerantPoints`

Признак наличия толерантных точек

### `Init(LegacySplineImageData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.Init(LegacySplineImageData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Инициализация по представлению доставшемуся в наследство

Parameters:
- `iSpline`: Сплайн

### `Init(System.Int32,System.Int32,std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:SplineImageData.Init(System.Int32,System.Int32,std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Инициализация по устаревшим данным

Parameters:
- `iSpline`: Сплайн

### `Init(std.shared_ptr<RGPlatform.Geometry.BaseSpline2D>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:SplineImageData.Init(std.shared_ptr<RGPlatform.Geometry.BaseSpline2D>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Инициализация по сплайну

Parameters:
- `iSpline`: Сплайн

### `Init(std.shared_ptr<RGPlatform.Geometry.Polyline2D>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:SplineImageData.Init(std.shared_ptr<RGPlatform.Geometry.Polyline2D>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Инициализация по полилинии

Parameters:
- `iPolyLine`: Полилилиния

### `Init(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.Init(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Инициализация по полилинии

Parameters:
- `iPolyLine`: Полилилиния

### `Init(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,<unknown type>,std.optional<std.pair<System.Double,System.Double>>,System.Int32,System.Boolean)`

ID: `M:SplineImageData.Init(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,<unknown type>,std.optional<std.pair<System.Double,System.Double>>,System.Int32,System.Boolean)`

Инициализация по определению сплайна

### `IsApproximation`

ID: `M:SplineImageData.IsApproximation`

Признак аппроксимации

### `IsClosed(RGPlatform.Geometry.Context*,TFDocument*,System.Double)`

ID: `M:SplineImageData.IsClosed(RGPlatform.Geometry.Context*,TFDocument*,System.Double)`

Проверка того, что начальная и конечная точка совпадают

### `IsControlPolygon`

ID: `M:SplineImageData.IsControlPolygon`

Признак построения сплайна по контрольному полигону

### `IsCreateExtendRequired`

ID: `M:SplineImageData.IsCreateExtendRequired`

Требуетя создать данные для укорачивания кривой на основе интервала обрезки

### `IsCropped(RGPlatform.Geometry.Context*)`

ID: `M:SplineImageData.IsCropped(RGPlatform.Geometry.Context*)`

Кривая укорочена или расширенна, результирующая кривая вырезается или получается расширением из исходной кривой

### `IsDegreeConstrained`

ID: `M:SplineImageData.IsDegreeConstrained`

Признак ограничения степени пользователем, это значит что пользователь задал собственное значение степени

### `IsEndTangentConstrained`

ID: `M:SplineImageData.IsEndTangentConstrained`

Первая производная ограничена в последней точке

Returns: True или False

### `IsExtended(RGPlatform.Geometry.Context*)`

ID: `M:SplineImageData.IsExtended(RGPlatform.Geometry.Context*)`

Кривая расширена или укорочена. Результирующая кривая получается путем расширения или укорачивания исходной кривой.

### `IsInterpolation`

ID: `M:SplineImageData.IsInterpolation`

Признак интерполяционого сплайна

### `IsKnotsFixed`

ID: `M:SplineImageData.IsKnotsFixed`

Узлы сплайна фиксированы

### `IsPositiveExtended(RGPlatform.Geometry.Context*)`

ID: `M:SplineImageData.IsPositiveExtended(RGPlatform.Geometry.Context*)`

Кривая расширена c одного или с двух концов

### `IsRepairIntermediateVersion`

ID: `M:SplineImageData.IsRepairIntermediateVersion`

Исправление интервалов обрезки промежуточных версий

### `IsStartTangentConstrained`

ID: `M:SplineImageData.IsStartTangentConstrained`

Первая производная ограничена в первой точке

Returns: True или False

### `IsUnderEdit`

ID: `M:SplineImageData.IsUnderEdit`

Признак редактирования сплайна

Parameters:
- `iValue`: Флаг

### `Parameterise(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

ID: `M:SplineImageData.Parameterise(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

Определить параметр точки, лежащей на кривой

Parameters:
- `iContext`: Контекст геометрии
- `iPointInPageCs`: Точка на кривой с учётом масштаба страницы
- `ioParam`: Найденный параметр на кривой (на входе может содержать начальное приближение)
- `iUseGuess`: Использовать ли начальное приближение

Returns: true - в случае успеха, false - иначе

### `PointsCount`

ID: `M:SplineImageData.PointsCount`

Получить количество точек сплайна

### `PreprocessData(TFDocument!System.Runtime.CompilerServices.IsConst*)`

ID: `M:SplineImageData.PreprocessData(TFDocument!System.Runtime.CompilerServices.IsConst*)`

Обработать даныне перед построением сплайна

### `ResetPointsData`

ID: `M:SplineImageData.ResetPointsData`

Удалить всю информацию о сплайне, за исключением, типа построения (_periodic, _interpolation)

### `SetCloseContiniouslyRequired(System.Boolean)`

ID: `M:SplineImageData.SetCloseContiniouslyRequired(System.Boolean)`

Установить флаг дополнительных модификаций контрольного полигона для замкнутой кривой

Parameters:
- `iValue`: Флаг

### `SetCreateExtendRequired(System.Boolean)`

ID: `M:SplineImageData.SetCreateExtendRequired(System.Boolean)`

Требуетя создать данные для укорачивания кривой на основе интервала обрезки

### `SetCroppedEnd(System.Double)`

ID: `M:SplineImageData.SetCroppedEnd(System.Double)`

Установить конечный параметр обрезки сплайна на интервале

Parameters:
- `iStart`: Параметр конца вырезаемого сегмента

### `SetCroppedInterval(RGK.Geometry.Interval)`

ID: `M:SplineImageData.SetCroppedInterval(RGK.Geometry.Interval)`

Установить вырезаемый интервал

Parameters:
- `iInterval`: Вырезаемый интервал

### `SetCroppedInterval(System.Double,System.Double)`

ID: `M:SplineImageData.SetCroppedInterval(System.Double,System.Double)`

Установить вырезаемый интервал

Parameters:
- `iStart`: Параметр конца вырезаемого сегмента

### `SetCroppedStart(System.Double)`

ID: `M:SplineImageData.SetCroppedStart(System.Double)`

Установить начальный параметр обрезки сплайна на интервале

Parameters:
- `iStart`: Параметр начала вырезаемого сегмента

### `SetCurve(std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetCurve(std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить кривую

### `SetDegree(System.Int32)`

ID: `M:SplineImageData.SetDegree(System.Int32)`

Установить степень сплайна (может игнорироваться)

### `SetForceSourceInterval(RGK.Geometry.Interval)`

ID: `M:SplineImageData.SetForceSourceInterval(RGK.Geometry.Interval)`

Установить интервал исходной кривой

Parameters:
- `iInterval`: Интервал

### `SetHighExtension(ExtendData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetHighExtension(ExtendData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить расширение в конце кривой

### `SetInterpolation(System.Boolean)`

ID: `M:SplineImageData.SetInterpolation(System.Boolean)`

Установить признак интерполяционого сплайна

Parameters:
- `iValue`: Флаг

### `SetKnotMethod(<unknown type>)`

ID: `M:SplineImageData.SetKnotMethod(<unknown type>)`

Устновить метод генерации узлов, для режима полилинии метод фикисрован - по длине

### `SetKnots(std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetKnots(std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить список узлов для сплайна

Parameters:
- `iKnots`: Список узлов

### `SetKnotsFixed(System.Boolean)`

ID: `M:SplineImageData.SetKnotsFixed(System.Boolean)`

Установить признак фиксации узлов

Parameters:
- `iFixed`: Флаг

### `SetLowExtension(ExtendData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetLowExtension(ExtendData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить расширение в начале кривой

### `SetModelPoint(System.UInt64,TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetModelPoint(System.UInt64,TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить модельную точку сплайна по индексу

### `SetParametes(std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetParametes(std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить параметры интерполяции для точек

Parameters:
- `iParameters`: Список параметров

### `SetPoints(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetPoints(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить точки на основе координат

Parameters:
- `iPoints`: Точки

### `SetPoints(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RealParameter,std.allocator<RealParameter>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetPoints(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RealParameter,std.allocator<RealParameter>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить точки на основе координат и весов

Parameters:
- `iPoints`: Точки
- `iWeights`: Веса

### `SetPoints(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetPoints(std.vector<TFModelPoint,std.allocator<TFModelPoint>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить точки на основе координат и весов

Parameters:
- `iPoints`: Точки
- `iWeights`: Веса

### `SetRepairIntermediateVersion(System.Boolean)`

ID: `M:SplineImageData.SetRepairIntermediateVersion(System.Boolean)`

Исправление интервалов обрезки промежуточных версий

### `SetTolerance(RealParameter*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.SetTolerance(RealParameter*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить точность аппроксимации толерантных точек

Parameters:
- `iTolerance`: Точность

### `SetTolerant(System.UInt64,System.Boolean)`

ID: `M:SplineImageData.SetTolerant(System.UInt64,System.Boolean)`

Установить признак толерантной точки по индексу

Parameters:
- `id`: Индекс точки
- `iValue`: Значение толерантности

### `SetUnderEdit(System.Boolean)`

ID: `M:SplineImageData.SetUnderEdit(System.Boolean)`

Установить признак редактирования сплайна

Parameters:
- `iValue`: Флаг

### `TrimOnInterval(RGPlatform.Geometry.Context*,TrimSplineData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TrimSplineResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SplineImageData.TrimOnInterval(RGPlatform.Geometry.Context*,TrimSplineData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TrimSplineResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить сплайн путем вырезания сплайна на интервала
