# TFlex.Model.Model3D.ProxyOperation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для 3D операций внешнего приложения, встраиваемых в модель

## Remarks

Виртуальные методы, которые предлагается перекрыть, предназначены для вызова внешней операцией, в которую экземпляр класса агрегируется. Эти методы вызываются системой автоматически и не должны вызываться приложением.

## Methods

### `AddAxis(System.Int32,TFlex.Model.Model3D.Geometry.BaseAxis)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.AddAxis(System.Int32,TFlex.Model.Model3D.Geometry.BaseAxis)`

Добавить ось в геометрию

Parameters:
- `index`: Допустимое значение 0,1,2

Remarks: Вызывается только в функции MakeGeometry

### `AddDiagnosticsMessage(TFlex.Model.DiagnosticsMessage)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.AddDiagnosticsMessage(TFlex.Model.DiagnosticsMessage)`

Добавить диагностическое сообщение. Надо вызывать из MakeGeometry

Parameters:
- `message`: Сообщение

### `AddDirection(System.Int32,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.AddDirection(System.Int32,TFlex.Model.Model3D.Geometry.BaseDirection)`

Добавить направление в геометрию

Parameters:
- `index`: Допустимое значение 0,1,2

Remarks: Вызывается только в функции MakeGeometry

### `AddPlane(System.Int32,TFlex.Model.Model3D.Geometry.BasePlane)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.AddPlane(System.Int32,TFlex.Model.Model3D.Geometry.BasePlane)`

Добавить плоскость в геометрию

Parameters:
- `index`: Допустимое значение 0,1,2

Remarks: Вызывается только в функции MakeGeometry

### `AddPoint(System.Int32,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.AddPoint(System.Int32,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Добавить точку в геометрию

Parameters:
- `index`: Допустимое значение 0,1,2

Remarks: Вызывается только в функции MakeGeometry

### `AddSolid(TFlex.Model.Model3D.ProxyOperation.TexturedBody)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.AddSolid(TFlex.Model.Model3D.ProxyOperation.TexturedBody)`

Добавить тело в список тел операции

Parameters:
- `solid`: Тело

Remarks: Вызывается только в функции MakeGeometry

### `AddToScene`

ID: `M:TFlex.Model.Model3D.ProxyOperation.AddToScene`

Прогрузка операции в сцену

Returns: Если операция реализует свою процедуру прогрузки, то нужно вернуть true

Remarks: По умолчанию, прогружаются тела, полученные в MakeGeometry и добавленные в список тел при помощи AddSolid

### `CanAddDiagnosticsMessage`

ID: `M:TFlex.Model.Model3D.ProxyOperation.CanAddDiagnosticsMessage`

Можно ли добавить диагностическое сообщение.

### `IsVirtualBody`

ID: `M:TFlex.Model.Model3D.ProxyOperation.IsVirtualBody`

Виртуальное тело в моделе, особенность представления тела операции в дереве модели (по аналогии с 3D фрагментом или массивом)

### `MakeGeometry`

ID: `M:TFlex.Model.Model3D.ProxyOperation.MakeGeometry`

Пересчитать объект. Сформировать список тел в операции.

Returns: Возвращается признак успешности выполнения пересчета

Remarks: Тела добавлются с помощью функции AddSolid

## Propertys

### `AttributesFromSource`

ID: `P:TFlex.Model.Model3D.ProxyOperation.AttributesFromSource`

Значение свойства "Атрибуты с исходной операции"

### `CanBeSuppressed`

ID: `P:TFlex.Model.Model3D.ProxyOperation.CanBeSuppressed`

Доступно ли подавление операции

### `Operation`

ID: `P:TFlex.Model.Model3D.ProxyOperation.Operation`

Внешняя операция, в которую агрегируется 3D операция внешнего приложения
