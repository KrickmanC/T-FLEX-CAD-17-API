# TFlex.Model.Model2D.BOMObject

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс спецификации

## Methods

### `AddRecord`

ID: `M:TFlex.Model.Model2D.BOMObject.AddRecord`

Добавить запись

### `BeginEdit`

ID: `M:TFlex.Model.Model2D.BOMObject.BeginEdit`

Начать изменение спецификации

### `CreateCustomColumn(System.String,TFlex.Model.Model2D.BOMObject.ColumnSettings)`

ID: `M:TFlex.Model.Model2D.BOMObject.CreateCustomColumn(System.String,TFlex.Model.Model2D.BOMObject.ColumnSettings)`

Создать колонку пользовательского типа

Parameters:
- `name`: Имя колонки
- `settings`: Параметры колонки

### `CreateField(System.String,TFlex.Model.Model2D.BOMObject.FieldType)`

ID: `M:TFlex.Model.Model2D.BOMObject.CreateField(System.String,TFlex.Model.Model2D.BOMObject.FieldType)`

Создать поле

### `CreateStandardColumn(System.String,TFlex.Model.Model2D.BOMObject.StandardField,TFlex.Model.Model2D.BOMObject.ColumnSettings)`

ID: `M:TFlex.Model.Model2D.BOMObject.CreateStandardColumn(System.String,TFlex.Model.Model2D.BOMObject.StandardField,TFlex.Model.Model2D.BOMObject.ColumnSettings)`

Создать колонку стандартного типа

Parameters:
- `name`: Название
- `type`: Тип
- `settings`: Параметры колонки

### `CreateVariableColumn(System.String,System.String,TFlex.Model.Model2D.BOMObject.ColumnSettings)`

ID: `M:TFlex.Model.Model2D.BOMObject.CreateVariableColumn(System.String,System.String,TFlex.Model.Model2D.BOMObject.ColumnSettings)`

Создать колонку переменного типа

Parameters:
- `name`: Название
- `variableName`: Имя переменной, значение которой будет заносится в создаваемую колонку
- `settings`: Параметры колонки

### `DeleteAllRecords`

ID: `M:TFlex.Model.Model2D.BOMObject.DeleteAllRecords`

Удалить все записи

### `DeleteRecord`

ID: `M:TFlex.Model.Model2D.BOMObject.DeleteRecord`

Удалить текущую запись

### `EditRecord`

ID: `M:TFlex.Model.Model2D.BOMObject.EditRecord`

Редактировать текущую запись

### `EndEdit`

ID: `M:TFlex.Model.Model2D.BOMObject.EndEdit`

Завершить изменение спецификации

### `GetAllFields`

ID: `M:TFlex.Model.Model2D.BOMObject.GetAllFields`

Получить имена всех полей

### `GetBOMGroups`

ID: `M:TFlex.Model.Model2D.BOMObject.GetBOMGroups`

Получить массив всех разделов спецификации

### `GetFieldGuidValueIndirect(System.UInt32)`

ID: `M:TFlex.Model.Model2D.BOMObject.GetFieldGuidValueIndirect(System.UInt32)`

Получить значение поля в виде GUID

Parameters:
- `fieldIndex`: Индекс поля

### `GetFieldIntValueIndirect(System.UInt32)`

ID: `M:TFlex.Model.Model2D.BOMObject.GetFieldIntValueIndirect(System.UInt32)`

Получить целое значение поля

Parameters:
- `fieldIndex`: Индекс поля

### `GetStandardFieldValue(TFlex.Model.Model2D.BOMObject.StandardField)`

ID: `M:TFlex.Model.Model2D.BOMObject.GetStandardFieldValue(TFlex.Model.Model2D.BOMObject.StandardField)`

Получить значение стандартного поля

Parameters:
- `field`: Стандартное поле

### `GetUserFieldValue(System.String)`

ID: `M:TFlex.Model.Model2D.BOMObject.GetUserFieldValue(System.String)`

Получить значение пользовательского поля

Parameters:
- `fieldName`: Пользовательское поле

### `GetVisibleFields`

ID: `M:TFlex.Model.Model2D.BOMObject.GetVisibleFields`

Получить имена видимых полей в порядке отображения

### `MoveToFrontRecord`

ID: `M:TFlex.Model.Model2D.BOMObject.MoveToFrontRecord`

Перевести курсор на первую запись спецификации

### `MoveToNextRecord`

ID: `M:TFlex.Model.Model2D.BOMObject.MoveToNextRecord`

Перевести курсор на следующую запись спецификации

### `Refresh`

ID: `M:TFlex.Model.Model2D.BOMObject.Refresh`

Обновить спецификацию

### `Refresh(System.Boolean)`

ID: `M:TFlex.Model.Model2D.BOMObject.Refresh(System.Boolean)`

Обновить данные спецификации и спецификацию

Parameters:
- `refreshData`: Обновить данные спецификации

### `SeekToRecordID(System.UInt32)`

ID: `M:TFlex.Model.Model2D.BOMObject.SeekToRecordID(System.UInt32)`

Перевести курсор на запись спецификации с заданным ID

Parameters:
- `id`: Идентификатор записи спецификации

### `SetFieldGuidValueIndirect(System.UInt32,System.Guid)`

ID: `M:TFlex.Model.Model2D.BOMObject.SetFieldGuidValueIndirect(System.UInt32,System.Guid)`

Установить значение поля в виде GUID

Parameters:
- `fieldIndex`: Индекс поля
- `value`: GUID

### `SetFieldIntValueIndirect(System.UInt32,System.Int32)`

ID: `M:TFlex.Model.Model2D.BOMObject.SetFieldIntValueIndirect(System.UInt32,System.Int32)`

Установить целое значение поля

Parameters:
- `fieldIndex`: Индекс поля
- `value`: Значение поля

### `SetVersions(TFlex.Model.Model2D.BOMObject.Version[])`

ID: `M:TFlex.Model.Model2D.BOMObject.SetVersions(TFlex.Model.Model2D.BOMObject.Version[])`

Установить исполнения

Parameters:
- `versions`: Массив исполнений

### `UpdateRecord`

ID: `M:TFlex.Model.Model2D.BOMObject.UpdateRecord`

Обновить текущую запись

### `UpdateStandardFieldValue(TFlex.Model.Model2D.BOMObject.StandardField,System.String)`

ID: `M:TFlex.Model.Model2D.BOMObject.UpdateStandardFieldValue(TFlex.Model.Model2D.BOMObject.StandardField,System.String)`

Установить значение стандартного поля

Parameters:
- `field`: Стандартное поле
- `value`: Значение

### `UpdateUserFieldValue(System.String,System.String)`

ID: `M:TFlex.Model.Model2D.BOMObject.UpdateUserFieldValue(System.String,System.String)`

Установить значение пользовательского поля

Parameters:
- `fieldName`: Имя пользовательского поля
- `value`: Значение

## Propertys

### `FriendlyName`

ID: `P:TFlex.Model.Model2D.BOMObject.FriendlyName`

Название спецификации

### `IsUsedForSetupPositions`

ID: `P:TFlex.Model.Model2D.BOMObject.IsUsedForSetupPositions`

Используется для простановки позиций

### `LinkedFragment`

ID: `P:TFlex.Model.Model2D.BOMObject.LinkedFragment`

Связанный фрагмент

### `NewGroupUseMaxPosition`

ID: `P:TFlex.Model.Model2D.BOMObject.NewGroupUseMaxPosition`

Начинать нумерацию в разделе после максимального значения в предыдущем разделе

### `RecordFlags`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordFlags`

Флаги состояния текущей записи

### `RecordGroup`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordGroup`

Номер раздела текущей записи

### `RecordGroupFullName`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordGroupFullName`

Полное имя раздела текущей записи

### `RecordID`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordID`

ID текущей записи

### `RecordPosition`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordPosition`

Номер позиции текущей записи

### `RecordSpaceAfter`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordSpaceAfter`

Пропуск строк после текущей записи

### `RecordSpaceBefore`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordSpaceBefore`

Пропуск строк перед текущей записью

### `RecordVersion`

ID: `P:TFlex.Model.Model2D.BOMObject.RecordVersion`

Номер исполнения текущей записи

### `ReportFileLink`

ID: `P:TFlex.Model.Model2D.BOMObject.ReportFileLink`

Ссылка на документ спецификации

### `ReportID`

ID: `P:TFlex.Model.Model2D.BOMObject.ReportID`

Идентификатор связаного объекта в документе спецификации

### `SortByPosition`

ID: `P:TFlex.Model.Model2D.BOMObject.SortByPosition`

Сортировка по позициям

### `SubType`

ID: `P:TFlex.Model.Model2D.BOMObject.SubType`

Подтип спецификации
