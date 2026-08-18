# TFlex.MessagesBar

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Область сообщений T-FLEX CAD

## Methods

### `AddMessage(System.String,System.String,TFlex.Model.Document)`

ID: `M:TFlex.MessagesBar.AddMessage(System.String,System.String,TFlex.Model.Document)`

Добавить сообщение

Parameters:
- `title`: Заголовок
- `text`: Сообщение
- `document`: Связанный документ

### `AddMessage(System.String,System.String,TFlex.Model.Document,System.Collections.Generic.List`1{TFlex.MessagesBarButton},System.EventHandler`1{TFlex.MessagesBarClickEventArgs},System.IntPtr)`

ID: `M:TFlex.MessagesBar.AddMessage(System.String,System.String,TFlex.Model.Document,System.Collections.Generic.List`1{TFlex.MessagesBarButton},System.EventHandler`1{TFlex.MessagesBarClickEventArgs},System.IntPtr)`

Добавить сообщение

Parameters:
- `title`: Заголовок
- `text`: Сообщение
- `document`: Связанный документ
- `buttons`: Кнопки
- `buttonClicked`: Обработчик события нажатия на кнопки
- `tag`: Пользовательские данные

### `AddMessage(TFlex.MessagesBarMessage)`

ID: `M:TFlex.MessagesBar.AddMessage(TFlex.MessagesBarMessage)`

Добавить сообщение

Parameters:
- `message`: Сообщение

### `CloseMessage(System.IntPtr)`

ID: `M:TFlex.MessagesBar.CloseMessage(System.IntPtr)`

Закрыть сообщение

Parameters:
- `messageId`: Идентификатор сообщения
