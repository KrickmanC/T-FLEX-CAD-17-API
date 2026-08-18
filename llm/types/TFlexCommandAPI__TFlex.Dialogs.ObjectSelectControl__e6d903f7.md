# TFlex.Dialogs.ObjectSelectControl

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Элемент управления для выбора объектов. Показывается в виде поля ввода или списка.

## Constructors

### `ObjectSelectControl(System.String)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор элемента

### `ObjectSelectControl(System.String,TFlex.Dialogs.ObjectSelectControlMode)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.#ctor(System.String,TFlex.Dialogs.ObjectSelectControlMode)`

Parameters:
- `id`: Идентификатор элемента
- `mode`: Режим выбора объектов

## Methods

### `ObjectSelectControl(System.String)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор элемента

### `ObjectSelectControl(System.String,TFlex.Dialogs.ObjectSelectControlMode)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.#ctor(System.String,TFlex.Dialogs.ObjectSelectControlMode)`

Parameters:
- `id`: Идентификатор элемента
- `mode`: Режим выбора объектов

### `BeginUserEdit(System.Int32)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.BeginUserEdit(System.Int32)`

Начать операцию пользовательского редактирования указанного объекта

### `BeginUserInsert`

ID: `M:TFlex.Dialogs.ObjectSelectControl.BeginUserInsert`

Начать операцию пользовательского добавления нового объекта

### `BeginUserInsert(System.Int32)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.BeginUserInsert(System.Int32)`

Начать операцию пользовательского добавления нового объекта

### `DoAutoEnableButtons`

ID: `M:TFlex.Dialogs.ObjectSelectControl.DoAutoEnableButtons`

Выполнить включение или выключение кнопок согласно состоянию

### `EndUserEdit`

ID: `M:TFlex.Dialogs.ObjectSelectControl.EndUserEdit`

Завершить операцию пользовательского добавления/редактирования объектов

### `EndUserEdit(TFlex.Dialogs.ObjectSelectControlItem)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.EndUserEdit(TFlex.Dialogs.ObjectSelectControlItem)`

Завершить операцию пользовательского добавления/редактирования объектов

### `RemoveSelectedObjects`

ID: `M:TFlex.Dialogs.ObjectSelectControl.RemoveSelectedObjects`

Удалить выбранные объекты

### `RemoveSelectedObjects(System.Boolean)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.RemoveSelectedObjects(System.Boolean)`

Удалить выбранные объекты

### `ResetFilter`

ID: `M:TFlex.Dialogs.ObjectSelectControl.ResetFilter`

Сбрасывает фильтр поиска

### `SetAutoBeginUserInsert(System.Boolean)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetAutoBeginUserInsert(System.Boolean)`

Постоянно находится в режиме добавления или редактирования объекта

### `SetAutoBeginUserInsert(System.Boolean,System.Boolean)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetAutoBeginUserInsert(System.Boolean,System.Boolean)`

Постоянно находится в режиме добавления или редактирования объекта

### `SetFilter(System.Func`2{TFlex.Dialogs.ObjectSelectControlPlainObject,System.Boolean},TFlex.Model.Document)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetFilter(System.Func`2{TFlex.Dialogs.ObjectSelectControlPlainObject,System.Boolean},TFlex.Model.Document)`

Устанавливает фильтр поиска

### `SetFilter(TFlex.Dialogs.ObjectSelectControlFilter)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetFilter(TFlex.Dialogs.ObjectSelectControlFilter)`

Устанавливает фильтр поиска

### `SetSingleObject(TFlex.Dialogs.ObjectSelectControlPlainObject)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetSingleObject(TFlex.Dialogs.ObjectSelectControlPlainObject)`

Устанавливает объект, когда элемент управления находится в режиме выбора одного объекта

### `SetSingleObject(TFlex.Dialogs.ObjectSelectControlPlainObject,System.Boolean)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetSingleObject(TFlex.Dialogs.ObjectSelectControlPlainObject,System.Boolean)`

Устанавливает объект, когда элемент управления находится в режиме выбора одного объекта

### `SetSingleObject(TFlex.Model.ModelObject)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetSingleObject(TFlex.Model.ModelObject)`

Устанавливает объект, когда элемент управления находится в режиме выбора одного объекта

### `SetSingleObject(TFlex.Model.ModelObject,System.Boolean)`

ID: `M:TFlex.Dialogs.ObjectSelectControl.SetSingleObject(TFlex.Model.ModelObject,System.Boolean)`

Устанавливает объект, когда элемент управления находится в режиме выбора одного объекта

## Propertys

### `AllowUserAdd`

ID: `P:TFlex.Dialogs.ObjectSelectControl.AllowUserAdd`

Разрешает пользователю инициировать добавление новых объектов

### `AllowUserClear`

ID: `P:TFlex.Dialogs.ObjectSelectControl.AllowUserClear`

Разрешает пользователю очищать список

### `AllowUserRemove`

ID: `P:TFlex.Dialogs.ObjectSelectControl.AllowUserRemove`

Разрешает пользователю удаление объектов

### `AutoBeginUserInsert`

ID: `P:TFlex.Dialogs.ObjectSelectControl.AutoBeginUserInsert`

Постоянно находится в режиме добавления или редактирования объекта

### `AutoEnableButtons`

ID: `P:TFlex.Dialogs.ObjectSelectControl.AutoEnableButtons`

Автоматическое управление состоянием доступности кнопок

### `AutoRequirementMet`

ID: `P:TFlex.Dialogs.ObjectSelectControl.AutoRequirementMet`

Автоматически выставлять свойство IsRequarementMet. Также см. IsRequired.

### `AutoSelectNextAfterRemove`

ID: `P:TFlex.Dialogs.ObjectSelectControl.AutoSelectNextAfterRemove`

Выделять следующий объект после удаления

### `Filter`

ID: `P:TFlex.Dialogs.ObjectSelectControl.Filter`

Управление фильтром поиска

### `HighlightedRow`

ID: `P:TFlex.Dialogs.ObjectSelectControl.HighlightedRow`

Индекс объекта, над которым в списке находится указатель мыши

### `IsInUserEdit`

ID: `P:TFlex.Dialogs.ObjectSelectControl.IsInUserEdit`

Возвращает true если элемент управления находится в режиме редактирования

### `Mode`

ID: `P:TFlex.Dialogs.ObjectSelectControl.Mode`

Режим выбора объектов

### `Objects`

ID: `P:TFlex.Dialogs.ObjectSelectControl.Objects`

Доступ к объектам, отображаемым в списке

### `SelectedRow`

ID: `P:TFlex.Dialogs.ObjectSelectControl.SelectedRow`

Возвращает первый выбранный объект или -1

### `SelectedRows`

ID: `P:TFlex.Dialogs.ObjectSelectControl.SelectedRows`

Возвращает коллекцию индексов выбранных элементов

### `SingleObject`

ID: `P:TFlex.Dialogs.ObjectSelectControl.SingleObject`

Используется для установки или получения объекта, когда элемент управления находится в режиме выбора одного объекта

### `StopEditOnActiveLost`

ID: `P:TFlex.Dialogs.ObjectSelectControl.StopEditOnActiveLost`

Прекращать редактирование если элемент управления перестаёт быть активным

### `UserEditObject`

ID: `P:TFlex.Dialogs.ObjectSelectControl.UserEditObject`

Получить или установить данные редактируемого объекта

### `UserEditObjectItem`

ID: `P:TFlex.Dialogs.ObjectSelectControl.UserEditObjectItem`

Возвращает редактируемый элемент

### `UserEditPos`

ID: `P:TFlex.Dialogs.ObjectSelectControl.UserEditPos`

Возвращает положение редактируемого элемента

## Events

### `ItemHighlighted`

ID: `E:TFlex.Dialogs.ObjectSelectControl.ItemHighlighted`

Событие наведения указателя мыши на объект в списке

### `ObjectReplacedByUser`

ID: `E:TFlex.Dialogs.ObjectSelectControl.ObjectReplacedByUser`

Событие замены объекта пользователем

### `StateUpdated`

ID: `E:TFlex.Dialogs.ObjectSelectControl.StateUpdated`

Событие изменения состояния
