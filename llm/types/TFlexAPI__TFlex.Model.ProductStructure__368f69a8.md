# TFlex.Model.ProductStructure

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс структуры изделия

## Methods

### `AddElement`

ID: `M:TFlex.Model.ProductStructure.AddElement`

Добавить элемент в структуру изделия

### `AddExternalReport(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.ProductStructure.AddExternalReport(TFlex.Model.FileLink)`

Добавить ссылку на внешний отчёт

### `CreateChangesScope`

ID: `M:TFlex.Model.ProductStructure.CreateChangesScope`

Создать область изменений. Структура изделия не будет автоматически пересчитываться при изменениях. Вместо этого она пересчитается когда будет вызван Dispose.

Remarks: Для использования в using.

### `CreateProductStructure(TFlex.Model.Document,TFlex.Model.Data.ProductStructure.Scheme)`

ID: `M:TFlex.Model.ProductStructure.CreateProductStructure(TFlex.Model.Document,TFlex.Model.Data.ProductStructure.Scheme)`

Создать новую структуру изделия

Parameters:
- `doc`: Документ, в котором создаётся новая структура
- `scheme`: Тип структуры изделия

### `CreateProductStructure(TFlex.Model.Document,TFlex.Model.FileLink)`

ID: `M:TFlex.Model.ProductStructure.CreateProductStructure(TFlex.Model.Document,TFlex.Model.FileLink)`

Создать новую структуру изделия

Parameters:
- `doc`: Документ, в котором создаётся новая структура
- `schemeFileLink`: Файл с типом структуры изделия

### `ExportToCSV(TFlex.Model.ProductStructureCsvExportOptions)`

ID: `M:TFlex.Model.ProductStructure.ExportToCSV(TFlex.Model.ProductStructureCsvExportOptions)`

Экспортировать структуру изделия в CSV

Parameters:
- `options`: Параметры экспорта

### `ExportToExcel(TFlex.Model.ProductStructureExcelExportOptions)`

ID: `M:TFlex.Model.ProductStructure.ExportToExcel(TFlex.Model.ProductStructureExcelExportOptions)`

Экспортировать структуру изделия в Excel

Parameters:
- `options`: Параметры экспорта

### `ExportToXml(TFlex.Model.ProductStructureXmlExportOptions)`

ID: `M:TFlex.Model.ProductStructure.ExportToXml(TFlex.Model.ProductStructureXmlExportOptions)`

Экспортировать структуру изделия в xml

Parameters:
- `options`: Параметры экспорта

### `GetActiveProductStructure(TFlex.Model.Document)`

ID: `M:TFlex.Model.ProductStructure.GetActiveProductStructure(TFlex.Model.Document)`

Получить активную структуру изделия

### `GetAllRowElements`

ID: `M:TFlex.Model.ProductStructure.GetAllRowElements`

Получить все элементы структуры изделия

### `GetExternalReports`

ID: `M:TFlex.Model.ProductStructure.GetExternalReports`

Получить коллекцию ссылок на внешние отчёты структуры изделия

### `GetRowElementGroups`

ID: `M:TFlex.Model.ProductStructure.GetRowElementGroups`

Получить группы элементов структуры изделия

Remarks: Для группировки и объединения используется представление по умолчанию

### `GetRowElementGroups(System.Guid)`

ID: `M:TFlex.Model.ProductStructure.GetRowElementGroups(System.Guid)`

Получить группы элементов структуры изделия

Parameters:
- `groupingID`: Идентификатор представления, используемого для группировки и объединения элементов

### `GetRowElementGroups(System.Int32)`

ID: `M:TFlex.Model.ProductStructure.GetRowElementGroups(System.Int32)`

Получить группы элементов структуры изделия

Parameters:
- `groupingIndex`: Индекс представления, используемого для группировки и объединения элементов

### `GetScheme`

ID: `M:TFlex.Model.ProductStructure.GetScheme`

Получить тип структуры изделия

### `HighlightRowElementsConnectedObjects(System.Collections.Generic.IEnumerable`1{TFlex.Model.RowElement})`

ID: `M:TFlex.Model.ProductStructure.HighlightRowElementsConnectedObjects(System.Collections.Generic.IEnumerable`1{TFlex.Model.RowElement})`

Подсветить связанные с записями модельные объекты в сцене(в виде)

### `InitializeByPrototype(System.String)`

ID: `M:TFlex.Model.ProductStructure.InitializeByPrototype(System.String)`

Инициалихация структуры изделия по прототипу

Parameters:
- `prototypeName`: Имя прототипа

### `RemoveExternalReport(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.ProductStructure.RemoveExternalReport(TFlex.Model.FileLink)`

Удалить ссылку на внешний отчёт

### `RunReportGeneration(System.Guid,TFlex.Model.ProductStructureReportOptions)`

ID: `M:TFlex.Model.ProductStructure.RunReportGeneration(System.Guid,TFlex.Model.ProductStructureReportOptions)`

Запустить генерацию отчета структуры изделия

Parameters:
- `reportID`: Идентификатор отчета. Можно получить из схемы структуры изделия.
- `options`: Параметры генерации

### `SetActiveProductStructure(TFlex.Model.ProductStructure)`

ID: `M:TFlex.Model.ProductStructure.SetActiveProductStructure(TFlex.Model.ProductStructure)`

Сделать структуру изделия активной

### `SetScheme(TFlex.Model.Data.ProductStructure.Scheme)`

ID: `M:TFlex.Model.ProductStructure.SetScheme(TFlex.Model.Data.ProductStructure.Scheme)`

Изменить тип структуры изделия

Parameters:
- `scheme`: Тип структуры изделия

### `ShowInProductStructureWindow`

ID: `M:TFlex.Model.ProductStructure.ShowInProductStructureWindow`

Показать структуру изделия в окне "Структура изделия"

### `UpdateReports`

ID: `M:TFlex.Model.ProductStructure.UpdateReports`

Обновить все отчёты структуры изделия

### `UpdateReports(System.Collections.Generic.IEnumerable`1{TFlex.Model.Model2D.RichText})`

ID: `M:TFlex.Model.ProductStructure.UpdateReports(System.Collections.Generic.IEnumerable`1{TFlex.Model.Model2D.RichText})`

Обновить выбранные отчёты структуры изделия

### `UpdateStructure`

ID: `M:TFlex.Model.ProductStructure.UpdateStructure`

Обновить структуру изделия

## Propertys

### `IsCreatedForVersion`

ID: `P:TFlex.Model.ProductStructure.IsCreatedForVersion`

Структура изделия связана с исполнением

### `IsShownInProductStructureWindow`

ID: `P:TFlex.Model.ProductStructure.IsShownInProductStructureWindow`

Структура изделия показана в окне "Структура изделия"

### `SchemeId`

ID: `P:TFlex.Model.ProductStructure.SchemeId`

Идентификатор типа структуры изделия
