# TFlex.Model.Model3D.Projection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех типов проекций

## Constructors

### `Projection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Projection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `Projection(TFlex.Model.Document,System.Boolean,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Projection.#ctor(TFlex.Model.Document,System.Boolean,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

## Methods

### `Projection(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Projection.#ctor(TFlex.Model.Document)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Проекция создаётся на активной странице

### `Projection(TFlex.Model.Document,System.Boolean,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.Projection.#ctor(TFlex.Model.Document,System.Boolean,TFlex.Model.Page)`

Конструктор для создания новой проекции

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся проекция

### `AddBreak(System.Boolean,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Projection.AddBreak(System.Boolean,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Метод для добавления информации о новом разрыве в список

Parameters:
- `norm`: Ориентация разрыва
- `begin`: Параметр начала разрыва
- `end`: Параметр конца разрыва

### `Complete`

ID: `M:TFlex.Model.Model3D.Projection.Complete`

Для внутреннего использования

### `DeleteAllBreaks`

ID: `M:TFlex.Model.Model3D.Projection.DeleteAllBreaks`

Удаление всех разрывов

### `DeleteBreak(System.Int32)`

ID: `M:TFlex.Model.Model3D.Projection.DeleteBreak(System.Int32)`

Удаление разрыва

Parameters:
- `i`: Номер разрыва

### `Explode`

ID: `M:TFlex.Model.Model3D.Projection.Explode`

Разрушить проекцию

### `FromFile(System.String,System.String)`

ID: `M:TFlex.Model.Model3D.Projection.FromFile(System.String,System.String)`

Создание проекции из файла

Returns: Возвращает true - если файл по указанному пути может быть использован для проецирования

### `GetBrokenSize`

ID: `M:TFlex.Model.Model3D.Projection.GetBrokenSize`

Метод для получения размера массива разрывов

Returns: Получить количество разрывов

### `GetProjectedPoint(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.Projection.GetProjectedPoint(TFlex.Model.Model3D.Geometry.Point3D)`

Функция возвращает 3D точку по точке на проекции

Returns: Функция возвращает NULL когда проекция не рассчитана

### `GetProjectionTransform`

ID: `M:TFlex.Model.Model3D.Projection.GetProjectionTransform`

Функция возвращает матрицу преобразования точки в 3d пространстве в систему координат проекции

Returns: Функция возвращает NULL когда проекция не рассчитана

### `GetViewPoint`

ID: `M:TFlex.Model.Model3D.Projection.GetViewPoint`

Опросить координаты точки проецирования

Returns: Функция возвращает false когда точка взгляда проекции не рассчитана

### `ProjectPoint(TFlex.Model.Model3D.Geometry.Point3D)`

ID: `M:TFlex.Model.Model3D.Projection.ProjectPoint(TFlex.Model.Model3D.Geometry.Point3D)`

Функция проецирует данную точку на проекцию

Returns: Функция возвращает NULL когда проекция не рассчитана

### `Regenerate(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Projection.Regenerate(System.Boolean)`

Пометить объект как изменённый

### `ScaleFitToPageSize(System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Projection.ScaleFitToPageSize(System.Double,System.Double)`

Подбор масшатаба для проекции, чтобы умещаться на странице

Returns: Возвращает отрицательное значение, если не удалось подобрать масштаб

### `SetBegin(System.Int32,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Projection.SetBegin(System.Int32,TFlex.Model.Parameter)`

Установка начального отступа разрыва

Parameters:
- `i`: Номер разрыва
- `begin`: Значение начального отступа разрыва

### `SetConfiguration(System.String,System.String)`

ID: `M:TFlex.Model.Model3D.Projection.SetConfiguration(System.String,System.String)`

Установить имя конфигурации

Parameters:
- `version`: Версия
- `displayName`: Имя конфигурации

### `SetEnd(System.Int32,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Projection.SetEnd(System.Int32,TFlex.Model.Parameter)`

Установка конечного отступа разрыва

Parameters:
- `i`: Номер разрыва
- `end`: Значение конечного отступа разрыва

### `SetNormal(System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Projection.SetNormal(System.Int32,System.Boolean)`

Установка ориентации разрыва

Parameters:
- `i`: Номер разрыва
- `norm`: Ориентация разрыва

### `SetTieNode(TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model3D.Projection.SetTieNode(TFlex.Model.Model2D.Node)`

Установить привязку проекции в соответствующий узел страницы

Parameters:
- `nfix`: Узел привязки проекции

### `SetTiePoint(System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Projection.SetTiePoint(System.Double,System.Double)`

Установить привязку проекции в соответствующую точку страницы

Parameters:
- `x1`: Координата x точки привязки проекции
- `y1`: Координата y точки привязки проекции

### `SetViewType(TFlex.Model.Model3D.ProjectionType)`

ID: `M:TFlex.Model.Model3D.Projection.SetViewType(TFlex.Model.Model3D.ProjectionType)`

Установить направление проецирования для стандартных видов

Parameters:
- `type`: Значение направления проецирования

### `SetViewWorkplane(TFlex.Model.Model3D.Workplane)`

ID: `M:TFlex.Model.Model3D.Projection.SetViewWorkplane(TFlex.Model.Model3D.Workplane)`

Установить направление проецирования как нормаль к рабочей плоскости

Parameters:
- `wp`: Рабочая плоскость для задания направления проецирования

## Propertys

### `Angle`

ID: `P:TFlex.Model.Model3D.Projection.Angle`

Угол поворота проекции

### `Bind`

ID: `P:TFlex.Model.Model3D.Projection.Bind`

Проекция с которой берётся проекционная связь

### `BoundRect`

ID: `P:TFlex.Model.Model3D.Projection.BoundRect`

Ограничивающий прямоугольник проекции

### `BrokenAmplitude`

ID: `P:TFlex.Model.Model3D.Projection.BrokenAmplitude`

Амплитуда линии разрыва

### `BrokenAngle`

ID: `P:TFlex.Model.Model3D.Projection.BrokenAngle`

Угол поворота набора линий разрыва

### `BrokenBorder`

ID: `P:TFlex.Model.Model3D.Projection.BrokenBorder`

Длина выносной линии

### `BrokenHAlign`

ID: `P:TFlex.Model.Model3D.Projection.BrokenHAlign`

Тип горизонтального выравнивания

### `BrokenLength`

ID: `P:TFlex.Model.Model3D.Projection.BrokenLength`

Длина полупериода волны линии разрыва

### `BrokenLineColor`

ID: `P:TFlex.Model.Model3D.Projection.BrokenLineColor`

Цвет линий разрыва

### `BrokenLineDistance`

ID: `P:TFlex.Model.Model3D.Projection.BrokenLineDistance`

Расстояние между линиями разрыва

### `BrokenLineName`

ID: `P:TFlex.Model.Model3D.Projection.BrokenLineName`

Имя типа линий разрыва

### `BrokenLineScale`

ID: `P:TFlex.Model.Model3D.Projection.BrokenLineScale`

Масштаб линий разрыва

### `BrokenLineWidth`

ID: `P:TFlex.Model.Model3D.Projection.BrokenLineWidth`

Толщина линий разрыва

### `BrokenMetric`

ID: `P:TFlex.Model.Model3D.Projection.BrokenMetric`

Единицы измерения величины разрыва

### `BrokenType`

ID: `P:TFlex.Model.Model3D.Projection.BrokenType`

Тип линии разрыва

### `BrokenVAlign`

ID: `P:TFlex.Model.Model3D.Projection.BrokenVAlign`

Тип вертикального выравнивания

### `FileLink`

ID: `P:TFlex.Model.Model3D.Projection.FileLink`

Ссылка на файл, из которого берутся проецируемые элементы

### `GroupType`

ID: `P:TFlex.Model.Model3D.Projection.GroupType`

Тип объекта

### `Layers`

ID: `P:TFlex.Model.Model3D.Projection.Layers`

Множество слоёв

### `Page`

ID: `P:TFlex.Model.Model3D.Projection.Page`

Страница, где отображается проекция

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Save3DDim`

ID: `P:TFlex.Model.Model3D.Projection.Save3DDim`

Сохранять информацию для 3D размеров

### `Scale`

ID: `P:TFlex.Model.Model3D.Projection.Scale`

Масштаб проекции

### `SourcePage`

ID: `P:TFlex.Model.Model3D.Projection.SourcePage`

Исходная страница проекции
