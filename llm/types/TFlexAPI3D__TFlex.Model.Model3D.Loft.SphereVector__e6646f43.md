# TFlex.Model.Model3D.Loft.SphereVector

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Loft`

## Summary

Класс для задания вектора в абсолютных или относительных сферических координатах

## Constructors

### `SphereVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Loft.SphereVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор для задания вектора в сферических координатах заданных в локальной системе координат

Parameters:
- `phi`: Координата Phi в локальной системе координат
- `theta`: Координата Theta в локальной системе координат
- `magnitude`: Величина коэффициента

### `SphereVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Loft.SphereVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

Конструктор для задания вектора в сферических координат заданных в локальной системе координат

Parameters:
- `phi`: Координата Phi в локальной системе координат
- `theta`: Координата Theta в локальной системе координат
- `magnitude`: Величина коэффициента
- `lcs`: Локальная система координат

## Methods

### `SphereVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Loft.SphereVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор для задания вектора в сферических координатах заданных в локальной системе координат

Parameters:
- `phi`: Координата Phi в локальной системе координат
- `theta`: Координата Theta в локальной системе координат
- `magnitude`: Величина коэффициента

### `SphereVector(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Loft.SphereVector.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Model3D.LCS)`

Конструктор для задания вектора в сферических координат заданных в локальной системе координат

Parameters:
- `phi`: Координата Phi в локальной системе координат
- `theta`: Координата Theta в локальной системе координат
- `magnitude`: Величина коэффициента
- `lcs`: Локальная система координат

## Propertys

### `LocalSystem`

ID: `P:TFlex.Model.Model3D.Loft.SphereVector.LocalSystem`

Получить локальную систему координат

Remarks: Значение равно нулю если установлена глобальная система координат

### `Magnitude`

ID: `P:TFlex.Model.Model3D.Loft.SphereVector.Magnitude`

Получить коэффициент вектора

### `Phi`

ID: `P:TFlex.Model.Model3D.Loft.SphereVector.Phi`

Возвращает координату Phi

### `Theta`

ID: `P:TFlex.Model.Model3D.Loft.SphereVector.Theta`

Возвращает координату Theta

### `Type`

ID: `P:TFlex.Model.Model3D.Loft.SphereVector.Type`

Получить тип векторного условия
