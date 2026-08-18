# TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.Loop

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump`

## Summary

Одна из границ связанной области

## Constructors

### `Loop(TFlex.Model.Model3D.Geometry.BaseBody,System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.Loop.#ctor(TFlex.Model.Model3D.Geometry.BaseBody,System.UInt32)`

Конструктор сегмента проволочного тела

Parameters:
- `wire`: Составная кривая, образующая одну из границ листового тела
- `id`: Идентификатор цикла, уникальный в границах каждого 3D объекта внешнего приложения

Remarks: Использование уникальных и воспроизводимых при каждом пересчёте объекта идентификаторов циклов, позволяет обеспечить ассоциативность модели на уровне отдельных элементов топологии. Параметрическая область плоскость совпадает с плоскостью XY. Следовательно, составная кривая лежит в плоскости XY. Составная кривая должна быть замкнутая и не должна иметь самопересечений. Предполагается, что кривая получена в результате использования генератора WireFromCurvesGenerator

## Methods

### `Loop(TFlex.Model.Model3D.Geometry.BaseBody,System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.Loop.#ctor(TFlex.Model.Model3D.Geometry.BaseBody,System.UInt32)`

Конструктор сегмента проволочного тела

Parameters:
- `wire`: Составная кривая, образующая одну из границ листового тела
- `id`: Идентификатор цикла, уникальный в границах каждого 3D объекта внешнего приложения

Remarks: Использование уникальных и воспроизводимых при каждом пересчёте объекта идентификаторов циклов, позволяет обеспечить ассоциативность модели на уровне отдельных элементов топологии. Параметрическая область плоскость совпадает с плоскостью XY. Следовательно, составная кривая лежит в плоскости XY. Составная кривая должна быть замкнутая и не должна иметь самопересечений. Предполагается, что кривая получена в результате использования генератора WireFromCurvesGenerator
