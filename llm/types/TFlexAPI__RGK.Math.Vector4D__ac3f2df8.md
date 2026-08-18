# RGK.Math.Vector4D

Assembly: `TFlexAPI`
Namespace: `RGK.Math`

## Constructors

### `Vector4D`

ID: `M:RGK.Math.Vector4D.#ctor`

### `Vector4D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.Vector4D.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iPoint`: Точка
- `iWeight`: Вес точки

### `Vector4D(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector4D.#ctor(System.Double!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iVals`: Массив значений координат вектора в порядке X, Y, Z, W. Массив должен содержать 4 элемента.

### `Vector4D(System.Double,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.Vector4D.#ctor(System.Double,System.Double,System.Double,System.Double)`

Parameters:
- `x`: Значение координаты X
- `y`: Значение координаты Y
- `z`: Значение координаты Z
- `w`: Значение координаты W

## Methods

### `Vector4D`

ID: `M:RGK.Math.Vector4D.#ctor`

### `Vector4D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.Vector4D.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iPoint`: Точка
- `iWeight`: Вес точки

### `Vector4D(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector4D.#ctor(System.Double!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iVals`: Массив значений координат вектора в порядке X, Y, Z, W. Массив должен содержать 4 элемента.

### `Vector4D(System.Double,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.Vector4D.#ctor(System.Double,System.Double,System.Double,System.Double)`

Parameters:
- `x`: Значение координаты X
- `y`: Значение координаты Y
- `z`: Значение координаты Z
- `w`: Значение координаты W

### `CopyXYZW(System.Double*)`

ID: `M:RGK.Math.Vector4D.CopyXYZW(System.Double*)`

Parameters:
- `oResult`: Адрес массива координат. Массив должен содержать 4 элемента

### `Flush`

ID: `M:RGK.Math.Vector4D.Flush`

### `GetNormByLength(System.Double)`

ID: `M:RGK.Math.Vector4D.GetNormByLength(System.Double)`

Parameters:
- `iTolerance`: Точность

### `GetW`

ID: `M:RGK.Math.Vector4D.GetW`

Returns: Значение координаты W

### `GetX`

ID: `M:RGK.Math.Vector4D.GetX`

Returns: Значение координаты X

### `GetY`

ID: `M:RGK.Math.Vector4D.GetY`

Returns: Значение координаты Y

### `GetZ`

ID: `M:RGK.Math.Vector4D.GetZ`

Returns: Значение координаты Z

### `IsEqual(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector4D.IsEqual(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iOther`: Вектор, с которым сравнивается данный

Returns: true если векторы равны, false если не равны

### `Magnitude`

ID: `M:RGK.Math.Vector4D.Magnitude`

Returns: Значение длины вектора

### `Magnitude2`

ID: `M:RGK.Math.Vector4D.Magnitude2`

Returns: Значение длины вектора в квадрате

### `SetFromVector3D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.Vector4D.SetFromVector3D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iPoint`: Точка
- `iWeight`: Вес точки

### `SetNormByLength(System.Double,System.Double)`

ID: `M:RGK.Math.Vector4D.SetNormByLength(System.Double,System.Double)`

Parameters:
- `iDistance`: Длина
- `iTolerance`: Точность

### `SetXYZW(System.Double,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.Vector4D.SetXYZW(System.Double,System.Double,System.Double,System.Double)`

Parameters:
- `x`: Координата X
- `y`: Координата Y
- `z`: Координата Z
- `w`: Вес

### `ToVector3D`

ID: `M:RGK.Math.Vector4D.ToVector3D`

### `ToVector3D(System.Double)`

ID: `M:RGK.Math.Vector4D.ToVector3D(System.Double)`

### `Vector`

ID: `M:RGK.Math.Vector4D.Vector`

Returns: Массив из 4 элементов, содержащий координаты X,Y,Z,W

### `op_Addition(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector4D.op_Addition(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToAdd`: Вектор, с которым складывается данный

Returns: Новый объект

### `op_AdditionAssignment(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector4D.op_AdditionAssignment(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToAdd`: Вектор, с которым складывается данный

Returns: Ссылка на текущий объект

### `op_Assign(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector4D.op_Assign(System.Double!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iVals`: Массив значений координат вектора в порядке X, Y, Z, W. Массив должен содержать 4 элемента.

### `op_Division(System.Double)`

ID: `M:RGK.Math.Vector4D.op_Division(System.Double)`

Parameters:
- `iLambda`: Значение делителя

Returns: Новый объект

### `op_DivisionAssignment(System.Double)`

ID: `M:RGK.Math.Vector4D.op_DivisionAssignment(System.Double)`

Parameters:
- `iLambda`: Значение делителя

Returns: Ссылка на объект

### `op_MultiplicationAssignment(System.Double)`

ID: `M:RGK.Math.Vector4D.op_MultiplicationAssignment(System.Double)`

Parameters:
- `iLambda`: Значение множителя

Returns: Ссылка на текущий объект

### `op_Multiply(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector4D.op_Multiply(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToMul`: Второй множитель

Returns: Значение скалярного произведение векторов

### `op_Multiply(System.Double)`

ID: `M:RGK.Math.Vector4D.op_Multiply(System.Double)`

Parameters:
- `iLambda`: Значение множителя

Returns: Новый объект

### `op_Subscript(System.Int32)`

ID: `M:RGK.Math.Vector4D.op_Subscript(System.Int32)`

Parameters:
- `idx`: Индекс координаты 0 = X, 1 = Y, 2 = Z, 3 = W

Returns: Значение координаты

### `op_Subtraction(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector4D.op_Subtraction(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToDecr`: Вектор, который вычитается из данного

Returns: Новый объект

### `op_SubtractionAssignment(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector4D.op_SubtractionAssignment(RGK.Math.Vector4D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToDecr`: Вектор, который вычитается из данного

Returns: Ссылка на текущий объект

### `op_UnaryNegation`

ID: `M:RGK.Math.Vector4D.op_UnaryNegation`

Returns: Объект, являющийся противоположным вектором
