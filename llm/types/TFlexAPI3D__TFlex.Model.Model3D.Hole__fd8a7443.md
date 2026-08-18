# TFlex.Model.Model3D.Hole

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс операции 3D отверстия

## Constructors

### `Hole(System.String,TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Hole.#ctor(System.String,TFlex.Model.Document)`

Конструктор для создания 3D отверстия

Parameters:
- `fileName`: Имя документа отверстия
- `document`: Документ, в котором создаётся новый объект

## Methods

### `Hole(System.String,TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Hole.#ctor(System.String,TFlex.Model.Document)`

Конструктор для создания 3D отверстия

Parameters:
- `fileName`: Имя документа отверстия
- `document`: Документ, в котором создаётся новый объект

### `AddHole(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Model3D.Node3D)`

ID: `M:TFlex.Model.Model3D.Hole.AddHole(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Model3D.Node3D)`

Добавить отверстие на грани

Parameters:
- `face`: Грань на которой строится отверстие
- `node`: Точка задающая центр отверстия

Returns: Успешно или нет добавлено отверстие

### `AddHole(TFlex.Model.Model3D.Operation,TFlex.Model.Model3D.Node3D)`

ID: `M:TFlex.Model.Model3D.Hole.AddHole(TFlex.Model.Model3D.Operation,TFlex.Model.Model3D.Node3D)`

Добавить отверстие на грани

Parameters:
- `operation`: Операция, на которой строится отверстие
- `node`: Точка, задающая центр отверстия

Returns: Успешно или нет добавлено отверстие

### `AddHoles(TFlex.Model.Model3D.ArrayOperation)`

ID: `M:TFlex.Model.Model3D.Hole.AddHoles(TFlex.Model.Model3D.ArrayOperation)`

Добавить отверстия по массиву

Parameters:
- `arrayOperation`: Массив, задающий центры отверстий

Returns: Успешно или нет добавлены отверстия

### `DeleteHole(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.DeleteHole(System.Int32)`

Удалить отверстие по индексу

Parameters:
- `index`: Индекс удаляемого отверстия

Returns: Успешно или нет добавлено отверстие

### `GetBaseFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.GetBaseFace(System.Int32)`

Получение базовой грани для отверстия по индексу отверстия

Parameters:
- `hole`: Индекс отверстия

### `GetDirectionLCS(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.GetDirectionLCS(System.Int32)`

Получение системы координат, задающей направление, по индексу отверстия

Parameters:
- `hole`: Индекс отверстия

### `GetDirectionTopol(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.GetDirectionTopol(System.Int32)`

Получение элемента, задающего направление, по индексу отверстия

Parameters:
- `hole`: Индекс отверстия

### `GetRotation(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.GetRotation(System.Int32)`

Получение задающего поворот элемента по индексу отверстия

Parameters:
- `hole`: Индекс отверстия

### `GetTargetLCS(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.GetTargetLCS(System.Int32)`

Получение целевой системы координат, используемой для привязки отверстия

Parameters:
- `hole`: Индекс отверстия

### `GetVariableValue(System.Int32,System.String,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Hole.GetVariableValue(System.Int32,System.String,System.Boolean)`

Получить переменную отверстия по имени

Parameters:
- `hole`: Индекс отверстия
- `name`: Имя переменной отверстия
- `forSet`: Признак необходимости изменения переменной

Returns: Переменная отверстия

### `GetVariables(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.GetVariables(System.Int32)`

Получить переменные по индексу отверстия

Parameters:
- `hole`: Индекс отверстия

Returns: Переменные отверстия

### `IsOrientationSet(System.Int32)`

ID: `M:TFlex.Model.Model3D.Hole.IsOrientationSet(System.Int32)`

Проверка заданной ориентации по индексу отверстия

Parameters:
- `hole`: Индекс отверстия

### `SetBaseFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.Hole.SetBaseFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace)`

Задать базовую грань для отверстия

Parameters:
- `hole`: Индекс отверстия
- `baseFace`: Базовая грань для отверстия

Returns: Успешно или нет добавлена базовая грань

### `SetDirection(System.Int32,TFlex.Model.Model3D.Geometry.ModelTopol)`

ID: `M:TFlex.Model.Model3D.Hole.SetDirection(System.Int32,TFlex.Model.Model3D.Geometry.ModelTopol)`

Задать направление отверстия

Parameters:
- `hole`: Индекс отверстия
- `topol`: Элемент для направления

Returns: Успешно или нет задано направление

### `SetDirection(System.Int32,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Hole.SetDirection(System.Int32,TFlex.Model.Model3D.LCS)`

Задать направление отверстия

Parameters:
- `hole`: Индекс отверстия
- `lcs`: Система координат

Returns: Успешно или нет задано направление

### `SetRotation(System.Int32,TFlex.Model.Model3D.Geometry.ModelTopol)`

ID: `M:TFlex.Model.Model3D.Hole.SetRotation(System.Int32,TFlex.Model.Model3D.Geometry.ModelTopol)`

Задать поворот отверстия

Parameters:
- `hole`: Индекс отверстия
- `topol`: Элемент для поворота отверстия

Returns: Успешно или нет добавлена базовая грань

## Propertys

### `End`

ID: `P:TFlex.Model.Model3D.Hole.End`

Конец отверстия

### `EndFace`

ID: `P:TFlex.Model.Model3D.Hole.EndFace`

Грань определяющая конец отверстия

### `FileName`

ID: `P:TFlex.Model.Model3D.Hole.FileName`

Имя файла 3D Фрагмента

### `GroupType`

ID: `P:TFlex.Model.Model3D.Hole.GroupType`

Получить тип объекта

### `HideConnectors`

ID: `P:TFlex.Model.Model3D.Hole.HideConnectors`

Скрывать коннекторы

### `HoleBaseFaceMode`

ID: `P:TFlex.Model.Model3D.Hole.HoleBaseFaceMode`

Режим поиска базовой грани

### `HoleCount`

ID: `P:TFlex.Model.Model3D.Hole.HoleCount`

Количество отверстий

### `PathName`

ID: `P:TFlex.Model.Model3D.Hole.PathName`

Путь файла 3D Фрагмента
