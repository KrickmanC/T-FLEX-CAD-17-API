# RGPlatform.Geometry.Spline2D

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry`

## Summary

Двумерный сплайн

## Constructors

### `Spline2D`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor`

Конструктор по умолчанию

### `Spline2D(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Копирующий конструктор

Parameters:
- `iSpline`: Сплайн

### `Spline2D(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean)`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean)`

Создать двумерный сплайн по параметрам кривой, предназначен для использования в списках инициализации наследников

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iWeights`: Массив весов
- `iKnots`: Последовательность узлов
- `iDegree`: Степень кривой
- `iIsPeriodic`: Является ли кривая периодической
- `oResultCurve`: Созданная двумерная сплайн-кривая

### `Spline2D(std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>)`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor(std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>)`

Конструктор по RGK-сплайну

Parameters:
- `iRGKNURBSCurve`: Сплайн кривая в формате RGK

## Methods

### `Spline2D`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor`

Конструктор по умолчанию

### `Spline2D(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Копирующий конструктор

Parameters:
- `iSpline`: Сплайн

### `Spline2D(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean)`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean)`

Создать двумерный сплайн по параметрам кривой, предназначен для использования в списках инициализации наследников

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iWeights`: Массив весов
- `iKnots`: Последовательность узлов
- `iDegree`: Степень кривой
- `iIsPeriodic`: Является ли кривая периодической
- `oResultCurve`: Созданная двумерная сплайн-кривая

### `Spline2D(std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>)`

ID: `M:RGPlatform.Geometry.Spline2D.#ctor(std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>)`

Конструктор по RGK-сплайну

Parameters:
- `iRGKNURBSCurve`: Сплайн кривая в формате RGK

### `ApproximateWithArcs(RGPlatform.Geometry.Context*,System.Double,std.vector<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.allocator<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ApproximateWithArcs(RGPlatform.Geometry.Context*,System.Double,std.vector<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.allocator<std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст геометрии
- `iTolerance`: Максимальное отклонение от исходной кривой.
- `ioCurves`: Массив дуг или отрезков, аппроксимирующий исходную кривую.

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `AsSpline2D`

ID: `M:RGPlatform.Geometry.Spline2D.AsSpline2D`

Получить геометрию как двумерный сплайн

Returns: Указатель на данный объект двумерного сплайна

### `ClampCurve(RGPlatform.Geometry.Context*,System.Boolean,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ClampCurve(RGPlatform.Geometry.Context*,System.Boolean,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Преобразование несжатой (unclamped) кривой в сжатую (clamped)

Parameters:
- `iContext`: Контекст геометрии
- `iFromLeft`: Обработка левой части кривой
- `iFromRight`: Обработка правой части кривой
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Для обработки обоих концов оба входных флага надо выставить в true.

### `ConvertToPolyline(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ConvertToPolyline(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Адаптивный алгоритм получения полилинии.

Parameters:
- `iRGKContext`: Контекст RGK
- `iInterval`: Интервал, на котором выполняется расчёт полилинии
- `iScale`: Условный масштаб преобразования в единицы измерения устройства
- `ioPolyline`: Результирующая полилиния

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Точки добавляются к уже имеющимся в ioPolyline.

### `ConvertToPolyline(RGK.Common.Context*,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ConvertToPolyline(RGK.Common.Context*,System.Double,RGPlatform.Geometry.Polyline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Адаптивный алгоритм получения полилинии

Parameters:
- `iRGKContext`: Контекст RGK
- `iScale`: Условный масштаб преобразования в единицы измерения устройства
- `oPolyline`: Результирующая полилиния

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Точки добавляются к уже имеющимся в ioPolyline.

### `ConvertToRGK(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ConvertToRGK(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.ConvertToRGKResult*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Преобразовать кривую в набор RGK-кривых

Parameters:
- `iContext`: Контекст геометрии
- `iInterval`: Интервал RGP-кривой
- `oResult`: Результат преобразования

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Copy(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Spline2D.Copy(RGPlatform.Geometry.Context*)`

Создать копию объекта

Parameters:
- `iContext`: Контекст геометрии

Returns: Копия объекта

### `Create(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.Create(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать двумерный сплайн по параметрам кривой

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iWeights`: Массив весов
- `iKnots`: Последовательность узлов
- `iDegree`: Степень кривой
- `iIsPeriodic`: Является ли кривая периодической
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `CreateBezier(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.CreateBezier(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать кривую Безье

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iDegree`: Степень кривой
- `oResultCurve`: Созданная кривая Безье

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `CreateBezier(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.CreateBezier(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать кривую Безье

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iWeights`: Массив весов
- `iDegree`: Степень кривой
- `oResultCurve`: Созданная кривая Безье

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `CreateByControlPolygon(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.CreateByControlPolygon(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать двумерный сплайн по управляющему полигону с заданной параметризацией

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iWeights`: Массив весов
- `iKnots`: Последовательность узлов
- `iDegree`: Степень кривой
- `iIsPeriodic`: Является ли кривая периодической
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `CreateCropped(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.CreateCropped(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Построить кривую, совпадающую с данной на участке, ограниченном интервалом

Parameters:
- `iContext`: Контекст геометрии
- `iInterval`: Интервал
- `ioCurve`: Построенная кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `CreateCropped(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.CreateCropped(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

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

ID: `M:RGPlatform.Geometry.Spline2D.CreateReversed(RGPlatform.Geometry.Context*,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Построить кривую, совпадающую с данной, но с противоположной параметризацией

Parameters:
- `iContext`: Контекст геометрии
- `ioCurve`: Построенная кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Данная операция возможна не для всех типов кривых

### `CreateUniformByControlPolygon(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.CreateUniformByControlPolygon(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать двумерный сплайн с однородной параметризацией

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iWeights`: Массив весов
- `iDegree`: Степень кривой
- `iIsPeriodic`: Является ли кривая периодической
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `ElevateDegree(RGPlatform.Geometry.Context*,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ElevateDegree(RGPlatform.Geometry.Context*,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Повышение степени сплайна

Parameters:
- `iContext`: Контекст геометрии
- `iTimes`: Порядок повышения степени
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `EstimateDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.EstimateDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оценка расстояния от точки до объекта

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `oExact`: Флаг, определяющий является ли вычисленное приближённое расстояние точным
- `oDistance`: Приближённое расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `EstimateRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.EstimateRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оценить ограничивающий прямоугольник

Parameters:
- `iContext`: Контекст геометрии
- `oRect`: Вычисленная оценка ограничивающего прямоугольника

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение производной (заданного порядка) кривой по заданному параметру

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляется производная
- `iDerivOrder`: Порядок производной (>=0)
- `oDerivative`: Значение вычисленной производной

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.Evaluate(RGPlatform.Geometry.Context*,System.Double,System.UInt32,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить координаты точки и все производные по параметру кривой. Пакетный расчёт производных.

Parameters:
- `iContext`: Контекст геометрии
- `iU`: Параметр на кривой, в котором вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindArea(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.FindArea(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить площадь которую огрничивает кривая

Parameters:
- `iTolerance`: Точность вычисления
- `oArea`: Площадь
- `oHasArea`: Признак наличия площади

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindLength(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.FindLength(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить длину кривой

Parameters:
- `iContext`: Контекст геометрии
- `iInterval`: Интервал, соответствующий участку кривой, длина которого ищется
- `iTolerance`: Точность вычисления длины кривой
- `oLength`: Вычисленная длина кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindLength(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.FindLength(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить длину кривой

Parameters:
- `iContext`: Контекст геометрии
- `iTolerance`: Точность вычисления длины кривой
- `oLength`: Вычисленная длина кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindNearestPoint(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*,RGPlatform.Geometry.Point2D*)`

ID: `M:RGPlatform.Geometry.Spline2D.FindNearestPoint(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*,RGPlatform.Geometry.Point2D*)`

Получить параметр точки на кривой, ближайшей к передаваемой точке

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, для которой ищется ближайшая точка на кривой
- `iTolerance`: Точность, с которой ищется ближайшая точка
- `oParam`: Найденный параметр ближайшей точки на кривой
- `oPoint`: Найденная точка на кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindSelfIntersections(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Curve2DSelfIntersectionData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DIntersectionReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.FindSelfIntersections(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Curve2DSelfIntersectionData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DIntersectionReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Найти самопересечения кривой

Parameters:
- `iContext`: Контекст геометрии
- `iData`: Данные для пересечения
- `oReport`: Результат поиска самопересечений

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetControlPoint(System.Int32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetControlPoint(System.Int32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить управляющую точку с указанным индексом

Parameters:
- `iIndex`: Индекс точки
- `oPoint`: Управляющая точка с указанным индексом

### `GetControlPoints(std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetControlPoints(std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить массив управляющих точек

Parameters:
- `oControlPoints`: Массив управляющих точек

### `GetDegree`

ID: `M:RGPlatform.Geometry.Spline2D.GetDegree`

Получить степень сплайн-кривой

Returns: Степень сплайн-кривой

### `GetDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение расстояния от точки до объекта

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `oDistance`: Расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetDistanceWithClipping(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetDistanceWithClipping(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение расстояния от точки до кривой с заданной обрезкой

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `iClipInteval`: Интервал, задающий обрезку
- `oDistance`: Расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetEndParameter(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Spline2D.GetEndParameter(RGPlatform.Geometry.Context*)`

Вычислить конечный параметр кривой

Parameters:
- `iContext`: Контекст геометрии

Returns: Конечный параметр кривой

### `GetEndPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetEndPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить конечную точку кривой

Parameters:
- `oPoint`: Конечная точка кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetKnot(System.Int32)`

ID: `M:RGPlatform.Geometry.Spline2D.GetKnot(System.Int32)`

Получить узел с указанным индексом

Parameters:
- `iIndex`: Индекс узла

Returns: Узел с указанным индексом

### `GetKnots`

ID: `M:RGPlatform.Geometry.Spline2D.GetKnots`

Получить массив узлов

Returns: Массив узлов

### `GetNumberOfKnots`

ID: `M:RGPlatform.Geometry.Spline2D.GetNumberOfKnots`

Получить количество узловых значений

Returns: Количество узловых значений

### `GetNumberOfPoints`

ID: `M:RGPlatform.Geometry.Spline2D.GetNumberOfPoints`

Получить количество управляющих точек

Returns: Количество управляющих точек

### `GetRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение ограничивающего прямоугольника

Parameters:
- `iContext`: Контекст геометрии
- `oRect`: Вычисленный ограничивающий прямоугольник

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetRectangleWithClipping(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetRectangleWithClipping(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить ограничивающий прямоугольник с заданной обрезкой

Parameters:
- `iContext`: Контекст геометрии
- `iClipInteval`: Интервал, задающий обрезку
- `oRect`: Вычисленный ограничивающий прямоугольник

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetStartParameter(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Spline2D.GetStartParameter(RGPlatform.Geometry.Context*)`

Вычислить начальный параметр кривой

Parameters:
- `iContext`: Контекст геометрии

Returns: Начальный параметр кривой

### `GetStartPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.GetStartPoint(RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить начальную точку кривой

Parameters:
- `oPoint`: Начальная точка кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetType`

ID: `M:RGPlatform.Geometry.Spline2D.GetType`

Получить тип геометрии

Returns: Тип геометрии

### `GetWeight(System.Int32)`

ID: `M:RGPlatform.Geometry.Spline2D.GetWeight(System.Int32)`

Получить вес управляющей точки с указанным индексом

Parameters:
- `iIndex`: Индекс точки

Returns: Вес точки с указанным индексом

### `GetWeights`

ID: `M:RGPlatform.Geometry.Spline2D.GetWeights`

Получить массив весов

Returns: Массив весов

### `Initialize(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean)`

ID: `M:RGPlatform.Geometry.Spline2D.Initialize(RGPlatform.Geometry.Context*,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Boolean)`

Инициализировать двумерный сплайн по параметрам кривой, предназначен для использования в списках инициализации наследников

Parameters:
- `iContext`: Контекст геометрии
- `iPoints`: Массив управляющих точек кривой
- `iWeights`: Массив весов
- `iKnots`: Последовательность узлов
- `iDegree`: Степень кривой
- `iIsPeriodic`: Является ли кривая периодической
- `oResultCurve`: Созданная двумерная сплайн-кривая

### `InsertMultipleKnots(RGPlatform.Geometry.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.InsertMultipleKnots(RGPlatform.Geometry.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Вставка набора уникальных узлов с заданными кратностями

Parameters:
- `iContext`: Контекст вычисления
- `iInsertingKnots`: Набор узлов для вставки
- `iMultiplicities`: Кратности вставляемых узлов
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `IsBezier`

ID: `M:RGPlatform.Geometry.Spline2D.IsBezier`

Определить, является ли кривая кривой Безье

Returns: - true - кривая является кривой Безье - false - кривая не является кривой Безье

### `IsClosed`

ID: `M:RGPlatform.Geometry.Spline2D.IsClosed`

Проверить, является ли кривая замкнутой

Returns: true - кривая является замкнутой, false - кривая не является замкнутой

### `IsLeftClamped(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Spline2D.IsLeftClamped(RGPlatform.Geometry.Context*)`

Проверить, является ли кривая зажатой (clamped) слева

Parameters:
- `iContext`: Контекст геометрии

Returns: true - является, false - иначе

### `IsNonRational`

ID: `M:RGPlatform.Geometry.Spline2D.IsNonRational`

Определить, является ли кривая нерациональной

Returns: - true - кривая нерациональная - false - кривая рациональная

### `IsPeriodic`

ID: `M:RGPlatform.Geometry.Spline2D.IsPeriodic`

Определить, является ли кривая периодической

Returns: - true - кривая периодическая - false - кривая непериодическая

### `IsRightClamped(RGPlatform.Geometry.Context*)`

ID: `M:RGPlatform.Geometry.Spline2D.IsRightClamped(RGPlatform.Geometry.Context*)`

Проверить, является ли кривая зажатой (clamped) справа

Parameters:
- `iContext`: Контекст геометрии

Returns: true - является, false - иначе

### `IsValid`

ID: `M:RGPlatform.Geometry.Spline2D.IsValid`

Проверить, что кривая не вырождена

Returns: - true - кривая была задана - false - кривая не задана

### `MakeBezier(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.MakeBezier(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конвертация двумерной сплайн-кривой в кривую Безье

Parameters:
- `iContext`: Контекст геометрии
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `MakeBezier(RGPlatform.Geometry.Context*,System.Boolean,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.MakeBezier(RGPlatform.Geometry.Context*,System.Boolean,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конвертация двумерной сплайн-кривой в кривую Безье

Parameters:
- `iContext`: Контекст геометрии
- `iType`: true - RGP тип, false - Parasolid
- `oControlPolygon`: Контрольный полигон безье кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `ModifyControlPoint(RGPlatform.Geometry.Context*,System.Int32,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ModifyControlPoint(RGPlatform.Geometry.Context*,System.Int32,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать новую двумерную сплайн-кривую, изменив значение одной управляющей точки

Parameters:
- `iContext`: Контекст геометрии
- `iIndex`: Индекс управляющей точки
- `iPoint`: Новое значение управляющей точки
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `ModifyWeight(RGPlatform.Geometry.Context*,System.Int32,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ModifyWeight(RGPlatform.Geometry.Context*,System.Int32,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать новую двумерную сплайн-кривую, изменив вес одной управляющей точки

Parameters:
- `iContext`: Контекст геометрии
- `iIndex`: Индекс управляющей точки
- `iWeight`: Новое значение веса
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `NormalizeKnots(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.NormalizeKnots(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать новую двумерную сплайн-кривую, перепараметризовав существующую с границами [0, 1]

Parameters:
- `iContext`: Контекст геометрии
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `OutputPoints(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.FacetParameters!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.OutputPoints(RGPlatform.Geometry.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Curve2DGeometry.FacetParameters!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

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

ID: `M:RGPlatform.Geometry.Spline2D.Parameterise(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

Определить параметр точки, лежащей на кривой

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка на кривой
- `ioParam`: Найденный параметр на кривой (на входе может содержать начальное приближение)
- `iUseGuess`: Использовать ли начальное приближение

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `ReduceDegree(RGPlatform.Geometry.Context*,System.Double!System.Runtime.CompilerServices.IsConst,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ReduceDegree(RGPlatform.Geometry.Context*,System.Double!System.Runtime.CompilerServices.IsConst,System.Int32,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Понижение степени сплайна

Parameters:
- `iContext`: Контекст геометрии
- `iTolerance`: Передаваемая точность
- `iTimes`: Порядок понижения степени
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `RefineKnots(RGPlatform.Geometry.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.RefineKnots(RGPlatform.Geometry.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать новую двумерную сплайн-кривую, заменяя вектор узловых значений новыми

Parameters:
- `iContext`: Контекст геометрии
- `iKnots`: Новый вектор узловых значений (должен содержать существующий вектор узлов)
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `RemoveKnots(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.RemoveKnots(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать новую двумерную сплайн-кривую, удалив все возможные узлы

Parameters:
- `iContext`: Контекст геометрии
- `iTolerance`: Погрешность, оценивается как iTolerance=dw_min/(1+|P|_max)
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Reparametrization(RGPlatform.Geometry.Context*,System.Double,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.Reparametrization(RGPlatform.Geometry.Context*,System.Double,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать новую двумерную сплайн-кривую, перепараметризовав существующую

Parameters:
- `iContext`: Контекст геометрии
- `iMin`: Новое значение нижней границы параметра
- `iMax`: Новое значение верхней границы параметра
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Reverse(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.Reverse(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Изменение порядка обхода узлов

Parameters:
- `iContext`: Контекст геометрии
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `ShiftKnots(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.ShiftKnots(RGPlatform.Geometry.Context*,System.Double,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать новую двумерную сплайн-кривую, добавив к значениям узлов одно и то же число

Parameters:
- `iContext`: Контекст геометрии
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Transform(RGPlatform.Geometry.Context*,RGPlatform.Geometry.AffineMap2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.Transform(RGPlatform.Geometry.Context*,RGPlatform.Geometry.AffineMap2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать трансформированную копию объекта

Parameters:
- `iContext`: Контекст геометрии
- `iTransformation`: Трансформация

Returns: Трансформированная копия объекта

### `UnclampCurve(RGPlatform.Geometry.Context*,System.Boolean,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D.UnclampCurve(RGPlatform.Geometry.Context*,System.Boolean,System.Boolean,RGPlatform.Geometry.Spline2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Преобразование сжатой (clamped) кривой в несжатую (unclamped)

Parameters:
- `iContext`: Контекст геометрии
- `iFromLeft`: Обработка левой части кривой
- `iFromRight`: Обработка правой части кривой
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

Remarks: Для обработки обоих концов оба входных флага надо выставить в true.

### `_ConvertRGKParamToRGP(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Spline2D._ConvertRGKParamToRGP(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

## Fields

### `_rgkNURBS`

ID: `F:RGPlatform.Geometry.Spline2D._rgkNURBS`
