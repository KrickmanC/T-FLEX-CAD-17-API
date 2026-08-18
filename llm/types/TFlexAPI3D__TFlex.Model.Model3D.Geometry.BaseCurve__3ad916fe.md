# TFlex.Model.Model3D.Geometry.BaseCurve

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для кривых

## Constructors

### `BaseCurve`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.#ctor`

Конструкторы для геометрической кривой

### `BaseCurve(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной кривой

## Methods

### `BaseCurve`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.#ctor`

Конструкторы для геометрической кривой

### `BaseCurve(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной кривой

### `ApplyTransform(TFlex.Model.Model3D.Geometry.TransformationMatrix)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.ApplyTransform(TFlex.Model.Model3D.Geometry.TransformationMatrix)`

Трансформация кривой

Parameters:
- `transformation`: Матрица преобразования

Remarks: Создаётся новая кривая

### `Binormal(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Binormal(System.Double)`

Вычислить бинормаль в точке на кривой по параметру

Parameters:
- `t`: Параметр

### `ConvertParamByLength(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.ConvertParamByLength(System.Double)`

Конвертировать параметр по длине в параметр кривой

Parameters:
- `paramByLength`: Параметр по длине в диапазоне {0; Длина кривой}

### `ConvertParamByLengthRatio(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.ConvertParamByLengthRatio(System.Double)`

Конвертировать параметр отношения к длине в параметр кривой

Parameters:
- `paramByLengthRatio`: Параметр отношения к длине в диапазоне {0.0; 1.0}

### `ConvertToRGK(TFlex.Model.Document,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.ConvertToRGK(TFlex.Model.Document,System.IntPtr)`

Конвертировать кривую Parasolid в кривую RGK

### `Curvature(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Curvature(System.Double)`

Вычислить кривизну в точке на кривой по параметру

Parameters:
- `t`: Параметр

### `Derivative(System.Double,System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Derivative(System.Double,System.UInt32)`

Вычислить производные в точке на кривой по параметру

Parameters:
- `t`: Параметр
- `derivative`: Максимальный порядок производной

### `Dispose`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `Eval(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Eval(System.Double)`

Вычислить координаты точки на кривой по параметру

Parameters:
- `t`: Параметр

### `EvalPolyline(System.Double,System.Double,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.Point3D}ref )`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.EvalPolyline(System.Double,System.Double,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.Point3D}@)`

Получение точек полилинии аппроксимации кривой

Parameters:
- `tolerance`: Допустимое отклонение
- `segmentLengthFactor`: Коэффициент максимальной допустимой длины сегмента (1e-6..1)

### `IntersectCurve(TFlex.Model.Model3D.Geometry.BaseInterval,TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseInterval,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.BaseSurface)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.IntersectCurve(TFlex.Model.Model3D.Geometry.BaseInterval,TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseInterval,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.BaseSurface)`

Найти пересечение кривой с другой кривой

Parameters:
- `owninterval`: Собственный параметрический интервал, на котором ищется пересечение
- `curve`: Кривая, с которой ищется пересечение
- `interval`: Параметрический интервал кривой, на котором ищется пересечение
- `havebox`: Использовать область поиска пересечений
- `box`: Область поиска пересечений
- `havesurface`: Поверхность, на которой лежат кривые

### `Interval(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Interval(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Вычислить параметрический интервал на кривой, ограниченный двумя точками, лежащими на кривой

Parameters:
- `point1`: Первая точка на кривой
- `point2`: Вторая точка на кривой

### `Length(TFlex.Model.Model3D.Geometry.BaseInterval)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Length(TFlex.Model.Model3D.Geometry.BaseInterval)`

Вычислить длину кривой по параметру

Parameters:
- `interval`: Интервал на кривой

### `MakeReverseCurve`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.MakeReverseCurve`

Трансформация кривой

Remarks: Меняется направление кривой

### `Parameterize(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Parameterize(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Вычислить параметр на кривой, для точки, лежащей на кривой

Parameters:
- `point`: Точка на кривой

### `PrincipalNormal(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.PrincipalNormal(System.Double)`

Вычислить главную нормаль в точке на кривой по параметру

Parameters:
- `t`: Параметр

### `Tangent(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Tangent(System.Double)`

Вычислить касательную в точке на кривой по параметру

Parameters:
- `t`: Параметр

### `Update`

ID: `M:TFlex.Model.Model3D.Geometry.BaseCurve.Update`

Обновить геометрию для каждого конкретного порождённого типа

## Propertys

### `Param`

ID: `P:TFlex.Model.Model3D.Geometry.BaseCurve.Param`

Получить информацию о параметризации

### `ParasolidCurve`

ID: `P:TFlex.Model.Model3D.Geometry.BaseCurve.ParasolidCurve`

Кривая в формате Parasolid
