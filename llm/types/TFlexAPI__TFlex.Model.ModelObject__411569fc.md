# TFlex.Model.ModelObject

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Constructors

### `ModelObject(System.IntPtr,System.Boolean)`

ID: `M:TFlex.Model.ModelObject.#ctor(System.IntPtr,System.Boolean)`

Для внутреннего использования

## Methods

### `ModelObject(System.IntPtr,System.Boolean)`

ID: `M:TFlex.Model.ModelObject.#ctor(System.IntPtr,System.Boolean)`

Для внутреннего использования

### `Clone`

ID: `M:TFlex.Model.ModelObject.Clone`

Создаёт копию объекта

Returns: Объект, являющийся копией данного объекта

### `CompareTo(System.Object)`

ID: `M:TFlex.Model.ModelObject.CompareTo(System.Object)`

Сравнение объектов по идентификаторам

### `CopyProperties`

ID: `M:TFlex.Model.ModelObject.CopyProperties`

Копировать свойства в буфер

### `CreateStyle(System.IntPtr)`

ID: `M:TFlex.Model.ModelObject.CreateStyle(System.IntPtr)`

Для внутреннего использования

### `CreateStyle(System.IntPtr,System.IntPtr)`

ID: `M:TFlex.Model.ModelObject.CreateStyle(System.IntPtr,System.IntPtr)`

Для внутреннего использования

### `DependsOn(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObject.DependsOn(TFlex.Model.ModelObject)`

Проверка зависимости объектов

### `GetAttributes`

ID: `M:TFlex.Model.ModelObject.GetAttributes`

Контейнер атрибутов объекта. Приложение может использовать данный контейнер для хранения своих данных, связанных с объектом

### `GetFileLinkReference(System.Int32)`

ID: `M:TFlex.Model.ModelObject.GetFileLinkReference(System.Int32)`

Получить ссылку на файл по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится ссылка

Returns: Ссылка на файл

### `GetFileLinkReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.ModelObject.GetFileLinkReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

Получить ссылку на файл по ключу и индексу. Используется для организации массивов

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится ссылка
- `indices`: Координаты элемента

### `GetIntProp(System.String,System.Booleanref )`

ID: `M:TFlex.Model.ModelObject.GetIntProp(System.String,System.Boolean@)`

Измеримые свойства объекта

Parameters:
- `prop`: Имя свойства
- `exist`: Признак существования такого свойства

### `GetIntProperty(System.String)`

ID: `M:TFlex.Model.ModelObject.GetIntProperty(System.String)`

Получить значение свойства элемента

### `GetName(TFlex.Model.ModelObjectName)`

ID: `M:TFlex.Model.ModelObject.GetName(TFlex.Model.ModelObjectName)`

Получить имя объекта

Parameters:
- `nameType`: Тип имени

### `GetProperties`

ID: `M:TFlex.Model.ModelObject.GetProperties`

Получить описание свойств элемента

### `GetRealProp(System.String,System.Booleanref )`

ID: `M:TFlex.Model.ModelObject.GetRealProp(System.String,System.Boolean@)`

Измеримые свойства объекта

Parameters:
- `prop`: Имя свойства
- `exist`: Признак существования такого свойства

### `GetRealProperty(System.String)`

ID: `M:TFlex.Model.ModelObject.GetRealProperty(System.String)`

Получить значение свойства элемента

### `GetReference(System.Int32)`

ID: `M:TFlex.Model.ModelObject.GetReference(System.Int32)`

Получить ссылку на родительский объект по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект

### `GetReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.ModelObject.GetReference(System.Int32,TFlex.Model.ModelObject.ArrayIndices)`

Получить ссылку на родительский объект по ключу и индексу. Используется для организации массивов

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `indices`: Координаты элемента

### `GetRegenerationResult(System.Boolean)`

ID: `M:TFlex.Model.ModelObject.GetRegenerationResult(System.Boolean)`

Результат пересчета объекта

Parameters:
- `partialRegenAsSuccess`: Считать частичный пересчёт (с незначительными ошибками) как удавшийся

Returns: true - если пересчёт прошел успешно, иначе false

### `GetRelation(TFlex.Model.ModelObject,System.String)`

ID: `M:TFlex.Model.ModelObject.GetRelation(TFlex.Model.ModelObject,System.String)`

Измерить отношение двух объектов

Parameters:
- `other`: Второй объект
- `relationName`: Имя параметра для измерения, например Distance (см. команду Измерить в пользовательском интерфейсе)

### `GetTextProp(System.String,System.Booleanref )`

ID: `M:TFlex.Model.ModelObject.GetTextProp(System.String,System.Boolean@)`

Измеримые свойства объекта

Parameters:
- `prop`: Имя свойства
- `exist`: Признак существования такого свойства

### `GetTextProperty(System.String)`

ID: `M:TFlex.Model.ModelObject.GetTextProperty(System.String)`

Получить значение свойства элемента

### `IsKindOf(TFlex.Model.ObjectType)`

ID: `M:TFlex.Model.ModelObject.IsKindOf(TFlex.Model.ObjectType)`

Проверить принадлежность объекта указанному типу

Parameters:
- `type`: Тип для проверки

Returns: true если объект принадлежит указанному типу

### `MarkChanged`

ID: `M:TFlex.Model.ModelObject.MarkChanged`

Пометить объект как изменённый

### `Measure(TFlex.Model.ObjectArray,System.String,TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObject.Measure(TFlex.Model.ObjectArray,System.String,TFlex.Model.ModelObject)`

Измерить параметр одного объекта либо отношение нескольких объектов

Parameters:
- `objects`: Измеряемые объекты
- `valueName`: Имя параметра для измерения, например Distance (см. команду Измерить в пользовательском интерфейсе)
- `lcs`: Система координат

### `Measure(TFlex.Model.ObjectArray,TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObject.Measure(TFlex.Model.ObjectArray,TFlex.Model.ModelObject)`

Измерить все параметры одного объекта либо отношения нескольких объектов

Parameters:
- `objects`: Измеряемые объекты
- `lcs`: Система координат

### `PasteProperties`

ID: `M:TFlex.Model.ModelObject.PasteProperties`

Вставить свойства из буфера

### `Regenerate(System.Boolean)`

ID: `M:TFlex.Model.ModelObject.Regenerate(System.Boolean)`

Пересчитать объект

### `Replace(TFlex.Model.ModelObject,System.Boolean)`

ID: `M:TFlex.Model.ModelObject.Replace(TFlex.Model.ModelObject,System.Boolean)`

Заменить объект

Parameters:
- `source`: Исходный объект, который нужно заменить
- `deleteSource`: Удалить заменённый объект после замены

### `SetFileLinkReference(System.Int32,TFlex.Model.FileLink)`

ID: `M:TFlex.Model.ModelObject.SetFileLinkReference(System.Int32,TFlex.Model.FileLink)`

Установить ссылку на файл по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится ссылка
- `link`: Ссылка на файл

### `SetFileLinkReference(System.Int32,TFlex.Model.FileLink,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.ModelObject.SetFileLinkReference(System.Int32,TFlex.Model.FileLink,TFlex.Model.ModelObject.ArrayIndices)`

Установить ссылку на файл по ключу и индексу. Используется для организации массивов

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится ссылка
- `link`: Ссылка на файл
- `indices`: Координаты элемента

### `SetReference(System.Int32,TFlex.Model.ModelObject.Reference)`

ID: `M:TFlex.Model.ModelObject.SetReference(System.Int32,TFlex.Model.ModelObject.Reference)`

Установить ссылку на родительcкий объект по ключу

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `reference`: Ссылка на родительский объект

### `SetReference(System.Int32,TFlex.Model.ModelObject.Reference,TFlex.Model.ModelObject.ArrayIndices)`

ID: `M:TFlex.Model.ModelObject.SetReference(System.Int32,TFlex.Model.ModelObject.Reference,TFlex.Model.ModelObject.ArrayIndices)`

Установить ссылку на родительский объект по ключу и индексу. Используется для организации массивов

Parameters:
- `id`: Идентификатор ключа, по которому в контейнере ссылок хранится объект
- `reference`: Ссылка на родительский объект
- `indices`: Координаты элемента

## Propertys

### `DisplayName`

ID: `P:TFlex.Model.ModelObject.DisplayName`

Отображаемое название объекта

### `Document`

ID: `P:TFlex.Model.ModelObject.Document`

Документ, являющийся родительским для данного объекта

### `Editable`

ID: `P:TFlex.Model.ModelObject.Editable`

Объект находится в состоянии редактирования

### `GroupType`

ID: `P:TFlex.Model.ModelObject.GroupType`

Идентификатор типа данного объекта

Remarks: Возможные типы перечислены в перечислении ObjectType

### `ID`

ID: `P:TFlex.Model.ModelObject.ID`

Идентификатор объекта. Идентификатор является уникальным числом для каждого из объектов одного документа

Examples:
- `public static void ID(UInt32 ID) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа if(document.GetObjectByID(ID)!= null)//получение объекта по идентификатору { //действия с объектом } document.EndChanges();//Закрытие блока изменений документа }`

### `IsDisposed`

ID: `P:TFlex.Model.ModelObject.IsDisposed`

Объект удален из модели

### `IsInModelObjectGroup`

ID: `P:TFlex.Model.ModelObject.IsInModelObjectGroup`

Является ли объект элементом группы

### `IsVisible`

ID: `P:TFlex.Model.ModelObject.IsVisible`

Это свойство устарело и будет удалено. Пожалуйста, используйте свойство 'Visible'.

### `ModelObjectGroup`

ID: `P:TFlex.Model.ModelObject.ModelObjectGroup`

Группа, которая включает данный объект

### `Name`

ID: `P:TFlex.Model.ModelObject.Name`

Имя объекта

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `ObjectId`

ID: `P:TFlex.Model.ModelObject.ObjectId`

Идентификатор объекта. Идентификатор является уникальным для каждого из объектов одного документа

### `PageScale`

ID: `P:TFlex.Model.ModelObject.PageScale`

Масштаб страницы объекта

### `Parents`

ID: `P:TFlex.Model.ModelObject.Parents`

Контейнер родительских объектов

### `Visible`

ID: `P:TFlex.Model.ModelObject.Visible`

Является ли объект видимым
