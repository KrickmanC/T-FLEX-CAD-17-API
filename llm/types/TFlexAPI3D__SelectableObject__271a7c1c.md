# SelectableObject

Assembly: `TFlexAPI3D`

## Methods

### `GetCharacteristicDataCount`

ID: `M:SelectableObject.GetCharacteristicDataCount`

### `ReplaceCharacteristicDataReferences(CharacteristicDataToReplace!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SelectableObject.ReplaceCharacteristicDataReferences(CharacteristicDataToReplace!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Заменить ссылки на характерные данные других объектов

Parameters:
- `iData`: Входящие данные для замены ссылок

Returns: false, если хотя бы одна ссылка была удалена, true - иначе

Remarks: Если входящие данные не находят соответствия какой-либо ссылке, то эта ссылка просто пропускается.
