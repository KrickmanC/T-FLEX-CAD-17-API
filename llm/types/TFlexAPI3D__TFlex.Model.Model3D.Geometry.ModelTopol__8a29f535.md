# TFlex.Model.Model3D.Geometry.ModelTopol

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для модельных граней, циклов, рёбер и вершин

## Remarks

Для двух элементов поддерживается функция сравнения

## Methods

### `CreateReference`

ID: `M:TFlex.Model.Model3D.Geometry.ModelTopol.CreateReference`

Создать ссылку (создается либо топологическая ссылка, либо ссылочный элемент на топологию)

### `CreateReference(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelTopol.CreateReference(TFlex.Model.Document)`

Создать ссылку в целевом документ (создается либо топологическая ссылка, либо ссылочный элемент на топологию)

### `Dispose`

ID: `M:TFlex.Model.Model3D.Geometry.ModelTopol.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

## Propertys

### `BaseBody`

ID: `P:TFlex.Model.Model3D.Geometry.ModelTopol.BaseBody`

Получить модельное тело, в котором определён элемент

### `Body`

ID: `P:TFlex.Model.Model3D.Geometry.ModelTopol.Body`

Получить модельное тело, в котором определён элемент

### `Box`

ID: `P:TFlex.Model.Model3D.Geometry.ModelTopol.Box`

Получить границы элемента

Returns: Объект, хранящий границы и ссылку на эти геометрические данные элемента

### `ExistentReference`

ID: `P:TFlex.Model.Model3D.Geometry.ModelTopol.ExistentReference`

Возвращается ссылка, если она существует

### `Name`

ID: `P:TFlex.Model.Model3D.Geometry.ModelTopol.Name`

Название элемента

### `Owner`

ID: `P:TFlex.Model.Model3D.Geometry.ModelTopol.Owner`

Получить родительскую операцию

Returns: Объект класса, которому принадлежит геометрический элемент

### `Reference`

ID: `P:TFlex.Model.Model3D.Geometry.ModelTopol.Reference`

Если ссылки не существует, то она создаётся
