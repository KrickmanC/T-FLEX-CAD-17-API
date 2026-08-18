# TFlex.Model.Data.Filters.ComparisonOperator

Assembly: `TFlexAPIData`
Namespace: `TFlex.Model.Data.Filters`

## Summary

Оператор сравнения

## Methods

### `Compare(System.Object,System.Object)`

ID: `M:TFlex.Model.Data.Filters.ComparisonOperator.Compare(System.Object,System.Object)`

Возвращает значение, указывающее, выполняется ли условие оператора сравнения для указанных операндов

Parameters:
- `firstOperand`: Первый операнд
- `secondOperand`: Второй операнд

Returns: Значение true, если условие оператора выполняется для указанных операндов; в противном случае - значение false

### `Equals(System.Object)`

ID: `M:TFlex.Model.Data.Filters.ComparisonOperator.Equals(System.Object)`

Возвращает значение, указывающее, равен ли заданный объект текущему

Parameters:
- `obj`: Объект для сравнения

Returns: Значение true, если объекты равны; в противном случае - значение false

### `GetAllOperators`

ID: `M:TFlex.Model.Data.Filters.ComparisonOperator.GetAllOperators`

Возвращает список всех операторов сравнения

Returns: Список операторов сравнения

### `GetHashCode`

ID: `M:TFlex.Model.Data.Filters.ComparisonOperator.GetHashCode`

Возвращает хэш-код оператора сравнения

Returns: Хэш-код в виде 32-битового целого числа со знаком

### `GetOperator(TFlex.Model.Data.Filters.ComparisonOperatorType)`

ID: `M:TFlex.Model.Data.Filters.ComparisonOperator.GetOperator(TFlex.Model.Data.Filters.ComparisonOperatorType)`

Возвращает оператор сравнения по его типу

Parameters:
- `type`: Тип оператора сравнения

Returns: Оператор сравнения

### `op_Equality(TFlex.Model.Data.Filters.ComparisonOperator,TFlex.Model.Data.Filters.ComparisonOperator)`

ID: `M:TFlex.Model.Data.Filters.ComparisonOperator.op_Equality(TFlex.Model.Data.Filters.ComparisonOperator,TFlex.Model.Data.Filters.ComparisonOperator)`

Определяет, равны ли указанные операции

Parameters:
- `x`: Первая операция для сравнения
- `y`: Вторая операция для сравнения

Returns: Значение true, если операции равны; в противном случае - значение false

### `op_Inequality(TFlex.Model.Data.Filters.ComparisonOperator,TFlex.Model.Data.Filters.ComparisonOperator)`

ID: `M:TFlex.Model.Data.Filters.ComparisonOperator.op_Inequality(TFlex.Model.Data.Filters.ComparisonOperator,TFlex.Model.Data.Filters.ComparisonOperator)`

Определяет, различаются ли указанные операции

Parameters:
- `x`: Первая операция для сравнения
- `y`: Вторая операция для сравнения

Returns: Значение true, если операции различаются; в противном случае - значение false

## Propertys

### `RequireValueList`

ID: `P:TFlex.Model.Data.Filters.ComparisonOperator.RequireValueList`

Возвращает значение, указывающее, должен ли быть операнд списком значений

### `SupportsSecondOperand`

ID: `P:TFlex.Model.Data.Filters.ComparisonOperator.SupportsSecondOperand`

Возвращает значение, указывающее, поддерживается ли оператором сравнения второй операнд

### `Type`

ID: `P:TFlex.Model.Data.Filters.ComparisonOperator.Type`

Возвращает тип оператора

## Fields

### `ContainsSubstring`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.ContainsSubstring`

Возвращает оператор "Содержит"

### `EndsWithSubstring`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.EndsWithSubstring`

Возвращает оператор "Заканчивается на"

### `Equal`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.Equal`

Возвращает оператор "="

### `GreaterThan`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.GreaterThan`

Возвращает оператор ">"

### `GreaterThanOrEqual`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.GreaterThanOrEqual`

Возвращает оператор ">="

### `IsEmptyString`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.IsEmptyString`

Возвращает оператор "Не содержит текст"

### `IsNotEmptyString`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.IsNotEmptyString`

Возвращает оператор "Содержит текст"

### `IsNotNull`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.IsNotNull`

Возвращает оператор "Содержит какие-либо данные"

### `IsNotOneOf`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.IsNotOneOf`

Возвращает оператор "Не входит в список"

### `IsNull`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.IsNull`

Возвращает оператор "Не содержит данных"

### `IsOneOf`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.IsOneOf`

Возвращает оператор "Входит в список"

### `LessThan`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.LessThan`

Возвращает оператор "<"

### `LessThanOrEqual`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.LessThanOrEqual`

Возвращает оператор "<="

### `MatchMask`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.MatchMask`

Возвращает оператор "Соответствует маске"

### `NotContainSubstring`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.NotContainSubstring`

Возвращает оператор "Не содержит"

### `NotEqual`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.NotEqual`

Возвращает оператор "!="

### `NotMatchMask`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.NotMatchMask`

Возвращает оператор "Не соответствует маске"

### `StartsWithSubstring`

ID: `F:TFlex.Model.Data.Filters.ComparisonOperator.StartsWithSubstring`

Возвращает оператор "Начинается с"
