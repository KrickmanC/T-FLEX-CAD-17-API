# TFlex.Dialogs.NumericInputControl

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Контрол ввода числового значения

## Constructors

### `NumericInputControl(System.String)`

ID: `M:TFlex.Dialogs.NumericInputControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор элемента

## Methods

### `NumericInputControl(System.String)`

ID: `M:TFlex.Dialogs.NumericInputControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор элемента

### `CanUserIncrement(System.Boolean)`

ID: `M:TFlex.Dialogs.NumericInputControl.CanUserIncrement(System.Boolean)`

Возвращает true, если значение еще можно увеличить (уменьшить) без выхода за границы

### `ClearDefaultValue`

ID: `M:TFlex.Dialogs.NumericInputControl.ClearDefaultValue`

Сбрасывает значение по умолчанию

### `ClearValue`

ID: `M:TFlex.Dialogs.NumericInputControl.ClearValue`

Сбросить текущее значение. Элемент будет отображать значение по умолчанию

### `Decrement`

ID: `M:TFlex.Dialogs.NumericInputControl.Decrement`

Уменьшить текущее значение

### `Decrement(System.Boolean)`

ID: `M:TFlex.Dialogs.NumericInputControl.Decrement(System.Boolean)`

Уменьшить текущее значение

### `Increment`

ID: `M:TFlex.Dialogs.NumericInputControl.Increment`

Увеличить текущее значение

### `Increment(System.Boolean)`

ID: `M:TFlex.Dialogs.NumericInputControl.Increment(System.Boolean)`

Увеличить текущее значение

### `SetDefaultValue(System.Double)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetDefaultValue(System.Double)`

Устанавливает значение по умолчанию

### `SetDefaultValue(System.Double,TFlex.Model.Units.Unit)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetDefaultValue(System.Double,TFlex.Model.Units.Unit)`

Устанавливает значение по умолчанию

### `SetDefaultValue(TFlex.Model.Variable)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetDefaultValue(TFlex.Model.Variable)`

Устанавливает значение по умолчанию

### `SetDefaultValue(TFlex.Model.Variable,TFlex.Model.Units.Unit)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetDefaultValue(TFlex.Model.Variable,TFlex.Model.Units.Unit)`

Устанавливает значение по умолчанию

### `SetMax(System.Double)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetMax(System.Double)`

Устанавливает максимальное допустимое значение

### `SetMax(System.Double,System.Boolean)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetMax(System.Double,System.Boolean)`

Устанавливает максимальное допустимое значение

### `SetMin(System.Double)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetMin(System.Double)`

Устанавливает минимальное допустимое значение

### `SetMin(System.Double,System.Boolean)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetMin(System.Double,System.Boolean)`

Устанавливает минимальное допустимое значение

### `SetRange(System.Double,System.Double)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetRange(System.Double,System.Double)`

Устанавливает диапазон допустимых значений

### `SetRange(System.Double,System.Double,System.Boolean)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetRange(System.Double,System.Double,System.Boolean)`

Устанавливает диапазон допустимых значений

### `SetRange(TFlex.Dialogs.Range)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetRange(TFlex.Dialogs.Range)`

Устанавливает диапазон допустимых значений

### `SetRange(TFlex.Dialogs.Range,System.Boolean)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetRange(TFlex.Dialogs.Range,System.Boolean)`

Устанавливает диапазон допустимых значений

### `SetValue(System.Double)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetValue(System.Double)`

Установить текущее значение

### `SetValue(System.Double,TFlex.Model.Variable)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetValue(System.Double,TFlex.Model.Variable)`

Установить текущее значение

### `SetValue(System.Double,TFlex.Model.Variable,TFlex.Model.Units.Unit)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetValue(System.Double,TFlex.Model.Variable,TFlex.Model.Units.Unit)`

Установить текущее значение

### `SetVariable(TFlex.Model.Variable)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetVariable(TFlex.Model.Variable)`

Устанавливает текущую переменную

### `SetVariable(TFlex.Model.Variable,TFlex.Model.Units.Unit)`

ID: `M:TFlex.Dialogs.NumericInputControl.SetVariable(TFlex.Model.Variable,TFlex.Model.Units.Unit)`

Устанавливает текущую переменную

### `UserIncrement(System.Int32)`

ID: `M:TFlex.Dialogs.NumericInputControl.UserIncrement(System.Int32)`

Увеличить или уменьшить значение на UserIncrementStep заданное число раз

## Propertys

### `AllowVariable`

ID: `P:TFlex.Dialogs.NumericInputControl.AllowVariable`

Управление флагом, разрешающим задание переменной пользователем

### `AutoApplyByTimeout`

ID: `P:TFlex.Dialogs.NumericInputControl.AutoApplyByTimeout`

Управление флагом автоматического применения значения по таймауту. Имеет смысл когда пользователь вводит число, а не выражение.

### `CanDecrement`

ID: `P:TFlex.Dialogs.NumericInputControl.CanDecrement`

Возвращает true, если можно уменьшить значение

### `CanIncrement`

ID: `P:TFlex.Dialogs.NumericInputControl.CanIncrement`

Возвращает true, если можно увеличить значение

### `ClampedValue`

ID: `P:TFlex.Dialogs.NumericInputControl.ClampedValue`

Возвращает текущее значение, при необходимости обрезанное диапазоном допустимых значений (Range)

### `DefaultText`

ID: `P:TFlex.Dialogs.NumericInputControl.DefaultText`

Возвращает значение по умолчанию в виде текста

### `DefaultUnit`

ID: `P:TFlex.Dialogs.NumericInputControl.DefaultUnit`

Управление единицей измерения по умолчанию

### `DefaultValue`

ID: `P:TFlex.Dialogs.NumericInputControl.DefaultValue`

Управление значением по умолчанию

### `DefaultVariable`

ID: `P:TFlex.Dialogs.NumericInputControl.DefaultVariable`

Управление переменой по умолчанию

### `DefaultVariableStringValue`

ID: `P:TFlex.Dialogs.NumericInputControl.DefaultVariableStringValue`

Возвращает значение переменной по умолчанию в виде текста

### `EffectiveIncrementStep`

ID: `P:TFlex.Dialogs.NumericInputControl.EffectiveIncrementStep`

Реальный шаг прокрутки

### `EffectiveUserIncrementStep`

ID: `P:TFlex.Dialogs.NumericInputControl.EffectiveUserIncrementStep`

Возвращает обработанный UserIncrementStep

### `HasDefaultValue`

ID: `P:TFlex.Dialogs.NumericInputControl.HasDefaultValue`

Возвращает true, если значение по умолчанию задано

### `HasUpDown`

ID: `P:TFlex.Dialogs.NumericInputControl.HasUpDown`

Показывать кнопки Up/Down

### `HasValue`

ID: `P:TFlex.Dialogs.NumericInputControl.HasValue`

Возвращает True, если числовое значение доступно

### `IncrementStep`

ID: `P:TFlex.Dialogs.NumericInputControl.IncrementStep`

Шаг прокрутки

### `IsAutoFormat`

ID: `P:TFlex.Dialogs.NumericInputControl.IsAutoFormat`

Управление флагом автоматического форматирования

### `IsDefaultValue`

ID: `P:TFlex.Dialogs.NumericInputControl.IsDefaultValue`

Возвращает true, если текущее значение является значением по умолчанию

### `IsIntegral`

ID: `P:TFlex.Dialogs.NumericInputControl.IsIntegral`

Разрешать только целые числа

### `IsValueInRange`

ID: `P:TFlex.Dialogs.NumericInputControl.IsValueInRange`

Возвращает True, если числовое значение находится в пределах диапазоа допустимых значений (Range)

### `Max`

ID: `P:TFlex.Dialogs.NumericInputControl.Max`

Управление максимальным допустимым значением

### `Min`

ID: `P:TFlex.Dialogs.NumericInputControl.Min`

Управление минимальным допустимым значением

### `OriginalIsDefaultValue`

ID: `P:TFlex.Dialogs.NumericInputControl.OriginalIsDefaultValue`

Возвращает True, если исходное (стабильное) значение является значением по умолчанию

### `OriginalUnit`

ID: `P:TFlex.Dialogs.NumericInputControl.OriginalUnit`

Исходная (стабильная) единица измерения

### `OriginalValue`

ID: `P:TFlex.Dialogs.NumericInputControl.OriginalValue`

Исходное (стабильное) значение

### `OriginalVariable`

ID: `P:TFlex.Dialogs.NumericInputControl.OriginalVariable`

Исходная (стабильная) переменная

### `Precision`

ID: `P:TFlex.Dialogs.NumericInputControl.Precision`

Точность

### `Range`

ID: `P:TFlex.Dialogs.NumericInputControl.Range`

Управление диапазоном допустимых значений

### `SpinStepAction`

ID: `P:TFlex.Dialogs.NumericInputControl.SpinStepAction`

Действие при прокрутке колёсиком мыши

### `State`

ID: `P:TFlex.Dialogs.NumericInputControl.State`

Возвращает состояние NumericInputControl

### `Unit`

ID: `P:TFlex.Dialogs.NumericInputControl.Unit`

Единица измерения

### `UserIncrementStep`

ID: `P:TFlex.Dialogs.NumericInputControl.UserIncrementStep`

Шаг прокрутки, который может быть изменён пользователем

### `Value`

ID: `P:TFlex.Dialogs.NumericInputControl.Value`

Текущее значение

### `Variable`

ID: `P:TFlex.Dialogs.NumericInputControl.Variable`

Текущая переменная

### `VariableStringValue`

ID: `P:TFlex.Dialogs.NumericInputControl.VariableStringValue`

Возвращает значение текущей переменной как строку

## Events

### `ValueChanged`

ID: `E:TFlex.Dialogs.NumericInputControl.ValueChanged`

Событие изменения значения
