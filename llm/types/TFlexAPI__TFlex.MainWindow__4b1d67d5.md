# TFlex.MainWindow

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Главное окно системы T-FLEX CAD

## Constructors

### `MainWindow`

ID: `M:TFlex.MainWindow.#ctor`

Конструктор

## Methods

### `MainWindow`

ID: `M:TFlex.MainWindow.#ctor`

Конструктор

### `BringToForeground`

ID: `M:TFlex.MainWindow.BringToForeground`

На передний план

### `Close`

ID: `M:TFlex.MainWindow.Close`

Закрыть главное окно

### `EndWaitCursor`

ID: `M:TFlex.MainWindow.EndWaitCursor`

Сбрасывает курсор ожидания

### `InsertPluginMenuItem(System.Int32,System.String,TFlex.MainWindow.InsertMenuPosition,TFlex.Plugin)`

ID: `M:TFlex.MainWindow.InsertPluginMenuItem(System.Int32,System.String,TFlex.MainWindow.InsertMenuPosition,TFlex.Plugin)`

Вставить пункт меню приложения

Parameters:
- `command`: Идентификатор зарегестрированной в приложении команды
- `caption`: Текст пункта меню
- `position`: Место для вставки
- `plugin`: Объект приложения

### `InsertPluginSubMenu(System.String,TFlex.MainWindow.InsertMenuPosition,TFlex.Plugin)`

ID: `M:TFlex.MainWindow.InsertPluginSubMenu(System.String,TFlex.MainWindow.InsertMenuPosition,TFlex.Plugin)`

Вставить подменю приложения

Parameters:
- `caption`: Название подменю
- `position`: Место для вставки
- `plugin`: Объект приложения

### `InsertPluginSubMenu(System.String,TFlex.Menu,System.Int32,TFlex.Plugin)`

ID: `M:TFlex.MainWindow.InsertPluginSubMenu(System.String,TFlex.Menu,System.Int32,TFlex.Plugin)`

Вставить подменю приложения

Parameters:
- `caption`: Название подменю
- `menu`: Объект подменю
- `mainMenuPosition`: Номер позиции для вставки
- `plugin`: Объект приложения

### `InsertPluginSubMenu(System.String,TFlex.Menu,TFlex.MainWindow.InsertMenuPosition,TFlex.Plugin)`

ID: `M:TFlex.MainWindow.InsertPluginSubMenu(System.String,TFlex.Menu,TFlex.MainWindow.InsertMenuPosition,TFlex.Plugin)`

Вставить подменю приложения

Parameters:
- `caption`: Название подменю
- `menu`: Объект подменю
- `position`: Место для вставки
- `plugin`: Объект приложения

### `ProcessCommand(System.Int32)`

ID: `M:TFlex.MainWindow.ProcessCommand(System.Int32)`

Выполнить команду

### `StartWaitCursor`

ID: `M:TFlex.MainWindow.StartWaitCursor`

Устанавливает курсор ожидания

## Propertys

### `Bounds`

ID: `P:TFlex.MainWindow.Bounds`

Прямоугольник границ окна

### `Handle`

ID: `P:TFlex.MainWindow.Handle`

Дескриптор окна

### `Maximized`

ID: `P:TFlex.MainWindow.Maximized`

Окно развернуто

### `MessagesBar`

ID: `P:TFlex.MainWindow.MessagesBar`

Получить область сообщений

### `RibbonBar`

ID: `P:TFlex.MainWindow.RibbonBar`

Получить ленту

### `StatusBar`

ID: `P:TFlex.MainWindow.StatusBar`

Получить статусную строку
