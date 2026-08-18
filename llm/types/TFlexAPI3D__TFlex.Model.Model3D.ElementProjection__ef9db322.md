# TFlex.Model.Model3D.ElementProjection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс создания проекции набора топологических элементов

## Constructors

### `ElementProjection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ElementProjection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `ElementProjection(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.ElementProjection.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

## Methods

### `ElementProjection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ElementProjection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `ElementProjection(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.ElementProjection.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

### `AddBody(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.ElementProjection.AddBody(TFlex.Model.Model3D.Operation)`

Добавить операцию как тело для проецирования

Parameters:
- `operation`: Добавляемая операция

### `AddGeometry(TFlex.Model.Model3D.Geometry.ModelTopol)`

ID: `M:TFlex.Model.Model3D.ElementProjection.AddGeometry(TFlex.Model.Model3D.Geometry.ModelTopol)`

Добавить геометрический объект (грань, ребро, цикл) для проецирования

Parameters:
- `g`: Добавляемый объект

### `AddObject(TFlex.Model.Model3D.Object3D)`

ID: `M:TFlex.Model.Model3D.ElementProjection.AddObject(TFlex.Model.Model3D.Object3D)`

Добавить модельный объект (путь, профиль, операцию) для проецирования

Parameters:
- `o`: Добавляемый объект

### `RemoveAllObjects`

ID: `M:TFlex.Model.Model3D.ElementProjection.RemoveAllObjects`

Удалить все заданные для проецирования объекты из проекции
