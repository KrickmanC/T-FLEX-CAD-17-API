# TFlex.Model.Model2D.Constraint

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Methods

### `CreateAlignHorizontal(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateAlignHorizontal(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

Создать ограничение "Выравнивание по горизонтали"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iPoint1`: Характерная точка первого опорного объекта
- `iObject2`: Второй опорный объект
- `iPoint2`: Характерная точка второго опорного объекта

Returns: Объект "Ограничение" - в случае успеха

### `CreateAlignVertical(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateAlignVertical(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

Создать ограничение "Выравнивание по вертикали"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iPoint1`: Характерная точка первого опорного объекта
- `iObject2`: Второй опорный объект
- `iPoint2`: Характерная точка второго опорного объекта

Returns: Объект "Ограничение" - в случае успеха

### `CreateCoincident(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateCoincident(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

Создать ограничение "Совпадение"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iPoint1`: Характерная точка первого опорного объекта
- `iObject2`: Второй опорный объект
- `iPoint2`: Характерная точка второго опорного объекта

Returns: Объект "Ограничение" - в случае успеха

### `CreateCollinear(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateCollinear(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Коллинеарность"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iObject2`: Второй опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateConcentric(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateConcentric(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Соосность"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iObject2`: Второй опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateEqualLength(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateEqualLength(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Равная длина"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iObject2`: Второй опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateEqualRadius(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateEqualRadius(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Равный радиус"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iObject2`: Второй опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateFixed(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateFixed(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

Создать ограничение "Фиксация"

Parameters:
- `iDoc`: Текущий документ
- `iObject`: Опорный объект
- `iPoint`: Характерная точка для ограничения

Returns: Объект "Ограничение" - в случае успеха

### `CreateFixedAngle(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateFixedAngle(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Фиксированный угол"

Parameters:
- `iDoc`: Текущий документ
- `iObject`: Опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateFixedLength(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateFixedLength(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Фиксированная длина"

Parameters:
- `iDoc`: Текущий документ
- `iObject`: Опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateHorizontal(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateHorizontal(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Горизонтальность"

Parameters:
- `iDoc`: Текущий документ
- `iObject`: Опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateMidPoint(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateMidPoint(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType)`

Создать ограничение "Симметрия"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iPoint1`: Характерная точка первого опорного объекта
- `iObject2`: Второй опорный объект
- `iPoint2`: Характерная точка второго опорного объекта
- `iObject3`: Опорный объект, задающий центр для первого и второго опорных объектов
- `iPoint3`: Характерная точка третьего опорного объекта

Returns: Объект "Ограничение" - в случае успеха

### `CreateParallel(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateParallel(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Параллельность"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iObject2`: Второй опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreatePerpendicular(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreatePerpendicular(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Перпендикулярность"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iObject2`: Второй опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateSymmetric(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateSymmetric(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.ConstraintPointType,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Симметрия"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iPoint1`: Характерная точка первого опорного объекта
- `iObject2`: Второй опорный объект
- `iPoint2`: Характерная точка второго опорного объекта
- `iObject3`: Опорный объект, задающий ось симметрии

Returns: Объект "Ограничение" - в случае успеха

### `CreateTangent(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateTangent(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Касательность"

Parameters:
- `iDoc`: Текущий документ
- `iObject1`: Первый опорный объект
- `iObject2`: Второй опорный объект

Returns: Объект "Ограничение" - в случае успеха

### `CreateVertical(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.Constraint.CreateVertical(TFlex.Model.Document,TFlex.Model.Model2D.Object2D)`

Создать ограничение "Вертиклаьность"

Parameters:
- `iDoc`: Текущий документ
- `iObject`: Опорный объект

Returns: Объект "Ограничение" - в случае успеха

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Model2D.Constraint.GroupType`

Тип объекта

### `Layer`

ID: `P:TFlex.Model.Model2D.Constraint.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`
