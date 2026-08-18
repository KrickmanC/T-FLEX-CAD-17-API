# TFlex.Model.Data.Filters.TermGroup

Assembly: `TFlexAPIData`
Namespace: `TFlex.Model.Data.Filters`

## Summary

Группа условий фильтра

## Constructors

### `TermGroup`

ID: `M:TFlex.Model.Data.Filters.TermGroup.#ctor`

Создает новую группу условий

## Methods

### `TermGroup`

ID: `M:TFlex.Model.Data.Filters.TermGroup.#ctor`

Создает новую группу условий

### `Add(TFlex.Model.Data.Filters.TermGroupItem)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.Add(TFlex.Model.Data.Filters.TermGroupItem)`

Добавляет указанный элемент в текущую группу условий

Parameters:
- `item`: Элемент для добавления

### `AddGroup(TFlex.Model.Data.Filters.LogicalOperator)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.AddGroup(TFlex.Model.Data.Filters.LogicalOperator)`

Добавляет дочернюю группу условий в текущую группу

Parameters:
- `logicalOperator`: Логический оператор

Returns: Добавленная группа условий

### `Clear`

ID: `M:TFlex.Model.Data.Filters.TermGroup.Clear`

Очищает текущую группу условий

### `Contains(TFlex.Model.Data.Filters.TermGroupItem)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.Contains(TFlex.Model.Data.Filters.TermGroupItem)`

Возвращает значение, указывающее, содержится ли заданный элемент в группе условий

Parameters:
- `item`: Элемент для проверки

Returns: Значение true, если элемент содержится в группе условий; в противном случае - значение false

### `Copy`

ID: `M:TFlex.Model.Data.Filters.TermGroup.Copy`

Копирует текущую группу условий

### `CopyTo(TFlex.Model.Data.Filters.TermGroupItem[],System.Int32)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.CopyTo(TFlex.Model.Data.Filters.TermGroupItem[],System.Int32)`

Копирует элементы группы условий в заданный массив элементов, начиная с указанного индекса

Parameters:
- `array`: Массив элементов
- `arrayIndex`: Индекс в массиве элементов

### `GetEnumerator`

ID: `M:TFlex.Model.Data.Filters.TermGroup.GetEnumerator`

Возвращает перечислитель элементов в группе условий

Returns: Перечислитель элементов в группе условий

### `GetText`

ID: `M:TFlex.Model.Data.Filters.TermGroup.GetText`

Возвращает текстовое представление группы условий

Returns: Текстовое представление группы условий

### `IndexOf(TFlex.Model.Data.Filters.TermGroupItem)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.IndexOf(TFlex.Model.Data.Filters.TermGroupItem)`

Возвращает индекс указанного элемента в текущей группе условий

Parameters:
- `item`: Элемент группы условий

Returns: Индекс элемента в группе

### `Insert(System.Int32,TFlex.Model.Data.Filters.TermGroupItem)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.Insert(System.Int32,TFlex.Model.Data.Filters.TermGroupItem)`

Добавляет в текущую группу условий указанный элемент по заданному индексу

Parameters:
- `index`: Индекс, по которому следует вставить элемент
- `item`: Элемент, добавляемый в группу условий

### `Match(System.Object)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.Match(System.Object)`

Возвращает значение, указывающее, соответствует ли указанный объект условиям группы

Parameters:
- `obj`: Объект для проверки

Returns: Значение true, если объект соответствует условиям группы; в противном случае - значение false

### `Remove(TFlex.Model.Data.Filters.TermGroupItem)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.Remove(TFlex.Model.Data.Filters.TermGroupItem)`

Удаляет указанный элемент из текущей группы условий

Parameters:
- `item`: Элемент для удаления

Returns: Значение true, если элемент успешно удален из группы; в противном случае - значение false

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.RemoveAt(System.Int32)`

Удаляет из текущей группы условий элемент с указанным индексом

Parameters:
- `index`: Индекс элемента в группе

### `RemoveEmptyGroups(System.Boolean)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.RemoveEmptyGroups(System.Boolean)`

Удаляет из текущей группы элементы, которые являются пустыми группами

Parameters:
- `recursive`: Значение true, если требуется удалять элементы в дочерних группах; в противном случае - значение false

Returns: Список групп условий, удалённых в результате операции

### `RemoveErrorItems(System.Boolean)`

ID: `M:TFlex.Model.Data.Filters.TermGroup.RemoveErrorItems(System.Boolean)`

Удаляет из текущей группы элементы, которые находятся в ошибочном состоянии

Parameters:
- `recursive`: Значение true, если требуется удалять элементы в дочерних группах; в противном случае - значение false

Returns: Список элементов группы, удаленных в результате операции

### `ToString`

ID: `M:TFlex.Model.Data.Filters.TermGroup.ToString`

Возвращает строковое представление группы условий

Returns: Строковое представление группы условий

## Propertys

### `AsGroup`

ID: `P:TFlex.Model.Data.Filters.TermGroup.AsGroup`

Приводит текущий объект к типу `T:TFlex.Model.Data.Filters.TermGroup`

### `Count`

ID: `P:TFlex.Model.Data.Filters.TermGroup.Count`

Возвращает количество элементов в группе условий

### `IsReadOnly`

ID: `P:TFlex.Model.Data.Filters.TermGroup.IsReadOnly`

Возвращает значение, указывающее, является ли группа условий доступной только для чтения

### `Item(System.Int32)`

ID: `P:TFlex.Model.Data.Filters.TermGroup.Item(System.Int32)`

Возвращает элемент, находящийся в группе условий по указанному индексу

Parameters:
- `index`: Индекс элемента в группе

Returns: Элемент, находящийся в группе условий по указанному индексу
