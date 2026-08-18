# filtering.TermGroup

Assembly: `TFlexAPI`
Namespace: `filtering`

## Methods

### `AddGroup(filtering.LogicalOperator)`

ID: `M:filtering.TermGroup.AddGroup(filtering.LogicalOperator)`

Добавляет дочернюю группу условий в текущую группу

Parameters:
- `logicalOperator`: Логический оператор

Returns: Добавленная группа условий

### `AsGroup`

ID: `M:filtering.TermGroup.AsGroup`

Приводит текущий объект к типу `T:filtering.TermGroup`

### `Insert(System.Int32,filtering.TermGroupItem*)`

ID: `M:filtering.TermGroup.Insert(System.Int32,filtering.TermGroupItem*)`

Добавляет в текущую группу условий указанный элемент по заданному индексу

Parameters:
- `index`: Индекс, по которому следует вставить элемент
- `pItem`: Элемент, добавляемый в группу условий

### `Match(filtering.IFilteringObject*)`

ID: `M:filtering.TermGroup.Match(filtering.IFilteringObject*)`

Возвращает значение, указывающее, соответствует ли указанный объект условиям группы

Parameters:
- `pObject`: Объект для проверки

Returns: Значение true, если объект соответствует условиям группы; в противном случае - значение false

### `RemoveEmptyGroups(System.Boolean)`

ID: `M:filtering.TermGroup.RemoveEmptyGroups(System.Boolean)`

Удаляет из текущей группы элементы, которые являются пустыми группами

Parameters:
- `recursive`: Значение true, если требуется удалять элементы в дочерних группах; в противном случае - значение false

### `RemoveErrorItems(System.Boolean)`

ID: `M:filtering.TermGroup.RemoveErrorItems(System.Boolean)`

Удаляет из текущей группы элементы, которые находятся в ошибочном состоянии

Parameters:
- `recursive`: Значение true, если требуется удалять элементы в дочерних группах; в противном случае - значение false

### `RemoveItemAt(System.Int32)`

ID: `M:filtering.TermGroup.RemoveItemAt(System.Int32)`

Удаляет из текущей группы условий элемент с указанным индексом

Parameters:
- `index`: Индекс элемента в группе

### `ToString`

ID: `M:filtering.TermGroup.ToString`

Возвращает строковое представление группы условий

Returns: Строковое представление группы условий
