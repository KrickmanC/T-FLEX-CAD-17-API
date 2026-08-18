# TFlex.Model.Model3D.Section3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех типов сечений

## Constructors

### `Section3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Section3D.#ctor(TFlex.Model.Document)`

Конструктор для создания нового сечения

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `Section3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Section3D.#ctor(TFlex.Model.Document)`

Конструктор для создания нового сечения

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `Geometry`

ID: `P:TFlex.Model.Model3D.Section3D.Geometry`

Получить геометрические данные сечения

### `GroupType`

ID: `P:TFlex.Model.Model3D.Section3D.GroupType`

Тип объекта

### `Orientation`

ID: `P:TFlex.Model.Model3D.Section3D.Orientation`

Направление сечения

Remarks: По умолчанию значение ориентации false

### `Page`

ID: `P:TFlex.Model.Model3D.Section3D.Page`

Страница

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `ShowOn3D`

ID: `P:TFlex.Model.Model3D.Section3D.ShowOn3D`

Признак рисования сечения в 3D сцене

### `UseColorFromBody`

ID: `P:TFlex.Model.Model3D.Section3D.UseColorFromBody`

Признак использования цвета с тела
