# TFlex.Model.Model3D.ExternalOperation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Constructors

### `ExternalOperation(TFlex.Model.Model3D.ProxyOperation,TFlex.Model.Document,TFlex.Plugin)`

ID: `M:TFlex.Model.Model3D.ExternalOperation.#ctor(TFlex.Model.Model3D.ProxyOperation,TFlex.Model.Document,TFlex.Plugin)`

Конструктор для создания внешней операции

Parameters:
- `proxy`: 3D операция внешнего приложения
- `document`: Документ, в котором создаётся новый объект
- `application`: Плагин

## Methods

### `ExternalOperation(TFlex.Model.Model3D.ProxyOperation,TFlex.Model.Document,TFlex.Plugin)`

ID: `M:TFlex.Model.Model3D.ExternalOperation.#ctor(TFlex.Model.Model3D.ProxyOperation,TFlex.Model.Document,TFlex.Plugin)`

Конструктор для создания внешней операции

Parameters:
- `proxy`: 3D операция внешнего приложения
- `document`: Документ, в котором создаётся новый объект
- `application`: Плагин

## Propertys

### `ConstObject`

ID: `P:TFlex.Model.Model3D.ExternalOperation.ConstObject`

3D операция внешнего приложения, встраиваемого в модель, для опроса её свойств

Remarks: Разделение методов доступа к данным необходимо для работы механизма отката действий

### `GroupType`

ID: `P:TFlex.Model.Model3D.ExternalOperation.GroupType`

Идентификатор типа объекта

### `PluginGuid`

ID: `P:TFlex.Model.Model3D.ExternalOperation.PluginGuid`

System::Guid плагина

### `TypeID`

ID: `P:TFlex.Model.Model3D.ExternalOperation.TypeID`

Пользовательский идентификатор типа объекта

### `VolatileObject`

ID: `P:TFlex.Model.Model3D.ExternalOperation.VolatileObject`

3D операция внешнего приложения, встраиваемого в модель, для изменения её свойств

Remarks: Разделение методов доступа к данным необходимо для работы механизма отката действий
