# TFlex.Model.Model2D.ExternalObject

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Methods

### `ResetPlugin(TFlex.Plugin,System.Int32)`

ID: `M:TFlex.Model.Model2D.ExternalObject.ResetPlugin(TFlex.Plugin,System.Int32)`

Перезадать приложение, определяющее промежуточный (прокси-) объект

## Propertys

### `Color`

ID: `P:TFlex.Model.Model2D.ExternalObject.Color`

Цвет

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `Layer`

ID: `P:TFlex.Model.Model2D.ExternalObject.Layer`

Слой

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.ExternalObject.Level`

Уровень

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Page`

ID: `P:TFlex.Model.Model2D.ExternalObject.Page`

Страница

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Priority`

ID: `P:TFlex.Model.Model2D.ExternalObject.Priority`

Приоритет
