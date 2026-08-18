# TFlex.Model.Data.Filters.TermGroupItem

Assembly: `TFlexAPIData`
Namespace: `TFlex.Model.Data.Filters`

## Summary

Элемент группы условий

## Methods

### `Copy`

ID: `M:TFlex.Model.Data.Filters.TermGroupItem.Copy`

Создает копию текущего элемента в указанной группе условий

Returns: Новый элемент группы условий

### `Match(System.Object)`

ID: `M:TFlex.Model.Data.Filters.TermGroupItem.Match(System.Object)`

Возвращает значение, указывающее, соответствует ли указанный объект условиям текущего элемента

Parameters:
- `obj`: Объект для проверки

Returns: Значение true, если объект соответствует условиям текущего элемента; в противном случае - значение false

## Propertys

### `AsGroup`

ID: `P:TFlex.Model.Data.Filters.TermGroupItem.AsGroup`

Преобразует текущий элемент к типу `T:TFlex.Model.Data.Filters.TermGroup` (если он является группой условий)

### `AsTerm`

ID: `P:TFlex.Model.Data.Filters.TermGroupItem.AsTerm`

Преобразует текущий элемент к типу `T:TFlex.Model.Data.Filters.Term` (если он является условием)

### `IsError`

ID: `P:TFlex.Model.Data.Filters.TermGroupItem.IsError`

Возвращает значение, указывающее, находится ли элемент в ошибочном состоянии

### `IsGroup`

ID: `P:TFlex.Model.Data.Filters.TermGroupItem.IsGroup`

Возвращает значение, указывающее, является ли текущий элемент группой условий

### `IsTerm`

ID: `P:TFlex.Model.Data.Filters.TermGroupItem.IsTerm`

Возвращает значение, указывающее, является ли текущий элемент условием

### `LogicalOperator`

ID: `P:TFlex.Model.Data.Filters.TermGroupItem.LogicalOperator`

Логический оператор, которым текущий элемент соединяется с предыдущим элементом в группе условий
