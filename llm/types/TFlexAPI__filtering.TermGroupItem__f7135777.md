# filtering.TermGroupItem

Assembly: `TFlexAPI`
Namespace: `filtering`

## Methods

### `AsGroup`

ID: `M:filtering.TermGroupItem.AsGroup`

Приводит текущий элемент к типу `T:filtering.TermGroup` (если он является группой условий)

### `AsTerm`

ID: `M:filtering.TermGroupItem.AsTerm`

Преобразует текущий элемент к типу `T:filtering.Term` (если он является условием)

### `GetLogicalOperator`

ID: `M:filtering.TermGroupItem.GetLogicalOperator`

Логический оператор, которым текущий элемент соединяется с предыдущим элементом в группе условий

### `IsError`

ID: `M:filtering.TermGroupItem.IsError`

Возвращает значение, указывающее, находится ли элемент в ошибочном состоянии

### `IsGroup`

ID: `M:filtering.TermGroupItem.IsGroup`

Возвращает значение, указывающее, является ли текущий элемент группой условий

### `IsTerm`

ID: `M:filtering.TermGroupItem.IsTerm`

Возвращает значение, указывающее, является ли текущий элемент условием

### `Match(filtering.IFilteringObject*)`

ID: `M:filtering.TermGroupItem.Match(filtering.IFilteringObject*)`

Возвращает значение, указывающее, соответствует ли указанный объект условиям текущего элемента

Parameters:
- `pObject`: объект для проверки

Returns: Значение true, если объект соответствует условиям текущего элемента; в противном случае - значение false
