# TFlex.Model.Model2D.Picture

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс картинки

## Constructors

### `Picture(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Picture.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объекта

### `Picture(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.Model2D.Picture.#ctor(TFlex.Model.Document,System.String)`

Конструктор с именем файла картинки

Parameters:
- `Doc`: Документ объекта
- `filePath`: Имя файла картинки

### `Picture(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model2D.Picture.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла картинки

Parameters:
- `link`: Ссылка на файл картинки

## Methods

### `Picture(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Picture.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ объекта

### `Picture(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.Model2D.Picture.#ctor(TFlex.Model.Document,System.String)`

Конструктор с именем файла картинки

Parameters:
- `Doc`: Документ объекта
- `filePath`: Имя файла картинки

### `Picture(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model2D.Picture.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла картинки

Parameters:
- `link`: Ссылка на файл картинки

## Propertys

### `Angle`

ID: `P:TFlex.Model.Model2D.Picture.Angle`

Угол поворота картинки

### `FileLink`

ID: `P:TFlex.Model.Model2D.Picture.FileLink`

Ссылка на файл картинки

### `FilePath`

ID: `P:TFlex.Model.Model2D.Picture.FilePath`

Имя файла картинки

### `FullFilePath`

ID: `P:TFlex.Model.Model2D.Picture.FullFilePath`

Полный путь файла картинки

### `GroupType`

ID: `P:TFlex.Model.Model2D.Picture.GroupType`

Тип объекта

### `IsMultipage`

ID: `P:TFlex.Model.Model2D.Picture.IsMultipage`

true, если картинка содержит несколько страниц

### `Layer`

ID: `P:TFlex.Model.Model2D.Picture.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.Picture.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Node1`

ID: `P:TFlex.Model.Model2D.Picture.Node1`

Первый узел привязки картинки

### `Node2`

ID: `P:TFlex.Model.Model2D.Picture.Node2`

Второй узел привязки картинки

### `Page`

ID: `P:TFlex.Model.Model2D.Picture.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `PictureFixingMode`

ID: `P:TFlex.Model.Model2D.Picture.PictureFixingMode`

Способ привязки картинки

### `Priority`

ID: `P:TFlex.Model.Model2D.Picture.Priority`

Приоритет объекта

### `Scale`

ID: `P:TFlex.Model.Model2D.Picture.Scale`

Масштаб изображения

### `ShownPageCount`

ID: `P:TFlex.Model.Model2D.Picture.ShownPageCount`

Количество страниц изображения

### `ShownPageID`

ID: `P:TFlex.Model.Model2D.Picture.ShownPageID`

ID отображаемой страницы чертежа

Remarks: Используется только для чертежей T-Flex

### `ShownPageIndex`

ID: `P:TFlex.Model.Model2D.Picture.ShownPageIndex`

Индекс отображаемой страницы

Remarks: Для чертежей T-Flex не используется

### `ShownPageName`

ID: `P:TFlex.Model.Model2D.Picture.ShownPageName`

Имя отображаемой страницы

### `X1`

ID: `P:TFlex.Model.Model2D.Picture.X1`

Координата X первой точки привязки

### `X2`

ID: `P:TFlex.Model.Model2D.Picture.X2`

Координата X второй точки привязки

### `Y1`

ID: `P:TFlex.Model.Model2D.Picture.Y1`

Координата Y первой точки привязки

### `Y2`

ID: `P:TFlex.Model.Model2D.Picture.Y2`

Координата Y второй точки привязки
