# TFlex.Model.Model2D.Area

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Область штриховки/заливки

## Constructors

### `Area(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Area.#ctor(TFlex.Model.Document)`

Конструктор

## Methods

### `Area(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Area.#ctor(TFlex.Model.Document)`

Конструктор

### `AppendContour`

ID: `M:TFlex.Model.Model2D.Area.AppendContour`

Добавление контура

### `ApplyContours`

ID: `M:TFlex.Model.Model2D.Area.ApplyContours`

Подтвердить создание автоматически найденных контуров

Returns: true, если создан хотя бы один контур

### `DeleteAllContours`

ID: `M:TFlex.Model.Model2D.Area.DeleteAllContours`

Удаление всех контуров

### `DeleteContour(System.Int32)`

ID: `M:TFlex.Model.Model2D.Area.DeleteContour(System.Int32)`

Удаление контура по указанному индексу

Parameters:
- `index`: Индекс (номер) контура

### `Dispose`

ID: `M:TFlex.Model.Model2D.Area.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `FindContour(System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.Area.FindContour(System.Double,System.Double)`

Автоматический поиск контуров штриховки по точке.

Parameters:
- `x`: Координата X точки поиска
- `y`: Координата Y точки поиска

Returns: true, если найден хотя бы один контур

Remarks: Последовательность вызовов данной функции должна завершаться вызовом функции ApplyContours

### `FindContour(System.Double,System.Double,TFlex.Model.Model2D.FindAreaContourOptions)`

ID: `M:TFlex.Model.Model2D.Area.FindContour(System.Double,System.Double,TFlex.Model.Model2D.FindAreaContourOptions)`

Автоматический поиск контуров штриховки по точке.

Parameters:
- `x`: Координата X точки поиска
- `y`: Координата Y точки поиска
- `options`: Опции поиска контуров

Returns: true, если найден хотя бы один контур

Remarks: Последовательность вызовов данной функции должна завершаться вызовом функции ApplyContours

### `GetContour(System.Int32)`

ID: `M:TFlex.Model.Model2D.Area.GetContour(System.Int32)`

Получение контура по указанному индексу

Parameters:
- `index`: Индекс (номер) контура

Returns: Контур с указанным индексом

### `InsertContour(System.Int32)`

ID: `M:TFlex.Model.Model2D.Area.InsertContour(System.Int32)`

Вставка контура по указанному индексу

Parameters:
- `index`: Индекс (номер) контура

Returns: Вставляемый контур

### `MakeCopy(TFlex.Model.Document,System.Double,System.Double,System.Double,System.Double,System.Boolean)`

ID: `M:TFlex.Model.Model2D.Area.MakeCopy(TFlex.Model.Document,System.Double,System.Double,System.Double,System.Double,System.Boolean)`

Создает копию штриховки в другом документе.

### `get_ContourCount`

ID: `M:TFlex.Model.Model2D.Area.get_ContourCount`

Returns: Количества контуров штриховки

## Propertys

### `Circular`

ID: `P:TFlex.Model.Model2D.Area.Circular`

Параметр "Круговая штриховка"

Remarks: Данный метод выполняет указанное действие только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Hatch.

### `Color`

ID: `P:TFlex.Model.Model2D.Area.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `ContourCount`

ID: `P:TFlex.Model.Model2D.Area.ContourCount`

Количество контуров штриховки

### `EraseBackground`

ID: `P:TFlex.Model.Model2D.Area.EraseBackground`

Параметр "невидимые линии" (очистка фона)

### `FillStyle`

ID: `P:TFlex.Model.Model2D.Area.FillStyle`

Способ заполнения контура

### `GroupType`

ID: `P:TFlex.Model.Model2D.Area.GroupType`

Тип объекта

### `HatchAngle1`

ID: `P:TFlex.Model.Model2D.Area.HatchAngle1`

Первый угол штриховки контура

Remarks: Данное свойство имеет смысл только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Hatch

### `HatchAngle2`

ID: `P:TFlex.Model.Model2D.Area.HatchAngle2`

Второй угол штриховки контура

Remarks: Данное свойство имеет смысл только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Hatch

### `HatchStep1`

ID: `P:TFlex.Model.Model2D.Area.HatchStep1`

Первый шаг штриховки контура

Remarks: Данный метод выполняет указанное действие только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Hatch

### `HatchStep2`

ID: `P:TFlex.Model.Model2D.Area.HatchStep2`

Второй шаг штриховки контура

Remarks: Данный метод выполняет указанное действие только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Hatch

### `Layer`

ID: `P:TFlex.Model.Model2D.Area.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.Area.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `LineWidth`

ID: `P:TFlex.Model.Model2D.Area.LineWidth`

Толщина линии

Remarks: Данный метод выполняет указанное действие только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Hatch или `T:TFlex.Model.Model2D.AreaFillStyle` .Pattern.

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `Outline`

ID: `P:TFlex.Model.Model2D.Area.Outline`

Наличие обводки у контуров штриховки

### `OutlineColor`

ID: `P:TFlex.Model.Model2D.Area.OutlineColor`

Цвет линий обводки

### `OutlinePatternName`

ID: `P:TFlex.Model.Model2D.Area.OutlinePatternName`

Имя образца штриховой линии обводки

### `OutlinePatternScale`

ID: `P:TFlex.Model.Model2D.Area.OutlinePatternScale`

Масштаб штрихов линий обводки

### `OutlineWidth`

ID: `P:TFlex.Model.Model2D.Area.OutlineWidth`

Толщина линий обводки

### `Page`

ID: `P:TFlex.Model.Model2D.Area.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `PatternAngle`

ID: `P:TFlex.Model.Model2D.Area.PatternAngle`

Угол штриховки по образцу

Remarks: Данный метод выполняет указанное действие только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Pattern

### `PatternName`

ID: `P:TFlex.Model.Model2D.Area.PatternName`

Имя штриховки по образцу

Remarks: Данный метод выполняет указанное действие только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Pattern

### `PatternScale`

ID: `P:TFlex.Model.Model2D.Area.PatternScale`

Значение масштаба штриховки по образцу

Remarks: Данный метод выполняет указанное действие только в случае, если способ заполнения контура имеет значение `T:TFlex.Model.Model2D.AreaFillStyle` .Pattern

### `Priority`

ID: `P:TFlex.Model.Model2D.Area.Priority`

Приоритет объекта

### `Width`

ID: `P:TFlex.Model.Model2D.Area.Width`

Толщина линий обводки
