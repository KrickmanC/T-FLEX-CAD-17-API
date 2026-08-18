# TFlex.Model.ProxyObject

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс прокси объекта

## Constructors

### `ProxyObject`

ID: `M:TFlex.Model.ProxyObject.#ctor`

Конструктор

### `ProxyObject(System.IntPtr)`

ID: `M:TFlex.Model.ProxyObject.#ctor(System.IntPtr)`

Конструктор, принимающий родительский объект

Parameters:
- `OwnerHandle`: 

## Methods

### `ProxyObject`

ID: `M:TFlex.Model.ProxyObject.#ctor`

Конструктор

### `ProxyObject(System.IntPtr)`

ID: `M:TFlex.Model.ProxyObject.#ctor(System.IntPtr)`

Конструктор, принимающий родительский объект

Parameters:
- `OwnerHandle`: 

### `AddDiagnosticsMessage(TFlex.Model.DiagnosticsMessage)`

ID: `M:TFlex.Model.ProxyObject.AddDiagnosticsMessage(TFlex.Model.DiagnosticsMessage)`

Добавить диагностическое сообщение. Надо вызывать из Draw

Parameters:
- `message`: Сообщение

### `CanAddDiagnosticsMessage`

ID: `M:TFlex.Model.ProxyObject.CanAddDiagnosticsMessage`

Можно ли добавить диагностическое сообщение.

### `Clone(System.IntPtr)`

ID: `M:TFlex.Model.ProxyObject.Clone(System.IntPtr)`

Метод создает неполную копию прокси объекта

Parameters:
- `OwnerHandle`: 

Returns: Новый прокси объект, который является неполной копией текущего

### `Draw(TFlex.Drawing.Graphics)`

ID: `M:TFlex.Model.ProxyObject.Draw(TFlex.Drawing.Graphics)`

Метод для прорисовки объекта

Parameters:
- `graphics`: Объект класса `T:TFlex.Drawing.Graphics`

### `Draw(TFlex.Model.ProxyObjectDrawContext)`

ID: `M:TFlex.Model.ProxyObject.Draw(TFlex.Model.ProxyObjectDrawContext)`

Метод для прорисовки объекта

Parameters:
- `context`: Объект класса `T:TFlex.Model.ProxyObjectDrawContext`

### `Edit(TFlex.Model.View)`

ID: `M:TFlex.Model.ProxyObject.Edit(TFlex.Model.View)`

Виртуальный метод изменения прокси объекта

Parameters:
- `View`: Вид

### `EditProperties`

ID: `M:TFlex.Model.ProxyObject.EditProperties`

Метод для редактирования свойств прокси объекта

Returns: Результат изменения свойств прокси объекта

### `Equals(TFlex.Model.ProxyObject)`

ID: `M:TFlex.Model.ProxyObject.Equals(TFlex.Model.ProxyObject)`

Метод выполняет сравнение прокси объекта `T:TFlex.Model.ProxyObject` с исходным

Parameters:
- `object`: Прокси объект, с которым сравнивает текущий прокси объект

Returns: true, если объекты одинаковы, в противном случае false

### `GetContextMenu(TFlex.Menu)`

ID: `M:TFlex.Model.ProxyObject.GetContextMenu(TFlex.Menu)`

Метод вызывается при вызове контекстного меню прокси объекта

Parameters:
- `Menu`: Контекстное меню

Remarks: В реализации данного метода можно добавить или удалить команды

### `GetMarkObjects`

ID: `M:TFlex.Model.ProxyObject.GetMarkObjects`

Получить список дополнительных объектов для пометки при выборе

### `GetNode(System.Int32,System.Doubleref ,System.Doubleref )`

ID: `M:TFlex.Model.ProxyObject.GetNode(System.Int32,System.Double@,System.Double@)`

Получить координаты узла привязки по ID

Parameters:
- `id`: ID узла
- `x`: Координата x узла
- `y`: Координата y узла

### `GetNodeCount`

ID: `M:TFlex.Model.ProxyObject.GetNodeCount`

Получить количество узлов в модели

### `GetNodeID(System.Int32)`

ID: `M:TFlex.Model.ProxyObject.GetNodeID(System.Int32)`

Получить идентификатор узла по номеру

Parameters:
- `Number`: Номер узла модели

### `GetPropList(TFlex.Model.PropertyArray)`

ID: `M:TFlex.Model.ProxyObject.GetPropList(TFlex.Model.PropertyArray)`

Получить массив свойств

Parameters:
- `Array`: Ссылка на массив

### `GetRealProp(System.String)`

ID: `M:TFlex.Model.ProxyObject.GetRealProp(System.String)`

Получить значение свойства с действительным значением по имени

Parameters:
- `name`: Имя свойства

### `GetTextProp(System.String)`

ID: `M:TFlex.Model.ProxyObject.GetTextProp(System.String)`

Получить значение текстового свойства по имени

Parameters:
- `name`: Имя свойства

### `IsReallyChanged`

ID: `M:TFlex.Model.ProxyObject.IsReallyChanged`

изменился ли в действительности прокси объект

### `OnCommand(System.Int32,TFlex.Model.View)`

ID: `M:TFlex.Model.ProxyObject.OnCommand(System.Int32,TFlex.Model.View)`

Метод для обработки команд контекстного меню

Parameters:
- `commandID`: Идентификатор команды объекта
- `view`: Вид документа

### `OnDelete`

ID: `M:TFlex.Model.ProxyObject.OnDelete`

Событие возникающее при удалении прокси объекта

### `OnUndoAction(TFlex.Model.ProxyObject.UndoActionType)`

ID: `M:TFlex.Model.ProxyObject.OnUndoAction(TFlex.Model.ProxyObject.UndoActionType)`

Обработчик события отмены

Parameters:
- `type`: Тип отмены

### `Read(System.IO.Stream,System.Int32)`

ID: `M:TFlex.Model.ProxyObject.Read(System.IO.Stream,System.Int32)`

Метод для считывания данных прокси объекта из файла

Parameters:
- `stream`: Поток из которого происходит считывание данных
- `Version`: Версия объекта, на момент сохранения объекта в файл

### `Write(System.IO.Stream)`

ID: `M:TFlex.Model.ProxyObject.Write(System.IO.Stream)`

Метод для записи данных прокси объекта в файл

Parameters:
- `stream`: Поток в который происходит запись данных

## Propertys

### `IconID`

ID: `P:TFlex.Model.ProxyObject.IconID`

Идентификатор иконки прокси объекта

### `IsAlwaysDrawing`

ID: `P:TFlex.Model.ProxyObject.IsAlwaysDrawing`

Отключить кэширование рисования

### `IsConstruction`

ID: `P:TFlex.Model.ProxyObject.IsConstruction`

Определить прокси объект как элемент построения

### `Owner`

ID: `P:TFlex.Model.ProxyObject.Owner`

Владелец объекта

### `Plugin`

ID: `P:TFlex.Model.ProxyObject.Plugin`

Приложение, определяющее промежуточный (прокси-) объект

### `TypeID`

ID: `P:TFlex.Model.ProxyObject.TypeID`

Идентификатор типа объекта

Remarks: Тип объекта является уникальным в пределах приложения и не должен меняться. В соответствии с типом, система вызывает метод `M:TFlex.Plugin.CreateObject(TFlex.Model.Document,System.IntPtr,System.Int32)` для создания прокси объекта при чтении файла, выполнении отмены действий и т.д.

### `TypeName`

ID: `P:TFlex.Model.ProxyObject.TypeName`

Имя типа объекта

### `Version`

ID: `P:TFlex.Model.ProxyObject.Version`

Версия прокси объекта
