# TFlex.Model.ModelObject.Reference.ReferenceStates

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.ModelObject.Reference`

## Summary

Флаги для управления ссылками. В настоящей версии, актуальны только для 3D

## Fields

### `NotCheckChanged`

ID: `F:TFlex.Model.ModelObject.Reference.ReferenceStates.NotCheckChanged`

Не проверять изменён ли родитель

### `NotMark`

ID: `F:TFlex.Model.ModelObject.Reference.ReferenceStates.NotMark`

Не маркировать родительскую операцию (используется в операциях, в которых помимо самой операции задаются ссылки на отдельные элементы этой операции. Поскольку маркируются эти элементы, то весь объект маркировать не надо. Например, операция сглаживания)

### `NotShowInTree`

ID: `F:TFlex.Model.ModelObject.Reference.ReferenceStates.NotShowInTree`

Не показывать ссылку в дереве моделей

### `SupplementalInformation`

ID: `F:TFlex.Model.ModelObject.Reference.ReferenceStates.SupplementalInformation`

Если объект ссылается на операцию, то возможны два варианта: объект подменяет эту операцию или объект опрашивает только информацию с этой операции. Во втором случае, чтобы операция оставалась в сцене, нужно передавать этот параметр.
