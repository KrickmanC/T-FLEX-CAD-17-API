# TFlex.Model.Model2D.LeaderNote

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Надпись

## Constructors

### `LeaderNote(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LeaderNote.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объекта

## Methods

### `LeaderNote(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LeaderNote.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объекта

### `AddMultipleLeaderString(System.String)`

ID: `M:TFlex.Model.Model2D.LeaderNote.AddMultipleLeaderString(System.String)`

Добавление новой дополнительной полки надписи

Parameters:
- `text`: Строка на добавляемой полке

Returns: Индекс добавленной полки

### `ClearMultipleLeader`

ID: `M:TFlex.Model.Model2D.LeaderNote.ClearMultipleLeader`

Удаление всех дополнительных полок надписи

### `GetLeaderDOCsLinks(System.Int32)`

ID: `M:TFlex.Model.Model2D.LeaderNote.GetLeaderDOCsLinks(System.Int32)`

Получение позиций полках надписи

Parameters:
- `StringIndex`: Индекс дополнительной полки (начиная с 0). "-1" для основной полки.

Returns: Список позиций

### `GetMultipleLeaderString(System.Int32)`

ID: `M:TFlex.Model.Model2D.LeaderNote.GetMultipleLeaderString(System.Int32)`

Получение строки на дополнительной полке надписи

Parameters:
- `index`: Индекс дополнительной полки (начиная с 0)

Returns: Строка, на дополнительной полке надписи

### `GetObjectKnotLists`

ID: `M:TFlex.Model.Model2D.LeaderNote.GetObjectKnotLists`

Получить списки узлов объекта (стрелки)

Returns: Списки узлов объекта

### `RemoveMultipleLeaderString(System.Int32)`

ID: `M:TFlex.Model.Model2D.LeaderNote.RemoveMultipleLeaderString(System.Int32)`

Удаление дополнительной полки надписи

Parameters:
- `index`: Индекс удаляемой полки

### `SetArrowAbsolute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetArrowAbsolute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки стрелки к абсолютным координатам

Parameters:
- `x`: Абцисса привязки
- `y`: Ордината привязки

### `SetArrowCircle(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetArrowCircle(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки стрелки к окружности

Parameters:
- `circle`: Окружность привязки
- `cosAngle`: Косинус угла, на котором находится точка привязки
- `sinAngle`: Синус угла, на котором находится точка привязки

### `SetArrowConstructionLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetArrowConstructionLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Установка параметров привязки стрелки к прямой

Parameters:
- `line`: Прямая привязки
- `nod`: Узел привязки (на прямой)
- `offset`: Смещение точки привязки по прямой относительно узла

### `SetArrowEllipse(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetArrowEllipse(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

Установка параметров привязки стрелки к эллипсу

Parameters:
- `ellipse`: Эллипс привязки
- `parameter`: Параметр положения точки привязки на эллипсе

### `SetArrowNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetArrowNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка привязки стрелки к узлу

Parameters:
- `nod`: Узел привязки
- `dX`: Смещение по X от узла привязки
- `dY`: Смещение по Y от узла привязки

### `SetArrowOutlineLine(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetArrowOutlineLine(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

Установка параметров привязки стрелки к отрезку

Parameters:
- `line`: Отрезок привязки
- `isOnEnd`: Указывает на то, что привязка происходит к концу отрезка (иначе - к началу)
- `offset`: Смещение точки привязки по отрезку относительно выбранного конца отрезка

### `SetArrowPolyline(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetArrowPolyline(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

Установка параметров привязки стрелки к полилинии

Parameters:
- `polyline`: Полилиния привязки
- `parameter`: Параметр положения точки привязки на полилинии

### `SetDefaults`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetDefaults`

Установка параметров надписи в соответствии с параметрами по умолчанию

### `SetLeaderAbsolute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderAbsolute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка позиции текста по абсолютным координатам

Parameters:
- `x`: Координата X
- `y`: Координата Y

### `SetLeaderCircle(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderCircle(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки полки к окружности

Parameters:
- `circle`: Окружность привязки
- `cosAngle`: Косинус угла, на котором находится точка привязки
- `sinAngle`: Синус угла, на котором находится точка привязки

### `SetLeaderConstructionLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderConstructionLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Установка параметров привязки полки к прямой

Parameters:
- `line`: Прямая привязки
- `nod`: Узел привязки (на прямой)
- `offset`: Смещение точки привязки по прямой относительно узла

### `SetLeaderDOCsLinks(System.Int32,System.Collections.Generic.List`1{System.Guid})`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderDOCsLinks(System.Int32,System.Collections.Generic.List`1{System.Guid})`

Установка позиций полках надписи

Parameters:
- `StringIndex`: Индекс дополнительной полки (начиная с 0). "-1" для основной полки.
- `guids`: Список позиций

### `SetLeaderEllipse(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderEllipse(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

Установка параметров привязки полки к эллипсу

Parameters:
- `ellipse`: Эллипс привязки
- `parameter`: Параметр положения точки привязки на эллипсе

### `SetLeaderFirstPoint(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderFirstPoint(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки полки относительно положения стрелки

Parameters:
- `dX`: Смещение оси X
- `dY`: Смещение оси Y

### `SetLeaderMultiPoints(System.Collections.Generic.IList`1{TFlex.Drawing.Point})`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderMultiPoints(System.Collections.Generic.IList`1{TFlex.Drawing.Point})`

Построить выносную линию в соответствии с заданной последовательностью точек

Parameters:
- `points`: Коллекция точек для построения выносной линии

### `SetLeaderNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки полки к узлу

Parameters:
- `nod`: Узел привязки
- `dX`: Смещение относительно узла привязки по оси X
- `dY`: Смещение относительно узла привязки по оси Y

### `SetLeaderOutlineLine(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderOutlineLine(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

Установка параметров привязки полки к отрезку

Parameters:
- `line`: Отрезок привязки
- `isOnEnd`: Указывает на то, что привязка происходит к концу отрезка (иначе - к началу)
- `offset`: Смещение точки привязки по отрезку относительно выбранного конца отрезка

### `SetLeaderPolyline(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetLeaderPolyline(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

Установка параметров привязки полки к полилинии

Parameters:
- `polyline`: Полилиния привязки
- `parameter`: Параметр положения точки привязки на полилинии

### `SetMultipleLeaderString(System.Int32,System.String)`

ID: `M:TFlex.Model.Model2D.LeaderNote.SetMultipleLeaderString(System.Int32,System.String)`

Установка строки на дополнительной полке надписи

Parameters:
- `index`: Индекс дополнительной полки (начиная с 0)
- `text`: Устанавливаемая строка

## Propertys

### `ArrowAttachmentObject`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowAttachmentObject`

Объект, к которому привязана стрелка

### `ArrowAttachmentType`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowAttachmentType`

Тип привязки стрелки надписи

### `ArrowHeight`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowHeight`

Высота прямоугольника прямоугольной стрелки

### `ArrowIsAttchedFromEnd`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowIsAttchedFromEnd`

Привязка стрелки выполняется с конца объекта

### `ArrowOffsetX`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowOffsetX`

Смещение стрелки относительно узла привязки или (значение ArrowOffsetX) по линии привязки

### `ArrowOffsetY`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowOffsetY`

Смещение стрелки относительно узла привязки или (значение ArrowOffsetY) по линии привязки

### `ArrowOwnHeight`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowOwnHeight`

Высота прямоугольника стрелки. Eсли данное значение больше 0 - используется соответствующее значение из статуса

### `ArrowOwnSize`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowOwnSize`

Размер стрелки. Eсли данное значение меньше 0 - используется соответствующее значение из статуса

### `ArrowPoint`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowPoint`

Положение стрелки в абсолютных координатах

### `ArrowSize`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowSize`

Размер стрелки, радиус стрелки-окружности или ширина стрелки-прямоугольника

### `ArrowThickness`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowThickness`

Толщина линии стрелки

### `ArrowType`

ID: `P:TFlex.Model.Model2D.LeaderNote.ArrowType`

Тип стрелки. При установки типа (-1) надпись будет рисоваться без стрелки

### `Color`

ID: `P:TFlex.Model.Model2D.LeaderNote.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `CornerSize`

ID: `P:TFlex.Model.Model2D.LeaderNote.CornerSize`

Размер уголка

### `CornerThickness`

ID: `P:TFlex.Model.Model2D.LeaderNote.CornerThickness`

Толщина линии уголка

### `CornerType`

ID: `P:TFlex.Model.Model2D.LeaderNote.CornerType`

Тип уголка надписи

### `Direction`

ID: `P:TFlex.Model.Model2D.LeaderNote.Direction`

Направление полки надписи

### `FontStyle`

ID: `P:TFlex.Model.Model2D.LeaderNote.FontStyle`

Стиль шрифта текста для получения или установки его параметров

### `GroupType`

ID: `P:TFlex.Model.Model2D.LeaderNote.GroupType`

Тип объекта

### `Layer`

ID: `P:TFlex.Model.Model2D.LeaderNote.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `LeaderAttachmentObject`

ID: `P:TFlex.Model.Model2D.LeaderNote.LeaderAttachmentObject`

Объект, к которому привязана надпись

### `LeaderAttachmentType`

ID: `P:TFlex.Model.Model2D.LeaderNote.LeaderAttachmentType`

Тип привязки надписи

### `LeaderIsAttchedFromEnd`

ID: `P:TFlex.Model.Model2D.LeaderNote.LeaderIsAttchedFromEnd`

Привязка надписи выполняется с конца объекта

### `LeaderOffsetX`

ID: `P:TFlex.Model.Model2D.LeaderNote.LeaderOffsetX`

Смещение надписи относительно узла привязки или (значение LeaderOffsetX) по линии привязки

### `LeaderOffsetY`

ID: `P:TFlex.Model.Model2D.LeaderNote.LeaderOffsetY`

Смещение надписи относительно узла привязки или (значение LeaderOffsetY) по линии привязки

### `LeaderPoint`

ID: `P:TFlex.Model.Model2D.LeaderNote.LeaderPoint`

Положение надписи в абсолютных координатах

### `Level`

ID: `P:TFlex.Model.Model2D.LeaderNote.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `MultipleLeaderCount`

ID: `P:TFlex.Model.Model2D.LeaderNote.MultipleLeaderCount`

Количество дополнительных полок надписи

### `Page`

ID: `P:TFlex.Model.Model2D.LeaderNote.Page`

Cтраница, на которой размещается объект

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `ParentWeld`

ID: `P:TFlex.Model.Model2D.LeaderNote.ParentWeld`

Родительский сварной шов

### `Priority`

ID: `P:TFlex.Model.Model2D.LeaderNote.Priority`

Приоритет объекта

### `Standard`

ID: `P:TFlex.Model.Model2D.LeaderNote.Standard`

Стандарт изображения надписи

### `StartAtBottom`

ID: `P:TFlex.Model.Model2D.LeaderNote.StartAtBottom`

Расположение дополнительных полок: true - добавлять снизу вверх, false - сверху вниз

### `StringsAlignment`

ID: `P:TFlex.Model.Model2D.LeaderNote.StringsAlignment`

Параметр выравнивания дополнительных полок по длине наибольшей из полок

### `StringsHeight`

ID: `P:TFlex.Model.Model2D.LeaderNote.StringsHeight`

Высота строк

### `SymbolType`

ID: `P:TFlex.Model.Model2D.LeaderNote.SymbolType`

Тип символа на стрелке

### `TextOnArrow`

ID: `P:TFlex.Model.Model2D.LeaderNote.TextOnArrow`

Текст на стрелке

### `TextOnLeader`

ID: `P:TFlex.Model.Model2D.LeaderNote.TextOnLeader`

Текст на полке надписи

### `TextUnderArrow`

ID: `P:TFlex.Model.Model2D.LeaderNote.TextUnderArrow`

Текст под стрелкой

### `TextUnderLeader`

ID: `P:TFlex.Model.Model2D.LeaderNote.TextUnderLeader`

Текст под полкой надписи
