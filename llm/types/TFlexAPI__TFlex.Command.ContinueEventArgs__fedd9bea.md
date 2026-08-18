# TFlex.Command.ContinueEventArgs

Assembly: `TFlexAPI`
Namespace: `TFlex.Command`

## Summary

Класс аргументов события завершения выполнения вложенной команды приложения

## Remarks

Вложенной командой называется команда, функция `TFlex.Command.PluginCommand.Run(TFlex.Model.View, bool)` которой вызвана внутри обработчика выполнения другой (вызывающей) команды

## Propertys

### `PreviousCommand`

ID: `P:TFlex.Command.ContinueEventArgs.PreviousCommand`

Вложенная команда, которая завершилась

### `Result`

ID: `P:TFlex.Command.ContinueEventArgs.Result`

Объект, который был передан из вложенной команды
