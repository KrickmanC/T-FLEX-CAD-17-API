# TFlex.Model.Model3D.Geometry.BaseBody

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс хранения тел

## Methods

### `ApplyTransform(TFlex.Model.Model3D.Geometry.TransformationMatrix)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.ApplyTransform(TFlex.Model.Model3D.Geometry.TransformationMatrix)`

Трансформация геометрии тела

Parameters:
- `transformation`: Матрица преобразования

Remarks: Создаётся новое тело

### `Check`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.Check`

Проверить тело Parasolid

### `CheckAllBodies(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.CheckAllBodies(TFlex.Model.Document)`

Проверить все тела Parasolid

### `CheckBodies(System.Collections.Generic.ICollection`1{TFlex.Model.Model3D.Geometry.BaseBody})`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.CheckBodies(System.Collections.Generic.ICollection`1{TFlex.Model.Model3D.Geometry.BaseBody})`

Проверить тела Parasolid

### `Clash(TFlex.Model.Model3D.Geometry.BaseBody,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.Clash(TFlex.Model.Model3D.Geometry.BaseBody,System.Boolean,System.Boolean)`

Функция определяет столкновение тел

Parameters:
- `body`: Тело для проверки
- `isFindAllClashes`: Найти все столкновения
- `isFindIntersect`: Исследовать столкновения

Returns: Информация о столкновении тел

### `ClashBody(TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.ClashBody(TFlex.Model.Model3D.Geometry.BaseBody)`

Функция определяет перекрытие тел

Parameters:
- `body`: Тело для проверки

Returns: Тип пересечения

### `ContainsPoint(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.ContainsPoint(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Функция определяет положение точки относительно тела

Parameters:
- `point`: Точка

Returns: Положение точки относительно тела

### `ConvertToRGK(TFlex.Model.Document,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.ConvertToRGK(TFlex.Model.Document,System.IntPtr)`

Конвертировать тело Parasolid в тело RGK

### `ConvertToRGK(TFlex.Model.Document,System.IntPtr,TFlex.Model.Model3D.Geometry.BaseBody.ConvertToRGKOptions)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.ConvertToRGK(TFlex.Model.Document,System.IntPtr,TFlex.Model.Model3D.Geometry.BaseBody.ConvertToRGKOptions)`

Конвертировать тело Parasolid в тело RGK

### `Facet(System.Double,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.Facet(System.Double,System.Boolean,System.Boolean)`

Функция создаёт плоскогранную сетку

Returns: Сетка

### `FindBoundBox`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.FindBoundBox`

Получить границы тела

### `FindExtreme(TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.FindExtreme(TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

Найти экстремальную точку на теле в заданном направлении

Parameters:
- `direction1`: Первое направление поиска
- `direction2`: Второе направление поиска
- `direction3`: Третье направление поиска

Remarks: Экстремальная точка ищется в направлении 1. Если решение неоднозначное, то количество экстремальных точек последовательно редуцируется по направлениям 2 и 3. Все три направления взаимно ортогональны

### `IntersectWire(TFlex.Model.Model3D.Geometry.BaseBody,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.Point3D}ref )`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.IntersectWire(TFlex.Model.Model3D.Geometry.BaseBody,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.Point3D}@)`

Найти точки пересечения проволочных тел

Parameters:
- `sourceWire`: проволочное тело

Returns: true, если найдены точки пересечения

### `RangePoint(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.RangePoint(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Найти точку на теле ближайшую к данной точке

Parameters:
- `point`: Точка

Returns: Точка на теле ближайшая к данной точке

### `RangePoint(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.Point3Dref ,TFlex.Model.Model3D.Geometry.UVref )`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.RangePoint(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.Point3D@,TFlex.Model.Model3D.Geometry.UV@)`

Найти точку на теле ближайшую к данной точке

Parameters:
- `point`: Точка

Returns: Точка на теле ближайшая к данной точке

### `RangeTopol(TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.RangeTopol(TFlex.Model.Model3D.Geometry.BaseBody)`

Найти ближайшие расстояние между двумя телами

Parameters:
- `rhs`: Тело до которого ищется расстояние

Returns: Расстояние

### `RangeTopol(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.RangeTopol(TFlex.Model.Model3D.Geometry.BaseTopol)`

Найти ближайшее расстояние между телом и топологическим элементом

Parameters:
- `rhs`: Топологический элемент

Returns: Расстояние

### `SetApprox`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.SetApprox`

Функция формирует набор вспомогательных данных, ускоряющих выполнение функции `M:TFlex.Model.Model3D.Geometry.BaseBody.ContainsPoint(TFlex.Model.Model3D.Geometry.BasePoint3D)` , если выполняется несколько вызовов этой функции

### `UnsetApprox`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.UnsetApprox`

Если ранее была вызвана функция `M:TFlex.Model.Model3D.Geometry.BaseBody.SetApprox` , то по завершении работы нужно вызвать функцию удаления вспомогательных данных

### `WireEval(TFlex.Model.Model3D.Geometry.BasePoint3D,System.Int32,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.Point3D}ref )`

ID: `M:TFlex.Model.Model3D.Geometry.BaseBody.WireEval(TFlex.Model.Model3D.Geometry.BasePoint3D,System.Int32,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.Point3D}@)`

Получения производных в заданной точке на проволочном теле

Parameters:
- `point`: точка на проволочном теле

Returns: p[0] - точка, p[1] - первая производная, p[2] - вторая производная, p[n] - n-ая производная

## Propertys

### `Edges`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.Edges`

Множество рёбер

### `Faces`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.Faces`

Множество граней

### `IsClosedIfWire`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.IsClosedIfWire`

Если тело является контуром, то можно проверить его замкнутость

### `LengthIfWire`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.LengthIfWire`

Если тело является контуром, то можно получить его длину

### `Loops`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.Loops`

Множество циклов

### `NormalIfPlanarSheet`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.NormalIfPlanarSheet`

Для плоского листового тела возвращается нормаль к лицевой стороне тела

Returns: Нормаль к лицевой стороне тела

### `PlaneIfWire`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.PlaneIfWire`

Если тело является контуром, то можно проверить его планарность и получить плоскость, в которой он лежит

### `Vertices`

ID: `P:TFlex.Model.Model3D.Geometry.BaseBody.Vertices`

Множество вершин
