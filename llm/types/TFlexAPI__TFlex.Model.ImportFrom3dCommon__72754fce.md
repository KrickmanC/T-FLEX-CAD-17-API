# TFlex.Model.ImportFrom3dCommon

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс импорта из множества популярных форматов CAD-систем(step, acis, iges, SolidWorks, NX, SolidEdge, Creo,...)

## Methods

### `Import(System.String)`

ID: `M:TFlex.Model.ImportFrom3dCommon.Import(System.String)`

Функция импорта файла

Parameters:
- `fileName`: Имя входного файла

Returns: Результат импорта

## Propertys

### `AddBodyRecordsInProductStructure`

ID: `P:TFlex.Model.ImportFrom3dCommon.AddBodyRecordsInProductStructure`

Добавить записи о телах в структуру изделия

### `CheckImportGeomerty`

ID: `P:TFlex.Model.ImportFrom3dCommon.CheckImportGeomerty`

Сделать проверку тел, после импорта

### `CreateAccurateEdges`

ID: `P:TFlex.Model.ImportFrom3dCommon.CreateAccurateEdges`

Строить точные рёбра

### `CreateAssociativeLinks`

ID: `P:TFlex.Model.ImportFrom3dCommon.CreateAssociativeLinks`

Создавать ассоциативные связи

### `DefaultAnnotationFontName`

ID: `P:TFlex.Model.ImportFrom3dCommon.DefaultAnnotationFontName`

Выбор шрифта по умолчанию для текста

### `DefaultUnit`

ID: `P:TFlex.Model.ImportFrom3dCommon.DefaultUnit`

Единица измерения по умолчанию

### `DocumentPrototypePath`

ID: `P:TFlex.Model.ImportFrom3dCommon.DocumentPrototypePath`

Путь к документу, который используется в качестве прототипа

### `Heal`

ID: `P:TFlex.Model.ImportFrom3dCommon.Heal`

Лечение геометрии

### `Import3DNodes`

ID: `P:TFlex.Model.ImportFrom3dCommon.Import3DNodes`

Импортировать облака точек

### `ImportAnotations`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportAnotations`

Импортировать аннотации

### `ImportCoordinateSystems`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportCoordinateSystems`

Импортировать системы координат

### `ImportHideBodies`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportHideBodies`

Импортировать скрытые тела

### `ImportLayers`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportLayers`

Импортировать слои

### `ImportMeshBodies`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportMeshBodies`

Импортировать сеточные тела в виде 3D изображений

### `ImportOnlyFromActiveFilter`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportOnlyFromActiveFilter`

Импортировать тела только с активного слоя

### `ImportPlanes`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportPlanes`

Импортировать плоскости

### `ImportSheetBodies`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportSheetBodies`

Импортировать поверхности

### `ImportSolidBodies`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportSolidBodies`

Импортировать твёрдые тела

### `ImportWireBodies`

ID: `P:TFlex.Model.ImportFrom3dCommon.ImportWireBodies`

Импортировать проволочные тела(кривые)

### `OverrideAnnotationFont`

ID: `P:TFlex.Model.ImportFrom3dCommon.OverrideAnnotationFont`

Переопределить шрифт

### `PathToAssemblyFolder`

ID: `P:TFlex.Model.ImportFrom3dCommon.PathToAssemblyFolder`

Путь к папке, в которую будут сохраняться создаваемые фрагменты в режиме сборки(используются только для типа импорта - сборка)

### `RecognizeAnnotation`

ID: `P:TFlex.Model.ImportFrom3dCommon.RecognizeAnnotation`

Распозновать элементы оформления

### `SewTolerance`

ID: `P:TFlex.Model.ImportFrom3dCommon.SewTolerance`

Точность сшивки в мм

### `Sewing`

ID: `P:TFlex.Model.ImportFrom3dCommon.Sewing`

Сшивка

### `ShowDialog`

ID: `P:TFlex.Model.ImportFrom3dCommon.ShowDialog`

Показывать диалог опций импорта

### `SimplifyGeometry`

ID: `P:TFlex.Model.ImportFrom3dCommon.SimplifyGeometry`

Упрощать геометрию

### `UpdateProductStructure`

ID: `P:TFlex.Model.ImportFrom3dCommon.UpdateProductStructure`

Обновить структуру изделия

## Fields

### `Configurations`

ID: `F:TFlex.Model.ImportFrom3dCommon.Configurations`

Импортировать исполнения

### `Mode`

ID: `F:TFlex.Model.ImportFrom3dCommon.Mode`

Тип импорта
