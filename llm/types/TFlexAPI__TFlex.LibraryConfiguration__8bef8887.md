# TFlex.LibraryConfiguration

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Класс конфигурации библиотек. Данный класс является набором библиотек и групп библиотек

## Constructors

### `LibraryConfiguration(System.String,System.String)`

ID: `M:TFlex.LibraryConfiguration.#ctor(System.String,System.String)`

Конструктор

Parameters:
- `name`: Имя конфигурации библиотеки
- `path`: Путь к конфигурации

## Methods

### `LibraryConfiguration(System.String,System.String)`

ID: `M:TFlex.LibraryConfiguration.#ctor(System.String,System.String)`

Конструктор

Parameters:
- `name`: Имя конфигурации библиотеки
- `path`: Путь к конфигурации

### `GetEnumerator`

ID: `M:TFlex.LibraryConfiguration.GetEnumerator`

Получить перечислитель библиотек

### `GetGroup(System.Int32)`

ID: `M:TFlex.LibraryConfiguration.GetGroup(System.Int32)`

Получить группу по индексу

Parameters:
- `index`: 

### `GetGroups`

ID: `M:TFlex.LibraryConfiguration.GetGroups`

Получить перечислитель групп

### `GetLibrariesWithoutGroup`

ID: `M:TFlex.LibraryConfiguration.GetLibrariesWithoutGroup`

Получить перечислитель библиотек, не входящих ни в одну группу.

### `GetLibrary(System.Int32)`

ID: `M:TFlex.LibraryConfiguration.GetLibrary(System.Int32)`

Получить библиотеку по индексу

Parameters:
- `index`: 

### `Save`

ID: `M:TFlex.LibraryConfiguration.Save`

Сохранить конфигурацию

### `SaveAs(System.String)`

ID: `M:TFlex.LibraryConfiguration.SaveAs(System.String)`

Сохранить конфигурацию как

Parameters:
- `path`: Путь для сохранения

## Propertys

### `Count`

ID: `P:TFlex.LibraryConfiguration.Count`

Количество библиотек

### `GroupsCount`

ID: `P:TFlex.LibraryConfiguration.GroupsCount`

Количество групп

### `Name`

ID: `P:TFlex.LibraryConfiguration.Name`

Имя конфигурации библиотеки

### `Path`

ID: `P:TFlex.LibraryConfiguration.Path`

Путь к конфигурации
