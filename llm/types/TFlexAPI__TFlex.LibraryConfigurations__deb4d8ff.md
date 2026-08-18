# TFlex.LibraryConfigurations

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Конфигурации библиотек

## Constructors

### `LibraryConfigurations`

ID: `M:TFlex.LibraryConfigurations.#ctor`

Конструктор

## Methods

### `LibraryConfigurations`

ID: `M:TFlex.LibraryConfigurations.#ctor`

Конструктор

### `Add(TFlex.LibraryConfiguration)`

ID: `M:TFlex.LibraryConfigurations.Add(TFlex.LibraryConfiguration)`

Добавить конфигурацию

Parameters:
- `configuration`: Конфигурация для добавления

### `Close(System.Int32)`

ID: `M:TFlex.LibraryConfigurations.Close(System.Int32)`

Закрыть конфигурацию с указанным номером

Parameters:
- `index`: Номер конфигурации

### `Close(TFlex.LibraryConfiguration)`

ID: `M:TFlex.LibraryConfigurations.Close(TFlex.LibraryConfiguration)`

Закрыть конфигурацию

Parameters:
- `configuration`: Конфигурация для закрытия

### `GetEnumerator`

ID: `M:TFlex.LibraryConfigurations.GetEnumerator`

Получить перечислитель

### `GetLibraryConfiguration(System.Int32)`

ID: `M:TFlex.LibraryConfigurations.GetLibraryConfiguration(System.Int32)`

Получить конфигурацию по номеру

Parameters:
- `index`: Номер конфигурации

### `Open(System.String)`

ID: `M:TFlex.LibraryConfigurations.Open(System.String)`

Открыть конфигурацию

Parameters:
- `path`: Путь к конфигурации

### `SetActive(System.Int32)`

ID: `M:TFlex.LibraryConfigurations.SetActive(System.Int32)`

Установить активную конфигурацию

Parameters:
- `index`: Номер конфигурации

## Propertys

### `Active`

ID: `P:TFlex.LibraryConfigurations.Active`

Получить активную конфигурацию

### `Count`

ID: `P:TFlex.LibraryConfigurations.Count`

Количество элементов
