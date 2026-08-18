# TFlex.Dialogs.InputControlBase

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Базовый класс для элементов ввода значений

## Methods

### `ApplyChanges`

ID: `M:TFlex.Dialogs.InputControlBase.ApplyChanges`

Применить изменения пользователя

### `ClearOriginalValueIsFromUser`

ID: `M:TFlex.Dialogs.InputControlBase.ClearOriginalValueIsFromUser`

Сбрасывает значение флага OriginalValueIsFromUser

### `DeselectAll`

ID: `M:TFlex.Dialogs.InputControlBase.DeselectAll`

Сбросить селекцию текста

### `EndUserEdit(System.Boolean)`

ID: `M:TFlex.Dialogs.InputControlBase.EndUserEdit(System.Boolean)`

Завершить редактирование

Parameters:
- `tryApply`: Если True, будет сделана попытка применить изменения

Remarks: Данный метод применяет либо отменяет изменения пользователя

### `RevertChanges`

ID: `M:TFlex.Dialogs.InputControlBase.RevertChanges`

Отменить изменения пользователя

### `Select(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.InputControlBase.Select(System.Int32,System.Int32)`

Выделить указанный текст

### `SelectAll`

ID: `M:TFlex.Dialogs.InputControlBase.SelectAll`

Выделить весь текст

## Propertys

### `Buttons`

ID: `P:TFlex.Dialogs.InputControlBase.Buttons`

Доступ к дополнительным кнопкам

### `CurrentValueListIndex`

ID: `P:TFlex.Dialogs.InputControlBase.CurrentValueListIndex`

Индекс текущего элемента списка (для итерации колёсиком мыши)

### `FocusLostBehavior`

ID: `P:TFlex.Dialogs.InputControlBase.FocusLostBehavior`

Поведение при потере фокуса

### `IsAutocomplete`

ID: `P:TFlex.Dialogs.InputControlBase.IsAutocomplete`

Флаг индикатор того, что у контрола включено автодополнение

### `IsDirty`

ID: `P:TFlex.Dialogs.InputControlBase.IsDirty`

Получить флаг IsDirty

### `IsManyValues`

ID: `P:TFlex.Dialogs.InputControlBase.IsManyValues`

Флаг индикатор того, что контрол отображает сразу несколько значений

### `IsUserValue`

ID: `P:TFlex.Dialogs.InputControlBase.IsUserValue`

Возвращает True, если текущее значение получено от пользователя

### `IsValid`

ID: `P:TFlex.Dialogs.InputControlBase.IsValid`

Управление состоянием корректности ввода

### `ManyValuesText`

ID: `P:TFlex.Dialogs.InputControlBase.ManyValuesText`

Текст, показываемый пользователю в режиме IsManyValues

### `OriginalValueIsFromUser`

ID: `P:TFlex.Dialogs.InputControlBase.OriginalValueIsFromUser`

Возвращает True, если стабильное значение получено от пользователя (а не задано программно)

### `SelectionLength`

ID: `P:TFlex.Dialogs.InputControlBase.SelectionLength`

Длина селекции

### `SelectionStart`

ID: `P:TFlex.Dialogs.InputControlBase.SelectionStart`

Позиция начала селекции

### `Text`

ID: `P:TFlex.Dialogs.InputControlBase.Text`

Получить текст

### `ValueList`

ID: `P:TFlex.Dialogs.InputControlBase.ValueList`

Доступ к списку значений

### `ValueListMode`

ID: `P:TFlex.Dialogs.InputControlBase.ValueListMode`

Режим списка значений

## Events

### `ChangesApplied`

ID: `E:TFlex.Dialogs.InputControlBase.ChangesApplied`

Событие применения изменений

### `ChangesReverted`

ID: `E:TFlex.Dialogs.InputControlBase.ChangesReverted`

События отмены изменений
