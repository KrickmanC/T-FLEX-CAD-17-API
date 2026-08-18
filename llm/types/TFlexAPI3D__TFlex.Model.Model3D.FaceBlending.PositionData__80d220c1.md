# TFlex.Model.Model3D.FaceBlending.PositionData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.FaceBlending`

## Summary

Класс используемый для задания параметров переменного сглаживания

## Constructors

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius`: Радиус

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius1`: 1-й радиус
- `radius2`: 2-й радиус

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius1`: 1-й радиус
- `radius2`: 2-й радиус
- `rho`: Кривизна

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius1`: 1-й радиус
- `radius2`: 2-й радиус
- `rho`: Кривизна
- `depth`: Глубина
- `offset`: Смещение

## Methods

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius`: Радиус

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius1`: 1-й радиус
- `radius2`: 2-й радиус

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius1`: 1-й радиус
- `radius2`: 2-й радиус
- `rho`: Кривизна

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Положение на последовательности рёбер
- `radius1`: 1-й радиус
- `radius2`: 2-й радиус
- `rho`: Кривизна
- `depth`: Глубина
- `offset`: Смещение

## Propertys

### `Depth`

ID: `P:TFlex.Model.Model3D.FaceBlending.PositionData.Depth`

Глубина

Remarks: Глубину можно получить только если тип поверхности G2

### `Offset`

ID: `P:TFlex.Model.Model3D.FaceBlending.PositionData.Offset`

Смещение

Remarks: Смещение можно получить только если тип поверхности G2

### `Position`

ID: `P:TFlex.Model.Model3D.FaceBlending.PositionData.Position`

Значение позиции

### `Radius1`

ID: `P:TFlex.Model.Model3D.FaceBlending.PositionData.Radius1`

Первый радиус

### `Radius2`

ID: `P:TFlex.Model.Model3D.FaceBlending.PositionData.Radius2`

Второй радиус

### `Rho`

ID: `P:TFlex.Model.Model3D.FaceBlending.PositionData.Rho`

Кривизна

Remarks: Кривизна может быть установлена только если тип поверхности Conic
