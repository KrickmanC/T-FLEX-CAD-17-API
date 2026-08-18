# RGPlatform.Geometry.BaseSpline2D

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry`

## Summary

Абстракстный двумерный сплайн

## Constructors

### `BaseSpline2D`

ID: `M:RGPlatform.Geometry.BaseSpline2D.#ctor`

Конструктор по умолчанию

## Methods

### `BaseSpline2D`

ID: `M:RGPlatform.Geometry.BaseSpline2D.#ctor`

Конструктор по умолчанию

### `AsBaseSpline2D`

ID: `M:RGPlatform.Geometry.BaseSpline2D.AsBaseSpline2D`

Получить геометрию как двумерный сплайн

Returns: Указатель на данный объект двумерного сплайна

### `EstimateRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.EstimateRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оценить ограничивающий прямоугольник

Parameters:
- `iContext`: Контекст геометрии
- `oRect`: Вычисленная оценка ограничивающего прямоугольника

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `FindArea(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.FindArea(RGPlatform.Geometry.Context*,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить площадь которую огрничивает кривая

Parameters:
- `iTolerance`: Точность вычисления
- `oArea`: Площадь
- `oHasArea`: Признак наличия площади

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetControlPoint(System.Int32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetControlPoint(System.Int32,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить управляющую точку с указанным индексом

Parameters:
- `iIndex`: Индекс точки
- `oPoint`: Управляющая точка с указанным индексом

### `GetControlPoints(std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetControlPoints(std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить массив управляющих точек

Parameters:
- `oControlPoints`: Массив управляющих точек

### `GetDegree`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetDegree`

Получить степень сплайн-кривой

Returns: Степень сплайн-кривой

### `GetKnot(System.Int32)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetKnot(System.Int32)`

Получить узел с указанным индексом

Parameters:
- `iIndex`: Индекс узла

Returns: Узел с указанным индексом

### `GetKnots`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetKnots`

Получить массив узлов

Returns: Массив узлов

### `GetNumberOfKnots`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetNumberOfKnots`

Получить количество узловых значений

Returns: Количество узловых значений

### `GetNumberOfPoints`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetNumberOfPoints`

Получить количество управляющих точек

Returns: Количество управляющих точек

### `GetType`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetType`

Получить тип геометрии

Returns: Тип геометрии

### `GetWeight(System.Int32)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetWeight(System.Int32)`

Получить вес управляющей точки с указанным индексом

Parameters:
- `iIndex`: Индекс точки

Returns: Вес точки с указанным индексом

### `GetWeights`

ID: `M:RGPlatform.Geometry.BaseSpline2D.GetWeights`

Получить массив весов

Returns: Массив весов

### `IsBezier`

ID: `M:RGPlatform.Geometry.BaseSpline2D.IsBezier`

Определить, является ли кривая кривой Безье

Returns: - true - кривая является кривой Безье - false - кривая не является кривой Безье

### `IsNonRational`

ID: `M:RGPlatform.Geometry.BaseSpline2D.IsNonRational`

Определить, является ли кривая нерациональной

Returns: - true - кривая нерациональная - false - кривая рациональная

### `MakeBezier(RGPlatform.Geometry.Context*,System.Boolean,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.MakeBezier(RGPlatform.Geometry.Context*,System.Boolean,std.vector<RGPlatform.Geometry.Point2D,std.allocator<RGPlatform.Geometry.Point2D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конвертация двумерной сплайн-кривой в кривую Безье

Parameters:
- `iContext`: Контекст геометрии
- `iType`: true - RGP тип, false - Parasolid
- `oControlPolygon`: Контрольный полигон безье кривой

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `MakeBezier(RGPlatform.Geometry.Context*,std.shared_ptr<RGPlatform.Geometry.BaseSpline2D>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.BaseSpline2D.MakeBezier(RGPlatform.Geometry.Context*,std.shared_ptr<RGPlatform.Geometry.BaseSpline2D>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конвертация двумерной сплайн-кривой в кривую Безье

Parameters:
- `iContext`: Контекст геометрии
- `oResultCurve`: Созданная двумерная сплайн-кривая

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе
