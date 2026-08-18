# RGK.Math.AffineMap3D

Assembly: `TFlexAPI`
Namespace: `RGK.Math`

## Constructors

### `AffineMap3D`

ID: `M:RGK.Math.AffineMap3D.#ctor`

### `AffineMap3D(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.#ctor(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Исходная карта преобразования

## Methods

### `AffineMap3D`

ID: `M:RGK.Math.AffineMap3D.#ctor`

### `AffineMap3D(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.#ctor(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMap`: Исходная карта преобразования

### `CheckScaled(System.Double)`

ID: `M:RGK.Math.AffineMap3D.CheckScaled(System.Double)`

### `ClearT`

ID: `M:RGK.Math.AffineMap3D.ClearT`

### `Degenerated(System.Double)`

ID: `M:RGK.Math.AffineMap3D.Degenerated(System.Double)`

Parameters:
- `iLinearTolerance`: Допуск, с которым выполняется проверка вырожденности

Returns: true, если преобразование является вырожденным

### `Determinant`

ID: `M:RGK.Math.AffineMap3D.Determinant`

### `Dispose`

ID: `M:RGK.Math.AffineMap3D.Dispose`

### `GetMap(System.Double*,System.Int32)`

ID: `M:RGK.Math.AffineMap3D.GetMap(System.Double*,System.Int32)`

Parameters:
- `iViewMatrix`: Массив значений матрицы преобразования
- `iSize`: Размер массива значений матрицы преобразования. Количество элементов массива должно быть равно 12(вся матрица преобразований), 9(только повороты и масштабирование) или 3(только перемещение)

Returns: - Result::Success в случае успешного выполнения - Result::BadSize в случае неверно переданного размера массива

### `GetT`

ID: `M:RGK.Math.AffineMap3D.GetT`

Returns: Вектор переноса системы координат

### `HasOnlyUniformScale(System.Double)`

ID: `M:RGK.Math.AffineMap3D.HasOnlyUniformScale(System.Double)`

Parameters:
- `iTolerance`: Точность

Returns: true, если не содержит

### `InvMap`

ID: `M:RGK.Math.AffineMap3D.InvMap`

Returns: Новый объект карты преобразования

### `InvMapSelf`

ID: `M:RGK.Math.AffineMap3D.InvMapSelf`

Returns: Ссылка на текущий объект после выполнения преобразования

### `InvNormZ(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.InvNormZ(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

### `IsEqual(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.IsEqual(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

### `IsIdentity(System.Double)`

ID: `M:RGK.Math.AffineMap3D.IsIdentity(System.Double)`

Parameters:
- `iLinearTolerance`: Допуск, с которым выполняется сравнение с единичным преобразованием

Returns: true, если преобразование является единичным (эквивалентным)

### `IsOrthogonal(System.Double)`

ID: `M:RGK.Math.AffineMap3D.IsOrthogonal(System.Double)`

Parameters:
- `iTolerance`: Точность

Returns: true, если матрица ортогональна

### `Map(RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.Map(RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iLCS`: Исходная система координат

Returns: Результирующая система координат

### `Map(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Map(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iVector`: Исходный вектор
- `iWeight`: Вес

Returns: Результирующий вектор

### `Map(System.Double!System.Runtime.CompilerServices.IsConst*,System.Double*,RGK.Math.RepresentationType)`

ID: `M:RGK.Math.AffineMap3D.Map(System.Double!System.Runtime.CompilerServices.IsConst*,System.Double*,RGK.Math.RepresentationType)`

Parameters:
- `iVector`: Исходный вектор
- `oResult`: Результирующий вектор
- `oRep`: Тип представления

### `Map(System.Double,System.Double,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

ID: `M:RGK.Math.AffineMap3D.Map(System.Double,System.Double,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

Parameters:
- `iX`: Координата X исходной точки
- `iY`: Координата Y исходной точки
- `iZ`: Координата Z исходной точки
- `iWeight`: Вес точки
- `oX`: Координата X результирующей точки
- `oY`: Координата Y результирующей точки
- `oZ`: Координата Z результирующей точки
- `oHomgn`: Признак гомогенного преобразования

### `Multiply(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Multiply(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iToMul`: Карта, на которую производится умножение
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

Returns: Новая карта, соответствующая суммарному преобразованию

### `MultiplySelf(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.MultiplySelf(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iToMul`: Карта, на которую производится умножение
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

Returns: Ссылка на текущий объект

### `NormZ(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.NormZ(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

### `Reflect(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Reflect(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Parameters:
- `iPoint`: Точка отражения
- `iVector`: Отражаемый вектор
- `iLinearTolerance`: Допуск, с которым выполняется нормирование вектора

### `ResetMap`

ID: `M:RGK.Math.AffineMap3D.ResetMap`

### `ResetOperations`

ID: `M:RGK.Math.AffineMap3D.ResetOperations`

### `Rotate(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Rotate(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double,System.Double)`

Parameters:
- `iCenter`: Центр поворота
- `iAxis`: Угол поворота в радианах

### `Rotate(System.Double!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Rotate(System.Double!System.Runtime.CompilerServices.IsConst*,System.Double,System.Double)`

Parameters:
- `iRotationMatrix`: Матрица поворотов
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

### `Rotate(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Rotate(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

Parameters:
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

### `RotateX(System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.RotateX(System.Double,System.Double,System.Double)`

Parameters:
- `iAngle`: Угол поворота в радианах
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

### `RotateY(System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.RotateY(System.Double,System.Double,System.Double)`

Parameters:
- `iAngle`: Угол поворота в радианах
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

### `RotateZ(System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.RotateZ(System.Double,System.Double,System.Double)`

Parameters:
- `iAngle`: Угол поворота в радианах
- `iLinearTolerance`: Tolerance with which the resulting scaling is considered to be 1
- `iAngularTolerance`: Tolerance with which the resulting rotation angle is considered to be 0

### `Rotated`

ID: `M:RGK.Math.AffineMap3D.Rotated`

Returns: ненулевое значение, если карта содержит преобразование поворота

### `Scale(System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Scale(System.Double,System.Double)`

Parameters:
- `iFactor`: Значение масштаба
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным

### `Scale(System.Double,System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Scale(System.Double,System.Double,System.Double,System.Double)`

Parameters:
- `iFactorX`: Значение масштаба вдоль оси X
- `iFactorY`: Значение масштаба вдоль оси Y
- `iFactorZ`: Значение масштаба вдоль оси Z
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным

### `ScaleX(System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.ScaleX(System.Double,System.Double)`

Parameters:
- `iFactor`: Значение масштаба вдоль оси X
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным

### `ScaleY(System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.ScaleY(System.Double,System.Double)`

Parameters:
- `iFactor`: Значение масштаба вдоль оси Y
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным

### `ScaleZ(System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.ScaleZ(System.Double,System.Double)`

Parameters:
- `iFactor`: Значение масштаба вдоль оси Z
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным

### `Scaled`

ID: `M:RGK.Math.AffineMap3D.Scaled`

Returns: ненулевое значение, если карта содержит преобразование масштабирования

### `SetLCSOrts(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.SetLCSOrts(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double)`

Parameters:
- `iLinearTolerance`: Допуск, с которым результирующее преобразование масштабирования считается единичным
- `iAngularTolerance`: Допуск, с которым результирующее преобразование поворота считается нулевым

### `SetMap(System.Double!System.Runtime.CompilerServices.IsConst*,System.Double,System.Int32)`

ID: `M:RGK.Math.AffineMap3D.SetMap(System.Double!System.Runtime.CompilerServices.IsConst*,System.Double,System.Int32)`

Parameters:
- `iViewMatrix`: Массив значений матрицы преобразования. Количество элементов массива должно быть равно 12
- `iSize`: Размер массива значений матрицы преобразования. Количество элементов массива должно быть равно 12(вся матрица преобразований), 9(только повороты и масштабирование) или 3(только перемещение)

Returns: - Result::Success в случае успешного выполнения - Result::BadSize в случае неверно переданного размера массива

### `Transfer(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.Transfer(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iTranslation`: Вектор переноса

### `Transfer(System.Double,System.Double,System.Double)`

ID: `M:RGK.Math.AffineMap3D.Transfer(System.Double,System.Double,System.Double)`

Parameters:
- `iAlongX`: Перенос вдоль оси X
- `iAlongY`: Перенос вдоль оси Y
- `iAlongZ`: Перенос вдоль оси Z

### `Transferred`

ID: `M:RGK.Math.AffineMap3D.Transferred`

Returns: ненулевое значение, если карта содержит преобразование переноса

### `VMap(RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.VMap(RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iLCS`: Исходная система координат

Returns: Результирующая система координат

### `VMap(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.VMap(RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVector`: Исходный вектор

Returns: Результирующий вектор

### `VMap(System.Double,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.VMap(System.Double,System.Double,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iX`: Координата X исходной точки
- `iY`: Координата Y исходной точки
- `iZ`: Координата Z исходной точки
- `oX`: Координата X результирующей точки
- `oY`: Координата Y результирующей точки
- `oZ`: Координата Z результирующей точки

### `op_Assign(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Math.AffineMap3D.op_Assign(RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iToCopy`: Исходная карта преобразования

Returns: Ссылка на текущий объект
