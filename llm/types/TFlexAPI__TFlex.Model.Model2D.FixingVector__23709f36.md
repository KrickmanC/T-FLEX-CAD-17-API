# TFlex.Model.Model2D.FixingVector

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс вектора привязки

## Constructors

### `FixingVector(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.FixingVector.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

## Methods

### `FixingVector(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.FixingVector.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

### `FindByFragment(TFlex.Model.Model2D.Fragment)`

ID: `M:TFlex.Model.Model2D.FixingVector.FindByFragment(TFlex.Model.Model2D.Fragment)`

Найти все коннекторы поднятые из фрагмента

Parameters:
- `fragment`: Родительский фрагмент

## Propertys

### `Color`

ID: `P:TFlex.Model.Model2D.FixingVector.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `Comment`

ID: `P:TFlex.Model.Model2D.FixingVector.Comment`

Комментарий (Имя)

### `EndNode`

ID: `P:TFlex.Model.Model2D.FixingVector.EndNode`

Конечный узел

### `EndPoint`

ID: `P:TFlex.Model.Model2D.FixingVector.EndPoint`

Конечная точка

### `GroupType`

ID: `P:TFlex.Model.Model2D.FixingVector.GroupType`

Идентификатор типа объекта

### `Level`

ID: `P:TFlex.Model.Model2D.FixingVector.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Page`

ID: `P:TFlex.Model.Model2D.FixingVector.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `StartNode`

ID: `P:TFlex.Model.Model2D.FixingVector.StartNode`

Начальный узел

### `StartPoint`

ID: `P:TFlex.Model.Model2D.FixingVector.StartPoint`

Начальная точка

### `UseOnlyFirstPoint`

ID: `P:TFlex.Model.Model2D.FixingVector.UseOnlyFirstPoint`

Использовать только первую точку

Remarks: При установке данного свойства в true, второй узел удаляется. При установки данного свойства в false, после вызова данного свойства необходимо заново задать второй узел с помощью свойства `P:TFlex.Model.Model2D.FixingVector.EndNode`
