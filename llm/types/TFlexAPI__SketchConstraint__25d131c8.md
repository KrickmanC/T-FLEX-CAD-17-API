# SketchConstraint

Assembly: `TFlexAPI`

## Methods

### `CalculateHelpParameters(TFDocRegenContext*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SketchConstraint.CalculateHelpParameters(TFDocRegenContext*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `CreateAuto(TFDocument*,SketchType,CTFObject*,System.Int32!System.Runtime.CompilerServices.IsLong,CTFObject*,System.Int32!System.Runtime.CompilerServices.IsLong,CTFObject*,System.Int32!System.Runtime.CompilerServices.IsLong)`

ID: `M:SketchConstraint.CreateAuto(TFDocument*,SketchType,CTFObject*,System.Int32!System.Runtime.CompilerServices.IsLong,CTFObject*,System.Int32!System.Runtime.CompilerServices.IsLong,CTFObject*,System.Int32!System.Runtime.CompilerServices.IsLong)`

Создать ограничение

Remarks: Проверяет входящие параметры. В случае ошибки в параметрах возвращает nullptr

### `FindSpecificGeometry(TFDocRegenContext*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsConst)`

ID: `M:SketchConstraint.FindSpecificGeometry(TFDocRegenContext*,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsConst)`

### `GenerateMetafile(TFDocRegenContext*)`

ID: `M:SketchConstraint.GenerateMetafile(TFDocRegenContext*)`

### `GetStatusCode`

ID: `M:SketchConstraint.GetStatusCode`

### `HasConstraints`

ID: `M:SketchConstraint.HasConstraints`

### `ReplaceCharacteristicDataReferences(CharacteristicDataToReplace!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:SketchConstraint.ReplaceCharacteristicDataReferences(CharacteristicDataToReplace!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Заменить ссылки на характерные данные других объектов

Parameters:
- `iData`: Входящие данные для замены ссылок

Returns: false, если хотя бы одна ссылка была удалена, true - иначе

Remarks: Если входящие данные не находят соответствия как-либо ссылке, то она просто пропускается.
