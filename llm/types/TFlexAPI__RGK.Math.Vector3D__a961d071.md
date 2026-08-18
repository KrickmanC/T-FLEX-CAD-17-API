# RGK.Math.Vector3D

Assembly: `TFlexAPI`
Namespace: `RGK.Math`

## Constructors

### `Vector3D`

ID: `M:RGK.Math.Vector3D.#ctor`

### `Vector3D(RGK.Math.Vector2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.#ctor(RGK.Math.Vector2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iV`: Вектор с координатами X и Y

### `Vector3D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `Vector3D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iP1`: Второй вектор разницы

### `Vector3D(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Double!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iVals`: Массив значений координат вектора в порядке X, Y, Z. Массив должен содержать 3 элемента.

### `Vector3D(System.Double)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Double)`

Parameters:
- `iVal`: Значение компонент

### `Vector3D(System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Double,System.Double,System.Double)`

Parameters:
- `x`: Значение координаты X
- `y`: Значение координаты Y
- `z`: Значение координаты Z

### `Vector3D(System.Single!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Single!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iVals`: Массив значений координат вектора в порядке X, Y, Z. Массив должен содержать 3 элемента.

## Methods

### `Vector3D`

ID: `M:RGK.Math.Vector3D.#ctor`

### `Vector3D(RGK.Math.Vector2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.#ctor(RGK.Math.Vector2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iV`: Вектор с координатами X и Y

### `Vector3D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `Vector3D(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.#ctor(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iP1`: Второй вектор разницы

### `Vector3D(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Double!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iVals`: Массив значений координат вектора в порядке X, Y, Z. Массив должен содержать 3 элемента.

### `Vector3D(System.Double)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Double)`

Parameters:
- `iVal`: Значение компонент

### `Vector3D(System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Double,System.Double,System.Double)`

Parameters:
- `x`: Значение координаты X
- `y`: Значение координаты Y
- `z`: Значение координаты Z

### `Vector3D(System.Single!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector3D.#ctor(System.Single!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iVals`: Массив значений координат вектора в порядке X, Y, Z. Массив должен содержать 3 элемента.

### `ComponentMultiply(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.ComponentMultiply(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToMul`: Вектор, на который умножаем данный

Returns: Новый объект, компоненты которого являются компонент текущего объекта и вектора iToMul

### `CopyXYZ(System.Double*)`

ID: `M:RGK.Math.Vector3D.CopyXYZ(System.Double*)`

Parameters:
- `oResult`: Адрес массива координат. Массив должен содержать 3 элемента

### `CopyXYZ(System.Single*)`

ID: `M:RGK.Math.Vector3D.CopyXYZ(System.Single*)`

Parameters:
- `oResult`: Адрес массива координат. Массив должен содержать 3 элемента

### `CutCoord(System.Int32)`

ID: `M:RGK.Math.Vector3D.CutCoord(System.Int32)`

Returns: Результирующий вектор

### `CutCoordSelf(System.Int32)`

ID: `M:RGK.Math.Vector3D.CutCoordSelf(System.Int32)`

### `DistanceTo(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.DistanceTo(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iPointTo`: Точка до которой ищется расстояние

Returns: Расстояние

### `DistanceTo2(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.DistanceTo2(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iPointTo`: Точка до которой ищется квадрат расстояние

Returns: Расстояние

### `Flush`

ID: `M:RGK.Math.Vector3D.Flush`

### `GetAngle(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.GetAngle(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iOther`: Вектор, до которого нужно посчитать угол

Returns: Значение угла между векторами в радианах

### `GetMaxCoord`

ID: `M:RGK.Math.Vector3D.GetMaxCoord`

Returns: Координата, модуль которой является максимальным

### `GetMaxCoordinate(System.Boolean)`

ID: `M:RGK.Math.Vector3D.GetMaxCoordinate(System.Boolean)`

Parameters:
- `iWithSign`: Если true ищется знаковый максимум, иначе максимум по абсолютному значению

### `GetMinCoordinate(System.Boolean)`

ID: `M:RGK.Math.Vector3D.GetMinCoordinate(System.Boolean)`

Parameters:
- `iWithSign`: Если true ищется знаковый минимум, иначе минимум по абсолютному значению

### `GetNorm(System.Double)`

ID: `M:RGK.Math.Vector3D.GetNorm(System.Double)`

Returns: Новый объект, являющийся результатом нормирования

### `GetNormByLength(System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.GetNormByLength(System.Double,System.Double)`

Parameters:
- `iDistance`: Длина нормирования вектора

Returns: Новый объект, являющийся результатом нормирования

### `GetX`

ID: `M:RGK.Math.Vector3D.GetX`

Returns: Значение координаты X

### `GetXRef`

ID: `M:RGK.Math.Vector3D.GetXRef`

Returns: Значение координаты X

### `GetXYZ(System.Double*,System.Int32)`

ID: `M:RGK.Math.Vector3D.GetXYZ(System.Double*,System.Int32)`

### `GetY`

ID: `M:RGK.Math.Vector3D.GetY`

Returns: Значение координаты Y

### `GetYRef`

ID: `M:RGK.Math.Vector3D.GetYRef`

Returns: Значение координаты Y

### `GetZ`

ID: `M:RGK.Math.Vector3D.GetZ`

Returns: Значение координаты Z

### `GetZRef`

ID: `M:RGK.Math.Vector3D.GetZRef`

Returns: Значение координаты Z

### `IsColinear(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.IsColinear(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iAnother`: Вектор, с которым сравнивается данный
- `iLinearTolerance`: Линейная точность сравнения
- `iAngularTolerance`: Угловая точность сравнения

Returns: true если векторы параллельны, false если не параллельны

### `IsEqual(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.IsEqual(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iOther`: Вектор, с которым сравнивается данный

Returns: true если векторы равны, false если не равны

### `IsEqual(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.Vector3D.IsEqual(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iOther`: Вектор, с которым сравнивается данный
- `iLinearTolerance`: Линейная точность, с которой производится сравнение

Returns: true если векторы равны, false если не равны

### `IsEqual(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.IsEqual(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iOther`: Вектор, с которым сравнивается данный
- `iLinearTolerance`: Линейная точность, с которой производится сравнение
- `iAngularTolerance`: Угловая точность, с которой производится сравнение

Returns: true если векторы равны, false если не равны

### `IsNormal(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.IsNormal(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iAnother`: Вектор, с которым сравнивается данный
- `iLinearTolerance`: Линейная точность сравнения
- `iAngularTolerance`: Угловая точность сравнения

Returns: true если векторы ортогональны, false если не ортогональны

### `IsValid`

ID: `M:RGK.Math.Vector3D.IsValid`

Returns: true - вектор удовлетворяет вышеперечисленным условиям

### `IsValidNonZero`

ID: `M:RGK.Math.Vector3D.IsValidNonZero`

Returns: true - вектор удовлетворяет вышеперечисленным условиям

### `IsValidNonZero(System.Double)`

ID: `M:RGK.Math.Vector3D.IsValidNonZero(System.Double)`

Returns: true - вектор удовлетворяет вышеперечисленным условиям

### `Magnitude`

ID: `M:RGK.Math.Vector3D.Magnitude`

Returns: Значение длины вектора

### `Magnitude2`

ID: `M:RGK.Math.Vector3D.Magnitude2`

Returns: Значение длины вектора в квадрате

### `MakeOrtho(System.Double)`

ID: `M:RGK.Math.Vector3D.MakeOrtho(System.Double)`

Returns: Новый ортогональный вектор

### `MaxNorm`

ID: `M:RGK.Math.Vector3D.MaxNorm`

Returns: норма вектора

### `Permult(RGK.Math.Coordinates,RGK.Math.Coordinates,RGK.Math.Coordinates)`

ID: `M:RGK.Math.Vector3D.Permult(RGK.Math.Coordinates,RGK.Math.Coordinates,RGK.Math.Coordinates)`

### `SetNorm(System.Double)`

ID: `M:RGK.Math.Vector3D.SetNorm(System.Double)`

### `SetNormByLength(System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.SetNormByLength(System.Double,System.Double)`

### `SetXYZ(RGK.Math.Vector2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.SetXYZ(RGK.Math.Vector2D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVector`: Двумерный вектор

### `SetXYZ(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector3D.SetXYZ(System.Double!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iValues`: Значение компонент

### `SetXYZ(System.Double)`

ID: `M:RGK.Math.Vector3D.SetXYZ(System.Double)`

Parameters:
- `iComponentsValue`: Значение, в которое установятся, все компоненты вектора

### `SetXYZ(System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.Vector3D.SetXYZ(System.Double,System.Double,System.Double)`

Parameters:
- `x`: Координата X
- `y`: Координата Y
- `z`: Координата Z

### `SetXYZ(System.Single!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector3D.SetXYZ(System.Single!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iValues`: Значение компонент

### `VMap(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.VMap(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Карта преобразования

Returns: Новый объект

### `VMapSelf(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.VMapSelf(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Карта преобразования

Returns: Ссылка на текущий объект

### `Vector`

ID: `M:RGK.Math.Vector3D.Vector`

Returns: Массив из 3 элементов, содержащий координаты X,Y,Z

### `VectorMultiply(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.VectorMultiply(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToMul`: Вектор, на который умножается данный

Returns: Новый объект, являющийся векторным произведением текущего объекта и вектора iToMul

### `begin`

ID: `M:RGK.Math.Vector3D.begin`

### `end`

ID: `M:RGK.Math.Vector3D.end`

### `op_Addition(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_Addition(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToAdd`: Вектор, с которым складывается данный

Returns: Новый объект

### `op_AdditionAssignment(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_AdditionAssignment(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToAdd`: Вектор, с которым складывается данный

Returns: Ссылка на текущий объект

### `op_Assign(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_Assign(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iOther`: Исходный вектор

### `op_Assign(System.Double!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Math.Vector3D.op_Assign(System.Double!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `iToCopy`: Массив значений координат вектора в порядке X, Y, Z. Массив должен содержать 3 элемента.

### `op_Division(System.Double)`

ID: `M:RGK.Math.Vector3D.op_Division(System.Double)`

Parameters:
- `iLambda`: Значение делителя

Returns: Новый объект

### `op_DivisionAssignment(System.Double)`

ID: `M:RGK.Math.Vector3D.op_DivisionAssignment(System.Double)`

Parameters:
- `iLambda`: Значение делителя

Returns: Ссылка на объект

### `op_MultiplicationAssignment(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_MultiplicationAssignment(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Карта преобразования

Returns: Ссылка на текущий объект

### `op_MultiplicationAssignment(RGK.Math.ProjectiveMap3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_MultiplicationAssignment(RGK.Math.ProjectiveMap3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Карта преобразования

### `op_MultiplicationAssignment(System.Double)`

ID: `M:RGK.Math.Vector3D.op_MultiplicationAssignment(System.Double)`

Parameters:
- `iLambda`: Значение множителя

Returns: Ссылка на текущий объект

### `op_Multiply(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_Multiply(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Карта преобразования

Returns: Новый объект

### `op_Multiply(RGK.Math.ProjectiveMap3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_Multiply(RGK.Math.ProjectiveMap3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Карта преобразования

Returns: Новый объект

### `op_Multiply(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_Multiply(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToMul`: Второй множитель

Returns: Значение скалярного произведение векторов

### `op_Multiply(System.Double)`

ID: `M:RGK.Math.Vector3D.op_Multiply(System.Double)`

Parameters:
- `iLambda`: Значение множителя

Returns: Новый объект

### `op_Subscript(System.Int32)`

ID: `M:RGK.Math.Vector3D.op_Subscript(System.Int32)`

Parameters:
- `idx`: Индекс координаты 0 = X, 1 = Y, 2 = Z

Returns: Значение координаты

### `op_Subtraction(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_Subtraction(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToDecr`: Вектор, который вычитается из данного

Returns: Новый объект

### `op_SubtractionAssignment(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.Vector3D.op_SubtractionAssignment(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToDecr`: Вектор, который вычитается из данного

Returns: Ссылка на текущий объект

### `op_UnaryNegation`

ID: `M:RGK.Math.Vector3D.op_UnaryNegation`

Returns: Объект, являющийся противоположным вектором

## Members

### `size_type`

ID: `D:RGK.Math.Vector3D.size_type`

### `value_type`

ID: `D:RGK.Math.Vector3D.value_type`
