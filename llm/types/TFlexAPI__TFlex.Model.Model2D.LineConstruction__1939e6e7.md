# TFlex.Model.Model2D.LineConstruction

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Линия построения - прямая

## Constructors

### `LineConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LineConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `LineConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LineConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `SetAxisOfLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetAxisOfLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, являющаяся осью симметрии двух прямых

Parameters:
- `srcLine1`: Первая исходная прямая
- `srcLine2`: Вторая исходная прямая
- `variant`: Номер варианта прямой

### `SetDividingNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetDividingNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Прямая, перпендикулярная отрезку между двумя узлами, делящая отрезок в заданной пропорции

Parameters:
- `srcNode1`: Первый исходный узел
- `srcNode2`: Второй исходный узел
- `param`: Значение параметра, коэффициент. Имеет значение 0, если результирующая прямая продит через первый узел, 1, если проходит черз второй узел, 0.5, если делит отрезок пополам. Может принимать любое значение

### `SetHorizontal(TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetHorizontal(TFlex.Model.Parameter)`

Горизонтальная прямая

Parameters:
- `distance`: Устанавливаемое значение координаты Y

Remarks: Функция устанавливает параметры линии построения, соответствующие горизонтальной прямой. Прямая располагается на расстоянии distance от оси X системы координат модели (без учёта масштаба текущей страницы)

### `SetHorizontalThroughNode(TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetHorizontalThroughNode(TFlex.Model.Model2D.Node)`

Горизонтальная прямая, проходящая через узел

Parameters:
- `srcNode`: Исходный узел

### `SetOnAngleThroughNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetOnAngleThroughNode(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Прямая, проходящая через узел, под углом к горизонтали

Parameters:
- `srcNode`: Исходный узел
- `angle`: Значение угла в градусах

### `SetOnAngleToLineThroughNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetOnAngleToLineThroughNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Прямая, проходящая через узел, под углом к другой прямой

Parameters:
- `srcLine`: Исходная линия построения (прямая)
- `srcNode`: Исходный узел
- `angle`: Устанавливаемое значение угла в градусах

### `SetParallel(TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetParallel(TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

Параллельная прямая

Parameters:
- `srcLine`: Исходная линия построения (прямая)
- `distance`: Устанавливаемое значение расстояния

Remarks: Функция устанавливает параметры линии построения, соответствующие прямой, параллельной исходной прямой. Прямая располагается на расстоянии distance от исходной прямой (без учёта масштаба текущей страницы).

### `SetParallelTangentToCircle(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetParallelTangentToCircle(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, параллельная другой прямой, касательная к окружности

Parameters:
- `srcLine`: Исходная прямая
- `srcCircle`: Исходная окружность
- `variant`: Номер варианта прямой

### `SetParallelTangentToEllipse(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetParallelTangentToEllipse(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, параллельная другой прямой, касательная к эллипсу

Parameters:
- `srcLine`: Исходный узел
- `srcEllipse`: Исходный эллипс
- `variant`: Номер варианта прямой

### `SetParallelTangentToPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetParallelTangentToPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, параллельная другой прямой, касательная к сплайну или другой полилинии

Parameters:
- `srcLine`: Исходная прямая
- `srcPolyline`: Исходная полилиния
- `variant`: Номер варианта прямой

### `SetParallelThroughNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetParallelThroughNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

Прямая, параллельная другой прямой, проходящая через узел

Parameters:
- `srcLine`: Исходная прямая
- `srcNode`: Исходный узел

### `SetPerpendicularThroughNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetPerpendicularThroughNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

Прямая, перпендикулярная другой прямой, проходящая через узел

Parameters:
- `srcLine`: Исходная прямая
- `srcNode`: Исходный узел

### `SetSymmetric(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetSymmetric(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Прямая, симметричная другой прямой относительно оси (прямой)

Parameters:
- `srcLine`: Исходная прямая
- `axisLine`: Ось (прямая)

### `SetTangentToCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetTangentToCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, проходящая через узел, касательная к окружности

Parameters:
- `srcNode`: Исходный узел
- `srcCircle`: Исходная окружность
- `variant`: Номер варианта прямой

### `SetTangentToCircleOnAngle(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetTangentToCircleOnAngle(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32,TFlex.Model.Parameter)`

Прямая, касательная к окружности, под углом к другой прямой

Parameters:
- `srcLine`: Исходная прямая
- `srcCircle`: Исходная окружность
- `variant`: Номер варианта прямой
- `angle`: Значение угла в градусах

### `SetTangentToCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetTangentToCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, касательная к двум окружностям

Parameters:
- `srcCircle1`: Первая исходная окружность
- `srcCircle2`: Вторая исходная окружность
- `variant`: Номер варианта касания

### `SetThoughNodeTangentToEllipse(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetThoughNodeTangentToEllipse(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, проходящая через узел, касательная к эллипсу

Parameters:
- `srcNode`: Исходный узел
- `srcEllipse`: Исходный эллипс
- `variant`: Номер варианта касания прямой

### `SetThoughNodeTangentToPolyline(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetThoughNodeTangentToPolyline(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

Прямая, проходящая через узел, касательная к сплайну или другой полилинии

Parameters:
- `srcNode`: Исходный узел
- `srcPolyline`: Исходная полилиния
- `variant`: Номер варианта прямой

### `SetThroughNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetThroughNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Прямая, проходящая через два узла

Parameters:
- `srcNode1`: Первый исходный узел
- `srcNode2`: Второй исходный узел

### `SetVertical(TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetVertical(TFlex.Model.Parameter)`

Вертикальная прямая

Parameters:
- `distance`: Устанавливаемое значение координаты X

Remarks: Функция устанавливает параметры линии построения, соответствующие вертикальной прямой Прямая располагается на расстоянии distance от оси Y системы координат модели (без учёта масштаба текущей страницы)

### `SetVerticalThroughNode(TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LineConstruction.SetVerticalThroughNode(TFlex.Model.Model2D.Node)`

Вертикальная прямая, проходящая через узел

Parameters:
- `srcNode`: Исходный узел

## Propertys

### `ConstructionGeometry`

ID: `P:TFlex.Model.Model2D.LineConstruction.ConstructionGeometry`

Геометрия линии построения

### `GeometryType`

ID: `P:TFlex.Model.Model2D.LineConstruction.GeometryType`

Тип геометрии линии построения

### `LineConstructionGeometry`

ID: `P:TFlex.Model.Model2D.LineConstruction.LineConstructionGeometry`

Геометрия линии построения (прямой)

Remarks: После использования рекомендуется удалить полученную геометрию, использую функцию Dispose().

### `LineType`

ID: `P:TFlex.Model.Model2D.LineConstruction.LineType`

Тип привязки прямой

### `LineView`

ID: `P:TFlex.Model.Model2D.LineConstruction.LineView`

Вид прямой

### `SubType`

ID: `P:TFlex.Model.Model2D.LineConstruction.SubType`

Подтип линии построения
