# TFlex.Model.Page

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс страницы документа

## Constructors

### `Page(TFlex.Model.Document)`

ID: `M:TFlex.Model.Page.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ страницы

### `Page(TFlex.Model.Document,TFlex.Model.PageType)`

ID: `M:TFlex.Model.Page.#ctor(TFlex.Model.Document,TFlex.Model.PageType)`

Конструктор

Parameters:
- `document`: Документ страницы
- `pageType`: Тип страницы

### `Page(TFlex.Model.Page)`

ID: `M:TFlex.Model.Page.#ctor(TFlex.Model.Page)`

Конструктор

Parameters:
- `source`: Страница

## Methods

### `Page(TFlex.Model.Document)`

ID: `M:TFlex.Model.Page.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ страницы

### `Page(TFlex.Model.Document,TFlex.Model.PageType)`

ID: `M:TFlex.Model.Page.#ctor(TFlex.Model.Document,TFlex.Model.PageType)`

Конструктор

Parameters:
- `document`: Документ страницы
- `pageType`: Тип страницы

### `Page(TFlex.Model.Page)`

ID: `M:TFlex.Model.Page.#ctor(TFlex.Model.Page)`

Конструктор

Parameters:
- `source`: Страница

### `PrepareGraphics(TFlex.Drawing.Graphics)`

ID: `M:TFlex.Model.Page.PrepareGraphics(TFlex.Drawing.Graphics)`

Подготовка графического контекста для прорисовки на данной странице

Parameters:
- `graphics`: Графический контекст

### `ResetName`

ID: `M:TFlex.Model.Page.ResetName`

Перезадать имя страницы согласно правилам именования страниц

Remarks: Актуально после смены типа страницы

## Propertys

### `AngularDimensionMinimalDigits`

ID: `P:TFlex.Model.Page.AngularDimensionMinimalDigits`

Минимальное количество цифр после точки для угловых размеров

### `AngularDimensionPrecision`

ID: `P:TFlex.Model.Page.AngularDimensionPrecision`

Точность угловых размеров

### `AngularDimensionUnits`

ID: `P:TFlex.Model.Page.AngularDimensionUnits`

Единицы измерения угловых размеров

### `Bottom`

ID: `P:TFlex.Model.Page.Bottom`

Нижняя Y-координата границ бумаги

### `DefaultArrowSize`

ID: `P:TFlex.Model.Page.DefaultArrowSize`

Размер стрелок по умолчанию

### `DegreeCode`

ID: `P:TFlex.Model.Page.DegreeCode`

Код символа "градус"

### `DiameterCode`

ID: `P:TFlex.Model.Page.DiameterCode`

Код символа "диаметр"

### `DimensionQuality`

ID: `P:TFlex.Model.Page.DimensionQuality`

Квалитет размеров по умолчанию

### `DrawingLimits`

ID: `P:TFlex.Model.Page.DrawingLimits`

Прямоугольник границ элементов страницы

### `FontStyle`

ID: `P:TFlex.Model.Page.FontStyle`

Стиль шрифта текста

### `FragmentForNewPageFileLink`

ID: `P:TFlex.Model.Page.FragmentForNewPageFileLink`

Ссылка на документ, который будет вставлен, как фрагмент, при создании страницы, следующей за этой страницей

### `GroupType`

ID: `P:TFlex.Model.Page.GroupType`

Идентификатор типа объекта

### `IndexSymbolScale`

ID: `P:TFlex.Model.Page.IndexSymbolScale`

Масштаб подстрочных и надстрочных символов

### `IsSelectedForExporting`

ID: `P:TFlex.Model.Page.IsSelectedForExporting`

Страница, выбранная для экспорта

### `IsSelectedForPrinting`

ID: `P:TFlex.Model.Page.IsSelectedForPrinting`

Страница, выбранная для печати

### `Left`

ID: `P:TFlex.Model.Page.Left`

Левая X-координата границ бумаги

### `LinePatternScale`

ID: `P:TFlex.Model.Page.LinePatternScale`

Масштаб штрихов штриховых линий по умолчанию

### `LinearDimensionMinimalDigits`

ID: `P:TFlex.Model.Page.LinearDimensionMinimalDigits`

Минимальное количество цифр после точки для линейных размеров

### `LinearDimensionPrecision`

ID: `P:TFlex.Model.Page.LinearDimensionPrecision`

Точность линейных размеров

### `LinearDimensionUnits`

ID: `P:TFlex.Model.Page.LinearDimensionUnits`

Единицы измерения линейных размеров

### `Name`

ID: `P:TFlex.Model.Page.Name`

Имя страницы

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `PageType`

ID: `P:TFlex.Model.Page.PageType`

Тип страницы

### `PlusMinusCode`

ID: `P:TFlex.Model.Page.PlusMinusCode`

Код символа "плюс-минус"

### `Rank`

ID: `P:TFlex.Model.Page.Rank`

Порядковый номер страницы

### `Rectangle`

ID: `P:TFlex.Model.Page.Rectangle`

Прямоугольник границ страницы

### `Right`

ID: `P:TFlex.Model.Page.Right`

Правая X-координата границ бумаги

### `Scale`

ID: `P:TFlex.Model.Page.Scale`

Масштаб страницы

### `SelectionMode`

ID: `P:TFlex.Model.Page.SelectionMode`

Режим выбора элементов

### `SymbolFontName`

ID: `P:TFlex.Model.Page.SymbolFontName`

Имя символьного шрифта

### `ThickLineThickness`

ID: `P:TFlex.Model.Page.ThickLineThickness`

Толщина основных линий по умолчанию

### `ThinLineThickness`

ID: `P:TFlex.Model.Page.ThinLineThickness`

Толщина тонких линий по умолчанию

### `Top`

ID: `P:TFlex.Model.Page.Top`

Верхняя Y-координата границ бумаги
