# TFlex.Model.Model3D.TransformationGroupContainer

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Контейнер групп трансформаций.

## Methods

### `AddBaseTransfGroup`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.AddBaseTransfGroup`

Добавить новую группу базовых трансформаций в конец контейнера.

### `DeleteAllBaseTransfGroups`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.DeleteAllBaseTransfGroups`

Удалить все группы базовых трансформаций из контейнера.

### `DeleteBaseTransfGroup(System.Int32)`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.DeleteBaseTransfGroup(System.Int32)`

Удалить группу базовых трансформаций из контейнера.

Parameters:
- `index`: индекс удаляемой группы

### `GetBaseTransfCount`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.GetBaseTransfCount`

Получить общее число базовых трансформаций в контейнере.

### `GetBaseTransfGroupAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.GetBaseTransfGroupAt(System.Int32)`

Получить группу базовых трансформаций в контейнере с индексом index.

Parameters:
- `index`: индекс требуемой группы транформаций

### `GetBaseTransfGroups`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.GetBaseTransfGroups`

Получить список всех групп базовых трансформаций в контейнере.

### `MakeNonAssociative`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.MakeNonAssociative`

Заменить все преобразования одним неассоциативным преобразованием

### `MakeNoneAssociative`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.MakeNoneAssociative`

Заменить все преобразования одним неассоциативным преобразованием

### `MoveBaseTransfGroupDown(TFlex.Model.Model3D.TransformationGroup)`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.MoveBaseTransfGroupDown(TFlex.Model.Model3D.TransformationGroup)`

Переместить базовую группу трансформаций на 1 позицию вниз. В случае успеха transfGroup становится устаревшей (IsValid == false).

Parameters:
- `transfGroup`: перемещаемая группа

Returns: возвращает обновленную группу преобразований.

Remarks: после вызова этого метода полученные ранее объекты групп трансформаций TransformationGroup могут ссылаться на другие группы.

### `MoveBaseTransfGroupUp(TFlex.Model.Model3D.TransformationGroup)`

ID: `M:TFlex.Model.Model3D.TransformationGroupContainer.MoveBaseTransfGroupUp(TFlex.Model.Model3D.TransformationGroup)`

Переместить базовую группу трансформаций на 1 позицию вверх. В случае успеха transfGroup становится устаревшей (IsValid == false).

Parameters:
- `transfGroup`: перемещаемая группа

Returns: возвращает обновленную группу преобразований.

Remarks: после вызова этого метода полученные ранее объекты групп трансформаций TransformationGroup могут ссылаться на другие группы.

## Propertys

### `Owner`

ID: `P:TFlex.Model.Model3D.TransformationGroupContainer.Owner`

Объект, которому принадлежит контейнер.

### `SourceCSType`

ID: `P:TFlex.Model.Model3D.TransformationGroupContainer.SourceCSType`

Тип исходной системы координат преобразования
