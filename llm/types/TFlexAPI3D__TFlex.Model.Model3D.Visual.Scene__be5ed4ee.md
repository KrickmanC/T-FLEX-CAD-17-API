# TFlex.Model.Model3D.Visual.Scene

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Visual`

## Summary

Класс обеспечивает доступ к трёхмерной сцене документа

## Remarks

Сцена представляет из себя набор узлов, каждый из которых является изображением одного из трёхмерных модельных объектов

## Methods

### `Add(TFlex.Model.Model3D.Visual.ObjectRepresentation)`

ID: `M:TFlex.Model.Model3D.Visual.Scene.Add(TFlex.Model.Model3D.Visual.ObjectRepresentation)`

Добавление узла в сцену

### `Find(TFlex.Model.Model3D.Object3D)`

ID: `M:TFlex.Model.Model3D.Visual.Scene.Find(TFlex.Model.Model3D.Object3D)`

Поиск узла, соответствующего данному объекту

Remarks: Возвращает null в случае, если объект не представлен в сцене

### `GetScene(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Visual.Scene.GetScene(TFlex.Model.Document)`

Возвращает сцену, принадлежащую данному документу

### `Remove(TFlex.Model.Model3D.Visual.ObjectRepresentation)`

ID: `M:TFlex.Model.Model3D.Visual.Scene.Remove(TFlex.Model.Model3D.Visual.ObjectRepresentation)`

Удаление узла
