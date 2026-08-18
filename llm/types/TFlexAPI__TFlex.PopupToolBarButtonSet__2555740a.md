# TFlex.PopupToolBarButtonSet

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Набор кнопок, отображаемых в динамической панели

## Methods

### `Add(System.Int32)`

ID: `M:TFlex.PopupToolBarButtonSet.Add(System.Int32)`

Добавляет в этот набор кнопку с указанным идентификатором

Parameters:
- `id`: Идентификатор кнопки

Returns: true, если кнопка была добавлена в этот набор; false, если указанный идентификатор недействителен или используется одной из кнопок, уже имеющихся в этом наборе

### `Add(System.Int32,System.Boolean)`

ID: `M:TFlex.PopupToolBarButtonSet.Add(System.Int32,System.Boolean)`

Добавляет в этот набор кнопку с указанными параметрами

Parameters:
- `id`: Идентификатор кнопки
- `required`: true, если кнопка всегда должна отображаться в панели; false, если допускается расположение кнопки в расширенном меню

Returns: true, если кнопка была добавлена в этот набор; false, если указанный идентификатор некорректен или используется одной из кнопок, уже имеющихся в этом наборе

### `Add(System.Int32,System.Boolean,TFlex.Plugin)`

ID: `M:TFlex.PopupToolBarButtonSet.Add(System.Int32,System.Boolean,TFlex.Plugin)`

Добавляет в этот набор кнопку вызова указанной команды

Parameters:
- `commandId`: Идентификатор команды приложения
- `required`: true, если кнопка всегда должна отображаться в панели; false, если допускается расположение кнопки в расширенном меню
- `plugin`: Объект приложения

Returns: true, если кнопка была добавлена в этот набор; false, если указанный идентификатор команды недействителен или используется одной из кнопок, уже имеющихся в этом наборе

### `Add(System.Int32,TFlex.Plugin)`

ID: `M:TFlex.PopupToolBarButtonSet.Add(System.Int32,TFlex.Plugin)`

Добавляет в этот набор кнопку вызова указанной команды

Parameters:
- `commandId`: Идентификатор команды приложения
- `plugin`: Объект приложения

Returns: true, если кнопка была добавлена в этот набор; false, если указанный идентификатор команды недействителен или используется одной из кнопок, уже имеющихся в этом наборе

### `Contains(System.Int32)`

ID: `M:TFlex.PopupToolBarButtonSet.Contains(System.Int32)`

Определяет, есть в этом наборе указанная кнопка или нет

Parameters:
- `id`: Идентификатор кнопки

Returns: true, если этот набор содержит кнопку с указанным идентификатором, иначе false

### `Contains(System.Int32,TFlex.Plugin)`

ID: `M:TFlex.PopupToolBarButtonSet.Contains(System.Int32,TFlex.Plugin)`

Определяет, есть в этом наборе указанная кнопка или нет

Parameters:
- `commandId`: Идентификатор команды приложения
- `plugin`: Объект приложения

Returns: true, если этот набор содержит кнопку вызова указанной команды, иначе false

### `Remove(System.Int32)`

ID: `M:TFlex.PopupToolBarButtonSet.Remove(System.Int32)`

Удаляет из этого набора кнопку с указанным идентификатором

Parameters:
- `id`: Идентификатор кнопки

### `Remove(System.Int32,TFlex.Plugin)`

ID: `M:TFlex.PopupToolBarButtonSet.Remove(System.Int32,TFlex.Plugin)`

Удаляет указанную кнопку из этого набора

Parameters:
- `commandId`: Идентификатор команды приложения
- `plugin`: Объект приложения

### `RemoveAll`

ID: `M:TFlex.PopupToolBarButtonSet.RemoveAll`

Удаляет все кнопки из этого набора
