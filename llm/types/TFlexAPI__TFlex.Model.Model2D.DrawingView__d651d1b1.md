# TFlex.Model.Model2D.DrawingView

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс чертёжного вида

## Constructors

### `DrawingView(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.DrawingView.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `doc`: Документ объекта

### `DrawingView(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model2D.DrawingView.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Создание чертёжного вида с изображением заданной страницы

Parameters:
- `doc`: Документ объекта
- `pageToShow`: Отображаемая страница

## Methods

### `DrawingView(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.DrawingView.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `doc`: Документ объекта

### `DrawingView(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model2D.DrawingView.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Создание чертёжного вида с изображением заданной страницы

Parameters:
- `doc`: Документ объекта
- `pageToShow`: Отображаемая страница

### `AddExclusion(TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.DrawingView.AddExclusion(TFlex.Model.Model2D.Object2D)`

Добавить в исключения

Parameters:
- `object2D`: 2D объект

### `ClearExclusions`

ID: `M:TFlex.Model.Model2D.DrawingView.ClearExclusions`

Очистить исключения

### `RemoveExclusion(TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.DrawingView.RemoveExclusion(TFlex.Model.Model2D.Object2D)`

Удалить из исключения

Parameters:
- `object2D`: 2D объект

### `SetPosition(System.Double,System.Double,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.DrawingView.SetPosition(System.Double,System.Double,TFlex.Model.Parameter)`

Установка привязки по точке и углу

Parameters:
- `x`: Координата X
- `y`: Координата Y
- `angle`: Угол поворота

### `SetPosition(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.DrawingView.SetPosition(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Установка привязки по узлу и углу

Parameters:
- `node`: Узел привязки
- `angle`: Угол поворота

### `SetVector(TFlex.Model.Model2D.FixingVector,TFlex.Drawing.Point,TFlex.Drawing.Point)`

ID: `M:TFlex.Model.Model2D.DrawingView.SetVector(TFlex.Model.Model2D.FixingVector,TFlex.Drawing.Point,TFlex.Drawing.Point)`

Установка привязки по вектору и точкам

Parameters:
- `vector`: Вектор привязки на отображаемой странице
- `point1`: Первая точка на отображающей странице
- `point2`: Вторая точка на отображающей странице

### `SetVector(TFlex.Model.Model2D.FixingVector,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.DrawingView.SetVector(TFlex.Model.Model2D.FixingVector,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Установка привязки по вектору и узлам

Parameters:
- `vector`: Вектор привязки на отображамой странице
- `node1`: Первый узел на отображающей странице
- `node2`: Второй узел на отображающей странице

## Propertys

### `Angle`

ID: `P:TFlex.Model.Model2D.DrawingView.Angle`

Угол поворота изображения. При установке значения привязка по вектору отменяется

### `BreakSet`

ID: `P:TFlex.Model.Model2D.DrawingView.BreakSet`

Набор разрывов чертёжного вида

### `Clipping`

ID: `P:TFlex.Model.Model2D.DrawingView.Clipping`

Выполнять отсечение изображения по текущему прямоугольнику отсечения (свойство ClippingRectangle)

### `ClippingRectangle`

ID: `P:TFlex.Model.Model2D.DrawingView.ClippingRectangle`

Прямоугольная область отсечения в системе координат отображаемой страницы

### `GroupType`

ID: `P:TFlex.Model.Model2D.DrawingView.GroupType`

Тип объекта

### `HideBreaksLines`

ID: `P:TFlex.Model.Model2D.DrawingView.HideBreaksLines`

Скрывать линии разрывов

### `IsActive`

ID: `P:TFlex.Model.Model2D.DrawingView.IsActive`

Вид является активным

### `Layer`

ID: `P:TFlex.Model.Model2D.DrawingView.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `LeaderNote`

ID: `P:TFlex.Model.Model2D.DrawingView.LeaderNote`

Объект надписи обозначения (только для выносного вида)

### `Level`

ID: `P:TFlex.Model.Model2D.DrawingView.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Node1`

ID: `P:TFlex.Model.Model2D.DrawingView.Node1`

Первый узел привязки

### `Node2`

ID: `P:TFlex.Model.Model2D.DrawingView.Node2`

Второй узел привязки. Используется только в режиме привязки по вектору

### `OriginX`

ID: `P:TFlex.Model.Model2D.DrawingView.OriginX`

Координата X базовой точки на отображаемой странице

### `OriginY`

ID: `P:TFlex.Model.Model2D.DrawingView.OriginY`

Координата Y базовой точки на отображаемой странице

### `Page`

ID: `P:TFlex.Model.Model2D.DrawingView.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Priority`

ID: `P:TFlex.Model.Model2D.DrawingView.Priority`

Приоритет объекта

### `Scale`

ID: `P:TFlex.Model.Model2D.DrawingView.Scale`

Масштаб изображения

### `ShowConstructions`

ID: `P:TFlex.Model.Model2D.DrawingView.ShowConstructions`

Показывать линии построения

### `ShowPage`

ID: `P:TFlex.Model.Model2D.DrawingView.ShowPage`

Отображаемая на виде страница

### `SynchronizePageParameters`

ID: `P:TFlex.Model.Model2D.DrawingView.SynchronizePageParameters`

Синхронизировать параметры страницы

### `Transformation`

ID: `P:TFlex.Model.Model2D.DrawingView.Transformation`

Преобразование, применяемое при выводе отображаемой страницы

### `TransparentActivation`

ID: `P:TFlex.Model.Model2D.DrawingView.TransparentActivation`

Разрешить выполнение автоматической активации

### `Vector`

ID: `P:TFlex.Model.Model2D.DrawingView.Vector`

Вектор привязки

### `ViewFixingMode`

ID: `P:TFlex.Model.Model2D.DrawingView.ViewFixingMode`

Режим привязки

### `ViewSymbol`

ID: `P:TFlex.Model.Model2D.DrawingView.ViewSymbol`

Объект обозначения вида

### `Visible`

ID: `P:TFlex.Model.Model2D.DrawingView.Visible`

Изображение вида показывать

### `X1`

ID: `P:TFlex.Model.Model2D.DrawingView.X1`

Координата X первой точки привязки

### `X2`

ID: `P:TFlex.Model.Model2D.DrawingView.X2`

Координата X второй точки привязки. Используется только в режиме привязки по вектору

### `Y1`

ID: `P:TFlex.Model.Model2D.DrawingView.Y1`

Координата Y первой точки привязки

### `Y2`

ID: `P:TFlex.Model.Model2D.DrawingView.Y2`

Координата Y второй точки привязки. Используется только в режиме привязки по вектору
