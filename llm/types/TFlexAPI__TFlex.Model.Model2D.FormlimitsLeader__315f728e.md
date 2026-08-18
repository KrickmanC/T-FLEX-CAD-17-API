# TFlex.Model.Model2D.FormlimitsLeader

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс линии-выноски обозначения допуска формы

## Constructors

### `FormlimitsLeader(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.FormlimitsLeader.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объект

## Methods

### `FormlimitsLeader(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.FormlimitsLeader.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объект

### `SetConstruction(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.FormlimitsLeader.SetConstruction(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Установка параметров привязки к прямой

Parameters:
- `line`: Прямая
- `node`: Узел на прямой
- `offset`: Смещение точки привязки по прямой относительно узла

### `SetDimension(TFlex.Model.Model2D.Dimension,System.Boolean)`

ID: `M:TFlex.Model.Model2D.FormlimitsLeader.SetDimension(TFlex.Model.Model2D.Dimension,System.Boolean)`

Установка привязки к размеру

Parameters:
- `dim`: Размер привязки
- `isOnEnd`: Значение true указывает, что привязка выполняется к концу размера, false - к началу

### `SetFormlimitsObj(TFlex.Model.Model2D.Formlimits,System.Int32)`

ID: `M:TFlex.Model.Model2D.FormlimitsLeader.SetFormlimitsObj(TFlex.Model.Model2D.Formlimits,System.Int32)`

Установка привязки к обозначению допуска

Parameters:
- `obj`: Обозначение допуска привязки
- `position`: Номер точки привязки к таблице допуска (от 0 до 7)

### `SetOutline(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.FormlimitsLeader.SetOutline(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Parameter)`

Установка параметров привязки к отрезку

Parameters:
- `line`: Отрезок привязки
- `isOnEnd`: Значение true указывает, что привязка выполняется к концу отрезка, false - к началу
- `offset`: Смещение точки привязки по отрезку относительно выбранного конца отрезка

### `SetPoint(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.FormlimitsLeader.SetPoint(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка абсолютных координат точки привязки

Parameters:
- `x`: Координата x
- `y`: Координата y

## Propertys

### `ArrowSize`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.ArrowSize`

Размер стрелки

### `ArrowType`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.ArrowType`

Тип стрелки

### `Color`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `Construction`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Construction`

Линия построения, к которой привязана стрелка

### `Dimension`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Dimension`

Размер, к которому привязана стрелка

### `FontStyle`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.FontStyle`

Стиль шрифта текста для получения или установки его параметров

### `FormlimitsObj`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.FormlimitsObj`

Обозначение допуска, к которому привязан объект

### `Layer`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `LineWidth`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.LineWidth`

Толщина линий

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `Offsets`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Offsets`

Набор смещений, определяющих положение углов линии

### `Outline`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Outline`

Линия изображения, к которой привязана стрелка

### `Page`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Page`

Cтраница, на которой размещается объект

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Point`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Point`

Абсолютные координаты точки привязки

### `Position`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Position`

Номер точки привязки на таблице допуска (от 0 до 7)

### `Priority`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Priority`

Приоритет объекта

### `StartOffsetIsHoriz`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.StartOffsetIsHoriz`

Направление первого смещения: true - по горизонтали, false - по вертикали

### `X`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.X`

Координата X точки привязки

### `Y`

ID: `P:TFlex.Model.Model2D.FormlimitsLeader.Y`

Координата Y точки привязки
