# TFlex.Model.Model3D.Geometry.AffineTransformation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Аффинные преобразования

## Constructors

### `AffineTransformation`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.#ctor`

Конструктор для единичной трансформации

### `AffineTransformation(TFlex.Model.Model3D.Geometry.AffineTransformation)`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.#ctor(TFlex.Model.Model3D.Geometry.AffineTransformation)`

Копирующий конструктор

Parameters:
- `transformation`: Трансформация, с которой копируются параметры для данной трансформации

## Methods

### `AffineTransformation`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.#ctor`

Конструктор для единичной трансформации

### `AffineTransformation(TFlex.Model.Model3D.Geometry.AffineTransformation)`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.#ctor(TFlex.Model.Model3D.Geometry.AffineTransformation)`

Копирующий конструктор

Parameters:
- `transformation`: Трансформация, с которой копируются параметры для данной трансформации

### `Inverse`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.Inverse`

Обратная матрица

### `MoveToLCS(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.MoveToLCS(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.BaseDirection)`

Преобразование совмещением глобальной системы координат с локальной

Parameters:
- `origin`: Начало локальной системы координат
- `zaxis`: Ось Z локальной системы координат
- `xaxis`: Ось X локальной системы координат

### `Rotate(TFlex.Model.Model3D.Geometry.BaseAxis,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.Rotate(TFlex.Model.Model3D.Geometry.BaseAxis,System.Double)`

Вращение вокруг оси на заданный угол

Parameters:
- `axis`: Ось, относительно которой выполняется вращение
- `angle`: Угол в градусах, на который выполняется вращение

Remarks: Вызов данного метода добавляет данное преобразование к уже заданным в этой трансформации

### `Scale(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.Scale(System.Double,System.Double,System.Double)`

Масштабирование по осям глобальной системы координат

Parameters:
- `xscale`: Масштаб по оси X
- `yscale`: Масштаб по оси Y
- `zscale`: Масштаб по оси Z

Remarks: Вызов данного метода добавляет данное преобразование к уже заданным в этой трансформации

### `Transfer(TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.AffineTransformation.Transfer(TFlex.Model.Model3D.Geometry.BaseDirection)`

Перемещение по вектору

Parameters:
- `direction`: Вектор, на длину которого выполняется перемещение

Remarks: Вызов данного метода добавляет данное преобразование к уже заданным в этой трансформации
