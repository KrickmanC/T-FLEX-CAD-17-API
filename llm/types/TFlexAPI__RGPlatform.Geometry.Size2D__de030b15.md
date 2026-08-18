# RGPlatform.Geometry.Size2D

Assembly: `TFlexAPI`
Namespace: `RGPlatform.Geometry`

## Summary

Двумерный размер

## Constructors

### `Size2D`

ID: `M:RGPlatform.Geometry.Size2D.#ctor`

Конструктор по умолчанию

### `Size2D(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.#ctor(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по точке

Parameters:
- `iPoint`: Точка

### `Size2D(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.#ctor(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор копирования

Parameters:
- `iOther`: Другой объект размера

### `Size2D(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Size2D.#ctor(System.Double,System.Double)`

Конструктор по координатам

Parameters:
- `iDx`: X координата
- `iDy`: Y координата

## Methods

### `Size2D`

ID: `M:RGPlatform.Geometry.Size2D.#ctor`

Конструктор по умолчанию

### `Size2D(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.#ctor(RGPlatform.Geometry.Point2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по точке

Parameters:
- `iPoint`: Точка

### `Size2D(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.#ctor(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор копирования

Parameters:
- `iOther`: Другой объект размера

### `Size2D(System.Double,System.Double)`

ID: `M:RGPlatform.Geometry.Size2D.#ctor(System.Double,System.Double)`

Конструктор по координатам

Parameters:
- `iDx`: X координата
- `iDy`: Y координата

### `Angle`

ID: `M:RGPlatform.Geometry.Size2D.Angle`

Получить угол наклона отрезка к оси X

Returns: Угол наклона к оси X

### `Cx`

ID: `M:RGPlatform.Geometry.Size2D.Cx`

Получить X координату

Returns: X координата

### `Cy`

ID: `M:RGPlatform.Geometry.Size2D.Cy`

Получить Y координату

Returns: Y координата

### `GetLength`

ID: `M:RGPlatform.Geometry.Size2D.GetLength`

Вычислить длину (диагональ)

Returns: Вычисленная длина

### `op_Addition(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.op_Addition(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "+"

Parameters:
- `iSize`: Объект, с которым складывается данный

Returns: Сумма размеров

### `op_AdditionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.op_AdditionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "+="

Parameters:
- `iSize`: Объект, с которым складывается данный

Returns: Ссылка на данный размер

### `op_Division(System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:RGPlatform.Geometry.Size2D.op_Division(System.Double!System.Runtime.CompilerServices.IsConst)`

Оператор "/"

Parameters:
- `iVal`: Число, на которое делится размер

Returns: Результат деления размера на число

### `op_DivisionAssignment(System.Double)`

ID: `M:RGPlatform.Geometry.Size2D.op_DivisionAssignment(System.Double)`

Оператор "/="

Parameters:
- `iVal`: Число, на которое делится размер

Returns: Ссылка на данный размер

### `op_Equality(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.op_Equality(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "=="

Parameters:
- `iOther`: Размер, с которым сравнивается данный

Returns: true - равны, false - не равны

### `op_Inequality(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.op_Inequality(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "!="

Parameters:
- `iOther`: Размер, с которым сравнивается данный

Returns: true - не равны, false - равны

### `op_MultiplicationAssignment(System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:RGPlatform.Geometry.Size2D.op_MultiplicationAssignment(System.Double!System.Runtime.CompilerServices.IsConst)`

Оператор "*="

Parameters:
- `iVal`: Число, на которое умножается размер

Returns: Ссылка на данный размер

### `op_Multiply(System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:RGPlatform.Geometry.Size2D.op_Multiply(System.Double!System.Runtime.CompilerServices.IsConst)`

Оператор "*"

Parameters:
- `iVal`: Число, на которое умножается размер

Returns: Результат умножения размера на число

### `op_Subtraction(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.op_Subtraction(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "-"

Parameters:
- `iSize`: Объект, который вычитается из данного

Returns: Разность размеров

### `op_SubtractionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGPlatform.Geometry.Size2D.op_SubtractionAssignment(RGPlatform.Geometry.Size2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Оператор "-="

Parameters:
- `iSize`: Объект, который вычитается из данного

Returns: Ссылка на данный размер

### `op_UnaryNegation`

ID: `M:RGPlatform.Geometry.Size2D.op_UnaryNegation`

Оператор вычисления противоположного значения

Returns: Противоположный размер
