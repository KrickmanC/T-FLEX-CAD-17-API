# TFlex.Model.Model3D.MoveRotateTransformation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс преобразования перемещения/поворота

## Constructors

### `MoveRotateTransformation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.MoveRotateTransformation.#ctor(TFlex.Model.Document)`

Конструктор для создания нового преобразования перемещения поворота

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `MoveRotateTransformation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.MoveRotateTransformation.#ctor(TFlex.Model.Document)`

Конструктор для создания нового преобразования перемещения поворота

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddRotation(TFlex.Model.Model3D.StandardAxis,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.MoveRotateTransformation.AddRotation(TFlex.Model.Model3D.StandardAxis,TFlex.Model.Parameter)`

Добавить поворот вокруг оси

Parameters:
- `axis`: Ocь поворота
- `param`: Значение угла поворота

### `GetRotation(System.Int32,TFlex.Model.Model3D.StandardAxisref ,TFlex.Model.Parameterref )`

ID: `M:TFlex.Model.Model3D.MoveRotateTransformation.GetRotation(System.Int32,TFlex.Model.Model3D.StandardAxis@,TFlex.Model.Parameter@)`

Получить параметры поворота по индексу

Parameters:
- `index`: Номер поворота
- `axisIndex`: Если функция сработала успешно, то в неё помещается ось относительно которой производится поворот
- `param`: Если функция сработала успешно, то в неё помещается значение угла поворота

### `MoveRotation(System.Int32,TFlex.Model.Model3D.MoveType)`

ID: `M:TFlex.Model.Model3D.MoveRotateTransformation.MoveRotation(System.Int32,TFlex.Model.Model3D.MoveType)`

Переместить вращение вниз или вверх

Parameters:
- `index`: Индекс поворота
- `direction`: Направление перемещения

## Propertys

### `LCS`

ID: `P:TFlex.Model.Model3D.MoveRotateTransformation.LCS`

Система координат, относительно которой производится преобразование

### `Offset_X`

ID: `P:TFlex.Model.Model3D.MoveRotateTransformation.Offset_X`

Значение свойства перемещения вдоль оси X

### `Offset_Y`

ID: `P:TFlex.Model.Model3D.MoveRotateTransformation.Offset_Y`

Значение свойства перемещения вдоль оси Y

### `Offset_Z`

ID: `P:TFlex.Model.Model3D.MoveRotateTransformation.Offset_Z`

Значение свойства перемещения вдоль оси Z

### `OriginType`

ID: `P:TFlex.Model.Model3D.MoveRotateTransformation.OriginType`

Тип поиска системы координат, относительно которой производится преобразование

### `RotationsCount`

ID: `P:TFlex.Model.Model3D.MoveRotateTransformation.RotationsCount`

Количество поворотов

### `Scale`

ID: `P:TFlex.Model.Model3D.MoveRotateTransformation.Scale`

Значение свойства масштабирования
