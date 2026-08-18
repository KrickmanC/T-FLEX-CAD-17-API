# TFlex.Model.Model2D.EllipseConstruction

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Линия построения - эллипс

## Constructors

### `EllipseConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `EllipseConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `SetCenterAndLineAndNode(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetCenterAndLineAndNode(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

Эллипс с центром в узле, касательный к прямой, проходящий через узел

Parameters:
- `centerNode`: Центр эллипса
- `srcLine`: Прямая, которой касается эллипс
- `srcNode`: Узел, через который проходит эллипс

### `SetCenterAndLineAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetCenterAndLineAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

Эллипс проходящий через узел, касательный к прямой, с заданным радиусом

Parameters:
- `centerNode`: Узел, через который проходит эллипс
- `srcLine`: Прямая, которой касается эллипс
- `radius`: Радиус эллипса

### `SetCenterAndNodeAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetCenterAndNodeAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

Эллипс с центром, проходящий через узел и касательный к прямой

Parameters:
- `centerNode`: Центр эллипса
- `srcNode`: Узел, через который проходит эллипс
- `srcLine`: Прямая, которой касается эллипс

### `SetCenterAndNodeAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetCenterAndNodeAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Эллипс с центром в узле, проходящий через узел, с заданным радиусом

Parameters:
- `centerNode`: Центр эллипса
- `srcNode`: Узел, через который проходит эллипс
- `radius`: Радиус эллипса

### `SetCenterAndTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetCenterAndTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Эллипс с центром в узле, проходящий через два узла

Parameters:
- `centerNode`: Центр эллипса
- `srcNode1`: Первый узел, через который проходит эллипс
- `srcNode2`: Второй узел, через который проходит эллипс

### `SetCircleAndLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetCircleAndLine(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Эллипс с полуосью, заданной окружностью, касательный к прямой

Parameters:
- `srcCircle`: Окружность, задающая полуось эллипса
- `srcLine`: Прямая, которой касается эллипс

### `SetCircleAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetCircleAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

Эллипс с полуосью, заданной окружностью, проходящий через узел

Parameters:
- `srcCircle`: Окружность, задающая полуось эллипса
- `srcNode`: Узел, через который проходит эллипс

### `SetNodeAndTwoLines(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetNodeAndTwoLines(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Эллипс проходящий через узел, касательный к двум прямым

Parameters:
- `srcNode`: Узел, через который проходит эллипс
- `srcLine1`: Первая прямая, которой касается эллипс
- `srcLine2`: Вторая прямая, которой касается эллипс

### `SetOutline(TFlex.Model.Model2D.Outline)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetOutline(TFlex.Model.Model2D.Outline)`

Эллипс, проходящий по линии изображения (эллипсу или дуге эллипса)

Parameters:
- `srcOutline`: Линия изображения, по которой проходит эллипс

### `SetThreeNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetThreeNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Эллипс с заданной полуосью, проходящий через узел

Parameters:
- `srcNode1`: Первый узел полуоси эллипса
- `srcNode2`: Второй узел полуоси эллипса
- `srcNode3`: Узел, через который проходит эллипс

### `SetTwoNodesAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetTwoNodesAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

Эллипс с заданной полуосью, касательный к прямой

Parameters:
- `srcNode1`: Первый узел полуоси эллипса
- `srcNode2`: Второй узел полуоси эллипса
- `srcLine`: Прямая, которой касается эллипс

### `SetTwoNodesAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.EllipseConstruction.SetTwoNodesAndRadius(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Эллипс с заданной полуосью, с заданным радиусом

Parameters:
- `srcNode1`: Первый узел полуоси эллипса
- `srcNode2`: Второй узел полуоси эллипса
- `radius`: Радиус эллипса

## Propertys

### `ConstructionGeometry`

ID: `P:TFlex.Model.Model2D.EllipseConstruction.ConstructionGeometry`

Геометрия линии построения

### `EllipseConstructionGeometry`

ID: `P:TFlex.Model.Model2D.EllipseConstruction.EllipseConstructionGeometry`

Геометрия линии построения (эллипса)

Remarks: После использования рекомендуется удалить полученную геометрию, использую функцию Dispose().

### `EllipseType`

ID: `P:TFlex.Model.Model2D.EllipseConstruction.EllipseType`

Тип привязки эллипса

### `GeometryType`

ID: `P:TFlex.Model.Model2D.EllipseConstruction.GeometryType`

Тип геометрии линии построения

### `SubType`

ID: `P:TFlex.Model.Model2D.EllipseConstruction.SubType`

Подтип линии построения
