# filtering.Filter

Assembly: `TFlexAPI`
Namespace: `filtering`

## Methods

### `GetTerms`

ID: `M:filtering.Filter.GetTerms`

Возвращает корневую группу условий фильтра

### `IsValid`

ID: `M:filtering.Filter.IsValid`

Возвращает значение, указывающее, является ли фильтр допустимым

Returns: Значение true, если фильтр является допустимым; в противном случае - значение false

### `Match(filtering.IFilteringObject*)`

ID: `M:filtering.Filter.Match(filtering.IFilteringObject*)`

Возвращает значение, указывающее, соответствует ли указанный объект условиям фильтра

Parameters:
- `pObject`: Объект для проверки

Returns: Значение true, если объект соответствует условиям фильтра; в противном случае - значение false

### `Parse(ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,filtering.Term!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:filtering.Filter.Parse(ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,filtering.Term!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Перобразовывает заданное строковое представление фильтра в эквивалентный ему объект фильтра

Parameters:
- `str`: Строковое представление фильтра
- `templateTerm`: шаблон выражения

Returns: Фильтр, эквивалентный указанному строковому представлению

### `ToString`

ID: `M:filtering.Filter.ToString`

Возвращает строковое представление фильтра

Returns: Строковое представление фильтра
