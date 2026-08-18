# TFlex.Model.ModelObjectAttributes

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Methods

### `DeleteAllAttributes`

ID: `M:TFlex.Model.ModelObjectAttributes.DeleteAllAttributes`

Удалить все атрибуты

### `DeleteAllAttributes(System.Boolean)`

ID: `M:TFlex.Model.ModelObjectAttributes.DeleteAllAttributes(System.Boolean)`

Удалить все атрибуты

Parameters:
- `change`: Удалить значения атрибутов

### `DeleteAttribute(System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.DeleteAttribute(System.String)`

Удалить атрибут

Parameters:
- `attribName`: Имя атрибута

### `DeleteAttribute(System.String,System.Boolean)`

ID: `M:TFlex.Model.ModelObjectAttributes.DeleteAttribute(System.String,System.Boolean)`

Удалить атрибут

Parameters:
- `attribName`: Имя атрибута
- `change`: Удалить значение атрибута

### `GetAttributeType(System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.GetAttributeType(System.String)`

Получить тип атрибута атрибута

Parameters:
- `attribName`: Имя атрибута

Returns: Тип атрибута

### `GetEnumerator`

ID: `M:TFlex.Model.ModelObjectAttributes.GetEnumerator`

Получить перечислитель

### `GetIntAttribute(System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.GetIntAttribute(System.String)`

Получить значение целого атрибута

Parameters:
- `attribName`: Имя атрибута

Returns: Значение атрибута

### `GetRealAttribute(System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.GetRealAttribute(System.String)`

Получить значение вещественного атрибута

Parameters:
- `attribName`: Имя атрибута

Returns: Значение атрибута

### `GetTextAttribute(System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.GetTextAttribute(System.String)`

Получить значение текстового атрибута

Parameters:
- `attribName`: Имя атрибута

Returns: Значение атрибута

### `GetTextAttributeIfExist(System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.GetTextAttributeIfExist(System.String)`

Получить значение текстового атрибута

Parameters:
- `attribName`: Имя атрибута

Returns: Значение атрибута или null, если атрибута не существует

### `HaveAttribute(System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.HaveAttribute(System.String)`

Проверить существование атрибута

Parameters:
- `attribName`: Имя атрибута

Returns: true, если атрибут с таким именем существует, иначе false

### `MoveNext`

ID: `M:TFlex.Model.ModelObjectAttributes.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.ModelObjectAttributes.Reset`

Сбросить перечислитель

### `SetIntAttribute(System.String,System.Int32)`

ID: `M:TFlex.Model.ModelObjectAttributes.SetIntAttribute(System.String,System.Int32)`

Установить значение целого атрибута

Parameters:
- `attribName`: Имя атрибута
- `value`: Устанавливаемое значение атрибута

### `SetIntAttribute(System.String,System.Int32,System.Boolean)`

ID: `M:TFlex.Model.ModelObjectAttributes.SetIntAttribute(System.String,System.Int32,System.Boolean)`

Установить значение целого атрибута

Parameters:
- `attribName`: Имя атрибута
- `value`: Устанавливаемое значение атрибута
- `change`: Изменить значение атрибута

### `SetRealAttribute(System.String,System.Double)`

ID: `M:TFlex.Model.ModelObjectAttributes.SetRealAttribute(System.String,System.Double)`

Установить значение вещественного атрибута

Parameters:
- `attribName`: Имя атрибута
- `value`: Устанавливаемое значение атрибута

### `SetRealAttribute(System.String,System.Double,System.Boolean)`

ID: `M:TFlex.Model.ModelObjectAttributes.SetRealAttribute(System.String,System.Double,System.Boolean)`

Установить значение вещественного атрибута

Parameters:
- `attribName`: Имя атрибута
- `value`: Устанавливаемое значение атрибута
- `change`: Изменить значение атрибута

### `SetTextAttribute(System.String,System.String)`

ID: `M:TFlex.Model.ModelObjectAttributes.SetTextAttribute(System.String,System.String)`

Установить значение текстового атрибута

Parameters:
- `attribName`: Имя атрибута
- `value`: Устанавливаемое значение атрибута

### `SetTextAttribute(System.String,System.String,System.Boolean)`

ID: `M:TFlex.Model.ModelObjectAttributes.SetTextAttribute(System.String,System.String,System.Boolean)`

Установить значение текстового атрибута

Parameters:
- `attribName`: Имя атрибута
- `value`: Устанавливаемое значение атрибута
- `change`: Изменить значение атрибута

## Propertys

### `Current`

ID: `P:TFlex.Model.ModelObjectAttributes.Current`

Получить текущий элемент
