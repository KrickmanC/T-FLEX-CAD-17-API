# TFlex.Command.FilterOwner

Assembly: `TFlexAPI`
Namespace: `TFlex.Command`

## Methods

### `CreateSelectionFilterButton(System.Guid,System.String)`

ID: `M:TFlex.Command.FilterOwner.CreateSelectionFilterButton(System.Guid,System.String)`

Создать кнопку селекции

Parameters:
- `iconId`: Идентификатор, использованный для регистрации иконки при помощи `!:TFlex::Command::CustomCommand::RegisterAutomenuIcon`
- `toolTip`: Подсказка для кнопки

Returns: Созданная кнопка либо `null` в случае ошибки

### `CreateSelectionFilterButton(System.Guid,System.String,TFlex.Command.SelectionFilterButton)`

ID: `M:TFlex.Command.FilterOwner.CreateSelectionFilterButton(System.Guid,System.String,TFlex.Command.SelectionFilterButton)`

Создать кнопку селекции

Parameters:
- `iconId`: Идентификатор, использованный для регистрации иконки при помощи `!:TFlex::Command::CustomCommand::RegisterAutomenuIcon`
- `toolTip`: Подсказка для кнопки
- `neighbor`: Существующая кнопка селекции, которая должна предшествовать новой

Returns: Созданная кнопка либо `null` в случае ошибки

Remarks: Добавляет кнопку в конец панели, если `neighbor` не является существующей кнопкой селекции

### `CreateSelectionFilterButton(System.Guid,System.String,TFlex.Model.ObjectType)`

ID: `M:TFlex.Command.FilterOwner.CreateSelectionFilterButton(System.Guid,System.String,TFlex.Model.ObjectType)`

Создать кнопку селекции

Parameters:
- `iconId`: Идентификатор, использованный для регистрации иконки при помощи `!:TFlex::Command::CustomCommand::RegisterAutomenuIcon`
- `toolTip`: Подсказка для кнопки
- `neighbor`: Тип модельного объекта, соответствующий существующей кнопке селекции, которая должна предшествовать новой

Returns: Созданная кнопка либо `null` в случае ошибки

Remarks: Добавляет кнопку в конец панели, если `neighbor` не соответствует ни одной из существующих кнопок

### `OnSelectionFilterButtonClick(System.Int32)`

ID: `M:TFlex.Command.FilterOwner.OnSelectionFilterButtonClick(System.Int32)`

Для внутреннего использования

### `OnSelectionFilterButtonClick(System.Int32,System.IntPtr)`

ID: `M:TFlex.Command.FilterOwner.OnSelectionFilterButtonClick(System.Int32,System.IntPtr)`

Для внутреннего использования

### `OnSelectionFilterButtonClick(TFlex.Command.SelectionFilterButtonClickEventArgs)`

ID: `M:TFlex.Command.FilterOwner.OnSelectionFilterButtonClick(TFlex.Command.SelectionFilterButtonClickEventArgs)`

Вызывает событие `E:TFlex.Command.FilterOwner.SelectionFilterButtonClick`

Parameters:
- `args`: Аргументы события

### `RemoveOwnSelectionFilterButtons`

ID: `M:TFlex.Command.FilterOwner.RemoveOwnSelectionFilterButtons`

Удалить все созданные этим объектом кнопки селекции
