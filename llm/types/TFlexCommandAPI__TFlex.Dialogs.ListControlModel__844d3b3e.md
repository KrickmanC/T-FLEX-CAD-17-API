# TFlex.Dialogs.ListControlModel

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Абстрактная модель данных для ListControl

## Methods

### `GetData(System.Int32,System.Int32,TFlex.Dialogs.ListItemRole)`

ID: `M:TFlex.Dialogs.ListControlModel.GetData(System.Int32,System.Int32,TFlex.Dialogs.ListItemRole)`

Возвращает данные ячейки списка

### `GetHeader(System.Int32,TFlex.Dialogs.ListItemRole)`

ID: `M:TFlex.Dialogs.ListControlModel.GetHeader(System.Int32,TFlex.Dialogs.ListItemRole)`

Возвращает данные заголовка списка

### `GetRowData(System.Int32,TFlex.Dialogs.ListItemRole)`

ID: `M:TFlex.Dialogs.ListControlModel.GetRowData(System.Int32,TFlex.Dialogs.ListItemRole)`

Возвращает данные строки списка

### `OnColumnsInserted(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.ListControlModel.OnColumnsInserted(System.Int32,System.Int32)`

Уведомляет о добавлении новых столбцов

### `OnColumnsRemoved(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.ListControlModel.OnColumnsRemoved(System.Int32,System.Int32)`

Уведомляет об удалении столбцов

### `OnDataChanged(System.Int32,System.Int32,System.Int32,System.Int32,System.Collections.Generic.IList`1{TFlex.Dialogs.ListItemRole})`

ID: `M:TFlex.Dialogs.ListControlModel.OnDataChanged(System.Int32,System.Int32,System.Int32,System.Int32,System.Collections.Generic.IList`1{TFlex.Dialogs.ListItemRole})`

Уведомляет об изменении данных

### `OnDataReset`

ID: `M:TFlex.Dialogs.ListControlModel.OnDataReset`

Уведомляет о сбросе модели

### `OnHeaderChanged(System.Int32,System.Int32,System.Collections.Generic.IList`1{TFlex.Dialogs.ListItemRole})`

ID: `M:TFlex.Dialogs.ListControlModel.OnHeaderChanged(System.Int32,System.Int32,System.Collections.Generic.IList`1{TFlex.Dialogs.ListItemRole})`

Уведомляет об изменении данных заголовка

### `OnRowsInserted(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.ListControlModel.OnRowsInserted(System.Int32,System.Int32)`

Уведомляет об удалении строк

### `OnRowsRemoved(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.ListControlModel.OnRowsRemoved(System.Int32,System.Int32)`

Уведомляет об удалении строк

### `TryChangeData(System.Int32,System.Int32,TFlex.Dialogs.ListItemRole,System.Object)`

ID: `M:TFlex.Dialogs.ListControlModel.TryChangeData(System.Int32,System.Int32,TFlex.Dialogs.ListItemRole,System.Object)`

Попытаться изменить данные в модели.

### `TryChangeRowData(System.Int32,TFlex.Dialogs.ListItemRole,System.Object)`

ID: `M:TFlex.Dialogs.ListControlModel.TryChangeRowData(System.Int32,TFlex.Dialogs.ListItemRole,System.Object)`

Попытаться изменить данные в модели.

## Propertys

### `ColumnCount`

ID: `P:TFlex.Dialogs.ListControlModel.ColumnCount`

Количество столбцов в списке

### `RowCount`

ID: `P:TFlex.Dialogs.ListControlModel.RowCount`

Количество строк в списке

## Events

### `ColumnsInserted`

ID: `E:TFlex.Dialogs.ListControlModel.ColumnsInserted`

Событие добавления столбцов

### `ColumnsRemoved`

ID: `E:TFlex.Dialogs.ListControlModel.ColumnsRemoved`

Событие удаления столбцов

### `DataChanged`

ID: `E:TFlex.Dialogs.ListControlModel.DataChanged`

Событие изменения данных ячейки списка

### `DataReset`

ID: `E:TFlex.Dialogs.ListControlModel.DataReset`

Событие сброса модели

### `HeaderChanged`

ID: `E:TFlex.Dialogs.ListControlModel.HeaderChanged`

Событие изменения данных

### `RowDataChanged`

ID: `E:TFlex.Dialogs.ListControlModel.RowDataChanged`

Событие изменения данных строки списка

### `RowsInserted`

ID: `E:TFlex.Dialogs.ListControlModel.RowsInserted`

Событие добавления строк

### `RowsRemoved`

ID: `E:TFlex.Dialogs.ListControlModel.RowsRemoved`

Событие удаления строк
