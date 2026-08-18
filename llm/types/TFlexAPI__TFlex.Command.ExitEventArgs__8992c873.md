# TFlex.Command.ExitEventArgs

Assembly: `TFlexAPI`
Namespace: `TFlex.Command`

## Summary

Класс аргументов события, возникающего при завершении выполнения команды приложения

## Propertys

### `Result`

ID: `P:TFlex.Command.ExitEventArgs.Result`

Объект, который необходимо передать из вложенной команды в вызывающую

Remarks: Применяется только для вложенных команд приложения. Вложенной командой называется команда, функция `TFlex.Command.PluginCommand.Run(TFlex.Model.View, bool)` которой вызвана внутри обработчика выполнения другой (вызывающей) команды
