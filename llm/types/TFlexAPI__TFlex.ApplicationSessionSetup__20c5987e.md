# TFlex.ApplicationSessionSetup

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Параметры инициализации сессии по работе с OpenAPI из другого приложения

## Constructors

### `ApplicationSessionSetup`

ID: `M:TFlex.ApplicationSessionSetup.#ctor`

Конструктор

## Methods

### `ApplicationSessionSetup`

ID: `M:TFlex.ApplicationSessionSetup.#ctor`

Конструктор

## Propertys

### `DOCsAPIVersion`

ID: `P:TFlex.ApplicationSessionSetup.DOCsAPIVersion`

Номер версии T-FLEX DOCs, с которой нужно установить интеграцию

### `DOCsIntegrationRule`

ID: `P:TFlex.ApplicationSessionSetup.DOCsIntegrationRule`

Название правила настройки интеграции в T-FLEX DOCs

### `DOCsLanguage`

ID: `P:TFlex.ApplicationSessionSetup.DOCsLanguage`

Язык продукта T-FLEX DOCs, с которым необходимо установить интеграцию

Remarks: Используйте значение `TFlex::Application::Language::Default` для интеграции с T-FLEX DOCs той же языковой версии, что и T-FLEX CAD

### `DOCsProductName`

ID: `P:TFlex.ApplicationSessionSetup.DOCsProductName`

Название продукта T-FLEX DOCs, с которым необходимо установить интеграцию

### `DOCsRegistryKeyName`

ID: `P:TFlex.ApplicationSessionSetup.DOCsRegistryKeyName`

Ключ реестра продукта T-FLEX DOCs, с которым необходимо установить интеграцию

### `Enable3D`

ID: `P:TFlex.ApplicationSessionSetup.Enable3D`

Загрузить модуль работы с 3D информацией

### `EnableDOCs`

ID: `P:TFlex.ApplicationSessionSetup.EnableDOCs`

Разрешить интеграцию с T-FLEX DOCs

### `EnableMacros`

ID: `P:TFlex.ApplicationSessionSetup.EnableMacros`

Разрешить работу макросов

### `PromptToSaveModifiedDocuments`

ID: `P:TFlex.ApplicationSessionSetup.PromptToSaveModifiedDocuments`

Разрешить появление вопроса о необходимости сохранения изменённого документа

### `ProtectionLicense`

ID: `P:TFlex.ApplicationSessionSetup.ProtectionLicense`

Тип лицензии, который необходимо использовать при инициализации

### `ReadOnly`

ID: `P:TFlex.ApplicationSessionSetup.ReadOnly`

Режим работы "Только чтение"

Remarks: Невозможно создание новых объектов и сохранение изменённого файла
