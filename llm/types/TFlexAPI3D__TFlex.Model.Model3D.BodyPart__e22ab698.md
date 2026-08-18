# TFlex.Model.Model3D.BodyPart

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс тела в структуре модели

## Methods

### `CreatePart(TFlex.Model.Model3D.BodyPart.CreatePartOptions)`

ID: `M:TFlex.Model.Model3D.BodyPart.CreatePart(TFlex.Model.Model3D.BodyPart.CreatePartOptions)`

Создать деталь

Parameters:
- `options`: Параметры

Returns: Новый документ детали

### `GetOperationChain(System.UInt32)`

ID: `M:TFlex.Model.Model3D.BodyPart.GetOperationChain(System.UInt32)`

Получить операцию из цепочки тела

### `Unload(TFlex.Model.Model3D.BodyPart.UnloadBodyOptions)`

ID: `M:TFlex.Model.Model3D.BodyPart.Unload(TFlex.Model.Model3D.BodyPart.UnloadBodyOptions)`

Выгрузить деталь

Parameters:
- `options`: Параметры

Returns: Результат выгрузки

## Propertys

### `Active`

ID: `P:TFlex.Model.Model3D.BodyPart.Active`

Активное тело, не использовано в как заготовка в других телах

### `BaseOperation`

ID: `P:TFlex.Model.Model3D.BodyPart.BaseOperation`

Базовая операция в теле

### `CoatingMaterial`

ID: `P:TFlex.Model.Model3D.BodyPart.CoatingMaterial`

Покрытие

### `Color`

ID: `P:TFlex.Model.Model3D.BodyPart.Color`

Цвет

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `CountOperationChain`

ID: `P:TFlex.Model.Model3D.BodyPart.CountOperationChain`

Количество операций в цепочке тела

### `Layer`

ID: `P:TFlex.Model.Model3D.BodyPart.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model3D.BodyPart.Level`

Уровень

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Material`

ID: `P:TFlex.Model.Model3D.BodyPart.Material`

Материал

### `MeshDensity`

ID: `P:TFlex.Model.Model3D.BodyPart.MeshDensity`

Плотность сетки в диапазоне 0.0-1.0

### `Name`

ID: `P:TFlex.Model.Model3D.BodyPart.Name`

Имя тела

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `Suppression`

ID: `P:TFlex.Model.Model3D.BodyPart.Suppression`

Свойство подавленности операции

### `TopOperation`

ID: `P:TFlex.Model.Model3D.BodyPart.TopOperation`

Верхняя операция в теле

### `UseBodyAttributes`

ID: `P:TFlex.Model.Model3D.BodyPart.UseBodyAttributes`

Установлены атрибуты

### `Virtual`

ID: `P:TFlex.Model.Model3D.BodyPart.Virtual`

Виртуальное тело, состоит из одной операции - типа 3D фрагмент или массив(копия, симметрия)

### `Wireframe`

ID: `P:TFlex.Model.Model3D.BodyPart.Wireframe`

Признак рёберной отрисовки операции
