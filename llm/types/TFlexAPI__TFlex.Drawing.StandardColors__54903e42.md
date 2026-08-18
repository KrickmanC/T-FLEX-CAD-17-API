# TFlex.Drawing.StandardColors

Assembly: `TFlexAPI`
Namespace: `TFlex.Drawing`

## Summary

Стандартные цвета

## Remarks

Класс позволяет использовать во внешних приложениях стандартные цвета T-Flex, задаваемые в диалоге "Настройка->Установка->Цвета". Статические свойства типа int предназначены для использования в методах Color(int) внутри API. Статические свойства типа System.Drawing.Color могут использоваться в прочих случаях.

## Methods

### `ColorFromIndex(System.Int32)`

ID: `M:TFlex.Drawing.StandardColors.ColorFromIndex(System.Int32)`

Получить цвет по данному индексу

### `ColorNameFromIndex(System.Int32)`

ID: `M:TFlex.Drawing.StandardColors.ColorNameFromIndex(System.Int32)`

Получить имя цвет по данному индексу

### `FindClosestIndex(System.Drawing.Color)`

ID: `M:TFlex.Drawing.StandardColors.FindClosestIndex(System.Drawing.Color)`

Найти индекс, наиболее соответствующий данному цвету

Parameters:
- `color`: Системный цвет

Remarks: Этот метод выполняется дольше, чем остальные методы класса, поэтому при возможности его результаты следует кэшировать.

### `FindClosestIndex(System.UInt32)`

ID: `M:TFlex.Drawing.StandardColors.FindClosestIndex(System.UInt32)`

Найти индекс, наиболее соответствующий данному цвету

Parameters:
- `colorref`: Цвет в формате Windows GDI (COLORREF)

Remarks: Этот метод выполняется дольше, чем остальные методы класса, поэтому при возможности его результаты следует кэшировать.

### `IndexFromColor(System.Drawing.Color)`

ID: `M:TFlex.Drawing.StandardColors.IndexFromColor(System.Drawing.Color)`

Получить индекс для цвета, не входящего в основную палитру

## Propertys

### `ActiveDragger`

ID: `P:TFlex.Drawing.StandardColors.ActiveDragger`

Цвет активного манипулятора

### `ActiveDraggerIndex`

ID: `P:TFlex.Drawing.StandardColors.ActiveDraggerIndex`

Цвет активного манипулятора

### `ActiveEdgeMark`

ID: `P:TFlex.Drawing.StandardColors.ActiveEdgeMark`

Цвет пометки активных рёбер

### `ActiveEdgeMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.ActiveEdgeMarkIndex`

Цвет пометки активных рёбер

### `ActiveFaceEdge`

ID: `P:TFlex.Drawing.StandardColors.ActiveFaceEdge`

Цвет пометки рёбер активной грани

### `ActiveFaceEdgeIndex`

ID: `P:TFlex.Drawing.StandardColors.ActiveFaceEdgeIndex`

Цвет пометки рёбер активной грани

### `ActiveFaceMark`

ID: `P:TFlex.Drawing.StandardColors.ActiveFaceMark`

Цвет пометки активной грани

### `ActiveFaceMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.ActiveFaceMarkIndex`

Цвет пометки активной грани

### `ActiveNodeMark`

ID: `P:TFlex.Drawing.StandardColors.ActiveNodeMark`

Цвет пометки активных 3D узлов

### `ActiveNodeMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.ActiveNodeMarkIndex`

Цвет пометки активных 3D узлов

### `ActivePathMark`

ID: `P:TFlex.Drawing.StandardColors.ActivePathMark`

Цвет пометки активных путей и профилей

### `ActivePathMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.ActivePathMarkIndex`

Цвет пометки активных путей и профилей

### `ActiveService`

ID: `P:TFlex.Drawing.StandardColors.ActiveService`

Вспомогательный цвет активного элемента

### `ActiveServiceIndex`

ID: `P:TFlex.Drawing.StandardColors.ActiveServiceIndex`

Вспомогательный цвет активного элемента

### `ActiveView`

ID: `P:TFlex.Drawing.StandardColors.ActiveView`

Цвет рамки активного вида

### `ActiveViewIndex`

ID: `P:TFlex.Drawing.StandardColors.ActiveViewIndex`

Цвет рамки активного вида

### `Background`

ID: `P:TFlex.Drawing.StandardColors.Background`

Цвет фона 2D страниц документа

### `BackgroundIndex`

ID: `P:TFlex.Drawing.StandardColors.BackgroundIndex`

Цвет фона 2D страниц документа

### `ClipPlane`

ID: `P:TFlex.Drawing.StandardColors.ClipPlane`

Цвет плоскости обрезки

### `ClipPlaneIndex`

ID: `P:TFlex.Drawing.StandardColors.ClipPlaneIndex`

Цвет плоскости обрезки

### `Construction`

ID: `P:TFlex.Drawing.StandardColors.Construction`

Цвет линий построения по умолчанию

### `ConstructionIndex`

ID: `P:TFlex.Drawing.StandardColors.ConstructionIndex`

Цвет линий построения по умолчанию

### `Decoration1`

ID: `P:TFlex.Drawing.StandardColors.Decoration1`

Цвет декораций

### `Decoration1Index`

ID: `P:TFlex.Drawing.StandardColors.Decoration1Index`

Цвет декораций

### `Decoration2`

ID: `P:TFlex.Drawing.StandardColors.Decoration2`

Цвет декораций дополнительный

### `Decoration2Index`

ID: `P:TFlex.Drawing.StandardColors.Decoration2Index`

Цвет декораций дополнительный

### `Decoration3`

ID: `P:TFlex.Drawing.StandardColors.Decoration3`

Цвет декораций неактивных

### `Decoration3Index`

ID: `P:TFlex.Drawing.StandardColors.Decoration3Index`

Цвет декораций неактивных

### `Dragger`

ID: `P:TFlex.Drawing.StandardColors.Dragger`

Цвет манипулятора

### `DraggerIndex`

ID: `P:TFlex.Drawing.StandardColors.DraggerIndex`

Цвет манипулятора

### `DynamicMark`

ID: `P:TFlex.Drawing.StandardColors.DynamicMark`

Цвет динамической подсветки элементов в 3D окне

### `DynamicMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.DynamicMarkIndex`

Цвет динамической подсветки элементов в 3D окне

### `EdgeMark`

ID: `P:TFlex.Drawing.StandardColors.EdgeMark`

Цвет пометки рёбер

### `EdgeMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.EdgeMarkIndex`

Цвет пометки рёбер

### `EdgesInShading`

ID: `P:TFlex.Drawing.StandardColors.EdgesInShading`

Цвет рёбер при закраске модели

### `EdgesInShadingIndex`

ID: `P:TFlex.Drawing.StandardColors.EdgesInShadingIndex`

Цвет рёбер при закраске модели

### `FaceEdgeMark1`

ID: `P:TFlex.Drawing.StandardColors.FaceEdgeMark1`

Цвет пометки рёбер грани 1

### `FaceEdgeMark1Index`

ID: `P:TFlex.Drawing.StandardColors.FaceEdgeMark1Index`

Цвет пометки рёбер грани 1

### `FaceEdgeMark2`

ID: `P:TFlex.Drawing.StandardColors.FaceEdgeMark2`

Цвет пометки рёбер грани 2

### `FaceEdgeMark2Index`

ID: `P:TFlex.Drawing.StandardColors.FaceEdgeMark2Index`

Цвет пометки рёбер грани 2

### `FaceEdgeMark3`

ID: `P:TFlex.Drawing.StandardColors.FaceEdgeMark3`

Цвет пометки рёбер грани 3

### `FaceEdgeMark3Index`

ID: `P:TFlex.Drawing.StandardColors.FaceEdgeMark3Index`

Цвет пометки рёбер грани 3

### `FaceMark1`

ID: `P:TFlex.Drawing.StandardColors.FaceMark1`

Цвет пометки грани 1

### `FaceMark1Index`

ID: `P:TFlex.Drawing.StandardColors.FaceMark1Index`

Цвет пометки грани 1

### `FaceMark2`

ID: `P:TFlex.Drawing.StandardColors.FaceMark2`

Цвет пометки грани 2

### `FaceMark2Index`

ID: `P:TFlex.Drawing.StandardColors.FaceMark2Index`

Цвет пометки грани 2

### `FaceMark3`

ID: `P:TFlex.Drawing.StandardColors.FaceMark3`

Цвет пометки грани 3

### `FaceMark3Index`

ID: `P:TFlex.Drawing.StandardColors.FaceMark3Index`

Цвет пометки грани 3

### `Grid`

ID: `P:TFlex.Drawing.StandardColors.Grid`

Цвет сетки

### `GridIndex`

ID: `P:TFlex.Drawing.StandardColors.GridIndex`

Цвет сетки

### `LCSMark`

ID: `P:TFlex.Drawing.StandardColors.LCSMark`

Цвет пометки систем координат

### `LCSMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.LCSMarkIndex`

Цвет пометки систем координат

### `Node`

ID: `P:TFlex.Drawing.StandardColors.Node`

Цвет 2D узлов по умолчанию

### `NodeIndex`

ID: `P:TFlex.Drawing.StandardColors.NodeIndex`

Цвет 2D узлов по умолчанию

### `NodeMark1`

ID: `P:TFlex.Drawing.StandardColors.NodeMark1`

Цвет пометки 3D узлов 1

### `NodeMark1Index`

ID: `P:TFlex.Drawing.StandardColors.NodeMark1Index`

Цвет пометки 3D узлов 1

### `NodeMark2`

ID: `P:TFlex.Drawing.StandardColors.NodeMark2`

Цвет пометки 3D узлов 2

### `NodeMark2Index`

ID: `P:TFlex.Drawing.StandardColors.NodeMark2Index`

Цвет пометки 3D узлов 2

### `NodeMark3`

ID: `P:TFlex.Drawing.StandardColors.NodeMark3`

Цвет пометки 3D узлов 3

### `NodeMark3Index`

ID: `P:TFlex.Drawing.StandardColors.NodeMark3Index`

Цвет пометки 3D узлов 3

### `PageBorder`

ID: `P:TFlex.Drawing.StandardColors.PageBorder`

Цвет рамки форматки

### `PageBorderIndex`

ID: `P:TFlex.Drawing.StandardColors.PageBorderIndex`

Цвет рамки форматки

### `PathMark1`

ID: `P:TFlex.Drawing.StandardColors.PathMark1`

Цвет пометки путей и профилей 1

### `PathMark1Index`

ID: `P:TFlex.Drawing.StandardColors.PathMark1Index`

Цвет пометки путей и профилей 1

### `PathMark2`

ID: `P:TFlex.Drawing.StandardColors.PathMark2`

Цвет пометки путей и профилей 2

### `PathMark2Index`

ID: `P:TFlex.Drawing.StandardColors.PathMark2Index`

Цвет пометки путей и профилей 2

### `PathMark3`

ID: `P:TFlex.Drawing.StandardColors.PathMark3`

Цвет пометки путей и профилей 3

### `PathMark3Index`

ID: `P:TFlex.Drawing.StandardColors.PathMark3Index`

Цвет пометки путей и профилей 3

### `SameAsBackground`

ID: `P:TFlex.Drawing.StandardColors.SameAsBackground`

Цвет элементов, имеющих цвет фона

### `SameAsBackgroundIndex`

ID: `P:TFlex.Drawing.StandardColors.SameAsBackgroundIndex`

Цвет элементов, имеющих цвет фона

### `SectionMark`

ID: `P:TFlex.Drawing.StandardColors.SectionMark`

Цвет пометки сечений

### `SectionMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.SectionMarkIndex`

Цвет пометки сечений

### `Service1`

ID: `P:TFlex.Drawing.StandardColors.Service1`

Вспомогательный цвет 1 (нормали и касательные)

### `Service1Index`

ID: `P:TFlex.Drawing.StandardColors.Service1Index`

Вспомогательный цвет 1 (нормали и касательные)

### `Service2`

ID: `P:TFlex.Drawing.StandardColors.Service2`

Вспомогательный цвет 2 (точки соответствия...)

### `Service2Index`

ID: `P:TFlex.Drawing.StandardColors.Service2Index`

Вспомогательный цвет 2 (точки соответствия...)

### `Service3`

ID: `P:TFlex.Drawing.StandardColors.Service3`

Вспомогательный цвет 3 (точки соответствия...)

### `Service3Index`

ID: `P:TFlex.Drawing.StandardColors.Service3Index`

Вспомогательный цвет 3 (точки соответствия...)

### `Service4`

ID: `P:TFlex.Drawing.StandardColors.Service4`

Вспомогательный цвет 4 (точки соответствия...)

### `Service4Index`

ID: `P:TFlex.Drawing.StandardColors.Service4Index`

Вспомогательный цвет 4 (точки соответствия...)

### `SolidMark1`

ID: `P:TFlex.Drawing.StandardColors.SolidMark1`

Цвет пометки тела 1

### `SolidMark1Index`

ID: `P:TFlex.Drawing.StandardColors.SolidMark1Index`

Цвет пометки тела 1

### `SolidMark2`

ID: `P:TFlex.Drawing.StandardColors.SolidMark2`

Цвет пометки тела 2

### `SolidMark2Index`

ID: `P:TFlex.Drawing.StandardColors.SolidMark2Index`

Цвет пометки тела 2

### `SolidMark3`

ID: `P:TFlex.Drawing.StandardColors.SolidMark3`

Цвет пометки тела 3

### `SolidMark3Index`

ID: `P:TFlex.Drawing.StandardColors.SolidMark3Index`

Цвет пометки тела 3

### `WorkplaneMark`

ID: `P:TFlex.Drawing.StandardColors.WorkplaneMark`

Цвет пометки рабочих плоскостей

### `WorkplaneMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.WorkplaneMarkIndex`

Цвет пометки рабочих плоскостей

### `XorMark`

ID: `P:TFlex.Drawing.StandardColors.XorMark`

Цвет, используемый для пометки в режиме XOR

### `XorMarkIndex`

ID: `P:TFlex.Drawing.StandardColors.XorMarkIndex`

Цвет, используемый для пометки в режиме XOR
