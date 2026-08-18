# RGK.Geometry.NURBSCurve

Assembly: `TFlexAPI`
Namespace: `RGK.Geometry`

## Methods

### `CheckBezier`

ID: `M:RGK.Geometry.NURBSCurve.CheckBezier`

### `ClampCurve(RGK.Common.Context*,System.Boolean,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.ClampCurve(RGK.Common.Context*,System.Boolean,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `iFromLeft`: Обработка левой части кривой
- `iFromRight`: Обработка правой части кривой
- `oCurve`: Полученная сжатая кривая

Returns: - Result::Success в случае успешного выполнения

### `Copy(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Geometry.NURBSCurve.Copy(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*)`

Создание новой кривой с параметрами исходной на заданном интервале (копирование на интервале)

Parameters:
- `iContext`: Контекст создания NURBS поверхности
- `iInterval`: Заданный интервал параметров (подмножество исходного интервала)
- `oCurve`: Скопированная кривая
- `ipLCS`: Система координат для копирования кривой

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadKnots некорректно заданная последовательность узлов - Result::BadDegree некорректно задана степень NURBS - Result::BadWeights некорректно заданы веса для контрольных точек - Result::BadInterval некорректно задан интервал параметров

### `Copy(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Copy(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создание новой кривой с параметрами исходной (копирование)

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `oCurve`: Скопированная кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadKnots некорректно заданная последовательность узлов - Result::BadDegree некорректно задана степень NURBS - Result::BadWeights некорректно заданы веса для контрольных точек

### `Copy(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Copy(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создание новой кривой с параметрами исходной (копирование)

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `oCurve`: Скопированная кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadKnots некорректно заданная последовательность узлов - Result::BadDegree некорректно задана степень NURBS - Result::BadWeights некорректно заданы веса для контрольных точек

### `Create(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Create(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создаёт NURBS кривую с весами равными 1.0

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `iPoints`: Массив опорных точек кривой
- `iDegree`: Степень кривой
- `iKnots`: Последовательность узлов
- `isPeriodic`: Является ли кривая периодической
- `oCurve`: Созданная NURBS кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadKnots некорректно заданная последовательность узлов - Result::BadDegree некорректно задана степень NURBS

### `Create(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Create(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `iPoints`: Массив опорных точек кривой
- `iWeights`: Массив весов
- `iDegree`: Степень кривой
- `iKnots`: Последовательность узлов
- `isPeriodic`: Является ли кривая периодической
- `oCurve`: Созданная NURBS кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadKnots некорректно заданная последовательность узлов - Result::BadDegree некорректно задана степень NURBS - Result::BadWeights некорректно заданы веса для контрольных точек

### `Create(RGK.Common.Context*,std.vector<RGK.Math.Vector4D,std.allocator<RGK.Math.Vector4D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Create(RGK.Common.Context*,std.vector<RGK.Math.Vector4D,std.allocator<RGK.Math.Vector4D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `iPoints`: Массив опорных точек кривой с весами
- `iDegree`: Степень кривой
- `iKnots`: Последовательность узлов
- `isPeriodic`: Является ли кривая периодической
- `oCurve`: Созданная NURBS кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadKnots некорректно заданная последовательность узлов - Result::BadDegree некорректно задана степень NURBS - Result::BadWeights некорректно заданы веса для контрольных точек

### `CreateBezier(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.CreateBezier(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Создаёт кривую Безье с весами равными 1.0

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `iPoints`: Массив опорных точек кривой
- `iDegree`: Степень кривой
- `oCurve`: Созданная кривая Безье

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadKnots некорректно заданная последовательность узлов - Result::BadDegree некорректно задана степень NURBS

### `CreateBezier(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.CreateBezier(RGK.Common.Context*,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `iPoints`: Массив опорных точек кривой
- `iWeights`: Массив весов
- `iDegree`: Степень кривой
- `oCurve`: Созданная кривая Безье

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя - Result::BadDegree некорректно задана степень NURBS - Result::BadWeights некорректно заданы веса для контрольных точек

### `DeleteBezierRepresentation`

ID: `M:RGK.Geometry.NURBSCurve.DeleteBezierRepresentation`

### `ElevateDegree(RGK.Common.Context*,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.ElevateDegree(RGK.Common.Context*,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Повышение степени сплайна

Parameters:
- `iContext`: Контекст вычисления
- `iTimes`: Порядок повышения степени
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя

### `Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

В базовом классе метод реализован на основе сплайн-представления

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляется производная
- `iDerivOrder`: Порядок производной (>=0)
- `oDerivative`: Значение вычисленной производной

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*)`

ID: `M:RGK.Geometry.NURBSCurve.Evaluate(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector3D*)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных

Returns: - Result::Success в случае успешного выполнения - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `Evaluate4D(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector4D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Evaluate4D(RGK.Common.Context*,System.Double,System.UInt32,RGK.Math.Vector4D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

В базовом классе метод реализован на основе сплайн-представления

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляется производная
- `iDerivOrder`: Порядок производной (>=0)
- `oDerivative`: Значение вычисленной производной

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `Evaluate4D(RGK.Common.Context*,System.Double,System.UInt32,std.vector<RGK.Math.Vector4D,std.allocator<RGK.Math.Vector4D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Evaluate4D(RGK.Common.Context*,System.Double,System.UInt32,std.vector<RGK.Math.Vector4D,std.allocator<RGK.Math.Vector4D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных

Returns: - Result::Success в случае успешного выполнения - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `EvaluatePoints(RGK.Common.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.EvaluatePoints(RGK.Common.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметры на кривой, в которых вычисляются производные
- `iMaxDerivOrder`: Максимальный порядок рассчитываемых производных
- `oDerivatives`: Значения вычисленных производных

Returns: - Result::Success в случае успешного выполнения - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `FindLength(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,System.Int32)`

ID: `M:RGK.Geometry.NURBSCurve.FindLength(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean,System.Int32)`

Parameters:
- `iContext`: Контекст вычисления
- `iInterval`: Параметрический интервал кривой, на котором считается длина
- `iTolerance`: Запрашиваемая точность вычисления длины
- `oLength`: Найденная длина
- `iEstimate`: Использовать быструю приблизительную оценку
- `iNPoints`: Количество точек для оценки

Returns: - Result::Success в случае успешного выполнения

### `GetControlPoint(System.Int32)`

ID: `M:RGK.Geometry.NURBSCurve.GetControlPoint(System.Int32)`

Parameters:
- `index`: Индекс точки

Returns: Контрольная точка с указанным индексом

### `GetControlPoint4D(System.Int32)`

ID: `M:RGK.Geometry.NURBSCurve.GetControlPoint4D(System.Int32)`

Parameters:
- `index`: Индекс точки

Returns: Контрольная точка с указанным индексом

### `GetControlPoints`

ID: `M:RGK.Geometry.NURBSCurve.GetControlPoints`

Returns: Массив контрольных точек

### `GetControlPoints4D`

ID: `M:RGK.Geometry.NURBSCurve.GetControlPoints4D`

Returns: Массив контрольных точек

### `GetDegree`

ID: `M:RGK.Geometry.NURBSCurve.GetDegree`

Returns: Степень NURBS-кривой

### `GetInterval(RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.GetInterval(RGK.Geometry.Interval*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `oInterval`: Интервал

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported - для данного класса кривой функциональность не реализована

### `GetKnot(System.Int32)`

ID: `M:RGK.Geometry.NURBSCurve.GetKnot(System.Int32)`

Parameters:
- `index`: Индекс точки

Returns: Узловое значение с указанным индексом

### `GetKnots`

ID: `M:RGK.Geometry.NURBSCurve.GetKnots`

Returns: Массив узловых значений

### `GetNumberOfKnots`

ID: `M:RGK.Geometry.NURBSCurve.GetNumberOfKnots`

Returns: Количество узловых значений

### `GetNumberOfPoints`

ID: `M:RGK.Geometry.NURBSCurve.GetNumberOfPoints`

### `GetType`

ID: `M:RGK.Geometry.NURBSCurve.GetType`

Returns: Тип геометрии

### `GetWeight(System.Int32)`

ID: `M:RGK.Geometry.NURBSCurve.GetWeight(System.Int32)`

Returns: Вес точки с указанным индексом

### `GetWeights`

ID: `M:RGK.Geometry.NURBSCurve.GetWeights`

Returns: Массив весов

### `InsertMultipleKnots(RGK.Common.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.InsertMultipleKnots(RGK.Common.Context*,std.vector<System.Double,std.allocator<System.Double>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<System.Int32,std.allocator<System.Int32>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Вставка набора уникальных узлов с заданными кратностями

Parameters:
- `iContext`: Контекст вычисления
- `iInsertingKnots`: Набор узлов для вставки
- `iMultiplicities`: Кратности вставляемых узлов
- `oCurve`: Новая NURBS-кривая со вставленными узлами

Returns: - Result::Success в случае успешного выполнения - Result::InvalidInputParameter некорректно задана последовательность узлов и их кратностей - Result::NullPointer недопустимая передача нулевого указателя

### `IsBezier`

ID: `M:RGK.Geometry.NURBSCurve.IsBezier`

Returns: - true кривая является кривой Безье - false кривая не является кривой Безье

### `IsCoincident(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.IsCoincident(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания линии
- `iGeometry`: Геометрический объект, с которым выполняется сравнение
- `iData`: Выполнять сравнение по данным. То есть объекты считаются одинаковыми в случае совпадения всех параметров объектов
- `oCoincident`: Результат сравнения

Returns: - Result::Success в случае успешного выполнения

### `IsLeftClamped(RGK.Common.Context*)`

ID: `M:RGK.Geometry.NURBSCurve.IsLeftClamped(RGK.Common.Context*)`

Parameters:
- `iContext`: Контекст вычисления

Returns: true, если кривая Clamped слева

### `IsNonRational`

ID: `M:RGK.Geometry.NURBSCurve.IsNonRational`

Returns: - true кривая нерациональная - false кривая рациональная

### `IsPeriodic`

ID: `M:RGK.Geometry.NURBSCurve.IsPeriodic`

Returns: - true кривая периодическая - false кривая непериодическая

### `IsPlanar(RGK.Common.Context*,RGK.Geometry.Curve.IsPlanarData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IsPlanarReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.IsPlanar(RGK.Common.Context*,RGK.Geometry.Curve.IsPlanarData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.IsPlanarReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Проверка, что кривая или её участок является плоской

Parameters:
- `iData`: Параметры проверки
- `oReport`: Результаты проверки

Returns: - Result::Success в случае успешного выполнения

### `IsRightClamped(RGK.Common.Context*)`

ID: `M:RGK.Geometry.NURBSCurve.IsRightClamped(RGK.Common.Context*)`

Parameters:
- `iContext`: Контекст вычисления

Returns: true, если кривая Clamped справа

### `MakeBezier(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.MakeBezier(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `oCurve`: Созданная кривая Безье

Returns: - Result::Success в случае успешного выполнения

### `ModifyControlPoint(RGK.Common.Context*,System.Int32,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.ModifyControlPoint(RGK.Common.Context*,System.Int32,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `index`: Индекс контрольной точки
- `iPoint`: Новое значение контрольной точки
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::NullPointer недопустимая передача нулевого указателя

### `ModifyWeight(RGK.Common.Context*,System.Int32,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.ModifyWeight(RGK.Common.Context*,System.Int32,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `index`: Индекс контрольной точки
- `iWeight`: Новое значение веса
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::NullPointer недопустимая передача нулевого указателя

### `NormalizeKnots(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.NormalizeKnots(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя

### `ReduceDegree(RGK.Common.Context*,System.Double!System.Runtime.CompilerServices.IsConst,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.ReduceDegree(RGK.Common.Context*,System.Double!System.Runtime.CompilerServices.IsConst,System.Int32,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Понижение степени сплайна

Parameters:
- `iContext`: Контекст вычисления
- `iTolerance`: Передаваемая точность
- `iTimes`: Порядок понижения степени
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя

### `RemoveKnots(RGK.Common.Context*,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.RemoveKnots(RGK.Common.Context*,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iTolerance`: Погрешность, оценивается как iTolerance=dw_min/(1+|P|_max)
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::BadParameter некорректно задан iTimes - Result::NullPointer недопустимая передача нулевого указателя

### `Reparametrization(RGK.Common.Context*,System.Double,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Reparametrization(RGK.Common.Context*,System.Double,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iMin`: Новое значение нижней границы параметра
- `iMax`: Новое значение верхней границы параметра
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParametr некорректно задана последовательность узлов - Result::NullPointer недопустимая передача нулевого указателя

### `Reverse(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Reverse(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Изменение порядка обхода узлов

Parameters:
- `iContext`: Контекст вычисления
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя

### `ShiftKnots(RGK.Common.Context*,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.ShiftKnots(RGK.Common.Context*,System.Double,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `oCurve`: Созданная NURBS-кривая

Returns: - Result::Success в случае успешного выполнения - Result::NullPointer недопустимая передача нулевого указателя

### `SplineEvaluate(RGK.Common.Context*,System.Double,System.UInt32,std.vector<System.Int32,std.allocator<System.Int32>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.SplineEvaluate(RGK.Common.Context*,System.Double,System.UInt32,std.vector<System.Int32,std.allocator<System.Int32>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.Vector3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить значение производной (iDerivOrder) кривой по параметрам

Parameters:
- `iContext`: Контекст вычисления
- `iU`: Параметр на кривой, в котором вычисляется производная
- `iDerivOrder`: Порядок производной (>=0)
- `iDerivIndices`: Индексы переменных, по которым дифференцируем
- `oDerivative`: Значение вычисленной производной

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована - Result::BadParameter параметр за границами параметрической области. - Result::NullPointer недопустимая передача нулевого указателя

### `Transform(RGK.Common.Context*,RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.Transform(RGK.Common.Context*,RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания линии
- `iMap`: Аффинное преобразование
- `iTolerance`: Допустимая точность преобразований
- `oCopy`: Возвращается трансформированная геометрия
- `oExact`: Возвращается true-для точного преобразования

Returns: - Result::Success в случае успешного выполнения

### `UnclampCurve(RGK.Common.Context*,System.Boolean,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.UnclampCurve(RGK.Common.Context*,System.Boolean,System.Boolean,std.shared_ptr<RGK.Geometry.NURBSCurve!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания NURBS кривой
- `iFromLeft`: Обработка левой части кривой
- `iFromRight`: Обработка правой части кривой
- `oCurve`: Полученная несжатая кривая

Returns: - Result::Success в случае успешного выполнения

### `UpdateBezierRepresentation(RGK.Common.Context*,System.Boolean,std.shared_ptr<RGK.Geometry.BezierCurveRepresentation>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve.UpdateBezierRepresentation(RGK.Common.Context*,System.Boolean,std.shared_ptr<RGK.Geometry.BezierCurveRepresentation>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления

Returns: - Result::Success в случае успешного выполнения

### `_FindBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*,System.Boolean)`

ID: `M:RGK.Geometry.NURBSCurve._FindBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D!System.Runtime.CompilerServices.IsConst*,System.Boolean)`

Получить ограничивающий параллелепипед для NURBS-кривой на интервале в заданной (или текущей) системе координат

Parameters:
- `iContext`: Указатель на контекст вычисления
- `iInterval`: Интервал параметров, для которого выполняется расчёт ограничивающего параллелепипеда
- `oBox`: Результирующий ограничивающий параллелепипед для кривой
- `ipLCS`: Система координат для поиска ограничивающего параллелепипеда
- `iEstimate`: Выполнить быструю приблизительную оценку

Returns: - Result::NotSupported данный тип интервала не поддерживается - Result::Success в случае успешного выполнения

### `_FindMinimalBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

ID: `M:RGK.Geometry.NURBSCurve._FindMinimalBoundingBox(RGK.Common.Context*,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.LCS3D*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

Получить наименьший (ориентированный) ограничивающий параллелепипед для NURBS-кривой на интервале в заданной (или текущей) системе координат

Parameters:
- `iContext`: Указатель на контекст вычисления
- `iInterval`: Интервал параметров, для которого выполняется расчёт ограничивающего параллелепипеда
- `oBox`: Результирующий ограничивающий параллелепипед для кривой
- `oLCS`: Система координат ограничивающего параллелепипеда
- `iEstimate`: Выполнить быструю приблизительную оценку

Returns: - Result::NotSupported данный тип интервала не поддерживается - Result::Success в случае успешного выполнения

### `_FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve._FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка, для которой ищется ближайшая точка на кривой
- `iInterval`: Интервал поиска
- `iTolerance`: Точность, с которой ищется ближайшая точка
- `oParam`: Найденный параметр ближайшей точки на кривой

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована

### `_FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve._FindNearestPoint(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка, для которой ищется ближайшая точка на кривой
- `iTolerance`: Точность, с которой ищется ближайшая точка
- `oParam`: Найденный параметр ближайшей точки на кривой

Returns: - Result::Success в случае успешного выполнения - Result::NotSupported для данного класса кривой функциональность не реализована

### `_MakeNURBSCurve(RGK.Common.Context*,RGK.Geometry.MakeNURBSCurveData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.MakeNURBSCurveReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.NURBSCurve._MakeNURBSCurve(RGK.Common.Context*,RGK.Geometry.MakeNURBSCurveData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.MakeNURBSCurveReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст вычисления
- `iData`: Данные для интерполяции
- `oReport`: Результат построения

Returns: - Result::Success в случае успешного выполнения

### `_Parameterise(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

ID: `M:RGK.Geometry.NURBSCurve._Parameterise(RGK.Common.Context*,RGK.Math.Vector3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,System.Boolean)`

Parameters:
- `iContext`: Контекст вычисления
- `iPoint`: Точка на кривой
- `ioParam`: Найденный параметр на кривой (на входе может содержать начальное приближение)
- `iUseGuess`: Использовать ли начальное приближение

Returns: - Result::Success в случае успешного выполнения - Result::NotOnCurve точка не лежит на кривой
