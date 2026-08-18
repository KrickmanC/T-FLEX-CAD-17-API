# TFlex.Model.Model3D.TransformationContainer

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Контейнер преобразований 3D элемента

## Methods

### `Add(TFlex.Model.Model3D.Transformation)`

ID: `M:TFlex.Model.Model3D.TransformationContainer.Add(TFlex.Model.Model3D.Transformation)`

Добавить новое преобразование

Parameters:
- `transf`: Индекс в контейнере выбранных объектов

### `Count`

ID: `M:TFlex.Model.Model3D.TransformationContainer.Count`

Количество трансформаций

### `Dispose`

ID: `M:TFlex.Model.Model3D.TransformationContainer.Dispose`

Освободить данные

### `GetAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.TransformationContainer.GetAt(System.Int32)`

Получить преобразование по индексу

Parameters:
- `index`: Индекс в контейнере преобразований объекта

Returns: Преобразование, находящееся в контейнере преобразований объекта с указанным индексом. 0 в случае ошибки

### `MoveAt(System.Int32,TFlex.Model.Model3D.MoveType)`

ID: `M:TFlex.Model.Model3D.TransformationContainer.MoveAt(System.Int32,TFlex.Model.Model3D.MoveType)`

Переместить преобразование вниз или вверх в контейнере преобразований

Parameters:
- `index`: Индекс в контейнере преобразований объекта
- `direction`: Тип перемещения преобразования

### `MoveNext`

ID: `M:TFlex.Model.Model3D.TransformationContainer.MoveNext`

Перейти на следующее преобразование в списке

Returns: Успешно или нет выполнен переход

Remarks: Функция предназначена для перебора преобразований 3D элементов

### `RemoveAll`

ID: `M:TFlex.Model.Model3D.TransformationContainer.RemoveAll`

Удалить все преобразования

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.TransformationContainer.RemoveAt(System.Int32)`

Удалить преобразование по индексу

Parameters:
- `index`: Индекс в контейнере преобразований объекта

### `Reset`

ID: `M:TFlex.Model.Model3D.TransformationContainer.Reset`

Начать перебор преобразований с начала

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.TransformationContainer.Current`

Получить очередное преобразование
