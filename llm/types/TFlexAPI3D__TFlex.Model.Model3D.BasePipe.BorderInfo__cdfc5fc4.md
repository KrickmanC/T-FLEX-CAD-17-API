# TFlex.Model.Model3D.BasePipe.BorderInfo

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.BasePipe`

## Summary

Класс описывает границу трубопровода

## Methods

### `AddOffset(TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.BasePipe.BorderInfo.AddOffset(TFlex.Model.Parameter)`

Добавить параметрическое смещение границы трубопровода

### `GetOffsetList(System.Collections.Generic.List`1{TFlex.Model.Parameter}ref )`

ID: `M:TFlex.Model.Model3D.BasePipe.BorderInfo.GetOffsetList(System.Collections.Generic.List`1{TFlex.Model.Parameter}@)`

Получить список всех параметрических смещений границы трубопровода

### `RemoveOffset`

ID: `M:TFlex.Model.Model3D.BasePipe.BorderInfo.RemoveOffset`

Удалить все параметрические смещения границы трубопровода

### `Reset`

ID: `M:TFlex.Model.Model3D.BasePipe.BorderInfo.Reset`

Сбросить границу в значение по умолчанию, конечная граница в конце пути, начальная граница в начале

## Propertys

### `Offset`

ID: `P:TFlex.Model.Model3D.BasePipe.BorderInfo.Offset`

Полное значение смещения границы трубопровода в единицах пользователя

### `Point`

ID: `P:TFlex.Model.Model3D.BasePipe.BorderInfo.Point`

Добавить / удалить геометрическое смещение границы трубопровода, допустимо заначени null. Все предыдущие параметрические и геометрические смещения будут удалены.
