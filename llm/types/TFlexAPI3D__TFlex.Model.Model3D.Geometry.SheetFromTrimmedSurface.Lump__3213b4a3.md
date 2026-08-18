# TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface`

## Summary

Связанная область

## Constructors

### `Lump(TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.Loop[],System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.#ctor(TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.Loop[],System.UInt32)`

Конструктор для связанной области

Parameters:
- `loops`: Множество составных кривых, образующих границы связанной области
- `id`: Идентификатор грани, уникальный в границах каждого 3D объекта внешнего приложения

Remarks: Использование уникальных и воспроизводимых при каждом пересчёте объекта идентификаторов граней, позволяет обеспечить ассоциативность модели на уровне отдельных элементов топологии. Только одна составная кривая включает все остальные. Все кривые лежащие внутри не могут включать друг друга. Не допускается пересечение или касание между кривыми. Внешний цикл ориентирован против часовой стрелки. Внутренние циклы ориентированы по часовой стрелке

## Methods

### `Lump(TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.Loop[],System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.#ctor(TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump.Loop[],System.UInt32)`

Конструктор для связанной области

Parameters:
- `loops`: Множество составных кривых, образующих границы связанной области
- `id`: Идентификатор грани, уникальный в границах каждого 3D объекта внешнего приложения

Remarks: Использование уникальных и воспроизводимых при каждом пересчёте объекта идентификаторов граней, позволяет обеспечить ассоциативность модели на уровне отдельных элементов топологии. Только одна составная кривая включает все остальные. Все кривые лежащие внутри не могут включать друг друга. Не допускается пересечение или касание между кривыми. Внешний цикл ориентирован против часовой стрелки. Внутренние циклы ориентированы по часовой стрелке
