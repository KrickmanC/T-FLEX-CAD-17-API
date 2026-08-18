# TFlex.Model.Model3D.Spiral

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Спираль

## Constructors

### `Spiral(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Spiral.#ctor(TFlex.Model.Document)`

Конструктор для создания Пружины

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `Spiral(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Spiral.#ctor(TFlex.Model.Document)`

Конструктор для создания Пружины

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `SetEndSmooth(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Spiral.SetEndSmooth(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установить параметры сглаживания конечных витков

Parameters:
- `smooth`: Число сглаживаемых витков
- `degree`: Степень сглаживания

Remarks: Все значения должны быть нулевыми, или ненулевыми

### `SetStartSmooth(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Spiral.SetStartSmooth(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установить параметры сглаживания начальных витков

Parameters:
- `smooth`: Число сглаживаемых витков
- `degree`: Число сглаживаемых витков

Remarks: Все значения должны быть нулевыми, или ненулевыми

## Propertys

### `Angle`

ID: `P:TFlex.Model.Model3D.Spiral.Angle`

Угол

### `Coils`

ID: `P:TFlex.Model.Model3D.Spiral.Coils`

Число витков

### `Contour`

ID: `P:TFlex.Model.Model3D.Spiral.Contour`

Профиль, задающий сечение спирали

### `ContourFirstPoint`

ID: `P:TFlex.Model.Model3D.Spiral.ContourFirstPoint`

Первая точка на профиле

### `ContourSecondPoint`

ID: `P:TFlex.Model.Model3D.Spiral.ContourSecondPoint`

Вторая точка на профиле

### `CounterClockwise`

ID: `P:TFlex.Model.Model3D.Spiral.CounterClockwise`

Построение пружины против часовой стрелки

### `EndRadius`

ID: `P:TFlex.Model.Model3D.Spiral.EndRadius`

Конечный радиус витка пружины

### `FirstPoint`

ID: `P:TFlex.Model.Model3D.Spiral.FirstPoint`

Первая точка

### `GroupType`

ID: `P:TFlex.Model.Model3D.Spiral.GroupType`

Получить тип объекта

### `LengthMethod`

ID: `P:TFlex.Model.Model3D.Spiral.LengthMethod`

Тип

### `ProfileOrientation`

ID: `P:TFlex.Model.Model3D.Spiral.ProfileOrientation`

Тип ориентации профиля

### `ProfileReverse`

ID: `P:TFlex.Model.Model3D.Spiral.ProfileReverse`

Параметр реверса профиля

### `RadiusFromStartPoint`

ID: `P:TFlex.Model.Model3D.Spiral.RadiusFromStartPoint`

Параметр "Получить радиус по узлу"

### `SecondPoint`

ID: `P:TFlex.Model.Model3D.Spiral.SecondPoint`

Вторая точка

### `StartPoint`

ID: `P:TFlex.Model.Model3D.Spiral.StartPoint`

Установить стартовую точку

Remarks: Параметр point может быть равен 0

### `StartRadius`

ID: `P:TFlex.Model.Model3D.Spiral.StartRadius`

Начальный радиус витка пружины

### `Step`

ID: `P:TFlex.Model.Model3D.Spiral.Step`

Шаг витка пружины
