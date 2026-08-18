# TFlex.Model.Model3D.SimpleDrawingProjection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс стандартных видов проекций

## Constructors

### `SimpleDrawingProjection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `SimpleDrawingProjection(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

## Methods

### `SimpleDrawingProjection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `SimpleDrawingProjection(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

### `AddBody(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.AddBody(TFlex.Model.Model3D.Operation)`

Добавить операцию как тело для проецирования

Parameters:
- `operation`: Добавляемая операция

### `AddOperation(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.AddOperation(TFlex.Model.Model3D.Operation)`

Добавить операцию для проецирования

Parameters:
- `oper`: Добавляемая операция

### `GetEdgeMode`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.GetEdgeMode`

Опрос режима отрисовки рёбер в растровых проекциях

### `GetOutlineMode`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.GetOutlineMode`

Опрос режима отрисовки очерка в растровых проекциях

### `RemoveAllOperations`

ID: `M:TFlex.Model.Model3D.SimpleDrawingProjection.RemoveAllOperations`

Сбросить все проецируемые операции

## Propertys

### `AxisCreate`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.AxisCreate`

Признак режима создания осей

### `AxisLineColor`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.AxisLineColor`

Цвет осевых линий

### `AxisLineName`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.AxisLineName`

Имя типа осевых линий

### `AxisLineScale`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.AxisLineScale`

Масштаб осевых линий

### `AxisLineWidth`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.AxisLineWidth`

Толщина осевых линий

### `ConvertPolylinesToSplines`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.ConvertPolylinesToSplines`

Признак режима конвертации полилиний в сплайны

### `CreateHidden`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.CreateHidden`

Признак режима создания изображений с невидимыми линиями

### `CreateSection`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.CreateSection`

Признак режима создания изображений с линиями сечений

### `CreateTangentEdges`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.CreateTangentEdges`

Режим создания изображений с показом гладких сопряжений

### `CreateThreads`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.CreateThreads`

Признак режима создания изображений резьб

### `Explode`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.Explode`

Признак режима разборки

### `HiddenLineColor`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.HiddenLineColor`

Цвет невидимых линий

### `HiddenLineWidth`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.HiddenLineWidth`

Толщина невидимых линий

### `Monochrome`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.Monochrome`

Признак использования одного цвета на всей проекции

### `OverlapBodies`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.OverlapBodies`

Режим учёта перекрытия тел при проецировании

### `Perspective`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.Perspective`

Перспективная проекция

### `ProjectPrecision`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.ProjectPrecision`

Получить значение точности проецирования

### `ProjectionClass`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.ProjectionClass`

Тип проекции

### `RecognizeCircles`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.RecognizeCircles`

Признак режима распознавания дуг окружностей

### `RecognizeLines`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.RecognizeLines`

Признак режима распознавания отрезков

### `RegenerationMode`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.RegenerationMode`

Режим регенерации проекции

### `SmoothLineColor`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.SmoothLineColor`

Цвет линий гладких сопряжений

### `SmoothLineName`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.SmoothLineName`

Имя типа видимых линий гладких сопряжений

### `SmoothLineScale`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.SmoothLineScale`

Масштаб линий гладких сопряжений

### `SmoothLineWidth`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.SmoothLineWidth`

Толщина линий гладких сопряжений

### `ThreadLineColor`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.ThreadLineColor`

Цвет линий резьбы

### `ThreadLineName`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.ThreadLineName`

Имя типа линий резьбы

### `ThreadLineScale`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.ThreadLineScale`

Масштаб линий резьбы

### `ThreadLineWidth`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.ThreadLineWidth`

Толщина линий резьбы

### `VisibleLineColor`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.VisibleLineColor`

Цвет видимых линий

### `VisibleLineName`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.VisibleLineName`

Имя типа видимых линий

### `VisibleLineScale`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.VisibleLineScale`

Масштаб видимых линий

### `VisibleLineWidth`

ID: `P:TFlex.Model.Model3D.SimpleDrawingProjection.VisibleLineWidth`

Толщина видимых линий
