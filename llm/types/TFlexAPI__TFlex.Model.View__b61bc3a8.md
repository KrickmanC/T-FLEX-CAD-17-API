# TFlex.Model.View

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Данный класс реализует функциональность вида документа

## Remarks

Класс является базовым классом для классов `T:TFlex.Model.Model2D.View2D` и `T:TFlex.Model.Model3D.View3D` , являющимися 2D и 3D видами соответственно

## Methods

### `Activate`

ID: `M:TFlex.Model.View.Activate`

Активизировать вид

### `Close`

ID: `M:TFlex.Model.View.Close`

Закрыть вид

Returns: true, если операция завершилась успешно

### `PointToClient(System.Drawing.Point)`

ID: `M:TFlex.Model.View.PointToClient(System.Drawing.Point)`

Преобразование точки из экранных координат в оконные

Parameters:
- `screenPoint`: Точка в экранных координатах

### `PointToModel(System.Drawing.Point)`

ID: `M:TFlex.Model.View.PointToModel(System.Drawing.Point)`

Преобразование точки из экранных координат в модельные

Parameters:
- `screenPoint`: Точка в экранных координатах

### `PointToScreen(System.Drawing.Point)`

ID: `M:TFlex.Model.View.PointToScreen(System.Drawing.Point)`

Преобразование точки из оконных координат в экранные

Parameters:
- `clientPoint`: Точка в оконных координатах

### `Search(System.Double,System.Double,TFlex.Model.SelectionFilter,System.Double)`

ID: `M:TFlex.Model.View.Search(System.Double,System.Double,TFlex.Model.SelectionFilter,System.Double)`

Поиск элемента модели

Parameters:
- `x`: Координата X в модельных координатах
- `y`: Координата Y в модельных координатах
- `filter`: Фильтр выбираемых объектов
- `maxdist`: Расстояние до объекта, пикселей

### `Search(TFlex.Drawing.Point,TFlex.Model.SelectionFilter,System.Double)`

ID: `M:TFlex.Model.View.Search(TFlex.Drawing.Point,TFlex.Model.SelectionFilter,System.Double)`

Поиск элемента модели

Parameters:
- `point`: Точка в координатах модели
- `filter`: Фильтр выбираемых объектов
- `maxdist`: Расстояние до объекта, пикселей

### `Select(System.Double,System.Double,TFlex.Model.SelectionFilter,System.Double)`

ID: `M:TFlex.Model.View.Select(System.Double,System.Double,TFlex.Model.SelectionFilter,System.Double)`

Выбор элемента модели

Parameters:
- `x`: Координата X в модельных координатах
- `y`: Координата Y в модельных координатах
- `filter`: Фильтр выбираемых объектов
- `maxdist`: Расстояние до объекта, пикселей

### `Select(System.Drawing.Point,TFlex.Model.SelectionFilter)`

ID: `M:TFlex.Model.View.Select(System.Drawing.Point,TFlex.Model.SelectionFilter)`

Выбор элемента модели

Parameters:
- `point`: Точка в координатах экрана
- `filter`: Фильтр выбираемых объектов

### `Select(System.Int32,System.Int32,TFlex.Model.SelectionFilter)`

ID: `M:TFlex.Model.View.Select(System.Int32,System.Int32,TFlex.Model.SelectionFilter)`

Выбор элемента модели

Parameters:
- `x`: Координата X курсора
- `y`: Координата Y курсора
- `filter`: Фильтр выбираемых объектов

### `Select(TFlex.Drawing.Point,TFlex.Model.SelectionFilter,System.Double)`

ID: `M:TFlex.Model.View.Select(TFlex.Drawing.Point,TFlex.Model.SelectionFilter,System.Double)`

Выбор элемента модели

Parameters:
- `point`: Точка в координатах модели
- `filter`: Фильтр выбираемых объектов
- `maxdist`: Расстояние до объекта, пикселей

### `SetCursor(System.IntPtr)`

ID: `M:TFlex.Model.View.SetCursor(System.IntPtr)`

Установить курсор

### `Split(TFlex.Model.ViewType,TFlex.Model.ViewType,TFlex.Model.ViewType,TFlex.Model.ViewType)`

ID: `M:TFlex.Model.View.Split(TFlex.Model.ViewType,TFlex.Model.ViewType,TFlex.Model.ViewType,TFlex.Model.ViewType)`

Разделить вид

### `SplitHorizontally(TFlex.Model.ViewType,TFlex.Model.ViewType)`

ID: `M:TFlex.Model.View.SplitHorizontally(TFlex.Model.ViewType,TFlex.Model.ViewType)`

Разделить по горизонтали

### `SplitVertically(TFlex.Model.ViewType,TFlex.Model.ViewType)`

ID: `M:TFlex.Model.View.SplitVertically(TFlex.Model.ViewType,TFlex.Model.ViewType)`

Разделить по вертикали

## Propertys

### `Document`

ID: `P:TFlex.Model.View.Document`

Документ, видом которого является данный объект

### `Graphics`

ID: `P:TFlex.Model.View.Graphics`

Объект графического контекста для вывода графического изображения в данный вид

### `HWnd`

ID: `P:TFlex.Model.View.HWnd`

Дескриптор окна вида

### `HideConstructions`

ID: `P:TFlex.Model.View.HideConstructions`

Параметр "Скрыть линии построения"

### `Page`

ID: `P:TFlex.Model.View.Page`

Страница, которая отображается в данном виде
