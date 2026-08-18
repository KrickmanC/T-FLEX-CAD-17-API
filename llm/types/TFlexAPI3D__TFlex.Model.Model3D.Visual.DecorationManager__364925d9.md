# TFlex.Model.Model3D.Visual.DecorationManager

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Visual`

## Summary

Диспетчер декораций

## Remarks

Для того, чтобы декорация стала видимой, ее нужно добавить в диспетчер соответствующего документа

## Methods

### `AddDecoration(TFlex.Model.Model3D.Visual.Decoration)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationManager.AddDecoration(TFlex.Model.Model3D.Visual.Decoration)`

Регистрация декорации

Remarks: Недопустимо регистрировать декорацию более одного раза. Декорации, связанные с манипулятором, не надо регистрировать. Для зарегистрированной декорации Dispose() вызывается автоматически.

### `GetDecoration(System.String)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationManager.GetDecoration(System.String)`

Поиск декорации

### `GetManager(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationManager.GetManager(TFlex.Model.Document)`

Получение диспетчера для соответствующего документа

### `RemoveAllDecorations`

ID: `M:TFlex.Model.Model3D.Visual.DecorationManager.RemoveAllDecorations`

Удаление всех декораций

Remarks: После удаления декорации из диспетчера обращение к ней недопустимо. Метод Dispose() вызывается автоматически при удалении декорации.

### `RemoveDecoration(System.String)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationManager.RemoveDecoration(System.String)`

Удаление декорации

Remarks: После удаления декорации из диспетчера обращение к ней недопустимо. Метод Dispose() вызывается автоматически при удалении декорации.

## Propertys

### `Owner`

ID: `P:TFlex.Model.Model3D.Visual.DecorationManager.Owner`

Документ, соответствующий диспетчеру
