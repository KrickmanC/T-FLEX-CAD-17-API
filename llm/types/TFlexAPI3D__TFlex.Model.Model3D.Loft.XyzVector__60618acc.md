# TFlex.Model.Model3D.Loft.XyzVector

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Loft`

## Summary

Класс для задания векторного условия с помощью абсолютных или относительных координат X, Y, Z

## Constructors

### `XyzVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Loft.XyzVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор для задания вектора с помощью координат X, Y, Z заданных в локальной системе координат

Parameters:
- `x`: Координата X в локальной системе координат
- `y`: Координата Y в локальной системе координат
- `z`: Координата Z в локальной системе координат
- `magnitude`: Величина коэффициента

### `XyzVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Loft.XyzVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

Конструктор для задания вектора с помощью координат X, Y, Z заданных в локальной системе координат

Parameters:
- `x`: Координата X в локальной системе координат
- `y`: Координата Y в локальной системе координат
- `z`: Координата Z в локальной системе координат
- `magnitude`: Величина коэффициента
- `lcs`: Локальная система координат

## Methods

### `XyzVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Loft.XyzVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор для задания вектора с помощью координат X, Y, Z заданных в локальной системе координат

Parameters:
- `x`: Координата X в локальной системе координат
- `y`: Координата Y в локальной системе координат
- `z`: Координата Z в локальной системе координат
- `magnitude`: Величина коэффициента

### `XyzVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Loft.XyzVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

Конструктор для задания вектора с помощью координат X, Y, Z заданных в локальной системе координат

Parameters:
- `x`: Координата X в локальной системе координат
- `y`: Координата Y в локальной системе координат
- `z`: Координата Z в локальной системе координат
- `magnitude`: Величина коэффициента
- `lcs`: Локальная система координат

## Propertys

### `LocalSystem`

ID: `P:TFlex.Model.Model3D.Loft.XyzVector.LocalSystem`

Получить локальную систему координат

Remarks: Значение равно нулю если установлена глобальная система координат

### `Magnitude`

ID: `P:TFlex.Model.Model3D.Loft.XyzVector.Magnitude`

Получить коэффициент вектора

### `Type`

ID: `P:TFlex.Model.Model3D.Loft.XyzVector.Type`

Получить тип векторного условия

### `X`

ID: `P:TFlex.Model.Model3D.Loft.XyzVector.X`

Возвращает координату X

### `Y`

ID: `P:TFlex.Model.Model3D.Loft.XyzVector.Y`

Возвращает координату Y

### `Z`

ID: `P:TFlex.Model.Model3D.Loft.XyzVector.Z`

Возвращает координату Z
