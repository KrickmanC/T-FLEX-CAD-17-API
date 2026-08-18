# TFlex.StatusBar

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Статусная строка T-FLEX CAD

## Methods

### `EndProgress`

ID: `M:TFlex.StatusBar.EndProgress`

Закрыть индикатор состояния

### `LockProgress`

ID: `M:TFlex.StatusBar.LockProgress`

Заблокировать отображение индикации состояния

### `StartProgress(System.UInt32)`

ID: `M:TFlex.StatusBar.StartProgress(System.UInt32)`

Запустить индикатор состояния

Parameters:
- `total`: Длина диапазона

### `StartProgress(System.UInt32,System.UInt32)`

ID: `M:TFlex.StatusBar.StartProgress(System.UInt32,System.UInt32)`

Запустить индикатор состояния

Parameters:
- `total`: Длина диапазона
- `step`: Величина шага

### `StepProgress`

ID: `M:TFlex.StatusBar.StepProgress`

Выполнить один шаг индикатора состояния

### `UnlockProgress`

ID: `M:TFlex.StatusBar.UnlockProgress`

Разблокировать отображение индикации состояния

## Propertys

### `Command`

ID: `P:TFlex.StatusBar.Command`

Установить строку команды

### `Prompt`

ID: `P:TFlex.StatusBar.Prompt`

Установить строку подсказки
