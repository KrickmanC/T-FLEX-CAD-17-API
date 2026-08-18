# TFlex.Model.Model3D.ParallelPlaneWorkplane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Рабочая плоскость, параллельная плоскости

## Constructors

### `ParallelPlaneWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ParallelPlaneWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `ParallelPlaneWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.ParallelPlaneWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Methods

### `ParallelPlaneWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ParallelPlaneWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `ParallelPlaneWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.ParallelPlaneWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Propertys

### `BasePlane`

ID: `P:TFlex.Model.Model3D.ParallelPlaneWorkplane.BasePlane`

Плоскость, задающая положение рабочей плоскости

### `EdgeTangentToWorkplane`

ID: `P:TFlex.Model.Model3D.ParallelPlaneWorkplane.EdgeTangentToWorkplane`

Ребро, которого касается рабочая плоскость

Remarks: Положение рабочей плоскости задаётся четырьмя взаимоисключающими способами: смещением, точкой, гранью, ребром

### `FaceTangentToWorkplane`

ID: `P:TFlex.Model.Model3D.ParallelPlaneWorkplane.FaceTangentToWorkplane`

Поверхность, которой касается рабочая плоскость

Remarks: Положение рабочей плоскости задаётся четырьмя взаимоисключающими способами: смещением, точкой, гранью, ребром

### `Offset`

ID: `P:TFlex.Model.Model3D.ParallelPlaneWorkplane.Offset`

Смещение

Remarks: Положение рабочей плоскости задаётся четырьмя взаимоисключающими способами: смещением, точкой, гранью, ребром

### `PointOnWorkplane`

ID: `P:TFlex.Model.Model3D.ParallelPlaneWorkplane.PointOnWorkplane`

Точка, задающую положение рабочей плоскости

Remarks: Положение рабочей плоскости задаётся четырьмя взаимоисключающими способами: смещением, точкой, гранью, ребром
