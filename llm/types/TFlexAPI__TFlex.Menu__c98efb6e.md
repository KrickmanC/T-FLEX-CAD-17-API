# TFlex.Menu

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Класс меню

## Constructors

### `Menu`

ID: `M:TFlex.Menu.#ctor`

Конструктор

## Methods

### `Menu`

ID: `M:TFlex.Menu.#ctor`

Конструктор

### `Append(System.Int32,System.String,System.Boolean,System.Boolean,TFlex.Plugin)`

ID: `M:TFlex.Menu.Append(System.Int32,System.String,System.Boolean,System.Boolean,TFlex.Plugin)`

Добавить пункт меню

Parameters:
- `command`: Идентификатор зарегестрированной в приложении команды
- `caption`: Название пунтка меню
- `enable`: Доступность пункта меню
- `check`: Устанавливает галочку напротив пункта меню
- `plugin`: Объект приложения

### `Append(System.Int32,System.String,TFlex.Plugin)`

ID: `M:TFlex.Menu.Append(System.Int32,System.String,TFlex.Plugin)`

Добавить пункт меню

Parameters:
- `command`: Идентификатор зарегестрированной в приложении команды
- `caption`: Название пунтка меню
- `plugin`: Объект приложения

### `AppendSeparator`

ID: `M:TFlex.Menu.AppendSeparator`

Добавить разделитель в меню

### `AppendSubMenu(System.String)`

ID: `M:TFlex.Menu.AppendSubMenu(System.String)`

Добавить подменю

Parameters:
- `caption`: Название подменю

### `AppendSystemCommand(System.Int32)`

ID: `M:TFlex.Menu.AppendSystemCommand(System.Int32)`

Добавить пункт меню

Parameters:
- `CommandID`: Идентификатор системной команды

### `AppendSystemCommand(System.Int32,System.String)`

ID: `M:TFlex.Menu.AppendSystemCommand(System.Int32,System.String)`

Добавить пункт меню

Parameters:
- `CommandID`: Идентификатор системной команды
- `Caption`: Название пункта меню

### `CreatePopup`

ID: `M:TFlex.Menu.CreatePopup`

Создать контекстное меню

### `DeleteByCommand(System.Int32)`

ID: `M:TFlex.Menu.DeleteByCommand(System.Int32)`

Удалить команду по идентификатору

Parameters:
- `command`: Идентификатор команды

### `DeleteByIndex(System.Int32)`

ID: `M:TFlex.Menu.DeleteByIndex(System.Int32)`

Удалить команду по порядковому номеру

Parameters:
- `index`: Порядковый номер команды

### `Dispose`

ID: `M:TFlex.Menu.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `GetCaption(System.Int32)`

ID: `M:TFlex.Menu.GetCaption(System.Int32)`

Получить название пункта меню команды по её порядковому номеру

Parameters:
- `index`: Порядковый номер пункта меню команды

### `GetCommand(System.Int32)`

ID: `M:TFlex.Menu.GetCommand(System.Int32)`

Получить идентификатор команды по её порядковому номеру в меню

Parameters:
- `index`: Порядковый номер команды

### `GetCount`

ID: `M:TFlex.Menu.GetCount`

Получить общее количество пунктов меню

### `GetSubMenu(System.Int32)`

ID: `M:TFlex.Menu.GetSubMenu(System.Int32)`

Получить подменю по её порядковому номеру в меню

Parameters:
- `index`: Порядковый номер подменю

### `Insert(System.Int32,System.Int32,System.String,TFlex.Plugin)`

ID: `M:TFlex.Menu.Insert(System.Int32,System.Int32,System.String,TFlex.Plugin)`

Вставить пункт меню

Parameters:
- `index`: Номер пункта меню
- `command`: Идентификатор зарегестрированной в приложении команды
- `caption`: Название пунтка меню
- `plugin`: Объект приложения
