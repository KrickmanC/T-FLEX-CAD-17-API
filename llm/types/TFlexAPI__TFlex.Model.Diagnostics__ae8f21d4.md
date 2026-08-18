# TFlex.Model.Diagnostics

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс контейнера диагностических сообщений документа

## Methods

### `Add(TFlex.Model.DiagnosticsMessage)`

ID: `M:TFlex.Model.Diagnostics.Add(TFlex.Model.DiagnosticsMessage)`

Добавить сообщение

Parameters:
- `message`: Добавляемое сообщение

### `Enable(System.Boolean)`

ID: `M:TFlex.Model.Diagnostics.Enable(System.Boolean)`

Разрешить или запретить добавление сообщений в контейнер.

Parameters:
- `enable`: true, если необходимо разрешить выдачу сообщений; false в случае запрета

Returns: Значение параметра, которое было установлено до вызова данного метода

Remarks: В некоторых случаях полезно запретить вывод сообщений в окно диагностики системы. С этой целью можно воспользоваться данным методом. После завершения действий, связанных с данным запретом, необходимо установить данный параметр в значение, которое он имел до этого.

### `EndGroup`

ID: `M:TFlex.Model.Diagnostics.EndGroup`

Закрыть группу сообщений

Remarks: Этот метод закрывает группу сообщений, открытых с помощью метода `M:TFlex.Model.Diagnostics.StartGroup` .

### `Remove(TFlex.Model.DiagnosticsMessageId)`

ID: `M:TFlex.Model.Diagnostics.Remove(TFlex.Model.DiagnosticsMessageId)`

Удалить сообщение

Parameters:
- `id`: Идентификатор сообщения

### `RemoveAll`

ID: `M:TFlex.Model.Diagnostics.RemoveAll`

Удалить все сообщения контейнера

### `StartGroup`

ID: `M:TFlex.Model.Diagnostics.StartGroup`

Открыть группу сообщений

Remarks: Для того, чтобы избежать множества звуковых сигналов об ошибках, в системе введено понятие "группы сообщений". Звуковой сигнал об ошибке выдаётся один раз внутри группы сообщений. открытую группу сообщений необходимо закрыть при помощи метода `M:TFlex.Model.Diagnostics.EndGroup` . Группы могут быть вложенными.
