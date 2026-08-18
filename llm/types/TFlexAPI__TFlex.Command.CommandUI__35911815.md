# TFlex.Command.CommandUI

Assembly: `TFlexAPI`
Namespace: `TFlex.Command`

## Summary

Данный класс является вспомогательным классом, обеспечивающим разрешение или блокировку выполнения команды, а также установку переключателя команды в режим "включено" или "выключено".

## Methods

### `Enable`

ID: `M:TFlex.Command.CommandUI.Enable`

Разрешить выполнение данной команды

### `Enable(System.Boolean)`

ID: `M:TFlex.Command.CommandUI.Enable(System.Boolean)`

Разрешить выполнение данной команды

Parameters:
- `fEnable`: Разрешить или запретить выполнение команды

### `SetCheck`

ID: `M:TFlex.Command.CommandUI.SetCheck`

Установить состояние "Включено" для данной команды

### `SetCheck(System.Boolean)`

ID: `M:TFlex.Command.CommandUI.SetCheck(System.Boolean)`

Установить состояние "Включено" для данной команды

Parameters:
- `fSet`: Установить состояние "Включено" или "Выключено"

### `SetRadio`

ID: `M:TFlex.Command.CommandUI.SetRadio`

Установить состояние "Включено" в режиме переключателя для данной команды

### `SetRadio(System.Boolean)`

ID: `M:TFlex.Command.CommandUI.SetRadio(System.Boolean)`

Установить состояние "Включено" или "Выключено" в режиме переключателя в зависимости от значения параметра fSet

Parameters:
- `fSet`: Установить состояние "Включено" или "Выключено"

### `SetText(System.String)`

ID: `M:TFlex.Command.CommandUI.SetText(System.String)`

Установить название команды

Parameters:
- `name`: Название команды

## Propertys

### `Document`

ID: `P:TFlex.Command.CommandUI.Document`

Получить документ, который для данной команды является активным

Remarks: Может быть 0, если ни один документ не открыт

### `ID`

ID: `P:TFlex.Command.CommandUI.ID`

Получить идентификатор команды
