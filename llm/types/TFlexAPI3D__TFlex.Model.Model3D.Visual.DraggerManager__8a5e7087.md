# TFlex.Model.Model3D.Visual.DraggerManager

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Visual`

## Summary

Диспетчер манипуляторов

## Remarks

Для того, чтобы манипулятор изображался в 3D окне и мог выбираться, нужно зарегистрировать его в диспетчере соответствующего документа.

## Methods

### `AddDragger(TFlex.Model.Model3D.Visual.Dragger)`

ID: `M:TFlex.Model.Model3D.Visual.DraggerManager.AddDragger(TFlex.Model.Model3D.Visual.Dragger)`

Регистрирует манипулятор

Returns: Идентификатор, который может быть использован в методах GetDragger и RemoveDragger

Remarks: Только после вызова этого метода манипулятор изображается в 3D окне и может выбираться. Манипулятор может быть зарегистрирован только один раз в одном диспетчере.

### `GetDragger(System.Int32)`

ID: `M:TFlex.Model.Model3D.Visual.DraggerManager.GetDragger(System.Int32)`

Возвращает манипулятор с заданным идентификатором

Parameters:
- `id`: Идентификатор, возвращаемый методом AddDragger

### `GetManager(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Visual.DraggerManager.GetManager(TFlex.Model.Document)`

Возвращает диспетчер манипуляторов, связанный с заданным документом

### `RemoveAllDraggers`

ID: `M:TFlex.Model.Model3D.Visual.DraggerManager.RemoveAllDraggers`

Удаляет все манипуляторы

Remarks: После удаления манипулятора из диспетчера обращение к нему недопустимо.

### `RemoveDragger(System.Int32)`

ID: `M:TFlex.Model.Model3D.Visual.DraggerManager.RemoveDragger(System.Int32)`

Удаляет манипулятор с заданным идентификатором

Parameters:
- `id`: Идентификатор, возвращаемый методом AddDragger

Remarks: После удаления манипулятора из диспетчера обращение к нему недопустимо.

### `RemoveDragger(TFlex.Model.Model3D.Visual.Dragger)`

ID: `M:TFlex.Model.Model3D.Visual.DraggerManager.RemoveDragger(TFlex.Model.Model3D.Visual.Dragger)`

Удаляет манипулятор

Remarks: После удаления манипулятора из диспетчера обращение к нему недопустимо.

## Propertys

### `Owner`

ID: `P:TFlex.Model.Model3D.Visual.DraggerManager.Owner`

Возвращает документ, с которым связан диспетчер
