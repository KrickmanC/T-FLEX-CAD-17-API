# TFlex.Model.Data.Filters.Filter

Assembly: `TFlexAPIData`
Namespace: `TFlex.Model.Data.Filters`

## Summary

Фильтр

## Constructors

### `Filter`

ID: `M:TFlex.Model.Data.Filters.Filter.#ctor`

Создает новый экземпляр фильтра

## Methods

### `Filter`

ID: `M:TFlex.Model.Data.Filters.Filter.#ctor`

Создает новый экземпляр фильтра

### `IsValid`

ID: `M:TFlex.Model.Data.Filters.Filter.IsValid`

Возвращает значение, указывающее, является ли фильтр допустимым

Returns: Значение true, если фильтр является допустимым; в противном случае - значение false

### `Match(System.Object)`

ID: `M:TFlex.Model.Data.Filters.Filter.Match(System.Object)`

Возвращает значение, указывающее, соответствует ли указанный объект условиям фильтра

Parameters:
- `obj`: Объект для проверки

Returns: Значение true, если объект соответствует условиям фильтра; в противном случае - значение false

### `Parse(System.String,TFlex.Model.Data.Filters.Term)`

ID: `M:TFlex.Model.Data.Filters.Filter.Parse(System.String,TFlex.Model.Data.Filters.Term)`

Перобразовывает заданное строковое представление фильтра в эквивалентный ему объект фильтра

Parameters:
- `str`: Строковое представление фильтра
- `termTemplate`: Шаблонный параметр

Returns: Фильтр, эквивалентный указанному строковому представлению

### `ToString`

ID: `M:TFlex.Model.Data.Filters.Filter.ToString`

Возвращает строковое представление фильтра

Returns: Строковое представление фильтра

### `TryParse(System.String,TFlex.Model.Data.Filters.Term,TFlex.Model.Data.Filters.Filterref )`

ID: `M:TFlex.Model.Data.Filters.Filter.TryParse(System.String,TFlex.Model.Data.Filters.Term,TFlex.Model.Data.Filters.Filter@)`

Перобразовывает заданное строковое представление фильтра в эквивалентный ему объект фильтра

Parameters:
- `str`: Строковое представление фильтра
- `termTemplate`: Шаблонный параметр
- `filter`: Фильтр, эквивалентный указанному строковому представлению

Returns: Значение true, если объект фильтра успешно получен; в противном случае - значение false

### `Validate`

ID: `M:TFlex.Model.Data.Filters.Filter.Validate`

Проверяет фильтр на допустимость

## Propertys

### `Terms`

ID: `P:TFlex.Model.Data.Filters.Filter.Terms`

Возвращает корневую группу условий фильтра
