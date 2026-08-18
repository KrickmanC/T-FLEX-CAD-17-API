# TFModelDirection

Assembly: `TFlexAPI`

## Constructors

### `TFModelDirection`

ID: `M:TFModelDirection.#ctor`

### `TFModelDirection(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.#ctor(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Угол направления

Parameters:
- `iAngleWithOX`: Угол с осью X (угол наклона)
- `iMagnitude`: Величиная направления (Длинна вектора)

### `TFModelDirection(System.Double,System.Double)`

ID: `M:TFModelDirection.#ctor(System.Double,System.Double)`

Угол направления

Parameters:
- `iAngleWithOX`: Угол с осью X (угол наклона в радианах)
- `iMagnitude`: Величиная направления (Длинна вектора в милиметрах)

### `TFModelDirection(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.#ctor(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по двумя модельным точкам

Parameters:
- `iDestination`: Вторая точка направления
- `iMagnitude`: Величина направления

### `TFModelDirection(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:TFModelDirection.#ctor(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор по двумя модельным точкам

Parameters:
- `iDestination`: Вторая точка направления
- `iMagnitude`: Величина направления

### `TFModelDirection(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFModelDirection.DirectionType)`

ID: `M:TFModelDirection.#ctor(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFModelDirection.DirectionType)`

Конструктор по двумя модельным точкам

Parameters:
- `iDestination`: Вторая точка направления
- `iMagnitude`: Величина направления

### `TFModelDirection(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.#ctor(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по вектору направления

Parameters:
- `iDirection`: Направление

## Methods

### `TFModelDirection`

ID: `M:TFModelDirection.#ctor`

### `TFModelDirection(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.#ctor(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Угол направления

Parameters:
- `iAngleWithOX`: Угол с осью X (угол наклона)
- `iMagnitude`: Величиная направления (Длинна вектора)

### `TFModelDirection(System.Double,System.Double)`

ID: `M:TFModelDirection.#ctor(System.Double,System.Double)`

Угол направления

Parameters:
- `iAngleWithOX`: Угол с осью X (угол наклона в радианах)
- `iMagnitude`: Величиная направления (Длинна вектора в милиметрах)

### `TFModelDirection(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.#ctor(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по двумя модельным точкам

Parameters:
- `iDestination`: Вторая точка направления
- `iMagnitude`: Величина направления

### `TFModelDirection(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

ID: `M:TFModelDirection.#ctor(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double)`

Конструктор по двумя модельным точкам

Parameters:
- `iDestination`: Вторая точка направления
- `iMagnitude`: Величина направления

### `TFModelDirection(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFModelDirection.DirectionType)`

ID: `M:TFModelDirection.#ctor(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFModelDirection.DirectionType)`

Конструктор по двумя модельным точкам

Parameters:
- `iDestination`: Вторая точка направления
- `iMagnitude`: Величина направления

### `TFModelDirection(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.#ctor(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Конструктор по вектору направления

Parameters:
- `iDirection`: Направление

### `GetDestinationModelPoint`

ID: `M:TFModelDirection.GetDestinationModelPoint`

Получить точку задающую направление (может быть не задана)

### `GetDirectionBackward(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelDirection.GetDirectionBackward(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

Вычислить вектор направления от указанной точки в обратном направлении

Parameters:
- `iSource`: Точка начала
- `iDoc`: Документ
- `iPageScale`: Масштаб страницы

### `GetDirectionForward(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelDirection.GetDirectionForward(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

Вычислить вектор направления от указанной точки

Parameters:
- `iSource`: Точка начала
- `iDoc`: Документ
- `iPageScale`: Масштаб страницы

### `GetDirectionForward(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelDirection.GetDirectionForward(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

Вычислить вектор направления от указанной точки

Parameters:
- `iSource`: Точка начала
- `iDoc`: Документ
- `iPageScale`: Масштаб страницы

### `GetDirectionForwardInDefUnits(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst,RealParameter*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.GetDirectionForwardInDefUnits(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst,RealParameter*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RealParameter*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить длину и угол наклона направления в виде параметров (всегда в ед. изм по умолчанию). Внутри приосходит создание новых копий параметров в ед. измерения по умолчанию. Создавался для вывода в диалоги

Parameters:
- `iSource`: Точка начала
- `iDoc`: Документ
- `iPageScale`: Масштаб страницы
- `oMagnitude`: Длинна
- `oAngle`: Угол

### `GetDirectionMagnitude`

ID: `M:TFModelDirection.GetDirectionMagnitude`

Удалить

### `GetEditDestinationModelPoint`

ID: `M:TFModelDirection.GetEditDestinationModelPoint`

Получить точку задающую направление (может быть не задана)

### `GetParents(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CParentsArray*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ParentType,System.UInt32!System.Runtime.CompilerServices.IsConst)`

ID: `M:TFModelDirection.GetParents(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CParentsArray*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ParentType,System.UInt32!System.Runtime.CompilerServices.IsConst)`

### `GetType`

ID: `M:TFModelDirection.GetType`

Получить тип направления

### `HaveDestinationModelPoint`

ID: `M:TFModelDirection.HaveDestinationModelPoint`

Направление использует TFModelPoint в качестве точки назначения?

### `SetDestinationModelPoint(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFModelDirection.DirectionType)`

ID: `M:TFModelDirection.SetDestinationModelPoint(TFModelPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFModelDirection.DirectionType)`

Установить значение угла и скорректировать тип

### `SetDirectionAngleWithOX(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.SetDirectionAngleWithOX(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить значение угла и скорректировать тип

### `SetDirectionMagnitude(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFModelDirection.SetDirectionMagnitude(RealParameter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Установить значение длинны и скорректировать тип

## Fields

### `_destination`

ID: `F:TFModelDirection._destination`

### `_type`

ID: `F:TFModelDirection._type`
