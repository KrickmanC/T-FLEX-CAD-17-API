# CTfw32Doc

Assembly: `TFlexAPI3D`

## Methods

### `BeginChanges(ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CTfw32Doc.BeginChanges(ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Начать изменение документа с регистрацией в undo

Parameters:
- `undoBlockName`: Название блока undo

Returns: true - в случае успеха, false - иначе

Remarks: Блоки могут быть вложенными (с точки зрения вызовов BeginChanges() EndChanges() CancelChanges()). В этом случае, при вызове последнего EndChanges() будет сформирован один общий Undo-блок, а при последнем вызове CancelChanges() будет произведена отмена всех вложенных блоков. Недопустимо нарушение парности вызовов BeginChanges() и EndChanges() или CancelChanges(). Для удобства можно использовать RAII класс UndoBlock.

### `CancelChanges(System.Boolean)`

ID: `M:CTfw32Doc.CancelChanges(System.Boolean)`

Отменить текущие изменения документа и закрыть Undo-блок

Parameters:
- `regenerate`: true - выполнить пересчёт документа

Returns: true - в случае успеха, false - иначе

Remarks: Отменяет изменения только если открыт Undo-блок. Если Undo-блок вложенный - изменения не отменяет, но закрывает вложенный блок. Недопустимо нарушение парности вызовов BeginChanges() и EndChanges() или CancelChanges(). Для удобства можно использовать RAII класс UndoBlock.

### `EndChanges(System.Boolean,System.Boolean)`

ID: `M:CTfw32Doc.EndChanges(System.Boolean,System.Boolean)`

Закончить изменение документа с регистрацией в Undo

Parameters:
- `regenerate`: true - выполнить пересчёт документа
- `merge`: Объединить текущий Undo-блок с верхним Undo-блоком

Returns: true - в случае успеха, false - иначе

Remarks: Здесь регистрируется блок Undo, после его регистрации уже нельзя воспользоваться методом CancelChanges(). Недопустимо нарушение парности вызовов BeginChanges() и EndChanges() или CancelChanges(). Для удобства можно использовать RAII класс UndoBlock.

### `GetModelConfigurations`

ID: `M:CTfw32Doc.GetModelConfigurations`

### `GetUndoManager(System.Boolean)`

ID: `M:CTfw32Doc.GetUndoManager(System.Boolean)`

Получить Undo-менеджер

Parameters:
- `createIfNone`: Флаг того, что если менеджер не создан, то нужно ли его создавать (true - нужно, false - нет)

Returns: Указатель на Undo-менеджер документа, или nullptr в случае, если данный документ не может управлять Undo (IsFragment() == true)

### `IsChanging`

ID: `M:CTfw32Doc.IsChanging`

Изменяется ли документ в данный момент (открыт ли Undo-блок)

Returns: true - документ изменяется, false - иначе

### `IsObjectIncludedInCurrentChanges(CTFObject!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CTfw32Doc.IsObjectIncludedInCurrentChanges(CTFObject!System.Runtime.CompilerServices.IsConst*)`

Проверяет, зарегистрирован ли объект в текущем изменении документа (в текущем Undo-блоке)

Parameters:
- `object`: Указатель на объект

Returns: true - если объект зарегистрирован в текущем изменении, false - иначе

### `RedrawViews(TFlex.FlagSet<<unknown type>>)`

ID: `M:CTfw32Doc.RedrawViews(TFlex.FlagSet<<unknown type>>)`

Перерисовать все виды документа

Parameters:
- `params`: Параметры перерисовки

### `RegisterObjectCreation(CTFObject*)`

ID: `M:CTfw32Doc.RegisterObjectCreation(CTFObject*)`

Зарегистрировать создание объекта в документе и Undo-блоке

Parameters:
- `objectOnHeap`: Указатель на созданный объект в куче

Returns: true - в случае успеха, false - иначе

Remarks: Ответственность за удаление созданного объекта передаётся документу. В случае неудачи (например, если Undo-блок не открыт или данный документ не может изменяться) - удаляет созданный объект сразу. Сценарий использования: 1. Создаём объект в куче. 2. Передаём указатель на него в данный метод. 3. В случае успеха можем изменять объект по тому же указателю.

### `RegisterObjectCreationWithCopy(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CTfw32Doc.RegisterObjectCreationWithCopy(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Зарегистрировать создание объекта в документе и Undo-блоке

Parameters:
- `objectOnStack`: Cозданный на стеке объект

Returns: Указатель на объект в документе - в случае успеха, nullptr - иначе

Remarks: Делает копию созданного на стеке объекта. Сценарий использования: 1. Создаём объект в стеке. 2. Передаём его в данный метод. 3. В случае успеха можем изменять объект по указателю, который вернул данный метод.

### `RegisterObjectDeletion(System.UInt32,CTFObject**,System.UInt32)`

ID: `M:CTfw32Doc.RegisterObjectDeletion(System.UInt32,CTFObject**,System.UInt32)`

Зарегистрировать удаление объекта в документе и Undo-блоке

Parameters:
- `objectInDoc`: Указатель на удаляемый объект в документе
- `flags`: Параметры удаления объекта

Returns: true - в случае успеха, false - иначе

Remarks: Удаляет объект из документа, если открыт Undo-блок. Сценарий использования: 1. Находим в документе объект, который хотим удалить. 2. Передаём указатель на него в данный метод.

### `RegisterObjectForChange(CTFObject*)`

ID: `M:CTfw32Doc.RegisterObjectForChange(CTFObject*)`

Зарегистрировать объект в документе и Undo-блоке для дальнейшего изменения

Parameters:
- `objectInDoc`: Указатель на объект в документе (НЕ КОПИЯ)

Returns: true - в случае успеха, false - иначе

Remarks: Сценарий использования: 1. Находим в документе объект, который хотим отредактирвоать. 2. Передаём указатель на него в данный метод. 3. В случае успеха - изменяем объект по тому же указателю.

### `RegisterObjectReplacement(CTFObject*,CTFObject*)`

ID: `M:CTfw32Doc.RegisterObjectReplacement(CTFObject*,CTFObject*)`

Зарегистрировать замену объекта в документе на новый объект

Parameters:
- `objectInDoc`: Указатель на заменяемый объект в документе (НЕ КОПИЯ)
- `newObject`: Указатель на заменяющий объект в куче

Returns: true - в случае успеха, false - иначе

Remarks: Ответственность за удаление заменяющего объекта передаётся документу. В случае неудачи (например, если Undo-блок не открыт или данный документ не может изменяться) - удаляет заменяющий объект сразу. Сценарий использования: 1. Создаём заменяющий объект в куче. 2. Находим в документе объект, который хотим заменить. 3. Передаём указатели на заменяемый и заменяющий объекты в данный метод.
