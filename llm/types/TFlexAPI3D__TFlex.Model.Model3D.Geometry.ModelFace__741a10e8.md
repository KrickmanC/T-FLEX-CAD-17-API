# TFlex.Model.Model3D.Geometry.ModelFace

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Модельная грань

## Methods

### `Dispose`

ID: `M:TFlex.Model.Model3D.Geometry.ModelFace.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `IntersectCurve(TFlex.Model.Model3D.Geometry.BaseCurve,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelFace.IntersectCurve(TFlex.Model.Model3D.Geometry.BaseCurve,System.Double,System.Double)`

Ищет пересечения между указываемым участком кривой и гранью.

Parameters:
- `curve`: Изгиб, с которым будет искаться пересечение
- `IntervalStart`: Начало интервала изгиба
- `IntervalEnd`: Конец интервала изгиба

### `IntersectSurface(TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelFace.IntersectSurface(TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,TFlex.Model.Model3D.Geometry.BaseBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.UVBox,System.Boolean,TFlex.Model.Model3D.Geometry.BasePoint3D)`

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

ID: `M:TFlex.Model.Model3D.Geometry.ModelFace.OutputSurfTrimmed(System.Double)`

Возвращает обрезанную поверхность

Parameters:
- `tolerance`: Максимально допустимое расстояние между поверхностью грани и аппроксимирующей сплайновой поверхностью

Remarks: Рекомендуемая точность = 0.00001

## Propertys

### `Color`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.Color`

Цвет грани

### `Edges`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.Edges`

Множество рёбер

### `Geometry`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.Geometry`

Получить геометрические данные грани

### `Loops`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.Loops`

Множество циклов

### `Sense`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.Sense`

Получить признак совпадения ориентации поверхности и грани

### `Surface`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.Surface`

Получить поверхность, на которой лежит грань

### `UVBox`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.UVBox`

Получить UVbox грани

### `Vertices`

ID: `P:TFlex.Model.Model3D.Geometry.ModelFace.Vertices`

Множество вершин
