# TFlex.OpenDocumentOptions

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Параметры открытия документов

## Propertys

### `Cancellable`

ID: `P:TFlex.OpenDocumentOptions.Cancellable`

Указывает, должно ли выводиться окно отмены команды

Remarks: Может использоваться совместно с для возможности отмены команды как пользователем, так и программно

### `CancellationToken`

ID: `P:TFlex.OpenDocumentOptions.CancellationToken`

Объект для уведомления о необходимости отмены команды

Remarks: Может использоваться совместно с для возможности отмены команды как пользователем, так и программно

### `FileLinksRefreshMode`

ID: `P:TFlex.OpenDocumentOptions.FileLinksRefreshMode`

Режим обновления файловых ссылок

Remarks: Отличное от `null` значение имеет приоритет над

### `ForceNewObject`

ID: `P:TFlex.OpenDocumentOptions.ForceNewObject`

Создавать новый объект `T:TFlex.Model.Document` , даже если файл уже открыт

### `Import`

ID: `P:TFlex.OpenDocumentOptions.Import`

Импортировать файлы в форматах сторонних приложений

### `ReadOnly`

ID: `P:TFlex.OpenDocumentOptions.ReadOnly`

Открыть документ только для чтения

### `ThrowOnError`

ID: `P:TFlex.OpenDocumentOptions.ThrowOnError`

Выбрасывать исключение при возникновении ошибок

### `Visible`

ID: `P:TFlex.OpenDocumentOptions.Visible`

Указывает, должен ли открытый документ быть видимым
