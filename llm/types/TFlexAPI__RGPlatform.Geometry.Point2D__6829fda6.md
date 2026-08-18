# RGPlatform.Geometry.Point2D

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry`

## Summary

Двумерная точка

## Constructors

### `Point2D`

ID: `M:RGPlatform.Geometry.Point2D.#ctor`

Конструктор по умолчанию

### `Point2D(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.#ctor(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор копирования

Parameters:
- `iOther`: Вторая точка

### `Point2D(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.#ctor(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по размеру

Parameters:
- `iSize`: Размер, по которому строится точка

### `Point2D(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.#ctor(System.Double,System.Double)`

Конструктор по координатам

Parameters:
- `iX`: X-координата
- `iY`: Y-координата

## Methods

### `Point2D`

ID: `M:RGPlatform.Geometry.Point2D.#ctor`

Конструктор по умолчанию

### `Point2D(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.#ctor(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор копирования

Parameters:
- `iOther`: Вторая точка

### `Point2D(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.#ctor(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по размеру

Parameters:
- `iSize`: Размер, по которому строится точка

### `Point2D(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.#ctor(System.Double,System.Double)`

Конструктор по координатам

Parameters:
- `iX`: X-координата
- `iY`: Y-координата

### `Angle`

ID: `M:RGPlatform.Geometry.Point2D.Angle`

Получить угол радиус-вектора точки относительно оси X

Returns: Угол радиус-вектора точки относительно оси X

### `ConvertToRGK`

ID: `M:RGPlatform.Geometry.Point2D.ConvertToRGK`

Преобразовать данную точку в RGK-точку

Returns: Вычисленная RGK-точка

### `CreateSizeByDifference(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.CreateSizeByDifference(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать размер по разности точек

Parameters:
- `iPoint1`: Уменьшаемая точка
- `iPoint2`: Вычитаемая точка

Returns: Размер - результат вычитания

### `CreateSymmetricPoint(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Line2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.CreateSymmetricPoint(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Line2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Для заданной двумерной точки создать симметричную относительно заданной оси

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Заданная точка, для которой строится симметричная
- `iAxis`: Ось симметрии
- `oResultPoint`: Результат

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Dispose`

ID: `M:RGPlatform.Geometry.Point2D.Dispose`

### `DistanceTo(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.DistanceTo(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить расстояние до точки

Parameters:
- `iOther`: Точка, до которой вычисляется расстояние

Returns: Расстояние до точки

### `DistanceTo2(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.DistanceTo2(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить квадрат расстояния до точки

Parameters:
- `iOther`: Точка, до которой вычисляется квадрат расстояния

Returns: Квадрат расстояния до точки

### `EstimateDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.EstimateDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оценка расстояния от точки до объекта

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `oExact`: Флаг, определяющий является ли вычисленное приближённое расстояние точным
- `oDistance`: Приближённое расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetAngle(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.GetAngle(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение угла между векторами

Parameters:
- `iOther`: Вектор, до которого нужно посчитать угол

Returns: Значение угла между векторами в радианах

### `GetDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.GetDistance(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение расстояния от точки до объекта

Parameters:
- `iContext`: Контекст геометрии
- `iPoint`: Точка, до которой вычисляется расстояние
- `oDistance`: Расстояние от точки до объекта

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `GetRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.GetRectangle(RGPlatform.Geometry.Context*,RGPlatform.Geometry.Rectangle2D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получение ограничивающего прямоугольника

Parameters:
- `iContext`: Контекст геометрии
- `oRect`: Вычисленный ограничивающий прямоугольник

Returns: RGK::Common::Success - в случае успеха, код ошибки - иначе

### `Hypot`

ID: `M:RGPlatform.Geometry.Point2D.Hypot`

Получить расстояние до точки (0,0)

Returns: Расстояние до точки (0,0)

### `Hypot2`

ID: `M:RGPlatform.Geometry.Point2D.Hypot2`

Получить квадрат расстояния до точки (0,0)

Returns: Квадрат расстояния до точки (0,0)

### `IsCollinear(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.IsCollinear(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Проверка, что два вектора коллиниарны

Parameters:
- `iOther`: Второй вектор, с которым проверяется коллиниарность
- `iPrecision`: Угловая точность

Returns: true - если векторы коллиниарны, false - иначе

### `Normalize`

ID: `M:RGPlatform.Geometry.Point2D.Normalize`

Нормировать вектор, заданный точкой, до единичной длины

### `Normalized`

ID: `M:RGPlatform.Geometry.Point2D.Normalized`

Получить вектор, заданный точкой, нормированный до единичной длины

Returns: Вектор, заданный точкой, нормированный до единичной длины

### `Offset(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.Offset(System.Double,System.Double)`

Переместить точку на заданные приращения по осям

Parameters:
- `iDx`: Смещение по X
- `iDy`: Смещение по Y

Returns: Ссылка на себя

### `OffsetBy(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.OffsetBy(System.Double,System.Double)`

Получить точку смещением на заданные приращения по осям

Parameters:
- `iDx`: Смещение по X
- `iDy`: Смещение по Y

Returns: Новая точка - результат смещения

### `PsscalarProd(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.PsscalarProd(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить псевдоскалярное произведение векторов, заданных двумя точками

Parameters:
- `iPt1`: Первая точка, задающая радиус-вектор
- `iPt2`: Вторая точка, задающая радиус-вектор

Returns: Псевдоскалярное произведение

### `ScalarProd(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.ScalarProd(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить скалярное произведение векторов, заданных двумя точками

Parameters:
- `iPt1`: Первая точка, задающая радиус-вектор
- `iPt2`: Вторая точка, задающая радиус-вектор

Returns: Скалярное произведение

### `Set(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.Set(System.Double,System.Double)`

Установить координаты

Parameters:
- `iX`: X-координата
- `iY`: Y-координата

### `SetNull`

ID: `M:RGPlatform.Geometry.Point2D.SetNull`

Установить нулевые координаты

### `TransformPoint(RGPlatform.Geometry.AffineMap2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.TransformPoint(RGPlatform.Geometry.AffineMap2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создать трансформированную копию точки

### `Turned90(System.Boolean)`

ID: `M:RGPlatform.Geometry.Point2D.Turned90(System.Boolean)`

Получить точку, полученную поворотом относительно точки (0,0), на 90 градусов

Parameters:
- `iCCW`: true - поворот осуществляется против часовой стрелки, false - по часовой стрелке

Returns: Новая точка, полученная поворотом относительно точки (0,0), на 90 градусов

### `X`

ID: `M:RGPlatform.Geometry.Point2D.X`

Получить координату X

Returns: X-координата точки

### `XRef`

ID: `M:RGPlatform.Geometry.Point2D.XRef`

Получить ссылку на координату X

Returns: Ссылка на X-координату точки

### `Y`

ID: `M:RGPlatform.Geometry.Point2D.Y`

Получить координату Y

Returns: Y-координата точки

### `YRef`

ID: `M:RGPlatform.Geometry.Point2D.YRef`

Получить ссылку на координату Y

Returns: Ссылка на Y-координату точки

### `op_Addition(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_Addition(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор сложения

Parameters:
- `iPoint`: Прибавляемая точка

Returns: Новая точка - результат сложения

### `op_Addition(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_Addition(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор сложения

Parameters:
- `iSize`: Прибавляемый размер

Returns: Новая точка - результат сложения

### `op_AdditionAssignment(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_AdditionAssignment(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор сложения

Parameters:
- `iPoint`: Прибавляемая точка

Returns: Ссылка на себя

### `op_AdditionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_AdditionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор сложения

Parameters:
- `iSize`: Прибавляемый размер

Returns: Ссылка на себя

### `op_Division(System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.op_Division(System.Double)`

Получить точку делением (масштабированием)

Parameters:
- `iD`: Коэффициент масштабирования

Returns: Новая точка - результат масштабирования

### `op_DivisionAssignment(System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.op_DivisionAssignment(System.Double)`

Оператор деления (масштабирования)

Parameters:
- `iD`: Коэффициент масштабирования

Returns: Ссылка на себя

### `op_Equality(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_Equality(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "=="

Parameters:
- `iOther`: Точка, с которой сравнивается данная

Returns: true - равны, false - не равны

### `op_Inequality(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_Inequality(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "!="

Parameters:
- `iOther`: Точка, с которой сравнивается данная

Returns: true - не равны, false - равны

### `op_MultiplicationAssignment(System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.op_MultiplicationAssignment(System.Double)`

Оператор умножения (масштабирования)

Parameters:
- `iD`: Коэффициент масштабирования

Returns: Ссылка на себя

### `op_Multiply(System.Double)`

ID: `M:RGPlatform.Geometry.Point2D.op_Multiply(System.Double)`

Получить точку умножением (масштабированием)

Parameters:
- `iD`: Коэффициент масштабирования

Returns: Новая точка - результат масштабирования

### `op_Subtraction(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_Subtraction(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор вычитания

Parameters:
- `iPoint`: Вычитаемая точка

Returns: Новая точка - результат вычитания

### `op_Subtraction(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_Subtraction(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор вычитания

Parameters:
- `iSize`: Вычитаемый размер

Returns: Новая точка - результат вычитания

### `op_SubtractionAssignment(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_SubtractionAssignment(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор вычитания

Parameters:
- `iPoint`: Вычитаемая точка

Returns: Ссылка на себя

### `op_SubtractionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Point2D.op_SubtractionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор вычитания

Parameters:
- `iSize`: Вычитаемый размер

Returns: Ссылка на себя

### `op_UnaryNegation`

ID: `M:RGPlatform.Geometry.Point2D.op_UnaryNegation`

Оператор вычисления точки с противоположными координатами

Returns: Новая точка, симметричная данной относительно (0,0)
