# TFlex.Command.FilterOwnerExtensions

Assembly: `TFlexAPI`
Namespace: `TFlex.Command`

## Methods

### `GetSelectionFilterButtonState(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.Booleanref ,System.Booleanref )`

ID: `M:TFlex.Command.FilterOwnerExtensions.GetSelectionFilterButtonState(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.Boolean@,System.Boolean@)`

Получить состояние кнопки селекции

Parameters:
- `objectType`: Тип модельного объекта для которого требуется включить селекцию
- `checked`: Кнопка селектера активирована
- `disabled`: Кнопка селектора недоступна для изменения

### `HideAllSelectionFilterButtons(TFlex.Command.IFilterOwner)`

ID: `M:TFlex.Command.FilterOwnerExtensions.HideAllSelectionFilterButtons(TFlex.Command.IFilterOwner)`

Скрыть все фильтры селекции

### `ResumeSelectionFilterNotifications(TFlex.Command.IFilterOwner)`

ID: `M:TFlex.Command.FilterOwnerExtensions.ResumeSelectionFilterNotifications(TFlex.Command.IFilterOwner)`

Закончить настройку панели фильтров

Remarks: Возобновляет перерисовку панели

### `SetSelectionFilterButtonState(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.Boolean,System.Boolean)`

ID: `M:TFlex.Command.FilterOwnerExtensions.SetSelectionFilterButtonState(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.Boolean,System.Boolean)`

Установить состояние кнопки селекции

Parameters:
- `objectType`: Тип модельного объекта для которого требуется включить селекцию
- `checked`: Активировать фильтр
- `disabled`: Сделать недоступным для изменения

### `SetSelectionFilterButtonToolTip(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.String)`

ID: `M:TFlex.Command.FilterOwnerExtensions.SetSelectionFilterButtonToolTip(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.String)`

Установить подсказку у кнопки селектора

Parameters:
- `objectType`: Тип модельного объекта для которого требуется включить селекцию
- `toolTip`: Подсказка для кнопки

### `ShowSelectionFilterButton(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.Boolean)`

ID: `M:TFlex.Command.FilterOwnerExtensions.ShowSelectionFilterButton(TFlex.Command.IFilterOwner,TFlex.Model.ObjectType,System.Boolean)`

Показать кнопку фильтра селекции

Parameters:
- `objectType`: Тип модельного объекта для которого требуется включить селекцию
- `show`: Добавить фильтр

### `ShowSelectionFilterSet(TFlex.Command.IFilterOwner,TFlex.Command.SelectorSetType)`

ID: `M:TFlex.Command.FilterOwnerExtensions.ShowSelectionFilterSet(TFlex.Command.IFilterOwner,TFlex.Command.SelectorSetType)`

Показать конфигурацию селектора

Parameters:
- `setType`: Набор для селекции

### `SuspendSelectionFilterNotifications(TFlex.Command.IFilterOwner)`

ID: `M:TFlex.Command.FilterOwnerExtensions.SuspendSelectionFilterNotifications(TFlex.Command.IFilterOwner)`

Начать настройку панели фильтров

Remarks: Приостанавливает на время настройки перерисовку панели. После настройки панели необходимо вызвать метод: `!:TFlex::Command::FilterOwnerExtensions::EndSelectionFilterConfiguration()`
