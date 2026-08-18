# TFlex.Model.ConnectorParameters

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Сonnector parameters

## Methods

### `Find(System.String)`

ID: `M:TFlex.Model.ConnectorParameters.Find(System.String)`

Найти индекс по имени параметра

Parameters:
- `name`: Имя параметра

Returns: Индекс параметра

### `GetParameter(System.Int32)`

ID: `M:TFlex.Model.ConnectorParameters.GetParameter(System.Int32)`

Получить имя параметра по индексу

Parameters:
- `index`: Индекс параметра

Returns: Имя параметра

### `GetRealValue(System.Int32)`

ID: `M:TFlex.Model.ConnectorParameters.GetRealValue(System.Int32)`

Получить вещественное значение параметра

Parameters:
- `index`: Индекс параметра

### `GetTextValue(System.Int32)`

ID: `M:TFlex.Model.ConnectorParameters.GetTextValue(System.Int32)`

Получить текстовое значение параметра

Parameters:
- `index`: Индекс параметра

### `GetVariable(System.Int32)`

ID: `M:TFlex.Model.ConnectorParameters.GetVariable(System.Int32)`

Получить переменную связанную с параметром

Parameters:
- `index`: Индекс параметра

Returns: Переменная

### `IsReal(System.Int32)`

ID: `M:TFlex.Model.ConnectorParameters.IsReal(System.Int32)`

Проверить является ли значением параметра текстовое значение

Parameters:
- `index`: Индекс параметра

### `IsText(System.Int32)`

ID: `M:TFlex.Model.ConnectorParameters.IsText(System.Int32)`

Проверить является ли значением параметра вещественное число

Parameters:
- `index`: Индекс параметра

### `SetRealValue(System.String,System.Double)`

ID: `M:TFlex.Model.ConnectorParameters.SetRealValue(System.String,System.Double)`

Установить вещественное значение параметра

Parameters:
- `name`: Имя параметра
- `value`: Вещественное значение

Returns: Индекс параметра

### `SetRealValue(System.String,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.ConnectorParameters.SetRealValue(System.String,TFlex.Model.Parameter)`

Установить вещественное значение параметра

Parameters:
- `name`: Имя параметра
- `value`: Вещественное значение переменной

Returns: Индекс параметра

Remarks: Данный метод используется для установки выражения у параметра коннектора. Результатом выражения должно быть вещественное число.

### `SetTextValue(System.String,System.String)`

ID: `M:TFlex.Model.ConnectorParameters.SetTextValue(System.String,System.String)`

Установить текстовое значение параметра

Parameters:
- `name`: Имя параметра
- `value`: Текстовое значение

Returns: Индекс параметра

### `SetTextValue(System.String,TFlex.Model.Variable)`

ID: `M:TFlex.Model.ConnectorParameters.SetTextValue(System.String,TFlex.Model.Variable)`

Установить текстовое значение параметра

Parameters:
- `name`: Имя параметра
- `value`: Текстовое значение переменной

Returns: Индекс параметра

Remarks: Данный метод используется для установки выражения у параметра коннектора. Результатом выражения должно быть текстовое значение.

## Propertys

### `Count`

ID: `P:TFlex.Model.ConnectorParameters.Count`

Количество параметров коннектора
