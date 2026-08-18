# TFlex.Model.Model3D.View3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Данный класс представляет собой 3D вид документа

## Methods

### `ActivateWorkplane(TFlex.Model.Model3D.Workplane)`

ID: `M:TFlex.Model.Model3D.View3D.ActivateWorkplane(TFlex.Model.Model3D.Workplane)`

Переводит окно в режим черчения на рабочей плоскости.

Parameters:
- `workplane`: Рабочая плоскость

### `DeactivateWorkplane`

ID: `M:TFlex.Model.Model3D.View3D.DeactivateWorkplane`

Завершает режим черчения на рабочей плоскости.

### `FindBoundBox`

ID: `M:TFlex.Model.Model3D.View3D.FindBoundBox`

Получить границы 3D сцены

### `GetDefaultParameters`

ID: `M:TFlex.Model.Model3D.View3D.GetDefaultParameters`

Получить параметры 3D вида по умолчанию для новых видов

### `GetParameters`

ID: `M:TFlex.Model.Model3D.View3D.GetParameters`

Получить параметры 3D вида

Returns: Параметры 3D вида

### `MoveCameraToContainPoints(TFlex.Model.Model3D.FloatVector[],System.Double,System.Boolean)`

ID: `M:TFlex.Model.Model3D.View3D.MoveCameraToContainPoints(TFlex.Model.Model3D.FloatVector[],System.Double,System.Boolean)`

Parameters:
- `points`: Массив точек
- `margin`: 
- `perspectiveAngleChange`: 

### `Pick(System.Int32,System.Int32,System.Single,TFlex.Model.Model3D.Visual.Decoration,TFlex.Model.Model3D.FloatVectorref )`

ID: `M:TFlex.Model.Model3D.View3D.Pick(System.Int32,System.Int32,System.Single,TFlex.Model.Model3D.Visual.Decoration,TFlex.Model.Model3D.FloatVector@)`

Ищет точку на декорации по заданным экранным координатам

Parameters:
- `x`: Экранная координата X
- `y`: Экранная координата Y
- `tolerance`: Допустимое расстояние в пикселях от точки на экране до декорации
- `decorationRoot`: Декорация, на которой ведется поиск
- `closestPoint`: Найденная ближайшая точка на декорации

Returns: Декорация, которой непосредственно принадлежит найденная точка. Отличается от decorationRoot в случае, если decorationRoot - контейнер декораций. NULL в случае, если точка не найдена.

### `PointToRay(System.Int32,System.Int32,TFlex.Model.Model3D.FloatVectorref ,TFlex.Model.Model3D.FloatVectorref )`

ID: `M:TFlex.Model.Model3D.View3D.PointToRay(System.Int32,System.Int32,TFlex.Model.Model3D.FloatVector@,TFlex.Model.Model3D.FloatVector@)`

Преобразует точку на экране в луч в координатах модели

Parameters:
- `x`: Абцисса точки на экране
- `y`: Ордината точки на экране
- `rayStart`: Исходная точка луча
- `rayDir`: Направление луча

### `SetDefaultParameters(TFlex.Model.Model3D.View3D.Parameters)`

ID: `M:TFlex.Model.Model3D.View3D.SetDefaultParameters(TFlex.Model.Model3D.View3D.Parameters)`

Установить параметры 3D вида по умолчанию для новых видов

Parameters:
- `params`: Параметры 3D вида

### `SetParameters(TFlex.Model.Model3D.View3D.Parameters)`

ID: `M:TFlex.Model.Model3D.View3D.SetParameters(TFlex.Model.Model3D.View3D.Parameters)`

Установить параметры 3D вида

### `ShowObject(TFlex.Model.Model3D.Object3D)`

ID: `M:TFlex.Model.Model3D.View3D.ShowObject(TFlex.Model.Model3D.Object3D)`

Изменить масштаб изображения, чтобы показать объект

Parameters:
- `object`: Объект, который требуется показать

### `Zoom(System.Double)`

ID: `M:TFlex.Model.Model3D.View3D.Zoom(System.Double)`

Увеличить или уменьшить изображение

Parameters:
- `ratio`: Коэффициент увеличения

Remarks: Например, 2.0 соответствует увеличению в 2 раза, 0.5 - уменьшению в 2 раза

### `ZoomAll`

ID: `M:TFlex.Model.Model3D.View3D.ZoomAll`

Показать все объекты

### `ZoomIn`

ID: `M:TFlex.Model.Model3D.View3D.ZoomIn`

Увеличить изображение

### `ZoomOut`

ID: `M:TFlex.Model.Model3D.View3D.ZoomOut`

Уменьшить изображение

## Propertys

### `CurrentObject`

ID: `P:TFlex.Model.Model3D.View3D.CurrentObject`

Объект, выбранный под мышкой

### `DecorationScale`

ID: `P:TFlex.Model.Model3D.View3D.DecorationScale`

Возвращает коэффициент, используемый для определения шага манипуляторов

### `RecommendedDraggerStep`

ID: `P:TFlex.Model.Model3D.View3D.RecommendedDraggerStep`

Возвращает рекомендованное значение шага манипулятора при текущем приближении

### `Scene`

ID: `P:TFlex.Model.Model3D.View3D.Scene`

Сцена, изображаемая в этом виде

### `TreeViewRect`

ID: `P:TFlex.Model.Model3D.View3D.TreeViewRect`

Положение окна дерева модели
