# TFlex.Model.Model2D.Construction

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс линии построения

## Methods

### `UpdateLimits`

ID: `M:TFlex.Model.Model2D.Construction.UpdateLimits`

Обновление выступания линии построения

## Propertys

### `Color`

ID: `P:TFlex.Model.Model2D.Construction.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `ConstructionGeometry`

ID: `P:TFlex.Model.Model2D.Construction.ConstructionGeometry`

Геометрия линии построения

Remarks: После использования рекомендуется удалить полученную геометрию, использую функцию Dispose().

### `GeometryType`

ID: `P:TFlex.Model.Model2D.Construction.GeometryType`

Тип геометрии линии построения

### `GroupType`

ID: `P:TFlex.Model.Model2D.Construction.GroupType`

Тип объекта

### `IsFixedPosition`

ID: `P:TFlex.Model.Model2D.Construction.IsFixedPosition`

Lock position of line

### `IsFixedPositionLocked`

ID: `P:TFlex.Model.Model2D.Construction.IsFixedPositionLocked`

Block the ability to control fixation of construction line from interface

### `Layer`

ID: `P:TFlex.Model.Model2D.Construction.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.Construction.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Page`

ID: `P:TFlex.Model.Model2D.Construction.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Param`

ID: `P:TFlex.Model.Model2D.Construction.Param`

Значение параметра линии построения. Тип параметра зависит от типа линии построения.

### `SubType`

ID: `P:TFlex.Model.Model2D.Construction.SubType`

Подтип линии построения
