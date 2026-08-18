# TFlex.Model.Model3D.LoftOperation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция "по сечениям"

## Constructors

### `LoftOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.LoftOperation.#ctor(TFlex.Model.Document)`

Конструктор для создания Лофта

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `LoftOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.LoftOperation.#ctor(TFlex.Model.Document)`

Конструктор для создания Лофта

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddGuide(TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.LoftOperation.AddGuide(TFlex.Model.Model3D.Geometry.ModelContour)`

Добавить направляющую

### `AddMatch`

ID: `M:TFlex.Model.Model3D.LoftOperation.AddMatch`

Добавить соответствие

### `AddSection(TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.LoftOperation.AddSection(TFlex.Model.Model3D.Geometry.ModelContour)`

Добавить сечение

### `CountGuides`

ID: `M:TFlex.Model.Model3D.LoftOperation.CountGuides`

Количество направляющих

### `CountMatches`

ID: `M:TFlex.Model.Model3D.LoftOperation.CountMatches`

Количество соответствий

### `CountSections`

ID: `M:TFlex.Model.Model3D.LoftOperation.CountSections`

Количество сечений

### `GetGuide(System.Int32)`

ID: `M:TFlex.Model.Model3D.LoftOperation.GetGuide(System.Int32)`

Получить направляющую

Parameters:
- `guideIndex`: Индекс направляющей (начинается с 0)

Returns: Свойства направляющей

### `GetMatch(System.Int32)`

ID: `M:TFlex.Model.Model3D.LoftOperation.GetMatch(System.Int32)`

Получить соответствие

Parameters:
- `matchIndex`: Индекс соответствия (начинается с 0)

Returns: Свойства соответствия

### `GetPath`

ID: `M:TFlex.Model.Model3D.LoftOperation.GetPath`

Получить траекторию

Returns: Свойства траектории

### `GetSection(System.Int32)`

ID: `M:TFlex.Model.Model3D.LoftOperation.GetSection(System.Int32)`

Получить сечение

Parameters:
- `sectionIndex`: Индекс сечения (начинается с 0)

Returns: Свойства сечения

### `InsertGuide(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.LoftOperation.InsertGuide(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

Вставить направляющую

Parameters:
- `guideIndex`: Индекс направляющей (начинается с 0)

### `InsertMatch(System.Int32)`

ID: `M:TFlex.Model.Model3D.LoftOperation.InsertMatch(System.Int32)`

Вставить соответствие

Parameters:
- `matchIndex`: Индекс соответствия (начинается с 0)

### `InsertSection(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.LoftOperation.InsertSection(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

Вставить сечение

Parameters:
- `sectionIndex`: Индекс добавляемого сечения (начинается с 0)

### `RemoveGuide(System.Int32)`

ID: `M:TFlex.Model.Model3D.LoftOperation.RemoveGuide(System.Int32)`

Удалить направляющую

Parameters:
- `guideIndex`: Индекс удаляемой направляющей (начинается с 0)

### `RemoveMatch(System.Int32)`

ID: `M:TFlex.Model.Model3D.LoftOperation.RemoveMatch(System.Int32)`

Удалить соответствие

Parameters:
- `matchIndex`: Индекс удаляемого соответствия (начинается с 0)

### `RemoveSection(System.Int32)`

ID: `M:TFlex.Model.Model3D.LoftOperation.RemoveSection(System.Int32)`

Удалить сечение

Parameters:
- `sectionIndex`: Индекс удаляемого сечения (начинается с 0)

## Propertys

### `AutoAlignment`

ID: `P:TFlex.Model.Model3D.LoftOperation.AutoAlignment`

Автовыравнивание

### `Cut`

ID: `P:TFlex.Model.Model3D.LoftOperation.Cut`

Обрезка

### `Faces`

ID: `P:TFlex.Model.Model3D.LoftOperation.Faces`

Грани

### `GroupType`

ID: `P:TFlex.Model.Model3D.LoftOperation.GroupType`

Получить тип объекта

### `GuideAutoReverse`

ID: `P:TFlex.Model.Model3D.LoftOperation.GuideAutoReverse`

Автореверс направляющих

### `Linear`

ID: `P:TFlex.Model.Model3D.LoftOperation.Linear`

Линейчатое тело

### `Periodic`

ID: `P:TFlex.Model.Model3D.LoftOperation.Periodic`

Периодическое тело

Remarks: Данная опция не может быть использована, если задан вырожденный профиль

### `SectionAutoReverse`

ID: `P:TFlex.Model.Model3D.LoftOperation.SectionAutoReverse`

Автореверс сечений

### `Simplify`

ID: `P:TFlex.Model.Model3D.LoftOperation.Simplify`

Упрощённая геометрия

### `Synchronization`

ID: `P:TFlex.Model.Model3D.LoftOperation.Synchronization`

Синхронизировать

### `ThinWall`

ID: `P:TFlex.Model.Model3D.LoftOperation.ThinWall`

Тонкостенный элемент

### `Tolerance`

ID: `P:TFlex.Model.Model3D.LoftOperation.Tolerance`

Точность
