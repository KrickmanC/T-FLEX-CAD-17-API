# TFlex.Model.Model3D.MaterialOperation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция наложения материала

## Constructors

### `MaterialOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `MaterialOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `AddFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.AddFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить грань к наложению материала

Parameters:
- `Group`: Индекс группы граней
- `Face`: Грань

### `AddFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.AddFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить грань к наложению материала

Parameters:
- `Face`: Грань

Remarks: Грань добавляется в нулевую группу граней

### `AddGroup`

ID: `M:TFlex.Model.Model3D.MaterialOperation.AddGroup`

Добавить новую пустую группу граней к наложению материала

### `GetFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.GetFace(System.Int32)`

Получить грань по индексу

Parameters:
- `Index`: Индекс грани

Returns: Грань

Remarks: Возвращается грань из нулевой группы

### `GetFace(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.GetFace(System.Int32,System.Int32)`

Получить грань из заданной группы граней по индексу

Parameters:
- `Index`: Индекс грани
- `Group`: Индекс группы граней

Returns: Грань

### `GetFaceCount(System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.GetFaceCount(System.Int32)`

Число граней в заданной группе

Parameters:
- `Group`: Индекс группы граней

### `GetFaceMaterial(System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.GetFaceMaterial(System.Int32)`

Получить материал грани по индексу

Parameters:
- `Index`: Индекс грани

Returns: Грань

Remarks: Возвращается грань из нулевой группы

### `GetFaceMaterial(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.GetFaceMaterial(System.Int32,System.Int32)`

Получить материал грани из заданной группы граней по индексу

Parameters:
- `Index`: Индекс грани
- `Group`: Индекс группы граней

Returns: Грань

### `GetMappingCoordSystem(System.Int32,TFlex.Model.Model3D.Geometry.Point3Dref ,TFlex.Model.Model3D.Geometry.Directionref ,TFlex.Model.Model3D.Geometry.Directionref ,TFlex.Model.Model3D.Geometry.Directionref )`

ID: `M:TFlex.Model.Model3D.MaterialOperation.GetMappingCoordSystem(System.Int32,TFlex.Model.Model3D.Geometry.Point3D@,TFlex.Model.Model3D.Geometry.Direction@,TFlex.Model.Model3D.Geometry.Direction@,TFlex.Model.Model3D.Geometry.Direction@)`

Получить систему координат наложения текстуры для данной группы граней

Remarks: Система координат определена для наложения проецированием на плоскость, цилиндр, сферу, параллелепипед

### `GetMappingType(System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.GetMappingType(System.Int32)`

Получить способ наложения текстуры материала для заданной группы граней

### `RemoveFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.RemoveFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Исключить грань из операции наложения материала

Parameters:
- `Face`: Грань

### `RemoveGroup(System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.RemoveGroup(System.Int32)`

Удалить заданную группу граней из наложению материала

Remarks: Невозможно удалить все группы граней, нулевая группа граней есть всегда

### `SetMappingCoordSystem(System.Int32,TFlex.Model.Model3D.Geometry.Point3D,TFlex.Model.Model3D.Geometry.Direction,TFlex.Model.Model3D.Geometry.Direction,TFlex.Model.Model3D.Geometry.Direction)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.SetMappingCoordSystem(System.Int32,TFlex.Model.Model3D.Geometry.Point3D,TFlex.Model.Model3D.Geometry.Direction,TFlex.Model.Model3D.Geometry.Direction,TFlex.Model.Model3D.Geometry.Direction)`

Установить систему координат наложения текстуры для данной группы граней

Remarks: Система координат определена для наложения проецированием на плоскость, цилиндр, сферу, параллелепипед. Цепочка преобразований будет состоять из трёх сдвигов и трёх поворотов.

### `SetMappingCoordSystem(System.Int32,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.SetMappingCoordSystem(System.Int32,TFlex.Model.Model3D.LCS)`

Установить систему координат наложения текстуры для данной группы граней

Remarks: Система координат определена для наложения проецированием на плоскость, цилиндр, сферу, параллелепипед

### `SetMappingType(System.Int32,TFlex.Model.Model3D.MaterialOperation.MappingType)`

ID: `M:TFlex.Model.Model3D.MaterialOperation.SetMappingType(System.Int32,TFlex.Model.Model3D.MaterialOperation.MappingType)`

Установить способ наложения текстуры материала для заданной группы граней

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.MaterialOperation.Count`

Число граней

Remarks: Число граней в нулевой группе

### `GroupCount`

ID: `P:TFlex.Model.Model3D.MaterialOperation.GroupCount`

Число групп граней

### `GroupType`

ID: `P:TFlex.Model.Model3D.MaterialOperation.GroupType`

Получить тип объекта
