# TFlex.Dialogs.ModalDialog

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Модальный диалог

## Constructors

### `ModalDialog(System.String)`

ID: `M:TFlex.Dialogs.ModalDialog.#ctor(System.String)`

Parameters:
- `title`: Заголовок диалога

### `ModalDialog(System.String,TFlex.Command.PropertiesWindowFormBase)`

ID: `M:TFlex.Dialogs.ModalDialog.#ctor(System.String,TFlex.Command.PropertiesWindowFormBase)`

Parameters:
- `title`: Заголовок диалога
- `form`: Форма с контролами

### `ModalDialog(TFlex.Command.PropertiesWindowFormBase)`

ID: `M:TFlex.Dialogs.ModalDialog.#ctor(TFlex.Command.PropertiesWindowFormBase)`

Parameters:
- `form`: Форма с контролами

## Methods

### `ModalDialog(System.String)`

ID: `M:TFlex.Dialogs.ModalDialog.#ctor(System.String)`

Parameters:
- `title`: Заголовок диалога

### `ModalDialog(System.String,TFlex.Command.PropertiesWindowFormBase)`

ID: `M:TFlex.Dialogs.ModalDialog.#ctor(System.String,TFlex.Command.PropertiesWindowFormBase)`

Parameters:
- `title`: Заголовок диалога
- `form`: Форма с контролами

### `ModalDialog(TFlex.Command.PropertiesWindowFormBase)`

ID: `M:TFlex.Dialogs.ModalDialog.#ctor(TFlex.Command.PropertiesWindowFormBase)`

Parameters:
- `form`: Форма с контролами

### `ShowDialog`

ID: `M:TFlex.Dialogs.ModalDialog.ShowDialog`

Отображает модальный диалог

Returns: True, если пользователь закрыл диалог с помощью кнопки OK, иначе False

Remarks: Данный метод возвращает управление после закрытия диалога

## Propertys

### `CurrentPageIndex`

ID: `P:TFlex.Dialogs.ModalDialog.CurrentPageIndex`

Индекс текущей вкладки

### `Pages`

ID: `P:TFlex.Dialogs.ModalDialog.Pages`

Доступ к коллекции вкладок для данного диалога

### `Title`

ID: `P:TFlex.Dialogs.ModalDialog.Title`

Заголовок окна диалога
