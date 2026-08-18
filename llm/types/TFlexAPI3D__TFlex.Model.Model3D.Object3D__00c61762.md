# TFlex.Model.Model3D.Object3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для объектов 3D модели

## Methods

### `CancelRollback`

ID: `M:TFlex.Model.Model3D.Object3D.CancelRollback`

Завершить откат

### `Clone`

ID: `M:TFlex.Model.Model3D.Object3D.Clone`

Класс для передачи ссылки на геометрические свойства родительского объекта или на отдельные геометрические элементы тел модели (грани, циклы, рёбра, вершины)

### `CreateReference`

ID: `M:TFlex.Model.Model3D.Object3D.CreateReference`

Создаёт ссылочный элемент в исходном документе(внутренняя ссылка)

Returns: 3D объект

### `CreateReference(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Object3D.CreateReference(TFlex.Model.Document)`

Создаёт ссылочный элемент в указанном документе

Parameters:
- `targetDocument`: Документ, в котором создаётся ссылочный элемент

Returns: 3D объект

### `GetGeomReference(System.Int32)`

ID: `M:TFlex.Model.Model3D.Object3D.GetGeomReference(System.Int32)`

Получить ссылку на родительский объект по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект

Remarks: Поскольку геометрические данные связаны с родительской операцией, то саму родительскую операцию также можно получить по такому же ключу через функции `M:TFlex.Model.Model3D.Object3D.GetReference(System.Int32)` />

### `GetGeomReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.Model3D.Object3D.GetGeomReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

Получить ссылку на родительский объект по ключу и индексу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `indices`: Координаты элемента

Remarks: Используется для организации массивов. Поскольку геометрические данные связаны с родительской операцией, то саму родительскую операцию также можно получить по такому же ключу через функции `M:TFlex.Model.Model3D.Object3D.GetReference(System.Int32)` />

### `GetReference(System.Int32)`

ID: `M:TFlex.Model.Model3D.Object3D.GetReference(System.Int32)`

Получить ссылку на родительский объект по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект

### `GetReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.Model3D.Object3D.GetReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

Получить ссылку на родительский объект по ключу и индексу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `indices`: Координаты элемента

Remarks: Используется для организации массивов

### `RollbackToParents`

ID: `M:TFlex.Model.Model3D.Object3D.RollbackToParents`

Откат модели к состоянию, когда из сцены выгружены потомки объекта и он сам

Remarks: В сцене остаются прогруженными родителькие объекты

### `SetGeomReference(System.Int32,TFlex.Model.Model3D.Object3D.GeomReference)`

ID: `M:TFlex.Model.Model3D.Object3D.SetGeomReference(System.Int32,TFlex.Model.Model3D.Object3D.GeomReference)`

Установить ссылку на родительский объект по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `reference`: Ссылка на родительский объект

### `SetGeomReference(System.Int32,TFlex.Model.Model3D.Object3D.GeomReference,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.Model3D.Object3D.SetGeomReference(System.Int32,TFlex.Model.Model3D.Object3D.GeomReference,TFlex.Model.ModelObject.ArrayIndices)`

Установить ссылку на родительский объект по ключу и индексу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `reference`: Ссылка на родительский объект
- `indices`: Координаты элемента

Remarks: Используется для организации массивов

### `SetReference(System.Int32,TFlex.Model.ModelObject.Reference)`

ID: `M:TFlex.Model.Model3D.Object3D.SetReference(System.Int32,TFlex.Model.ModelObject.Reference)`

Установить ссылку на родительcкий объект по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `reference`: Ссылка на родительский объект

### `SetReference(System.Int32,TFlex.Model.ModelObject.Reference,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.Model3D.Object3D.SetReference(System.Int32,TFlex.Model.ModelObject.Reference,TFlex.Model.ModelObject.ArrayIndices)`

Установить ссылку на родительский объект по ключу и индексу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `reference`: Ссылка на родительский объект
- `indices`: Координаты элемента

Remarks: Используется для организации массивов

### `SetUniqueName(System.String)`

ID: `M:TFlex.Model.Model3D.Object3D.SetUniqueName(System.String)`

Установить новое уникальное имя с заданным префиксом

## Propertys

### `Auxiliary`

ID: `P:TFlex.Model.Model3D.Object3D.Auxiliary`

Внутрисистемный объект. Используется для Refer объектов фрагментов. Такие объекты скрыты от пользователя. Работа с такими объектами может быть реализована на уровне API.NET или ядром TFlex. Такие объекты не передаются на следующий уровень сборки.

### `Color`

ID: `P:TFlex.Model.Model3D.Object3D.Color`

Цвет

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `ConstTransformations`

ID: `P:TFlex.Model.Model3D.Object3D.ConstTransformations`

Преобразование 3D объекта для чтения (устаревшая версия трансформации - допускается чтение трансформации в старых документах.)

### `InScene`

ID: `P:TFlex.Model.Model3D.Object3D.InScene`

Объект в сцене

### `Layer`

ID: `P:TFlex.Model.Model3D.Object3D.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model3D.Object3D.Level`

Уровень

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Transformations`

ID: `P:TFlex.Model.Model3D.Object3D.Transformations`

Контейнер групп преобразований 3D объекта

### `VisibleInScene`

ID: `P:TFlex.Model.Model3D.Object3D.VisibleInScene`

Свойство видимости объекта

### `VolatileTransformations`

ID: `P:TFlex.Model.Model3D.Object3D.VolatileTransformations`

Преобразование 3D объекта для изменения
