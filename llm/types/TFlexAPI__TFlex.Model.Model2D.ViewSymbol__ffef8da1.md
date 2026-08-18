# TFlex.Model.Model2D.ViewSymbol

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс обозначения вида, разреза или сечения

## Propertys

### `Color`

ID: `P:TFlex.Model.Model2D.ViewSymbol.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `FontStyle`

ID: `P:TFlex.Model.Model2D.ViewSymbol.FontStyle`

Стиль шрифта текста для получения или установки его параметров

### `GroupType`

ID: `P:TFlex.Model.Model2D.ViewSymbol.GroupType`

Тип объекта

### `Layer`

ID: `P:TFlex.Model.Model2D.ViewSymbol.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.ViewSymbol.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Page`

ID: `P:TFlex.Model.Model2D.ViewSymbol.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Priority`

ID: `P:TFlex.Model.Model2D.ViewSymbol.Priority`

Приоритет объекта
