# TFlex.Command.PropertiesWindow

Assembly: `TFlexAPI`
Namespace: `TFlex.Command`

## Summary

Класс, представляющий служебное окно свойств объекта

## Constructors

### `PropertiesWindow`

ID: `M:TFlex.Command.PropertiesWindow.#ctor`

Конструктор

## Methods

### `PropertiesWindow`

ID: `M:TFlex.Command.PropertiesWindow.#ctor`

Конструктор

### `AppendBaseForm(TFlex.Command.PropertiesWindowFormBase)`

ID: `M:TFlex.Command.PropertiesWindow.AppendBaseForm(TFlex.Command.PropertiesWindowFormBase)`

Добавить вкладку к служебному окну свойств

Parameters:
- `form`: Вкладка служебного окна

### `AppendForm(TFlex.Command.PropertiesWindowForm)`

ID: `M:TFlex.Command.PropertiesWindow.AppendForm(TFlex.Command.PropertiesWindowForm)`

Добавить вкладку к служебному окну свойств

Parameters:
- `form`: Вкладка служебного окна

### `AppendForm(TFlex.Command.PropertiesWindowFormBase)`

ID: `M:TFlex.Command.PropertiesWindow.AppendForm(TFlex.Command.PropertiesWindowFormBase)`

Добавить вкладку к служебному окну свойств

Parameters:
- `form`: Вкладка служебного окна

### `AppendWpfForm(TFlex.Command.PropertiesWindowWpfForm)`

ID: `M:TFlex.Command.PropertiesWindow.AppendWpfForm(TFlex.Command.PropertiesWindowWpfForm)`

Добавить WPF вкладку к служебному окну свойств

Parameters:
- `form`: Вкладка служебного окна

### `Dispose`

ID: `M:TFlex.Command.PropertiesWindow.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `EnableHeaderButton(TFlex.Command.PropertiesWindowHeaderButton,System.Boolean)`

ID: `M:TFlex.Command.PropertiesWindow.EnableHeaderButton(TFlex.Command.PropertiesWindowHeaderButton,System.Boolean)`

Доступность кнопки служебного окна свойств

Parameters:
- `button`: Кнопка окна свойств
- `enable`: true - кнопка доступна, false - кнопка заблокирована

### `HeaderButtonEnabled(TFlex.Command.PropertiesWindowHeaderButton)`

ID: `M:TFlex.Command.PropertiesWindow.HeaderButtonEnabled(TFlex.Command.PropertiesWindowHeaderButton)`

Доступность кнопки служебного окна свойств

Parameters:
- `button`: Кнопка окна свойств

## Propertys

### `Caption`

ID: `P:TFlex.Command.PropertiesWindow.Caption`

Заголовок служебного окна свойств

### `PropertiesHeaderType`

ID: `P:TFlex.Command.PropertiesWindow.PropertiesHeaderType`

Набор кнопок служебного окна свойств

## Events

### `HeaderButtonPressed`

ID: `E:TFlex.Command.PropertiesWindow.HeaderButtonPressed`

Событие, возникающее при нажатии одной из кнопок служебного окна свойств
