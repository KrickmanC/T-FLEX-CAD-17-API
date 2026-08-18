# TFlex.Model.Model3D.Geometry.BaseSurface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для поверхностей

## Constructors

### `BaseSurface`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.#ctor`

Конструкторы для геометрической поверхности

### `BaseSurface(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной поверхности

## Methods

### `BaseSurface`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.#ctor`

Конструкторы для геометрической поверхности

### `BaseSurface(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной поверхности

### `ApplyTransform(TFlex.Model.Model3D.Geometry.TransformationMatrix)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.ApplyTransform(TFlex.Model.Model3D.Geometry.TransformationMatrix)`

Трансформация поверхности

Parameters:
- `transformation`: Матрица трансфорации

### `Derivative(TFlex.Model.Model3D.Geometry.UV,System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.Derivative(TFlex.Model.Model3D.Geometry.UV,System.UInt32,System.UInt32)`

Вычислить производные в точке на поверхности по параметрам

Parameters:
- `uv`: Параметры на поверхности
- `uderivs`: Максимальный порядок производной по U
- `vderivs`: Максимальный порядок производной по V

Remarks: Производные возвращаются в следующем порядке: i-ая производная ( i <= 'uderivs' ) по u и j-ая производная ( j <= 'vderivs' ) по v хранится по индексу = i + ( 'uderivs' + 1 ) ^ j ). Например, если 'uderivs' == 2 и 'vderivs' == 3, тогда массив из 12 векторов выглядит следующим образом : p(u,v) p(u,v) p(u,v) u uu Затем: p(u,v) p(u,v) p(u,v) v uv uuv Затем: p(u,v) p(u,v) p(u,v) vv uvv uuvv Затем: p(u,v) p(u,v) p(u,v) vvv uvvv uuvvv Здесь запись : p(u,v) uvv - означает первую производную по u и вторую производную по V

### `Eval(TFlex.Model.Model3D.Geometry.UV)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.Eval(TFlex.Model.Model3D.Geometry.UV)`

Вычислить координаты точки на поверхности по параметрам

Parameters:
- `uv`: Параметры на поверхности

### `IntersectCurve(TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseInterval,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.IntersectCurve(TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseInterval,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox)`

Найти пересечение поверхности с кривой

Parameters:
- `curve`: Кривая, с которой ищется пересечение
- `interval`: Параметрический интервал кривой, на котором ищется пересечение
- `havebox`: Использовать область поиска пересечений
- `box`: Область поиска пересечений

### `IntersectSurface(TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.IntersectSurface(TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Найти пересечение поверхности с другой поверхностью

Parameters:
- `surface`: Поверхность, с которой ищется пересечение
- `havebox`: Использовать область поиска пересечений
- `box`: Область поиска пересечений
- `haveuvbox1`: Использовать параметрическую область поиска пересечений для первой поверхности
- `uvbox1`: Параметрическая область поиска пересечений для первой поверхности
- `haveuvbox2`: Использовать параметрическую область поиска пересечений для второй поверхности
- `uvbox2`: Параметрическая область поиска пересечений для второй поверхности
- `havepoint`: Использовать точку для отбора одной из нескольких веток пересечения, на которой лежит точка
- `point`: Точка для отбора одной из нескольких веток пересечения, на которой лежит точка

### `Normal(TFlex.Model.Model3D.Geometry.UV)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.Normal(TFlex.Model.Model3D.Geometry.UV)`

Вычислить нормаль к поверхности в точке по параметрам

Parameters:
- `uv`: Параметры на поверхности

### `Parameterize(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.Parameterize(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Вычислить параметр на поверхности, для точки, лежащей на поверхности

Parameters:
- `point`: Точка на поверхности

### `Parameterize2(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.Parameterize2(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Вычислить параметры на поверхности, для точки, лежащей около нее

Parameters:
- `point`: Точка на кривой

### `PrincipalCurvature1(TFlex.Model.Model3D.Geometry.UV)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.PrincipalCurvature1(TFlex.Model.Model3D.Geometry.UV)`

Вычислить первую главную кривизну в точек на поверхности по параметрам

Parameters:
- `uv`: Параметры на поверхности

### `PrincipalCurvature2(TFlex.Model.Model3D.Geometry.UV)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.PrincipalCurvature2(TFlex.Model.Model3D.Geometry.UV)`

Вычислить вторую главную кривизну в точках на поверхности по параметрам

Parameters:
- `uv`: Параметры на поверхности

### `PrincipalDirection1(TFlex.Model.Model3D.Geometry.UV)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.PrincipalDirection1(TFlex.Model.Model3D.Geometry.UV)`

Вычислить первое главное направление в точке по параметрам

Parameters:
- `uv`: Параметры на поверхности

### `PrincipalDirection2(TFlex.Model.Model3D.Geometry.UV)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSurface.PrincipalDirection2(TFlex.Model.Model3D.Geometry.UV)`

Вычислить второе главное направление в точке по параметрам

Parameters:
- `uv`: параметры на поверхности

## Propertys

### `UParam`

ID: `P:TFlex.Model.Model3D.Geometry.BaseSurface.UParam`

Получить информацию о параметризации по U

### `VParam`

ID: `P:TFlex.Model.Model3D.Geometry.BaseSurface.VParam`

Получить информацию о параметризации по V
