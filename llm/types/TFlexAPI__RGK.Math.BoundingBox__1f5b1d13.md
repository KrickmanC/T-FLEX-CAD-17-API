# RGK.Math.BoundingBox

Assembly: `TFlexAPI`
Namespace: `RGK.Math`

## Summary

Класс ограничивающего параллелепипеда в трёхмерном пространстве, имеющий точки начала и конца, а также ребра, параллельные осям координат

## Constructors

### `BoundingBox`

ID: `M:RGK.Math.BoundingBox.#ctor`

Конструктор по умолчанию - создаёт вырожденный ограничивающий параллелепипед Границы такого параллелепипеда не определены

### `BoundingBox(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор для одной точки iPoint - создаёт вырожденный ограничивающий параллелепипед с точкой iPoint в качестве начала и конца, который ограничивает только эту точку

Parameters:
- `iPoint`: Точка, определяющая ограничивающий параллелепипед

### `BoundingBox(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по значениям начала (iMinBound) и конца (iMaxBound)

Parameters:
- `iMinBound`: Начало ограничивающего параллелепипеда
- `iMaxBound`: Конец ограничивающего параллелепипеда

### `BoundingBox(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.BoundingBox.#ctor(System.Double!System.Runtime.CompilerServices.IsConst*)`

Конструктор по массиву значений

Parameters:
- `iValues`: Массив 6 значений [Xmin, ..., Zmax]

### `BoundingBox(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.BoundingBox.#ctor(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

Конструктор по значениям

Parameters:
- `iMinX`: Минимальный размер вдоль первой оси
- `iMinY`: Минимальный размер вдоль второй оси
- `iMinZ`: Минимальный размер вдоль третье оси
- `iMaxX`: Максимальный размер вдоль первой оси
- `iMaxY`: Максимальный размер вдоль второй оси
- `iMaxZ`: Максимальный размер вдоль третье оси

## Methods

### `BoundingBox`

ID: `M:RGK.Math.BoundingBox.#ctor`

Конструктор по умолчанию - создаёт вырожденный ограничивающий параллелепипед Границы такого параллелепипеда не определены

### `BoundingBox(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор для одной точки iPoint - создаёт вырожденный ограничивающий параллелепипед с точкой iPoint в качестве начала и конца, который ограничивает только эту точку

Parameters:
- `iPoint`: Точка, определяющая ограничивающий параллелепипед

### `BoundingBox(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по значениям начала (iMinBound) и конца (iMaxBound)

Parameters:
- `iMinBound`: Начало ограничивающего параллелепипеда
- `iMaxBound`: Конец ограничивающего параллелепипеда

### `BoundingBox(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.BoundingBox.#ctor(System.Double!System.Runtime.CompilerServices.IsConst*)`

Конструктор по массиву значений

Parameters:
- `iValues`: Массив 6 значений [Xmin, ..., Zmax]

### `BoundingBox(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.BoundingBox.#ctor(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

Конструктор по значениям

Parameters:
- `iMinX`: Минимальный размер вдоль первой оси
- `iMinY`: Минимальный размер вдоль второй оси
- `iMinZ`: Минимальный размер вдоль третье оси
- `iMaxX`: Максимальный размер вдоль первой оси
- `iMaxY`: Максимальный размер вдоль второй оси
- `iMaxZ`: Максимальный размер вдоль третье оси

### `Contains(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Contains(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Проверить, содержится ли ограничивающий параллелепипед iBox в данном ограничивающем параллелепипеде

Parameters:
- `iBox`: ограничивающий параллелепипед для проверки принадлежности данному ограничивающему параллелепипеду

Returns: - true, если содержится - false, если не содержится

### `Contains(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

ID: `M:RGK.Math.BoundingBox.Contains(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

Проверить, содержится ли ограничивающий параллелепипед iBox в данном ограничивающем параллелепипеде, используя параметры контекста iContext

Parameters:
- `iBox`: ограничивающий параллелепипед для проверки принадлежности данному ограничивающему параллелепипеду
- `iContext`: Контекст вычислений

Returns: - true, если содержится - false, если не содержится

### `Contains(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.BoundingBox.Contains(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Проверить, содержится ли ограничивающий параллелепипед iBox в данном ограничивающем параллелепипеде, используя точность iTolerance

Parameters:
- `iBox`: ограничивающий параллелепипед для проверки принадлежности данному ограничивающему параллелепипеду
- `iTolerance`: Используемая точность

Returns: - true, если содержится - false, если не содержится

### `Contains(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Contains(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Проверить, содержит ли данный ограничивающий параллелепипед точку iPoint

Parameters:
- `iPoint`: Точка для проверки принадлежности данному ограничивающему параллелепипеду

Returns: - true, если содержит - false, если не содержит

### `Contains(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

ID: `M:RGK.Math.BoundingBox.Contains(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

Проверить, содержит ли данный ограничивающий параллелепипед точку iPoint, используя параметры контекста iContext

Parameters:
- `iPoint`: Точка для проверки принадлежности данному ограничивающему параллелепипеду
- `iContext`: Контекст вычислений

Returns: - true, если содержит - false, если не содержит

### `Contains(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.BoundingBox.Contains(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Проверить, содержит ли данный ограничивающий параллелепипед точку iPoint, используя точность iTolerance

Parameters:
- `iPoint`: Точка для проверки принадлежности данному ограничивающему параллелепипеду
- `iTolerance`: Используемая точность

Returns: - true, если содержит - false, если не содержит

### `CreateByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.CreateByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создание ограничивающего параллелепипеда по двум заданным точкам

Parameters:
- `iPoint1`: Первая точка
- `iPoint2`: Вторая точка

Returns: Ограничивающий параллелепипед для заданных точек

### `CreateByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.CreateByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создание ограничивающего параллелепипеда по трём заданным точкам

Parameters:
- `iPoint1`: Первая точка
- `iPoint2`: Вторая точка
- `iPoint3`: Третья точка

Returns: Ограничивающий параллелепипед для заданных точек

### `CreateByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.CreateByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создание ограничивающего параллелепипеда по четырём заданным точкам

Parameters:
- `iPoint1`: Первая точка
- `iPoint2`: Вторая точка
- `iPoint3`: Третья точка
- `iPoint4`: Четвёртая точка

Returns: Ограничивающий параллелепипед для заданных точек

### `CreateByPoints(System.UInt64,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.BoundingBox.CreateByPoints(System.UInt64,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*)`

Создание ограничивающего параллелепипеда по заданным точкам

Parameters:
- `iPointsCount`: Количество точек
- `iPoints`: Набор точек

Returns: Ограничивающий параллелепипед для заданного набора точек

### `CreateSizeBox(RGK.Common.Context*)`

ID: `M:RGK.Math.BoundingBox.CreateSizeBox(RGK.Common.Context*)`

Создание ограничивающего параллелепипеда со сторонами, соответствующими максимально допустимым габаритам модели, полученным из контекста вычислений

Parameters:
- `iContext`: Контекст вычислений

Returns: Ограничивающий параллелепипед максимально допустимых габаритов модели

### `GetBoxData(System.Double*)`

ID: `M:RGK.Math.BoundingBox.GetBoxData(System.Double*)`

Поместить данные о BoundBox в массив (необходима для низкоуровневой работы). порядок следования данных такой: _min.x,y,z,_max.x,y,z

Parameters:
- `ioBoxData`: Массив, в который будут записаны данные

### `GetBoxData(System.Single*)`

ID: `M:RGK.Math.BoundingBox.GetBoxData(System.Single*)`

Поместить данные о BoundBox в массив (необходима для низкоуровневой работы). порядок следования данных такой: _min.x,y,z,_max.x,y,z

Parameters:
- `ioBoxData`: Массив, в который будут записаны данные

### `GetCenter`

ID: `M:RGK.Math.BoundingBox.GetCenter`

Получить середину ограничивающего параллелепипеда

Returns: Середина ограничивающего параллелепипеда

### `GetDiagonal`

ID: `M:RGK.Math.BoundingBox.GetDiagonal`

Получить диагональ ограничивающего параллелепипеда

Returns: Диагональ ограничивающего параллелепипеда

### `GetDistanceTo(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetDistanceTo(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить расстояние от заданного ограничивающего параллелепипеда до данного

Parameters:
- `iBox`: Заданный ограничивающий параллелепипед

Returns: Расстояние между ограничивающими параллелепипедами

### `GetDistanceTo(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetDistanceTo(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить расстояние от заданной точки до данного ограничивающего параллелепипеда

Parameters:
- `iPoint`: Заданная точка

Returns: Расстояние от точки до ограничивающего параллелепипеда

### `GetDistanceTo2(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetDistanceTo2(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить квадрат расстояния от заданного ограничивающего параллелепипеда до данного

Parameters:
- `iBox`: Заданный ограничивающий параллелепипед

Returns: Квадрат расстояния между ограничивающими параллелепипедами

### `GetDistanceTo2(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetDistanceTo2(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить квадрат расстояния от заданной точки до данного ограничивающего параллелепипеда

Parameters:
- `iPoint`: Заданная точка

Returns: Квадрат расстояния от точки до ограничивающего параллелепипеда

### `GetEdges(std.pair<RGK.Math.Vector3D,RGK.Math.Vector3D>*)`

ID: `M:RGK.Math.BoundingBox.GetEdges(std.pair<RGK.Math.Vector3D,RGK.Math.Vector3D>*)`

Получить все ребра данного ограничивающего параллелепипеда

Parameters:
- `oEdges`: Ребра данного ограничивающего параллелепипеда

### `GetEdges(std.vector<std.pair<RGK.Math.Vector3D,RGK.Math.Vector3D>,std.allocator<std.pair<RGK.Math.Vector3D,RGK.Math.Vector3D>>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetEdges(std.vector<std.pair<RGK.Math.Vector3D,RGK.Math.Vector3D>,std.allocator<std.pair<RGK.Math.Vector3D,RGK.Math.Vector3D>>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить все ребра данного ограничивающего параллелепипеда

Parameters:
- `oEdges`: Ребра данного ограничивающего параллелепипеда

### `GetMaxBound`

ID: `M:RGK.Math.BoundingBox.GetMaxBound`

Получить конец ограничивающего параллелепипеда

Returns: Конец ограничивающего параллелепипеда

### `GetMaxDistanceTo(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetMaxDistanceTo(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить максимальное расстояние от заданного ограничивающего параллелепипеда до данного

Parameters:
- `iBox`: Заданный ограничивающий параллелепипед

Returns: Максимальное расстояние между ограничивающими параллелепипедами

### `GetMaxDistanceTo(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetMaxDistanceTo(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить максимальное расстояние от заданной точки до данного ограничивающего параллелепипеда

Parameters:
- `iPoint`: Заданная точка

Returns: Максимальное расстояние от точки до ограничивающего параллелепипеда

### `GetMaxDistanceTo2(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetMaxDistanceTo2(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить квадрат максимального расстояния от заданного ограничивающего параллелепипеда до данного

Parameters:
- `iBox`: Заданный ограничивающий параллелепипед

Returns: Квадрат максимального расстояния между ограничивающими параллелепипедами

### `GetMaxDistanceTo2(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetMaxDistanceTo2(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить квадрат максимального расстояния от заданной точки до данного ограничивающего параллелепипеда

Parameters:
- `iPoint`: Заданная точка

Returns: Квадрат максимального расстояния от точки до ограничивающего параллелепипеда

### `GetMaxSize`

ID: `M:RGK.Math.BoundingBox.GetMaxSize`

Получить максимальную длину ограничивающего параллелепипеда вдоль осей

Returns: Максимальная длина ограничивающего параллелепипеда вдоль осей

### `GetMinBound`

ID: `M:RGK.Math.BoundingBox.GetMinBound`

Получить начало ограничивающего параллелепипеда

Returns: Начало ограничивающего параллелепипеда

### `GetMinNonZeroSize(System.Double)`

ID: `M:RGK.Math.BoundingBox.GetMinNonZeroSize(System.Double)`

Получить минимальную ненулевую длину ограничивающего параллелепипеда вдоль осей (если таковая существует)

Parameters:
- `iTolerance`: Линейная точность

Returns: Минимальная ненулевая длина ограничивающего параллелепипеда вдоль осей

### `GetMinSize`

ID: `M:RGK.Math.BoundingBox.GetMinSize`

Получить минимальную длину ограничивающего параллелепипеда вдоль осей

Returns: Минимальная длина ограничивающего параллелепипеда вдоль осей

### `GetNorm(System.Double,RGK.Math.BoundingBox.BoundingBoxNorm)`

ID: `M:RGK.Math.BoundingBox.GetNorm(System.Double,RGK.Math.BoundingBox.BoundingBoxNorm)`

Получить норму данного ограничивающего параллелепипеда (с округлением к нулю)

Parameters:
- `iTolerance`: Линейная точность
- `iNorm`: Используемая норма

Returns: Норма

### `GetSizeX`

ID: `M:RGK.Math.BoundingBox.GetSizeX`

Получить длину ограничивающего параллелепипеда вдоль оси X

Returns: Длина ограничивающего параллелепипеда вдоль оси X

### `GetSizeY`

ID: `M:RGK.Math.BoundingBox.GetSizeY`

Получить длину ограничивающего параллелепипеда вдоль оси Y

Returns: Длина ограничивающего параллелепипеда вдоль оси Y

### `GetSizeZ`

ID: `M:RGK.Math.BoundingBox.GetSizeZ`

Получить длину ограничивающего параллелепипеда вдоль оси Z

Returns: Длина ограничивающего параллелепипеда вдоль оси Z

### `GetSurfaceArea`

ID: `M:RGK.Math.BoundingBox.GetSurfaceArea`

Получить площадь поверхности данного ограничивающего параллелепипеда

Returns: Площадь поверхности

### `GetVertices(RGK.Math.Vector3D*)`

ID: `M:RGK.Math.BoundingBox.GetVertices(RGK.Math.Vector3D*)`

Получить все вершины данного ограничивающего параллелепипеда

Parameters:
- `oVertices`: Вершины данного ограничивающего параллелепипеда

### `GetVertices(std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.GetVertices(std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить все вершины данного ограничивающего параллелепипеда

Parameters:
- `oVertices`: Вершины данного ограничивающего параллелепипеда

### `GetVolume`

ID: `M:RGK.Math.BoundingBox.GetVolume`

Получить объём данного ограничивающего параллелепипеда

Returns: Объём

### `InitByPoint(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.InitByPoint(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Инициализация ограничивающего параллелепипеда по заданной точке

Parameters:
- `iPoint`: Точка

### `InitByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.InitByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Инициализация ограничивающего параллелепипеда по двум заданным точкам

Parameters:
- `iPoint1`: Первая точка
- `iPoint2`: Вторая точка

### `InitByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.InitByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Инициализация ограничивающего параллелепипеда по трём заданным точкам

Parameters:
- `iPoint1`: Первая точка
- `iPoint2`: Вторая точка
- `iPoint3`: Третья точка

### `InitByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.InitByPoints(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Инициализация ограничивающего параллелепипеда по четырём заданным точкам

Parameters:
- `iPoint1`: Первая точка
- `iPoint2`: Вторая точка
- `iPoint3`: Третья точка
- `iPoint4`: Четвёртая точка

### `Intersect(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Intersect(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Пересечение данного ограничивающего параллелепипеда с ограничивающим параллелепипедом iBox

Parameters:
- `iBox`: Интервал для пересечения

Returns: - true, если пересекаются - false, если не пересекаются

### `Intersect(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

ID: `M:RGK.Math.BoundingBox.Intersect(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

Пересечение данного ограничивающего параллелепипеда с ограничивающим параллелепипедом iBox, используя параметры контекста iContext

Parameters:
- `iBox`: Интервал для пересечения
- `iContext`: Контекст вычислений

Returns: - true, если пересекаются - false, если не пересекаются

### `Intersect(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.BoundingBox.Intersect(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Пересечение данного ограничивающего параллелепипеда с плоскостью

Parameters:
- `iPoint`: Точка на плоскости
- `iZAxis`: Ось Z системы координат
- `iTolerance`: Точность

Returns: - true, если пересекаются - false, если не пересекаются

### `Intersection(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Intersection(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Пересечение данного ограничивающего параллелепипеда и ограничивающего параллелепипеда iBox

Parameters:
- `iBox`: Ограничивающий параллелепипед для пересечения
- `oResult`: Выходной ограничивающий параллелепипед пересечения

Returns: - true, если пересекаются - false, если не пересекаются

### `Intersection(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

ID: `M:RGK.Math.BoundingBox.Intersection(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

Пересечение данного ограничивающего параллелепипеда и ограничивающего параллелепипеда iBox, используя параметры контекста iContext

Parameters:
- `iBox`: Ограничивающий параллелепипед для пересечения
- `oResult`: Выходной ограничивающий параллелепипед пересечения
- `iContext`: Контекст вычислений

Returns: - true, если пересекаются - false, если не пересекаются

### `Intersection(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.BoundingBox.Intersection(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Пересечение данного ограничивающего параллелепипеда и ограничивающего параллелепипеда iBox, используя точность iTolerance

Parameters:
- `iBox`: Ограничивающий параллелепипед для пересечения
- `oResult`: Выходной ограничивающий параллелепипед пересечения
- `iTolerance`: Используемая точность

Returns: - true, если пересекаются - false, если не пересекаются

### `Intersects(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Intersects(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Проверить, пересекается ли данный ограничивающий параллелепипед с ограничивающим параллелепипедом iBox

Parameters:
- `iBox`: Ограничивающий параллелепипед для проверки

Returns: - true, если пересекается - false, если не пересекается

### `Intersects(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

ID: `M:RGK.Math.BoundingBox.Intersects(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Common.Context*)`

Проверить, пересекается ли данный ограничивающий параллелепипед с ограничивающим параллелепипедом iBox, используя параметры контекста iContext

Parameters:
- `iBox`: Ограничивающий параллелепипед для проверки
- `iContext`: Контекст вычислений

Returns: - true, если пересекается - false, если не пересекается

### `Intersects(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.BoundingBox.Intersects(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Проверить, пересекается ли данный ограничивающий параллелепипед с ограничивающим параллелепипедом iBox, используя точность iTolerance

Parameters:
- `iBox`: Ограничивающий параллелепипед для проверки
- `iTolerance`: Используемая точность

Returns: - true, если пересекается - false, если не пересекается

### `IsEqual(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.BoundingBox.IsEqual(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Проверить, является ли данный ограничивающий параллелепипед равным ограничивающему параллелепипеду iBox, используя точность iTolerance

Parameters:
- `iBox`: Ограничивающий параллелепипед для проверки
- `iTolerance`: Порог равенства значений

Returns: - true, если равны - false, если не равны

### `IsInfinite`

ID: `M:RGK.Math.BoundingBox.IsInfinite`

Проверить, является ли данный ограничивающий параллелепипед бесконечным (хотя бы по одной оси)

Returns: - true, если является бесконечным - false, если не является бесконечным

### `IsInfiniteX`

ID: `M:RGK.Math.BoundingBox.IsInfiniteX`

Проверить, является ли данный ограничивающий параллелепипед бесконечным по оси X

Returns: - true, если является бесконечным по оси - false, если не является бесконечным по оси

### `IsInfiniteXYZ`

ID: `M:RGK.Math.BoundingBox.IsInfiniteXYZ`

Проверить, является ли данный ограничивающий параллелепипед бесконечным по всем осям

Returns: - true, если является бесконечным - false, если не является бесконечным

### `IsInfiniteY`

ID: `M:RGK.Math.BoundingBox.IsInfiniteY`

Проверить, является ли данный ограничивающий параллелепипед бесконечным по оси Y

Returns: - true, если является бесконечным по оси - false, если не является бесконечным по оси

### `IsInfiniteZ`

ID: `M:RGK.Math.BoundingBox.IsInfiniteZ`

Проверить, является ли данный ограничивающий параллелепипед бесконечным по оси Z

Returns: - true, если является бесконечным по оси - false, если не является бесконечным по оси

### `IsNull(System.Double,RGK.Math.BoundingBox.BoundingBoxNorm)`

ID: `M:RGK.Math.BoundingBox.IsNull(System.Double,RGK.Math.BoundingBox.BoundingBoxNorm)`

Проверить, является ли данный ограничивающий параллелепипед вырожденным по норме (т.е. его норма не превосходит заданный порог)

Parameters:
- `iTolerance`: Порог равенства нулю
- `iNorm`: Используемая норма

Returns: - true, если является вырожденным - false, если не является вырожденным

### `IsVacuous`

ID: `M:RGK.Math.BoundingBox.IsVacuous`

Проверка на вырожденность, когда хотя бы одна из границ не определена

Returns: - true, если является вырожденным - false, если не является вырожденным

### `IsValid`

ID: `M:RGK.Math.BoundingBox.IsValid`

Проверка на корректность данного ограничивающего параллелепипеда

Returns: - true, если является корректным - false, если не является корректным

### `Mapping(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Mapping(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить ограничивающий параллелепипед, после применения операции аффинного преобразования

Parameters:
- `iMap`: Аффинное преобразование

Returns: Новый ограничивающий параллелепипед

### `Offset(System.Double)`

ID: `M:RGK.Math.BoundingBox.Offset(System.Double)`

Отступ от текущих размеров данного ограничивающего параллелепипеда на величину iOffset во всех направлениях

Parameters:
- `iOffset`: Значение отступа

Returns: Ссылка на данный ограничивающий параллелепипед

### `Offsetted(System.Double)`

ID: `M:RGK.Math.BoundingBox.Offsetted(System.Double)`

Получить ограничивающий параллелепипед отступа от данного на величину iOffset во всех направлениях

Parameters:
- `iOffset`: Значение отступа

Returns: Ограничивающий параллелепипед отступа

### `Scale(System.Double)`

ID: `M:RGK.Math.BoundingBox.Scale(System.Double)`

Изменить размеры ограничивающего параллелепипеда в iScaleFactor раз, не меняя его центр

Parameters:
- `iScaleFactor`: Значение коэффициента масштабирования

Returns: Ссылка на данный ограничивающий параллелепипед

### `Scaled(System.Double)`

ID: `M:RGK.Math.BoundingBox.Scaled(System.Double)`

Получить в iScaleFactor раз масштабированный ограничивающий параллелепипед с тем же центром

Parameters:
- `iScaleFactor`: Значение коэффициента масштабирования

Returns: Масштабированный ограничивающий параллелепипед

### `SelfMapping(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.SelfMapping(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить ограничивающий параллелепипед, после применения операции аффинного преобразования

Parameters:
- `iMap`: Аффинное преобразование

### `SelfMove(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.SelfMove(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Перемещение ограничивающего параллелепипеда на заданный вектор

Parameters:
- `iVector`: Вектор, задающий перемещение

### `SetBounds(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.SetBounds(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить значения начала и конца ограничивающего параллелепипеда равными iMinBound и iMaxBound соответственно

Parameters:
- `iMinBound`: Новое значение начала ограничивающего параллелепипеда
- `iMaxBound`: Новое значение конца ограничивающего параллелепипеда

### `SetCenter(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.SetCenter(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Переместить центр ограничивающего параллелепипеда в точку iCenter, не меняя его размеры

Parameters:
- `iCenter`: Новое значение центра ограничивающего параллелепипеда

### `SetDiagonal(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.SetDiagonal(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Изменить размеры ограничивающего параллелепипеда, не меняя его центр

Parameters:
- `iDiagonal`: Новое значение диагонали (вектора размеров вдоль осей) ограничивающего параллелепипеда

### `SetMaxBound(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.SetMaxBound(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить значение конца ограничивающего параллелепипеда равным iMaxBound

Parameters:
- `iMaxBound`: Новое значение конца ограничивающего параллелепипеда

### `SetMinBound(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.SetMinBound(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить значение начала ограничивающего параллелепипеда равным iMinBound

Parameters:
- `iMinBound`: Новое значение начала ограничивающего параллелепипеда

### `Union(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Union(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Объединение данного ограничивающего параллелепипеда и ограничивающего параллелепипеда iBox

Parameters:
- `iBox`: Ограничивающий параллелепипед для объединения

Returns: Ограничивающий параллелепипед объединения

### `Union(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Union(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Объединение данного ограничивающего параллелепипеда и точки iPoint

Parameters:
- `iPoint`: Точка для объединения

Returns: Ограничивающий параллелепипед объединения

### `Unite(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Unite(RGK.Math.BoundingBox!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Объединение данного ограничивающего параллелепипеда с ограничивающим параллелепипедом iBox

Parameters:
- `iBox`: Ограничивающий параллелепипед для объединения

Returns: Ссылка на данный ограничивающий параллелепипед

### `Unite(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.BoundingBox.Unite(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Объединение данного ограничивающего параллелепипеда с точкой iPoint

Parameters:
- `iPoint`: Точка для объединения

Returns: Ссылка на данный ограничивающий параллелепипед

### `op_FunctionCall(System.Boolean,System.Int32)`

ID: `M:RGK.Math.BoundingBox.op_FunctionCall(System.Boolean,System.Int32)`

Получить координату минимума или максимума вдоль соответствующей оси

Parameters:
- `iMin`: Минимум (true) или максимум (false)
- `iCoord`: Необходимая координата

Returns: Искомая координата

### `op_Subscript(System.Boolean)`

ID: `M:RGK.Math.BoundingBox.op_Subscript(System.Boolean)`

Получить минимум или максимум ограничивающего параллелепипеда

Parameters:
- `iMin`: Минимум (true) или максимум (false)

Returns: Искомая точка
