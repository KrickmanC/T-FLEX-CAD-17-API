# TFlex.Model.ModelConfigurations

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Контейнер конфигураций модели

## Methods

### `CreateConfiguration(System.String)`

ID: `M:TFlex.Model.ModelConfigurations.CreateConfiguration(System.String)`

Создание конфигурации с именем Name с текущим набором значений переменных

Parameters:
- `Name`: Имя конфигурации

### `CreateConfiguration(System.String,System.String,System.Boolean)`

ID: `M:TFlex.Model.ModelConfigurations.CreateConfiguration(System.String,System.String,System.Boolean)`

Создание конфигурации с именем name с текущим набором значений переменных

Parameters:
- `name`: Имя конфигурации
- `variationName`: Имя исполнения
- `isVariation`: Тип - исполнение или конфигурация

### `DeleteConfiguration(System.String)`

ID: `M:TFlex.Model.ModelConfigurations.DeleteConfiguration(System.String)`

Удаление конфигурации с именем Name

Parameters:
- `Name`: Имя конфигурации

### `GetConfiguration(System.Int32)`

ID: `M:TFlex.Model.ModelConfigurations.GetConfiguration(System.Int32)`

Получить конфигурацию модели с заданным номером

Parameters:
- `index`: Номер конфигурации

### `GetConfiguration(System.String)`

ID: `M:TFlex.Model.ModelConfigurations.GetConfiguration(System.String)`

Получить конфигурацию модели по идентификатору

Parameters:
- `id`: Идентификатор конфигурации

### `GetConfigurationId(System.Int32)`

ID: `M:TFlex.Model.ModelConfigurations.GetConfigurationId(System.Int32)`

Получение идентификатора конфигурации с номером Index

Parameters:
- `Index`: Индекс конфигурации

### `GetConfigurationIndex(System.String)`

ID: `M:TFlex.Model.ModelConfigurations.GetConfigurationIndex(System.String)`

Получение индекса конфигурации по идентификатору

Parameters:
- `id`: Идентификатор конфигурации

### `GetConfigurationName(System.Int32)`

ID: `M:TFlex.Model.ModelConfigurations.GetConfigurationName(System.Int32)`

Получение имени конфигурации с номером Index

Parameters:
- `Index`: Индекс конфигурации

### `GetConfigurationVersion(System.Int32)`

ID: `M:TFlex.Model.ModelConfigurations.GetConfigurationVersion(System.Int32)`

Получение версии конфигурации с номером Index

Parameters:
- `Index`: Индекс конфигурации

### `GetConfigurationWithCurrentValues`

ID: `M:TFlex.Model.ModelConfigurations.GetConfigurationWithCurrentValues`

Проверка существования конфигурации с текущим набором значений переменных.

### `GetModelConfiguration(System.Int32)`

ID: `M:TFlex.Model.ModelConfigurations.GetModelConfiguration(System.Int32)`

Получение конфигурации

Parameters:
- `index`: Индекс конфигурации

### `LoadConfigurationSolids(System.String)`

ID: `M:TFlex.Model.ModelConfigurations.LoadConfigurationSolids(System.String)`

Загрузка тел в текущую модель из конфигурации с именем Name

Parameters:
- `Name`: Имя конфигурации

### `LoadConfigurationVariables(System.String)`

ID: `M:TFlex.Model.ModelConfigurations.LoadConfigurationVariables(System.String)`

Загрузка переменных в текущую модель из конфигурации с именем Name

Parameters:
- `Name`: Имя конфигурации

### `RenameConfiguration(System.String,System.String)`

ID: `M:TFlex.Model.ModelConfigurations.RenameConfiguration(System.String,System.String)`

Переименовать конфигурацию

Parameters:
- `OldName`: Старое имя
- `NewName`: Новое имя

## Propertys

### `ConfigurationCount`

ID: `P:TFlex.Model.ModelConfigurations.ConfigurationCount`

Количество конфигураций модели
