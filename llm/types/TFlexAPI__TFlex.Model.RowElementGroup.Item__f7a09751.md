# TFlex.Model.RowElementGroup.Item

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.RowElementGroup`

## Summary

Запись группы элементов структуры изделия

## Remarks

Каждая запись представляет 1 или более элементов структуры изделия

## Propertys

### `ChildGroups`

ID: `P:TFlex.Model.RowElementGroup.Item.ChildGroups`

Коллекция дочерних групп элементов.

Remarks: Заполняется только, если используется представление с учётом иерархии

### `MergedCells`

ID: `P:TFlex.Model.RowElementGroup.Item.MergedCells`

Значения, полученные суммированием при объединении элементов. Ключ - идентификатор колонки.

### `MergedElements`

ID: `P:TFlex.Model.RowElementGroup.Item.MergedElements`

Коллекция объединенных записью элементов.

Remarks: Первый элемент главный
