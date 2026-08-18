# TFlex.Model.Model3D.Geometry.BaseDirection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для вектора

## Constructors

### `BaseDirection(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.#ctor(System.Double,System.Double,System.Double)`

Конструктор для геометрического вектора

### `BaseDirection(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельного вектора

## Methods

### `BaseDirection(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.#ctor(System.Double,System.Double,System.Double)`

Конструктор для геометрического вектора

### `BaseDirection(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельного вектора

### `Colinear(TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.Colinear(TFlex.Model.Model3D.Geometry.BaseDirection)`

Проверить данный вектор на коллинеарность с другим

Parameters:
- `other`: Вектор

### `CrossProduct(TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.CrossProduct(TFlex.Model.Model3D.Geometry.BaseDirection)`

Векторное произведение векторов

Parameters:
- `direction`: Вектор-сомножитель

### `MakeOrtho`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.MakeOrtho`

Сделать вектор, перпендикулярный данному

### `NormalizedVector`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.NormalizedVector`

Нормализованный вектор

### `Update`

ID: `M:TFlex.Model.Model3D.Geometry.BaseDirection.Update`

Обновить геометрию для каждого конкретного порождённого типа

## Propertys

### `Magnitude`

ID: `P:TFlex.Model.Model3D.Geometry.BaseDirection.Magnitude`

Длина вектора

### `X`

ID: `P:TFlex.Model.Model3D.Geometry.BaseDirection.X`

Получить X - координату вектора

### `Y`

ID: `P:TFlex.Model.Model3D.Geometry.BaseDirection.Y`

Получить Y - координату вектора

### `Z`

ID: `P:TFlex.Model.Model3D.Geometry.BaseDirection.Z`

Получить Z - координату вектора

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.Geometry.BaseDirection.default(System.Int32)`

Получить коодинату по номеру
