# TFlex.Model.Model2D.RoughnessSymbol

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс символа шероховатости

## Constructors

### `RoughnessSymbol(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

## Methods

### `RoughnessSymbol(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

### `SetAbsolute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetAbsolute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки к абсолютным координатам

Parameters:
- `x`: Абцисса привязки
- `y`: Ордината привязки

### `SetCircle(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetCircle(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки к окружности

Parameters:
- `circle`: Окружность привязки
- `cosAngle`: Косинус угла, на котором находится точка привязки
- `sinAngle`: Синус угла, на котором находится точка привязки

### `SetCircularDimension(TFlex.Model.Model2D.CircularDimension,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetCircularDimension(TFlex.Model.Model2D.CircularDimension,TFlex.Model.Parameter)`

Установка параметров привязки к размеру на окружности

Parameters:
- `dim`: Размер для привязки
- `offset`: Смещение положения точки привязки от окружности

### `SetConstructionLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetConstructionLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Установка параметров привязки к прямой

Parameters:
- `line`: Прямая привязки
- `nod`: Узел привязки (на прямой)
- `offset`: Смещение точки привязки по прямой относительно узла

### `SetEllipse(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetEllipse(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

Установка параметров привязки к эллипсу

Parameters:
- `ellipse`: Эллипс привязки
- `parameter`: Параметр положения точки привязки на эллипсе

### `SetHeightParameter(TFlex.Model.Model2D.RoughnessHeightParameterType,System.String,System.String,System.String,System.String)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetHeightParameter(TFlex.Model.Model2D.RoughnessHeightParameterType,System.String,System.String,System.String,System.String)`

Установка типа и строк высотного параметра

Parameters:
- `parameterType`: Тип высотного параметра
- `minimum`: Минимум
- `maximumOrNominal`: Максимум или номинал
- `deviation`: Отклонение
- `basicLength`: Базовая длина

### `SetLeaderNote(TFlex.Model.Model2D.LeaderNote,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetLeaderNote(TFlex.Model.Model2D.LeaderNote,TFlex.Model.Parameter)`

Установка параметров привязки к надписи

Parameters:
- `note`: Надпись для привязки
- `offset`: Смещение положения точки привязки от стрелки надписи

### `SetLeaderOffset(System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetLeaderOffset(System.Double,System.Double)`

Установка смещения выносной полки шероховатости

Parameters:
- `dX`: Смещение относительно точки привязки в направлении касательной к линии привязки
- `dY`: Смещение относительно точки привязки в направлении перпендикулярном линии привязки

### `SetLinearDimension(TFlex.Model.Model2D.LinearDimension,System.Boolean,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetLinearDimension(TFlex.Model.Model2D.LinearDimension,System.Boolean,TFlex.Model.Parameter)`

Установка параметров привязки к линейному размеру

Parameters:
- `dim`: Размер для привязки
- `onSecondLine`: Параметр, к какой из линий размера осуществлять привязку
- `offset`: Смещение положения точки привязки от размерной линии

### `SetNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров привязки к узлу

Parameters:
- `nod`: Узел привязки
- `dX`: Смещение относительно узла привязки по оси X
- `dY`: Смещение относительно узла привязки по оси Y

### `SetOutlineLine(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetOutlineLine(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

Установка параметров привязки к отрезку

Parameters:
- `line`: Отрезок привязки
- `isOnEnd`: Указывает на то, что привязка происходит к концу отрезка (иначе - к началу)
- `offset`: Смещение точки привязки по отрезку относительно выбранного конца отрезка

### `SetPolyline(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetPolyline(TFlex.Model.Model2D.Object2D,TFlex.Model.Parameter)`

Установка параметров привязки к полилинии

Parameters:
- `polyline`: Полилиния привязки
- `parameter`: Параметр положения точки привязки на полилинии

### `SetRelativeLength(TFlex.Model.Model2D.RoughnessRelativeLengthType,System.String,System.String,System.String,System.String)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetRelativeLength(TFlex.Model.Model2D.RoughnessRelativeLengthType,System.String,System.String,System.String,System.String)`

Установка типа и строк относительной опорной длины

Parameters:
- `parameterType`: Тип относительной опорной длины
- `minimum`: Минимум
- `maximumOrNominal`: Максимум или номинал
- `deviation`: Отклонения
- `p`: Параметр "p"

### `SetStepParameter(TFlex.Model.Model2D.RoughnessStepParameterType,System.String,System.String,System.String,System.String)`

ID: `M:TFlex.Model.Model2D.RoughnessSymbol.SetStepParameter(TFlex.Model.Model2D.RoughnessStepParameterType,System.String,System.String,System.String,System.String)`

Установка типа и строк шагового параметра

Parameters:
- `parameterType`: Тип шагового параметра
- `minimum`: Минимум
- `maximumOrNominal`: Максимум или номинал
- `deviation`: Отклонение
- `basicLength`: Базовая длина

## Propertys

### `ArrowSize`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.ArrowSize`

Размер стрелки

### `ArrowType`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.ArrowType`

Тип стрелки

Remarks: При установки типа (-1) надпись будет рисоваться без стрелки

### `AttachmentType`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.AttachmentType`

Тип привязки шероховатости

### `Color`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `DrawExtLine`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.DrawExtLine`

Параметр рисования выносной линии

### `FontStyle`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.FontStyle`

Стиль шрифта текста для получения или установки его параметров

### `GroupType`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.GroupType`

Тип объекта

### `HeightParameter`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.HeightParameter`

Высотный параметр шероховатости

### `Layer`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `LeaderDirection`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.LeaderDirection`

Направление выносной полки шероховатости

### `Level`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `OldStyle`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.OldStyle`

Флаг рисования шероховатости без учёта изменений №3 ГОСТ 2.309-73

### `Page`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Priority`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.Priority`

Приоритет объекта

### `RelativeLengthParameter`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.RelativeLengthParameter`

Параметры относительной опорной длины

### `SignOrientation`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.SignOrientation`

Положение знака шероховатости

Remarks: Если значение равно 1, то знак рисуется под линией привязки

### `StepParameter`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.StepParameter`

Шаговый параметр шероховатости

### `SymbolType`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.SymbolType`

Вид значка шероховатости

### `TextAfter`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.TextAfter`

Строка текста после знака шероховатости

### `TextBefore`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.TextBefore`

Строка текста перед знаком шероховатости

### `TextDirection`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.TextDirection`

Строка текста - направление неровностей

### `TextInstruction`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.TextInstruction`

Установить строку текста - указание

### `UnsetType`

ID: `P:TFlex.Model.Model2D.RoughnessSymbol.UnsetType`

Вид неуказываемой шероховатости
