# TFlex.Model.Model3D.Geometry.LoftGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор лофтинга

## Constructors

### `LoftGenerator(TFlex.Model.Model3D.ProxyObject3D)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D)`

Конструктор для задания базовых объектов

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `LoftGenerator(TFlex.Model.Model3D.ProxyObject3D)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D)`

Конструктор для задания базовых объектов

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.Run`

Функция генерации сглаживания

### `SetClose(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetClose(System.Boolean)`

Функция задаёт замкнутось лофтинга в направлении V

Parameters:
- `cl`: Параметр замкнутости

### `SetCondType(TFlex.Model.Model3D.Geometry.TFBoundCondType,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetCondType(TFlex.Model.Model3D.Geometry.TFBoundCondType,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBody)`

Функция задаёт граничное условие в начале-конце лофтинга

Parameters:
- `t`: Тип граничного условия
- `isFirst`: Параметр отвечающий за то для какого профиля (первого или последнего) задано условие
- `sheet`: Тело с которого берётся граничное условие

### `SetFApex(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetFApex(TFlex.Model.Model3D.Geometry.Point3D)`

Функция устанавливает точку начала лофтинга в качестве первого профиля

Parameters:
- `p`: Точка в которой начинается лофтинг

### `SetFApexDir(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetFApexDir(TFlex.Model.Model3D.Geometry.Point3D)`

Функция устанавливает задающию нормаль к касательной плоскости вершинного лофтинга

Parameters:
- `p`: Точка в которую "смотрит" нормаль из начальной точки лофтинга

### `SetFirstBody(TFlex.Model.Model3D.Geometry.BaseBody,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetFirstBody(TFlex.Model.Model3D.Geometry.BaseBody,System.Double)`

Функция тело с которого берутся касательные для начального профиля

Parameters:
- `b`: Твёрдое тело с которого берутся касательные
- `sc`: Коэффициент масштабирования касательного вектора

### `SetFmodul(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetFmodul(System.Double)`

Функция устанавливает модуль касательных в начале лофтинга

Parameters:
- `m`: Модуль касательных в начале лофтинга

### `SetLastBody(TFlex.Model.Model3D.Geometry.BaseBody,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetLastBody(TFlex.Model.Model3D.Geometry.BaseBody,System.Double)`

Функция тело с которого берутся касательные для конечного профиля

Parameters:
- `b`: Твёрдое тело с которого берутся касательные
- `sc`: Коэффициент масштабирования касательного вектора

### `SetPath(TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetPath(TFlex.Model.Model3D.Geometry.BaseBody)`

Функция устанавливает "осевой" путь для выполнения лофтинга с путём

Parameters:
- `p`: Путь, который используется для вычисления траекторий точек лофтинга

### `SetProfileU(TFlex.Model.Model3D.Geometry.BaseBody,System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetProfileU(TFlex.Model.Model3D.Geometry.BaseBody,System.Int32,System.Boolean)`

Функция задаёт профиль в направлении U

Parameters:
- `prf`: Тело профиля (листовое тело или проволока)
- `num`: Номер профиля в списке
- `orient`: Ориентация с которой профиль входит в генератор

### `SetProfileV(TFlex.Model.Model3D.Geometry.BaseBody,System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetProfileV(TFlex.Model.Model3D.Geometry.BaseBody,System.Int32,System.Boolean)`

Функция задаёт профиль в направлении V

Parameters:
- `prf`: Тело профиля (листовое тело или проволока)
- `num`: Номер профиля в списке
- `orient`: Ориентация с которой профиль входит в генератор

### `SetSApex(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetSApex(TFlex.Model.Model3D.Geometry.Point3D)`

Функция устанавливает точку завершения лофтинга в качестве последнего профиля

Parameters:
- `p`: Точка которой заканчивается лофтинг

### `SetSApexDir(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetSApexDir(TFlex.Model.Model3D.Geometry.Point3D)`

Функция устанавливает задающию нормаль к касательной плоскости вершинного лофтинга

Parameters:
- `p`: Точка в которую "смотрит" нормаль из конечной точки лофтинга

### `SetSimpl(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetSimpl(System.Boolean)`

Функция задаёт режим упрощения результирующей геометрии

Parameters:
- `toset`: Параметр необходимости упрощения

### `SetSmodul(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetSmodul(System.Double)`

Функция устанавливает модуль касательных в конце лофтинга

Parameters:
- `m`: Модуль касательных в конце лофтинга

### `SetSyncVertex(TFlex.Model.Model3D.Geometry.BaseTopol,System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetSyncVertex(TFlex.Model.Model3D.Geometry.BaseTopol,System.Int32,System.Int32)`

Функция устанавливает вершину соответствия между профилями

Parameters:
- `vert`: Существующая вершина
- `nSyncPoint`: Порядковый номер
- `nProfile`: порядковый номер профиля к которому отностится вершина

### `SetThicken(System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetThicken(System.Double,System.Double)`

Функция задаёт величины отступов для создания оболочечного тела

Parameters:
- `FrontOffset`: Величина фронтального отступа в метрах
- `BackOffset`: Величина обратного отступа в метрах

### `SetTolerance(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetTolerance(System.Double)`

Функция задаёт точность аппроксимации

Parameters:
- `tolerance`: Величина допуска в метрах (не меньше 1e-9)

### `SetType(TFlex.Model.Model3D.Geometry.LoftType)`

ID: `M:TFlex.Model.Model3D.Geometry.LoftGenerator.SetType(TFlex.Model.Model3D.Geometry.LoftType)`

Функция задаёт тип лофтинга (линейчатый или сплайновый)

Parameters:
- `t`: Требуемый тип лофтинга
