# TFlex.QualityManagement.RunScriptResult

Assembly: `TFlexAPI`
Namespace: `TFlex.QualityManagement`

## Summary

Класс результата проверки сценария, суммирующий результаты отдельных результатов проверок

## Methods

### `GetEnumerator`

ID: `M:TFlex.QualityManagement.RunScriptResult.GetEnumerator`

Получить перечислитель результатов проверок

### `LoadFromFile(System.String)`

ID: `M:TFlex.QualityManagement.RunScriptResult.LoadFromFile(System.String)`

Загрузить результат из файла по указанному пути. При ошибке загрузки выбрасывается исключение.

### `SaveToFile(System.String)`

ID: `M:TFlex.QualityManagement.RunScriptResult.SaveToFile(System.String)`

Сохранять результат в файл по указанному пути. При ошибке сохранения выбрасывается исключение.

### `TryLoadFromFile(System.String)`

ID: `M:TFlex.QualityManagement.RunScriptResult.TryLoadFromFile(System.String)`

Загрузить результат из файла по указанному пути. При ошибке загрузки возвращается null.

### `TrySaveToFile(System.String)`

ID: `M:TFlex.QualityManagement.RunScriptResult.TrySaveToFile(System.String)`

Сохранять результат в файл по указанному пути. При ошибке сохранения возвращается false.

## Propertys

### `IsFixable`

ID: `P:TFlex.QualityManagement.RunScriptResult.IsFixable`

Исправим ли результат
