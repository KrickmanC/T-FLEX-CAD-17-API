# TFlex.QualityManagement.Script

Assembly: `TFlexAPI`
Namespace: `TFlex.QualityManagement`

## Summary

Сценарий контроля качества

## Methods

### `FixAll(TFlex.Model.Document,TFlex.QualityManagement.RunScriptResult)`

ID: `M:TFlex.QualityManagement.Script.FixAll(TFlex.Model.Document,TFlex.QualityManagement.RunScriptResult)`

Запустить исправления из сценария на указанных документе и отчете о запуске сценария

### `LoadFromFile(System.String)`

ID: `M:TFlex.QualityManagement.Script.LoadFromFile(System.String)`

Загрузить сценарий из файла по указанному пути. При ошибке загрузки выбрасывается исключение.

### `Run(TFlex.Model.Document)`

ID: `M:TFlex.QualityManagement.Script.Run(TFlex.Model.Document)`

Запустить проверки из сценария на указанном документе

### `SaveToFile(System.String)`

ID: `M:TFlex.QualityManagement.Script.SaveToFile(System.String)`

Сохранять сценарий в файл по указанному пути. При ошибке сохранения выбрасывается исключение.

### `TryLoadFromFile(System.String)`

ID: `M:TFlex.QualityManagement.Script.TryLoadFromFile(System.String)`

Загрузить сценарий из файла по указанному пути. При ошибке загрузки возвращается null.

### `TrySaveToFile(System.String)`

ID: `M:TFlex.QualityManagement.Script.TrySaveToFile(System.String)`

Сохранять сценарий в файл по указанному пути. При ошибке сохранения возвращается false.
