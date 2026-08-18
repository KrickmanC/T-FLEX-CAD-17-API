# RGPlatform.Geometry.Curve2DGeometry.FacetParameters

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry.Curve2DGeometry`

## Summary

Класс параметров для построения сетки точек на кривой

## Constructors

### `FacetParameters(System.Double,System.Double,System.Double,System.Boolean)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FacetParameters.#ctor(System.Double,System.Double,System.Double,System.Boolean)`

Конструктор

Parameters:
- `iChordalTolerance`: Максимальное расстояние между кривой и хордой
- `iAngularTolerance`: Максимально допустимое угловое уклонение
- `iChordalMaximumLength`: Максимально допустимая длина хорды
- `iGeneral`: Использовать общий алгоритм разбиения

## Methods

### `FacetParameters(System.Double,System.Double,System.Double,System.Boolean)`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FacetParameters.#ctor(System.Double,System.Double,System.Double,System.Boolean)`

Конструктор

Parameters:
- `iChordalTolerance`: Максимальное расстояние между кривой и хордой
- `iAngularTolerance`: Максимально допустимое угловое уклонение
- `iChordalMaximumLength`: Максимально допустимая длина хорды
- `iGeneral`: Использовать общий алгоритм разбиения

### `ConvertToRGK`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FacetParameters.ConvertToRGK`

Преобразовать объект в RGK-представление

Returns: Вычисленное RGK-представление

### `GetAngularTolerance`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FacetParameters.GetAngularTolerance`

Получить максимально допустимое угловое уклонение

Returns: Максимально допустимое угловое уклонение

### `GetChordalMaximumLength`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FacetParameters.GetChordalMaximumLength`

Получить максимально допустимую длину хорды

Returns: Максимально допустимая длина хорды

### `GetChordalTolerance`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FacetParameters.GetChordalTolerance`

Получить максимальное расстояние между кривой и хордой

Returns: Максимальное расстояние между кривой и хордой

### `UseGeneral`

ID: `M:RGPlatform.Geometry.Curve2DGeometry.FacetParameters.UseGeneral`

Использовать общий алгоритм разбиения?

Returns: true - да, false - нет
