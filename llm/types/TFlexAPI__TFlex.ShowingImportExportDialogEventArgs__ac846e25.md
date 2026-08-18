# TFlex.ShowingImportExportDialogEventArgs

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Класс, содержащий данные о событии, возникающем перед открытием диалога импорта или экспорта

## Methods

### `AddFilter(System.String)`

ID: `M:TFlex.ShowingImportExportDialogEventArgs.AddFilter(System.String)`

Добавить фильтр к текущему диалогу

Parameters:
- `filter`: Тип импортируемого или экспортируемого файла

### `AddFilter(System.String,System.Int32)`

ID: `M:TFlex.ShowingImportExportDialogEventArgs.AddFilter(System.String,System.Int32)`

Добавить фильтр к текущему диалогу

Parameters:
- `filter`: Тип импортируемого или экспортируемого файла
- `filterID`: Идентификатор фильтра

### `AddFilter(System.String,System.Int32,System.String,System.String)`

ID: `M:TFlex.ShowingImportExportDialogEventArgs.AddFilter(System.String,System.Int32,System.String,System.String)`

Добавить фильтр к текущему диалогу

Parameters:
- `filter`: Тип импортируемого или экспортируемого файла
- `filterID`: Идентификатор фильтра
- `description`: Описание формата
- `group`: Группа в которую будет помещен фильтр
