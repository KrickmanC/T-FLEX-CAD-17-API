# TFlex.Model.BOMRecord

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Запись данных для спецификации

## Methods

### `AddCustomItem`

ID: `M:TFlex.Model.BOMRecord.AddCustomItem`

Добавить пользовательский элемент записи данных спецификации

### `DeleteCustomItem(System.Int32)`

ID: `M:TFlex.Model.BOMRecord.DeleteCustomItem(System.Int32)`

Удалить пользовательский элемент записи данных спецификации

### `GetCustomItem(System.Int32)`

ID: `M:TFlex.Model.BOMRecord.GetCustomItem(System.Int32)`

Получить пользовательский элемент записи данных спецификации

Parameters:
- `index`: Номер записи данных

### `GetStandardItem(TFlex.Model.StandardBOMItemType)`

ID: `M:TFlex.Model.BOMRecord.GetStandardItem(TFlex.Model.StandardBOMItemType)`

Получить стандартный элемент записи данных для спецификации

Parameters:
- `item`: Тип стандартного элемента записи данных для спецификации

## Propertys

### `CustomItemCount`

ID: `P:TFlex.Model.BOMRecord.CustomItemCount`

Количество пользовательских элементов записи данных спецификации

### `IncludeToAssemblyBOM`

ID: `P:TFlex.Model.BOMRecord.IncludeToAssemblyBOM`

Включать запись в спецификацию сборочного документа

### `IncludeToCurrentDocumentBOM`

ID: `P:TFlex.Model.BOMRecord.IncludeToCurrentDocumentBOM`

Включать запись в спецификацию текущего документа
