# TFlex.Model.Model2D.CircleConstruction

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Линия построения - окружность

## Constructors

### `CircleConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `CircleConstruction(TFlex.Model.Document,TFlex.Drawing.Point,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.#ctor(TFlex.Model.Document,TFlex.Drawing.Point,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Конструктор

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `centerPoint`: Точка задающая положение окружности
- `firstTangentPolyline`: Первый сплайн (полилиния), которого касается окружность
- `secondTangentPolyline`: Второй сплайн (полилиния), которого касается окружность

## Methods

### `CircleConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `CircleConstruction(TFlex.Model.Document,TFlex.Drawing.Point,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.#ctor(TFlex.Model.Document,TFlex.Drawing.Point,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Конструктор

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `centerPoint`: Точка задающая положение окружности
- `firstTangentPolyline`: Первый сплайн (полилиния), которого касается окружность
- `secondTangentPolyline`: Второй сплайн (полилиния), которого касается окружность

### `SetCenterAndCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetCenterAndCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

Окружность с центром в узле, касательная к окружности

Parameters:
- `centerNode`: Центр окружности
- `srcCircle`: Окружность, которой касается окружность

### `SetCenterAndEllipse(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetCenterAndEllipse(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

Окружность с центром в узле, касательная к эллипсу

Parameters:
- `centerNode`: Центр окружности
- `srcEllipse`: Эллипс, которого касается окружность

### `SetCenterAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetCenterAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

Окружность с центром в узле, касательная к прямой

Parameters:
- `centerNode`: Центр окружности
- `srcLine`: Прямая, которой касается окружность

### `SetCenterAndNode(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetCenterAndNode(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Окружность с центром в узле, проходящая через узел

Parameters:
- `centerNode`: Центр окружности
- `srcNode`: Узел, через который проходит окружность

### `SetCenterAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetCenterAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Окружность с центром в узле и заданным радиусом

Parameters:
- `centerNode`: Центр окружности
- `radius`: Радиус окружности

### `SetNodeTangentToLineAndCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetNodeTangentToLineAndCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, проходящая через узел, касательная к прямой и окружности

Parameters:
- `srcNode`: Узел, через который проходит окружность
- `srcLine`: Прямая, которой касается окружность
- `srcCircle`: Окружность, которой касается окружность
- `variant`: Номер варианта касания

### `SetNodeTangentToTwoCircles(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetNodeTangentToTwoCircles(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, проходящая через узел, касательная к двум окружностям

Parameters:
- `srcNode`: Узел, через который проходит окружность
- `srcCircle1`: Первая окружность, которой касается окружность
- `srcCircle2`: Вторая окружность, которой касается окружность
- `variant`: Номер варианта касания

### `SetNodeTangentToTwoLines(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetNodeTangentToTwoLines(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, проходящая через узел, касательная к двум прямым

Parameters:
- `srcNode`: Узел, через который проходит окружность
- `srcLine1`: Первая прямая, которой касается окружность
- `srcLine2`: Вторая прямая, которой касается окружность
- `variant`: Номер варианта касания

### `SetOffset(TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetOffset(TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

Окружность, концентричная исходной окружности на заданном расстоянии

Parameters:
- `srcCircle`: Исходная окружность
- `offset`: Расстояние

### `SetOutline(TFlex.Model.Model2D.Outline)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetOutline(TFlex.Model.Model2D.Outline)`

Окружность, проходящая по линии изображения (окружности или дуге окружности)

Parameters:
- `srcOutline`: Линия изображения, по которой проходит окружность

### `SetSymmetric(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetSymmetric(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Окружность, симметричная другой окружности относительно оси (прямой)

Parameters:
- `srcCircle`: Исходная окружность
- `axisLine`: Ось (прямая)

### `SetTangentToCircleAndEllipse(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToCircleAndEllipse(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к окружности и эллипсу

Parameters:
- `srcCircle`: Окружность, которой касается окружность
- `srcEllipse`: Эллипс, которого касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToCircleAndLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToCircleAndLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к окружности и прямой

Parameters:
- `srcCircle`: Окружность, которой касается окружность
- `srcLine`: Прямая, которой касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToCircleAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToCircleAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к окружности, проходящая через узел

Parameters:
- `srcCircle`: Окружность, которой касается окружность
- `srcNode`: Узел, через который проходит окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToCircleAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToCircleAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к окружности и сплайну или другой полилинии

Parameters:
- `srcCircle`: Окружность, которой касается окружность
- `srcPolyline`: Полилиния, которой касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToEllipseAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToEllipseAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к эллипсу и сплайну или другой полилинии

Parameters:
- `srcEllipse`: Эллипс, которого касается окружность
- `srcPolyline`: Полилиния, которой касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToLineAndEllipse(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToLineAndEllipse(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к прямой и эллипсу

Parameters:
- `srcLine`: Прямая, которой касается окружность
- `srcEllipse`: Эллипс, которого касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToLineAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToLineAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к прямой, проходящая через узел

Parameters:
- `srcLine`: Прямая, которой касается окружность
- `srcNode`: Узел, через который проходит окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToLineAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToLineAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к прямой и сплайну или другой полилинии

Parameters:
- `srcLine`: Прямая, которой касается окружность
- `srcPolyline`: Полилиния, которой касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToLineAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.ValueType!TFlex.Drawing.Point!System.Runtime.CompilerServices.IsBoxed)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToLineAndPolyline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.ValueType!TFlex.Drawing.Point!System.Runtime.CompilerServices.IsBoxed)`

Окружность, касательная к прямой и сплайну или другой полилинии

Parameters:
- `srcLine`: Прямая, которой касается окружность
- `srcPolyline`: Полилиния, которой касается окружность
- `radius`: Радиус окружности
- `point`: Ближняя точка, определяющая вариант касания

### `SetTangentToLineAndTwoCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToLineAndTwoCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, касательная к прямой и двум окружностям

Parameters:
- `srcLine`: Прямая, которой касается окружность
- `srcCircle1`: Первая окружность, которой касается окружность
- `srcCircle2`: Вторая окружность, которой касается окружность
- `variant`: Номер варианта касания

### `SetTangentToThreeCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToThreeCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, касательная к трём окружностям

Parameters:
- `srcCircle1`: Первая окружность, которой касается окружность
- `srcCircle2`: Вторая окружность, которой касается окружность
- `srcCircle3`: Третья окружность, которой касается окружность
- `variant`: Номер варианта касания

### `SetTangentToThreeLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToThreeLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, касательная к трём прямым

Parameters:
- `srcLine1`: Первая прямая, которой касается окружность
- `srcLine2`: Вторая прямая, которой касается окружность
- `srcLine3`: Третья прямая, которой касается окружность
- `variant`: Номер варианта касания

### `SetTangentToTwoCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToTwoCircles(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к двум окружностям

Parameters:
- `srcCircle1`: Первая окружность, которой касается окружность
- `srcCircle2`: Вторая окружность, которой касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToTwoEllipses(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToTwoEllipses(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к двум эллипсам

Parameters:
- `srcEllipse1`: Первый эллипс, которого касается окружность
- `srcEllipse2`: Второй эллипс, которого касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToTwoLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToTwoLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к двум прямым

Parameters:
- `srcLine1`: Первая прямая, которой касается окружность
- `srcLine2`: Вторая прямая, которой касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTangentToTwoLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToTwoLines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,TFlex.Model.Model2D.Node)`

Окружность, касательная к двум прямым

Parameters:
- `srcLine1`: Первая прямая, которой касается окружность
- `srcLine2`: Вторая прямая, которой касается окружность
- `radius`: Радиус окружности
- `anchorNode`: Узел привязки

### `SetTangentToTwoLinesAndCircle(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToTwoLinesAndCircle(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, касательная к двум прямым и окружности

Parameters:
- `srcLine1`: Первая прямая, которой касается окружность
- `srcLine2`: Вторая прямая, которой касается окружность
- `srcCircle`: Окружность, которой касается окружность
- `variant`: Номер варианта касания

### `SetTangentToTwoPolylines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTangentToTwoPolylines(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter,System.Int32)`

Окружность, касательная к двум сплайнам или другим полилиниям

Parameters:
- `srcPolyline1`: Первая полилиния, которой касается окружность
- `srcPolyline2`: Вторая полилиния, которой касается окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetThreeNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetThreeNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Окружность, проходящая через три узла

Parameters:
- `srcNode1`: Первый узел
- `srcNode2`: Второй узел
- `srcNode3`: Третий узел

### `SetTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter,System.Int32)`

Окружность, проходящая через два узла

Parameters:
- `srcNode1`: Первый узел, через который проходит окружность
- `srcNode2`: Второй узел, через который проходит окружность
- `radius`: Радиус окружности
- `variant`: Номер варианта касания

### `SetTwoNodesTangentToCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTwoNodesTangentToCircle(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, проходящая через два узла, касательная к окружности

Parameters:
- `srcNode1`: Первый узел, через который проходит окружность
- `srcNode2`: Второй узел, через который проходит окружность
- `srcCircle`: Окружность, которой касается окружность
- `variant`: Номер варианта касания

### `SetTwoNodesTangentToLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.CircleConstruction.SetTwoNodesTangentToLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,System.Int32)`

Окружность, проходящая через два узла, касательная к прямой

Parameters:
- `srcNode1`: Первый узел, через который проходит окружность
- `srcNode2`: Второй узел, через который проходит окружность
- `srcLine`: Прямая, которой касается окружность
- `variant`: Номер варианта касания

## Propertys

### `CircleConstructionGeometry`

ID: `P:TFlex.Model.Model2D.CircleConstruction.CircleConstructionGeometry`

Геометрия линии построения (окружности)

Remarks: После использования рекомендуется удалить полученную геометрию, использую функцию Dispose().

### `CircleType`

ID: `P:TFlex.Model.Model2D.CircleConstruction.CircleType`

Тип привязки окружности

### `ConstructionGeometry`

ID: `P:TFlex.Model.Model2D.CircleConstruction.ConstructionGeometry`

Геометрия линии построения

### `GeometryType`

ID: `P:TFlex.Model.Model2D.CircleConstruction.GeometryType`

Тип геометрии линии построения (окружность)

### `SubType`

ID: `P:TFlex.Model.Model2D.CircleConstruction.SubType`

Подтип линии построения
