# TFlex.Model.Model3D.Geometry.Face

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Геометрическая грань

## Methods

### `Dispose`

ID: `M:TFlex.Model.Model3D.Geometry.Face.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `FindAxis(System.Collections.Generic.IEnumerable`1{TFlex.Model.Model3D.Geometry.BaseTopol},System.Collections.Generic.IEnumerable`1{TFlex.Model.Model3D.Geometry.BaseTopol},TFlex.Model.Model3D.Geometry.BasePoint3Dref ,TFlex.Model.Model3D.Geometry.BasePoint3Dref ,System.Byte)`

ID: `M:TFlex.Model.Model3D.Geometry.Face.FindAxis(System.Collections.Generic.IEnumerable`1{TFlex.Model.Model3D.Geometry.BaseTopol},System.Collections.Generic.IEnumerable`1{TFlex.Model.Model3D.Geometry.BaseTopol},TFlex.Model.Model3D.Geometry.BasePoint3D@,TFlex.Model.Model3D.Geometry.BasePoint3D@,System.Byte)`

Найти точки оси для набора граней

Parameters:
- `excludeEdges`: Набор ребер, исключаемых из рассмотрения

### `IntersectCurve(TFlex.Model.Model3D.Geometry.BaseCurve,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.Face.IntersectCurve(TFlex.Model.Model3D.Geometry.BaseCurve,System.Double,System.Double)`

Ищет пересечения между указываемым участком кривой и гранью.

Parameters:
- `curve`: Изгиб, с которым будет искаться пересечение
- `IntervalStart`: Начало интервала изгиба
- `IntervalEnd`: Конец интервала изгиба

### `IntersectFace(TFlex.Model.Model3D.Geometry.Face,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.Face.IntersectFace(TFlex.Model.Model3D.Geometry.Face,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Найти пересечение грани с другой гранью

Parameters:
- `face`: Грань, с которой ищется пересечение
- `havebox`: Использовать область поиска пересечений
- `box`: Область поиска пересечений
- `haveuvbox1`: Использовать параметрическую область поиска пересечений для первой поверхности
- `uvbox1`: Параметрическая область поиска пересечений для первой поверхности
- `haveuvbox2`: Использовать параметрическую область поиска пересечений для второй поверхности
- `uvbox2`: Параметрическая область поиска пересечений для второй поверхности
- `havepoint`: Использовать точку для отбора одной из нескольких веток пересечения, на которой лежит точка
- `point`: Точка для отбора одной из нескольких веток пересечения, на которой лежит точка

### `IntersectSurface(TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.Face.IntersectSurface(TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Найти пересечение грани с другой поверхностью

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

### `OutputSurfTrimmed(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.Face.OutputSurfTrimmed(System.Double)`

Возвращает обрезанную поверхность

Parameters:
- `tolerance`: Максимально допустимое расстояние между поверхностью грани и аппроксимирующей сплайновой поверхностью

Remarks: Рекомендуемая точность = 0.00001

## Propertys

### `Edges`

ID: `P:TFlex.Model.Model3D.Geometry.Face.Edges`

Множество рёбер

### `Loops`

ID: `P:TFlex.Model.Model3D.Geometry.Face.Loops`

Множество циклов

### `Sense`

ID: `P:TFlex.Model.Model3D.Geometry.Face.Sense`

Получить признак совпадения ориентации поверхности и грани

### `Surface`

ID: `P:TFlex.Model.Model3D.Geometry.Face.Surface`

Получить поверхность, на которой лежит грань

### `UVBox`

ID: `P:TFlex.Model.Model3D.Geometry.Face.UVBox`

Получить UVbox грани

### `Vertices`

ID: `P:TFlex.Model.Model3D.Geometry.Face.Vertices`

Множество вершин
