# TFlex.Model.Model2D.Node

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс 2D узла

## Propertys

### `AbsX`

ID: `P:TFlex.Model.Model2D.Node.AbsX`

Координата X в системе координат модели (без учёта масштаба страницы)

### `AbsY`

ID: `P:TFlex.Model.Model2D.Node.AbsY`

Координата Y в системе координат модели (без учёта масштаба страницы)

### `Color`

ID: `P:TFlex.Model.Model2D.Node.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `Coordinates`

ID: `P:TFlex.Model.Model2D.Node.Coordinates`

Координаты узла в системе координат модели (без учёта масштаба страницы)

### `GroupType`

ID: `P:TFlex.Model.Model2D.Node.GroupType`

Тип объекта

### `Layer`

ID: `P:TFlex.Model.Model2D.Node.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.Node.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Page`

ID: `P:TFlex.Model.Model2D.Node.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `SubType`

ID: `P:TFlex.Model.Model2D.Node.SubType`

Подтип способа построения узла
