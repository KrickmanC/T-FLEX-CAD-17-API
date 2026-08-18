# TFlex.Model.Model3D.Visual.Dragger

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Visual`

## Summary

Манипулятор

## Constructors

### `Dragger`

ID: `M:TFlex.Model.Model3D.Visual.Dragger.#ctor`

Конструктор по умолчанию

## Methods

### `Dragger`

ID: `M:TFlex.Model.Model3D.Visual.Dragger.#ctor`

Конструктор по умолчанию

### `Activate(TFlex.Model.Model3D.View3D,System.Int32,System.Int32,System.Single)`

ID: `M:TFlex.Model.Model3D.Visual.Dragger.Activate(TFlex.Model.Model3D.View3D,System.Int32,System.Int32,System.Single)`

Активизация манипулятора

Parameters:
- `view`: Активный 3D вид
- `x`: Экранная координата X курсора
- `y`: Экранная координата Y курсора
- `tolerance`: Допустимое расстояние от курсора до декорации

Returns: Должен возвращать true в случае, когда манипулятор может активизироваться, иначе false

Remarks: Метод вызывается, когда пользователь нажал на кнопку мыши в тот момент, когда курсор находился над декорацией, ассоциированной с манипулятором. Для определения ближайшей к курсору точки на декорации можно воспользоваться методом FindClosestPoint со входными параметрами данного метода

### `FindClosestPoint(TFlex.Model.Model3D.View3D,System.Int32,System.Int32,System.Single,TFlex.Model.Model3D.FloatVectorref )`

ID: `M:TFlex.Model.Model3D.Visual.Dragger.FindClosestPoint(TFlex.Model.Model3D.View3D,System.Int32,System.Int32,System.Single,TFlex.Model.Model3D.FloatVector@)`

Поиск ближайшей точки на декорациях

Parameters:
- `view`: Активный 3D вид
- `x`: Экранная координата X курсора
- `y`: Экранная координата Y курсора
- `tolerance`: Допустимое расстояние от курсора до декорации
- `closestPoint`: Ближайшая найденная точка на декорации

Returns: Декорация, которой непосредственно принадлежит найденная точка, или 0 в случае ошибки

Remarks: Этим методом рекомендуется пользоваться внутри перекрытого метода Activated для того, чтобы найти точку, в которой луч пересёк декорации.

### `Release`

ID: `M:TFlex.Model.Model3D.Visual.Dragger.Release`

Конец перемещения

Remarks: Метод вызывается, когда пользователь отпускает левую кнопку мыши при активном манипуляторе.

### `UpdatePosition(TFlex.Model.Model3D.View3D,System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Visual.Dragger.UpdatePosition(TFlex.Model.Model3D.View3D,System.Int32,System.Int32)`

Обновление положения

Parameters:
- `view`: Активный 3D вид
- `x`: Экранная координата X курсора
- `y`: Экранная координата Y курсора

Returns: Должен возвращать true в случае, когда перемещение вызвало изменение данных и/или необходимость перерисовать декорации

Remarks: Метод вызывается, когда пользователь перемещает мышь с зажатой левой кнопкой при активном манипуляторе

## Propertys

### `Addition`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.Addition`

Дополнительная информация

Remarks: Рекомендуется в порождённых классах переопределять этот метод для получения данных

### `Cursor`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.Cursor`

Курсор

### `Decoration`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.Decoration`

Связанная декорация

Remarks: Клиент должен сам освободить ресурсы декорации по окончании использования, вызвав Dispose()

### `MaximalValue`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.MaximalValue`

Максимальное значение

Remarks: Может поддерживаться не всеми порождёнными классами

### `MaximalValueEnabled`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.MaximalValueEnabled`

Использование максимального значения

Remarks: Может поддерживаться не всеми порождёнными классами

### `MinimalValue`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.MinimalValue`

Минимальное значение

Remarks: Может поддерживаться не всеми порождёнными классами

### `MinimalValueEnabled`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.MinimalValueEnabled`

Использование минимального значения

Remarks: Может поддерживаться не всеми порождёнными классами

### `Step`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.Step`

Текущий шаг

Remarks: Рекомендуется в порождённых классах переопределять этот метод для получения шага

### `Transparent`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.Transparent`

Возможность выбора объектов, скрытых манипулятором

### `Value`

ID: `P:TFlex.Model.Model3D.Visual.Dragger.Value`

Текущее значение

Remarks: Рекомендуется в порождённых классах переопределять этот метод для получения данных

## Events

### `Activated`

ID: `E:TFlex.Model.Model3D.Visual.Dragger.Activated`

Событие происходит после того, как метод Activated возвращает true

### `Released`

ID: `E:TFlex.Model.Model3D.Visual.Dragger.Released`

Событие происходит после выхода из метода Release

### `Updated`

ID: `E:TFlex.Model.Model3D.Visual.Dragger.Updated`

Событие происходит после того, как метод UpdatePosition возвращает true
