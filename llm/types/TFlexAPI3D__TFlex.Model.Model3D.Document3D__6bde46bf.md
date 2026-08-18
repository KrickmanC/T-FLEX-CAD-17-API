# TFlex.Model.Model3D.Document3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Methods

### `ClearUdfParameters(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.ClearUdfParameters(TFlex.Model.Document)`

Очистить адаптивные параметры

### `Get3DWelds(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.Get3DWelds(TFlex.Model.Document)`

Контейнер 3D-сварных швов

### `GetAssemblyContextData3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetAssemblyContextData3D(TFlex.Model.Document)`

### `GetBends(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetBends(TFlex.Model.Document)`

Контейнер операций гибки

### `GetBooleans(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetBooleans(TFlex.Model.Document)`

Контейнер булевых операций

### `GetCAEStudies(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetCAEStudies(TFlex.Model.Document)`

Контейнер конечно-элементных задач модели

### `GetCameras(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetCameras(TFlex.Model.Document)`

Контейнер камер

### `GetCircularArrays(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetCircularArrays(TFlex.Model.Document)`

Контейнер операций "Круговой массив"

### `GetCopyOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetCopyOperations(TFlex.Model.Document)`

Контейнер операций копирования в T-Flex CAD до версии 11

### `GetCopyOperations2(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetCopyOperations2(TFlex.Model.Document)`

Контейнер операций копирования

### `GetCountTopologyReferences(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetCountTopologyReferences(TFlex.Model.Document)`

Количество топологических ссылок

### `GetCutOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetCutOperations(TFlex.Model.Document)`

Контейнер операций отсечения

### `GetDynamicStudies(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetDynamicStudies(TFlex.Model.Document)`

Контейнер динамических задач модели

### `GetEdgeBlendings(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetEdgeBlendings(TFlex.Model.Document)`

Контейнер операций сглаживания рёбер

### `GetExternalOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetExternalOperations(TFlex.Model.Document)`

Получить контейнер внешних операций документа

Parameters:
- `document`: Документ

### `GetExternalOperations(TFlex.Model.Document,System.Int32)`

ID: `M:TFlex.Model.Model3D.Document3D.GetExternalOperations(TFlex.Model.Document,System.Int32)`

Получить контейнер внешних операций документа

Parameters:
- `document`: Документ
- `typeId`: Пользовательский идентификатор типа объекта

### `GetExtrusions(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetExtrusions(TFlex.Model.Document)`

Контейнер операций выталкивания

### `GetFaceBlendings(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetFaceBlendings(TFlex.Model.Document)`

Контейнер операций сглаживания граней

### `GetFacesByPoint(TFlex.Model.Document,TFlex.Model.Model3D.Geometry.BasePoint3D,System.Collections.Generic.IList`1{TFlex.Model.Model3D.Operation})`

ID: `M:TFlex.Model.Model3D.Document3D.GetFacesByPoint(TFlex.Model.Document,TFlex.Model.Model3D.Geometry.BasePoint3D,System.Collections.Generic.IList`1{TFlex.Model.Model3D.Operation})`

Получить коллекцию граней, расположенных наиболее близко к заданной точке

Parameters:
- `point3D`: Точка, относительно которой будет выполняться поиск
- `operations`: Операции, для которых будет выполняться поиск

Returns: Коллекция граней

### `GetFillHoleOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetFillHoleOperations(TFlex.Model.Document)`

Контейнер операций "Заполнение области"

### `GetFragments3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetFragments3D(TFlex.Model.Document)`

Контейнер 3D фрагментов

### `GetHarnesses(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetHarnesses(TFlex.Model.Document)`

Контейнер жгутов

### `GetHoles(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetHoles(TFlex.Model.Document)`

Контейнер отверстий

### `GetImportedOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetImportedOperations(TFlex.Model.Document)`

Контейнер операций "Внешняя модель"

### `GetLCSs(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetLCSs(TFlex.Model.Document)`

Контейнер локальных систем координат (ЛСК)

### `GetLights(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetLights(TFlex.Model.Document)`

Контейнер источников света

### `GetLinearArrays(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetLinearArrays(TFlex.Model.Document)`

Контейнер операций "Линейный массив"

### `GetLoftOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetLoftOperations(TFlex.Model.Document)`

Контейнер операций "По сечениям"

### `GetLofts(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetLofts(TFlex.Model.Document)`

Контейнер операций "По сечениям"

### `GetMaterials(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetMaterials(TFlex.Model.Document)`

Контейнер материалов

### `GetMates(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetMates(TFlex.Model.Document)`

Контейнер всех сопряжений

### `GetModel3DObjectGroups(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetModel3DObjectGroups(TFlex.Model.Document)`

Контейнер групп объектов 3D модели

### `GetNodeArrays(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetNodeArrays(TFlex.Model.Document)`

Контейнер операций "Массив по точкам"

### `GetNodes3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetNodes3D(TFlex.Model.Document)`

Контейнер 3D узлов

### `GetOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetOperations(TFlex.Model.Document)`

Контейнер всех операций

### `GetParametricArrays(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetParametricArrays(TFlex.Model.Document)`

Контейнер операций "Параметрических массив"

### `GetPathArrays(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetPathArrays(TFlex.Model.Document)`

Контейнер операций "Массив по пути"

### `GetPaths3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetPaths3D(TFlex.Model.Document)`

Контейнер 3D путей

### `GetPictures3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetPictures3D(TFlex.Model.Document)`

Контейнер 3D картинок

### `GetPipes(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetPipes(TFlex.Model.Document)`

Контейнер операций "Трубопровод"

### `GetProfiles(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetProfiles(TFlex.Model.Document)`

Контейнер 3D профилей

### `GetProjections(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetProjections(TFlex.Model.Document)`

Контейнер проекций

### `GetRebends(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetRebends(TFlex.Model.Document)`

Контейнер операций повторной гибки

### `GetReferenceWorkplanes(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetReferenceWorkplanes(TFlex.Model.Document)`

Контейнер ссылочных рабочих плоскостей

### `GetRestraints(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetRestraints(TFlex.Model.Document)`

Контейнер граничных условий

### `GetRotations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetRotations(TFlex.Model.Document)`

Контейнер операций вращения

### `GetScenarios(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetScenarios(TFlex.Model.Document)`

Контейнер сценариев разборки

### `GetSections(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSections(TFlex.Model.Document)`

Контейнер сечений

### `GetSensors(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSensors(TFlex.Model.Document)`

Контейнер датчиков

### `GetSeparations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSeparations(TFlex.Model.Document)`

Контейнер операций разделения

### `GetSews(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSews(TFlex.Model.Document)`

Контейнер операций сшивки

### `GetSheetMetalFeatures(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSheetMetalFeatures(TFlex.Model.Document)`

Контейнер операций выштамповки

### `GetSheetMetalParts(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSheetMetalParts(TFlex.Model.Document)`

Контейнер заготовок для гибки

### `GetShells(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetShells(TFlex.Model.Document)`

Контейнер оболочек

### `GetSpirals(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSpirals(TFlex.Model.Document)`

Контейнер операций "Спираль"

### `GetSprings(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSprings(TFlex.Model.Document)`

Контейнер операций "Пружина"

### `GetSwepts(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSwepts(TFlex.Model.Document)`

Контейнер операций "По траектории"

### `GetSymmetryOperations(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSymmetryOperations(TFlex.Model.Document)`

Контейнер операций симметрии в T-Flex CAD до версии 11

### `GetSymmetryOperations2(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetSymmetryOperations2(TFlex.Model.Document)`

Контейнер операций симметрии

### `GetTapers(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetTapers(TFlex.Model.Document)`

Контейнер операций уклона

### `GetThreads(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetThreads(TFlex.Model.Document)`

Контейнер операций "Резьба"

### `GetThreeFaceBlendings(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetThreeFaceBlendings(TFlex.Model.Document)`

Контейнер операций сглаживания трёх граней

### `GetTopologyReferenceCount(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetTopologyReferenceCount(TFlex.Model.Document)`

Количество топологических ссылок

### `GetUnbends(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetUnbends(TFlex.Model.Document)`

Контейнер операций разгибания

### `GetWorkSurfaces(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetWorkSurfaces(TFlex.Model.Document)`

Контейнер рабочих поверхностей

### `GetWorkplanes(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Document3D.GetWorkplanes(TFlex.Model.Document)`

Контейнер рабочих плоскостей
