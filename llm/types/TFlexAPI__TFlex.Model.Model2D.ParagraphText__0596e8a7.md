# TFlex.Model.Model2D.ParagraphText

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс параграф текста

## Constructors

### `ParagraphText(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ParagraphText.#ctor(TFlex.Model.Document)`

Конструктор для создания нового параграф текста

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `ParagraphText(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ParagraphText.#ctor(TFlex.Model.Document)`

Конструктор для создания нового параграф текста

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddRectangle(TFlex.Model.Model2D.ParagraphText.TextRectangle)`

ID: `M:TFlex.Model.Model2D.ParagraphText.AddRectangle(TFlex.Model.Model2D.ParagraphText.TextRectangle)`

Добавление прямоугольника в конец массива прямоугольников

Parameters:
- `rect`: Параметры нового прямоугольника

### `GetRectangle(System.UInt32)`

ID: `M:TFlex.Model.Model2D.ParagraphText.GetRectangle(System.UInt32)`

Получение параметров прямоугольника

Parameters:
- `index`: Порядковый номер прямоугольника

### `GetRectanglesCount`

ID: `M:TFlex.Model.Model2D.ParagraphText.GetRectanglesCount`

Получение количества прямоугольников

### `SetHeightAction(TFlex.Model.Model2D.ParagraphText.FitHeightAction,TFlex.Model.Model2D.ParagraphText.TextRectangle)`

ID: `M:TFlex.Model.Model2D.ParagraphText.SetHeightAction(TFlex.Model.Model2D.ParagraphText.FitHeightAction,TFlex.Model.Model2D.ParagraphText.TextRectangle)`

Действие при необходимости увеличить высоту прямоугольника

Remarks: TextRectangle должен быть задан свойствами LeftPoint и RightPoint

### `SetRectangle(System.UInt32,TFlex.Model.Model2D.ParagraphText.TextRectangle)`

ID: `M:TFlex.Model.Model2D.ParagraphText.SetRectangle(System.UInt32,TFlex.Model.Model2D.ParagraphText.TextRectangle)`

Установка параметров прямоугольника

Parameters:
- `index`: Порядковый номер прямоугольника
- `rect`: Новые параметры прямоугольника

## Propertys

### `EmptyRectangleAction`

ID: `P:TFlex.Model.Model2D.ParagraphText.EmptyRectangleAction`

Действие с пустым прямоугольником

### `HeightAction`

ID: `P:TFlex.Model.Model2D.ParagraphText.HeightAction`

Действие при необходимости увеличить высоту прямоугольника

### `Page`

ID: `P:TFlex.Model.Model2D.ParagraphText.Page`

Установить страницу

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `SubType`

ID: `P:TFlex.Model.Model2D.ParagraphText.SubType`

Получение подтипа текста для задания способа его задания

Returns: Значение подтипа текста

### `WidthAction`

ID: `P:TFlex.Model.Model2D.ParagraphText.WidthAction`

Действие при необходимости увеличить ширину прямоугольника
