# TFlex.Model.Model3D.Visual.Group

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Visual`

## Summary

Базовый класс для групп

## Remarks

Класс служит для группировки узлов в дереве сцены. При выводе на экран, поиске и прочих действиях дерево обходится слева направо и сверху вниз.

## Methods

### `AddChild(TFlex.Model.Model3D.Visual.SceneNode)`

ID: `M:TFlex.Model.Model3D.Visual.Group.AddChild(TFlex.Model.Model3D.Visual.SceneNode)`

Узел становится правым потомком группы.

### `FindChild(TFlex.Model.Model3D.Visual.SceneNode)`

ID: `M:TFlex.Model.Model3D.Visual.Group.FindChild(TFlex.Model.Model3D.Visual.SceneNode)`

В случае, если node является потомком группы, возвращает его индекс, иначе возвращает -1.

### `GetChild(System.Int32)`

ID: `M:TFlex.Model.Model3D.Visual.Group.GetChild(System.Int32)`

Возвращает потомка с заданным индексом, null в случае, если такого не существует.

### `GetNumChildren`

ID: `M:TFlex.Model.Model3D.Visual.Group.GetNumChildren`

Возвращает число потомков группы.

### `InsertChild(System.Int32,TFlex.Model.Model3D.Visual.SceneNode)`

ID: `M:TFlex.Model.Model3D.Visual.Group.InsertChild(System.Int32,TFlex.Model.Model3D.Visual.SceneNode)`

Вставляет узел в число потомков.

### `RemoveChild(System.Int32)`

ID: `M:TFlex.Model.Model3D.Visual.Group.RemoveChild(System.Int32)`

Удаляет потомка с соответствующим индексом. Потомки с большими индексами сдвигаются влево.

### `RemoveChild(TFlex.Model.Model3D.Visual.SceneNode)`

ID: `M:TFlex.Model.Model3D.Visual.Group.RemoveChild(TFlex.Model.Model3D.Visual.SceneNode)`

Удаляет первого найденного потомка.
