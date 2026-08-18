# TFlex.Dialogs.BaseControl

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Базовый класс для элементов управления

## Methods

### `Activate`

ID: `M:TFlex.Dialogs.BaseControl.Activate`

Сделать элемент текущим активным элементом

### `DisableLocalization`

ID: `M:TFlex.Dialogs.BaseControl.DisableLocalization`

Отключить локализацию данного элемента

### `Focus`

ID: `M:TFlex.Dialogs.BaseControl.Focus`

Установить фокус ввода на элемент

### `RemoveAllEventHandlers(System.Boolean)`

ID: `M:TFlex.Dialogs.BaseControl.RemoveAllEventHandlers(System.Boolean)`

Отписать все подписанные обработчики событий

### `SetCustomLocalizationId(System.String)`

ID: `M:TFlex.Dialogs.BaseControl.SetCustomLocalizationId(System.String)`

Задать отдельный идентификатор для локализации

### `SetCustomLocalizationId(System.String,System.Boolean)`

ID: `M:TFlex.Dialogs.BaseControl.SetCustomLocalizationId(System.String,System.Boolean)`

Задать отдельный идентификатор для локализации

Parameters:
- `inherited`: Если true, то дочерние элементы наследуют заданный идентификатор

### `SuppressEvents`

ID: `M:TFlex.Dialogs.BaseControl.SuppressEvents`

Заглушить события

Remarks: Данный метод возвращает экземпляр класса EventSuppressor. Предполагается использование с ключевым словом using.

### `SuppressEvents(System.Boolean)`

ID: `M:TFlex.Dialogs.BaseControl.SuppressEvents(System.Boolean)`

Заглушить события

Parameters:
- `suppress`: Если true, то счётчик отключения событий будет увеличен, в противном случае уменьшен.

## Propertys

### `AutoAddLabelColon`

ID: `P:TFlex.Dialogs.BaseControl.AutoAddLabelColon`

Автоматически добавлять двоеточие к метке

### `Children`

ID: `P:TFlex.Dialogs.BaseControl.Children`

Доступ к дочерним элементам

### `CustomLocalizationId`

ID: `P:TFlex.Dialogs.BaseControl.CustomLocalizationId`

Отдельный идентификатор для локализации

### `ExtendedHintText`

ID: `P:TFlex.Dialogs.BaseControl.ExtendedHintText`

Расширенный текст подсказки

### `FullId`

ID: `P:TFlex.Dialogs.BaseControl.FullId`

Полный идентификатор элемента

Remarks: Состоит из идентификаторов всех родительских элементов и текущего, разделённых точкой

### `HintDelay`

ID: `P:TFlex.Dialogs.BaseControl.HintDelay`

Задержка показа подсказки в миллисекундах

### `HintDuration`

ID: `P:TFlex.Dialogs.BaseControl.HintDuration`

Продолжительность показа подсказки в миллисекундах

### `HintIcon`

ID: `P:TFlex.Dialogs.BaseControl.HintIcon`

Изображение для подсказки. Изображение показывается во всплывающей подсказке.

### `HintText`

ID: `P:TFlex.Dialogs.BaseControl.HintText`

Текст подсказки

### `HorizontalAlignment`

ID: `P:TFlex.Dialogs.BaseControl.HorizontalAlignment`

Горизонтальное выравнивание элемента

### `Id`

ID: `P:TFlex.Dialogs.BaseControl.Id`

Идентификатор элемента

### `IndexInParent`

ID: `P:TFlex.Dialogs.BaseControl.IndexInParent`

Индекс в родительском элементе

### `IsActive`

ID: `P:TFlex.Dialogs.BaseControl.IsActive`

Элемент является текущим активным элементом в форме

### `IsEnabled`

ID: `P:TFlex.Dialogs.BaseControl.IsEnabled`

Элемент включён

### `IsFocused`

ID: `P:TFlex.Dialogs.BaseControl.IsFocused`

Элемент имеет фокус ввода

### `IsReadOnly`

ID: `P:TFlex.Dialogs.BaseControl.IsReadOnly`

Элемент только для чтения

### `IsRequired`

ID: `P:TFlex.Dialogs.BaseControl.IsRequired`

Обязательный параметр. Влияет на отображение элемента.

### `IsRequirementMet`

ID: `P:TFlex.Dialogs.BaseControl.IsRequirementMet`

Обязательный параметр заполнен. Связан со свойством IsRequired. Влияет на отображение элемента.

### `IsVisible`

ID: `P:TFlex.Dialogs.BaseControl.IsVisible`

Элемент видимый

### `Label`

ID: `P:TFlex.Dialogs.BaseControl.Label`

Текст метки

### `LabelPadding`

ID: `P:TFlex.Dialogs.BaseControl.LabelPadding`

Выравнивание элемента по меткам

### `LabelPosition`

ID: `P:TFlex.Dialogs.BaseControl.LabelPosition`

Положение метки

### `LocalizationMode`

ID: `P:TFlex.Dialogs.BaseControl.LocalizationMode`

Режим локализации

### `LockBehavior`

ID: `P:TFlex.Dialogs.BaseControl.LockBehavior`

Режим работы чекбокса метки

### `LockMode`

ID: `P:TFlex.Dialogs.BaseControl.LockMode`

Режим отображения чекбокса метки

### `LockPadding`

ID: `P:TFlex.Dialogs.BaseControl.LockPadding`

Выравнивание меток по чекбоксам

### `LockState`

ID: `P:TFlex.Dialogs.BaseControl.LockState`

Текущее значение чекбокса метки

### `MaxHeight`

ID: `P:TFlex.Dialogs.BaseControl.MaxHeight`

Максимальная высота элемента

### `MaxWidth`

ID: `P:TFlex.Dialogs.BaseControl.MaxWidth`

Максимальная ширина элемента

### `MinHeight`

ID: `P:TFlex.Dialogs.BaseControl.MinHeight`

Минимальная высота элемента

### `MinWidth`

ID: `P:TFlex.Dialogs.BaseControl.MinWidth`

Минимальная ширина элемента

### `Parent`

ID: `P:TFlex.Dialogs.BaseControl.Parent`

Родительский элемент

### `PlaceholderText`

ID: `P:TFlex.Dialogs.BaseControl.PlaceholderText`

Замещающий текст

### `Tag`

ID: `P:TFlex.Dialogs.BaseControl.Tag`

Пользовательские данные

## Events

### `Activated`

ID: `E:TFlex.Dialogs.BaseControl.Activated`

Событие активации элемента

### `ActiveChanged`

ID: `E:TFlex.Dialogs.BaseControl.ActiveChanged`

Событие активации либо деактивации элемента

### `Deactivated`

ID: `E:TFlex.Dialogs.BaseControl.Deactivated`

Событие деактивации элемента

### `FocusChanged`

ID: `E:TFlex.Dialogs.BaseControl.FocusChanged`

Событие получения либо потери фокуса ввода

### `GotFocus`

ID: `E:TFlex.Dialogs.BaseControl.GotFocus`

Событие получения фокуса ввода

### `Locked`

ID: `E:TFlex.Dialogs.BaseControl.Locked`

Событие установки флажка у чекбокса метки

### `LockedChanged`

ID: `E:TFlex.Dialogs.BaseControl.LockedChanged`

Событие клика по чекбоксу метки

### `LostFocus`

ID: `E:TFlex.Dialogs.BaseControl.LostFocus`

Событие потери фокуса ввода

### `Unlocked`

ID: `E:TFlex.Dialogs.BaseControl.Unlocked`

Событие снятия флажка у чекбокса метки
