# DIMENSION

Assembly: `TFlexAPI`

## Methods

### `ReplaceCharacteristicDataReferences(CharacteristicDataToReplace!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:DIMENSION.ReplaceCharacteristicDataReferences(CharacteristicDataToReplace!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Заменить ссылки на характерные данные других объектов

Parameters:
- `iData`: Входящие данные для замены ссылок

Returns: false, если хотя бы одна ссылка была удалена, true - иначе

Remarks: Если входящие данные не находят соответствия как-либо ссылке, то она просто пропускается.
