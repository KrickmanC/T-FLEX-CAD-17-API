# TFlex.Model.Model2D.Formlimits

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс допусков формы, расположения и обозначения базы

## Constructors

### `Formlimits(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Formlimits.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объекта

## Methods

### `Formlimits(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Formlimits.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объекта

### `SetConstruction(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.Formlimits.SetConstruction(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Установка параметров привязки к прямой

Parameters:
- `line`: Прямая
- `node`: Узел на прямой
- `offset`: Смещение точки привязки по прямой относительно узла

### `SetDimension(TFlex.Model.Model2D.Dimension)`

ID: `M:TFlex.Model.Model2D.Formlimits.SetDimension(TFlex.Model.Model2D.Dimension)`

Установка привязки к размеру

Parameters:
- `dim`: Размер привязки

### `SetFormlimitsObj(TFlex.Model.Model2D.Formlimits)`

ID: `M:TFlex.Model.Model2D.Formlimits.SetFormlimitsObj(TFlex.Model.Model2D.Formlimits)`

Установка привязки к другому обозначению допуска

Parameters:
- `obj`: Обозначение допуска привязки

### `SetLeader(TFlex.Model.Model2D.FormlimitsLeader)`

ID: `M:TFlex.Model.Model2D.Formlimits.SetLeader(TFlex.Model.Model2D.FormlimitsLeader)`

Установить привязку к линии-выноске

Parameters:
- `leader`: Линия-выноска

### `SetNode(TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.Formlimits.SetNode(TFlex.Model.Model2D.Node)`

Установка привязки к узлу

Parameters:
- `node`: Узел привязки

### `SetOutline(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.Formlimits.SetOutline(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

Установка параметров привязки к отрезку

Parameters:
- `line`: Отрезок привязки
- `isOnEnd`: Значение true указывает, что привязка выполняется к концу отрезка, false - к началу
- `offset`: Смещение точки привязки по отрезку относительно выбранного конца отрезка

### `SetPoint(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.Formlimits.SetPoint(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка абсолютных координат точки привязки

Parameters:
- `x`: Координата X
- `y`: Координата Y

## Propertys

### `AltFit`

ID: `P:TFlex.Model.Model2D.Formlimits.AltFit`

Проставлять дополнительную посадку

### `AltFitView`

ID: `P:TFlex.Model.Model2D.Formlimits.AltFitView`

Вид простановки дополнительной посадки

### `AutoNamingDatum`

ID: `P:TFlex.Model.Model2D.Formlimits.AutoNamingDatum`

Автоматическое именование базы

### `Color`

ID: `P:TFlex.Model.Model2D.Formlimits.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `Construction`

ID: `P:TFlex.Model.Model2D.Formlimits.Construction`

Линия построения, к которой привязана стрелка

### `Dimension`

ID: `P:TFlex.Model.Model2D.Formlimits.Dimension`

Размер, к которому привязан данный объект

### `Fit`

ID: `P:TFlex.Model.Model2D.Formlimits.Fit`

Проставлять посадку

### `FitView`

ID: `P:TFlex.Model.Model2D.Formlimits.FitView`

Вид простановки посадки

### `FontStyle`

ID: `P:TFlex.Model.Model2D.Formlimits.FontStyle`

Стиль шрифта текста для получения или установки его параметров

### `FormlimitsObj`

ID: `P:TFlex.Model.Model2D.Formlimits.FormlimitsObj`

Другой объект обозначения допуска, к которому привязан данный объект

### `GroupType`

ID: `P:TFlex.Model.Model2D.Formlimits.GroupType`

Тип объекта

### `Layer`

ID: `P:TFlex.Model.Model2D.Formlimits.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Leader`

ID: `P:TFlex.Model.Model2D.Formlimits.Leader`

Линия-выноска, которая связана с данным объектом

### `Level`

ID: `P:TFlex.Model.Model2D.Formlimits.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `LineWidth`

ID: `P:TFlex.Model.Model2D.Formlimits.LineWidth`

Толщина линий объекта

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `Node`

ID: `P:TFlex.Model.Model2D.Formlimits.Node`

Узел привязки

### `Outline`

ID: `P:TFlex.Model.Model2D.Formlimits.Outline`

Линия изображения, к которой привязана стрелка

### `Page`

ID: `P:TFlex.Model.Model2D.Formlimits.Page`

Cтраница, на которой размещается объект

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Placement`

ID: `P:TFlex.Model.Model2D.Formlimits.Placement`

Номер точки привязки на таблице (от 0 до 7)

### `Point`

ID: `P:TFlex.Model.Model2D.Formlimits.Point`

Абсолютные координаты точки привязки

### `Priority`

ID: `P:TFlex.Model.Model2D.Formlimits.Priority`

Приоритет объекта

### `SubType`

ID: `P:TFlex.Model.Model2D.Formlimits.SubType`

Значение подтипа объекта

### `X`

ID: `P:TFlex.Model.Model2D.Formlimits.X`

Координата X точки привязки

### `Y`

ID: `P:TFlex.Model.Model2D.Formlimits.Y`

Координата Y точки привязки
