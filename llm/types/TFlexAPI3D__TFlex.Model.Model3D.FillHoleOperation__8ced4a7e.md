# TFlex.Model.Model3D.FillHoleOperation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Заполнение области

## Constructors

### `FillHoleOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.#ctor(TFlex.Model.Document)`

Конструктор для создания Заполнения области

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `FillHoleOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.#ctor(TFlex.Model.Document)`

Конструктор для создания Заполнения области

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddContour(TFlex.Model.Model3D.Geometry.ModelWire)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.AddContour(TFlex.Model.Model3D.Geometry.ModelWire)`

Добавить контур

### `CountContours`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.CountContours`

Количество контуров

### `GetContour(System.Int32)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.GetContour(System.Int32)`

Получить контур

Parameters:
- `contourIndex`: Индекс контура (начинается с 0)

Returns: Свойства контура

### `GetSourceOper`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.GetSourceOper`

Получить исходную операцию

### `InsertContour(System.Int32,TFlex.Model.Model3D.Geometry.ModelWire)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.InsertContour(System.Int32,TFlex.Model.Model3D.Geometry.ModelWire)`

Вставить контур

Parameters:
- `contourIndex`: Индекс добавляемого контура (начинается с 0)

### `IsExistSourceOper`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.IsExistSourceOper`

Задана ли исходная операция

### `RemoveContour(System.Int32)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.RemoveContour(System.Int32)`

Удалить контур

Parameters:
- `contourIndex`: Индекс удаляемого контура (начинается с 0)

### `RemoveSourceOper`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.RemoveSourceOper`

Удалить исходную операцию

### `SetSourceOper(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.SetSourceOper(TFlex.Model.Model3D.Operation)`

Задать исходную операцию

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.GroupType`

Получить тип объекта

### `MergeWithSourceOper`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.MergeWithSourceOper`

Объединить с исходной операцией

### `Split`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.Split`

Разбиение

### `ThinElement`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.ThinElement`

Тонкостенный элемент

### `Tolerance`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.Tolerance`

Точность
