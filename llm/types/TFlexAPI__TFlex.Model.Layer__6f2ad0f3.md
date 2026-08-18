# TFlex.Model.Layer

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс слоя

## Constructors

### `Layer(TFlex.Model.Document)`

ID: `M:TFlex.Model.Layer.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `doc`: Документ слоя

## Methods

### `Layer(TFlex.Model.Document)`

ID: `M:TFlex.Model.Layer.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `doc`: Документ слоя

## Propertys

### `Color`

ID: `P:TFlex.Model.Layer.Color`

Цвет слоя

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `ColorVariable`

ID: `P:TFlex.Model.Layer.ColorVariable`

Переменная цвета слоя

### `Frozen`

ID: `P:TFlex.Model.Layer.Frozen`

Параметр слоя "замороженный"

### `GroupType`

ID: `P:TFlex.Model.Layer.GroupType`

Тип объекта

### `Hidden`

ID: `P:TFlex.Model.Layer.Hidden`

Параметр слоя "невидимый"

### `HiddenOnFragment`

ID: `P:TFlex.Model.Layer.HiddenOnFragment`

Параметр слоя "невидимый на фрагменте"

### `HiddenVariable`

ID: `P:TFlex.Model.Layer.HiddenVariable`

Переменная, задающая параметр слоя "невидимый"

### `LineWidth`

ID: `P:TFlex.Model.Layer.LineWidth`

Значение толщины линии

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `Monochrome`

ID: `P:TFlex.Model.Layer.Monochrome`

Параметр слоя "одноцветный"

### `Name`

ID: `P:TFlex.Model.Layer.Name`

Имя слоя

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `ProgrammaticallyFrozen`

ID: `P:TFlex.Model.Layer.ProgrammaticallyFrozen`

Параметр слоя "замороженный". Недоступно из пользовательского интерфейса.

### `Screen`

ID: `P:TFlex.Model.Layer.Screen`

Параметр слоя "экранный"

### `SetLineWidth`

ID: `P:TFlex.Model.Layer.SetLineWidth`

Параметр слоя "Установлена толщина линии"

### `VisibleOnlyOnFragment`

ID: `P:TFlex.Model.Layer.VisibleOnlyOnFragment`

Параметр слоя "видимый только на фрагменте"
