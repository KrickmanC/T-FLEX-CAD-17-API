# TFModelPoint

Assembly: `TFlexAPI`

## Methods

### `DetachNode(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,TFDocument!System.Runtime.CompilerServices.IsConst*)`

ID: `M:TFModelPoint.DetachNode(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,TFDocument!System.Runtime.CompilerServices.IsConst*)`

Отвязаться от узла (обновляет координаты из узла)

### `GetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelPoint.GetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

Получить точку в системе координат страницы

### `GetPointInActiveLcs(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelPoint.GetPointInActiveLcs(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить точку в активной системе координат

### `GetPointInLcs(STATUS!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelPoint.GetPointInLcs(STATUS!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

Получить точку в локальной системе координат (если ЛСК не задана, то в СК страницы без учёта масштаба(!))

### `GetPointInSpecifiedLcs(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,FIXING_POINT!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelPoint.GetPointInSpecifiedLcs(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,FIXING_POINT!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst)`

Получить точку в указанной системе координат

### `Regenerate(TFDocument*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocRegenContext*)`

ID: `M:TFModelPoint.Regenerate(TFDocument*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocRegenContext*)`

### `SetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelPoint.SetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

Задать точку с учётом ЛСК (преобразует точку из системы координат страницы в координаты ЛСК, если она есть)

### `SetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Double)`

ID: `M:TFModelPoint.SetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,System.Double)`

Задать точку с выбором новой ЛСК (преобразует точку из системы координат страницы в координаты ЛСК)

### `SetPoint(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelPoint.SetPoint(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Задать точку (копирует все данные из входящей точки, кроме данных, относящихся к решателю ограничений)

### `SetPoint(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,FIXING_POINT!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelPoint.SetPoint(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,FIXING_POINT!System.Runtime.CompilerServices.IsConst*,System.Double!System.Runtime.CompilerServices.IsConst)`

Задать точку с выбором новой ЛСК (преобразует точку из системы координат страницы в координаты ЛСК)

### `SetPointByActivePage(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,STATUS!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelPoint.SetPointByActivePage(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,STATUS!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Задать точку с выбором новой ЛСК (активной да данной странице) и масштабом (преобразует точку из системы координат страницы в координаты ЛСК)

### `UpdateWithConstraints(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelPoint.UpdateWithConstraints(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst)`

Обновить с учётом ограничений
