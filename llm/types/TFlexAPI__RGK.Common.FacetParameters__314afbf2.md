# RGK.Common.FacetParameters

Assembly: `TFlexAPI`
Namespace: `RGK.Common`

## Summary

Параметры расчёта сетки

## Constructors

### `FacetParameters(System.Double,System.Double,System.Double,RGK.Generators.Faceter.MeshGeneratorType)`

ID: `M:RGK.Common.FacetParameters.#ctor(System.Double,System.Double,System.Double,RGK.Generators.Faceter.MeshGeneratorType)`

Parameters:
- `iBody`: Тело, для которого необходимо рассчитывать масс-инерционные характеристики
- `iLinearTolerance`: Максимально допустимое линейное уклонение
- `iAngularTolerance`: Максимально допустимое угловое уклонение
- `iChordalMaximumLength`: Максимально допустимая длина хорды

## Methods

### `FacetParameters(System.Double,System.Double,System.Double,RGK.Generators.Faceter.MeshGeneratorType)`

ID: `M:RGK.Common.FacetParameters.#ctor(System.Double,System.Double,System.Double,RGK.Generators.Faceter.MeshGeneratorType)`

Parameters:
- `iBody`: Тело, для которого необходимо рассчитывать масс-инерционные характеристики
- `iLinearTolerance`: Максимально допустимое линейное уклонение
- `iAngularTolerance`: Максимально допустимое угловое уклонение
- `iChordalMaximumLength`: Максимально допустимая длина хорды

### `GetAngularTolerance`

ID: `M:RGK.Common.FacetParameters.GetAngularTolerance`

Returns: Максимально допустимое угловое уклонение

### `GetChordalMaximumLength`

ID: `M:RGK.Common.FacetParameters.GetChordalMaximumLength`

Returns: Максимально допустимая длина хорды

### `GetLinearTolerance`

ID: `M:RGK.Common.FacetParameters.GetLinearTolerance`

Returns: Максимально допустимое линейное уклонение

### `GetMeshGeneratorType`

ID: `M:RGK.Common.FacetParameters.GetMeshGeneratorType`

Returns: Тип сетки

### `Set(System.Double,System.Double,System.Double)`

ID: `M:RGK.Common.FacetParameters.Set(System.Double,System.Double,System.Double)`

Parameters:
- `iLinearTolerance`: Максимально допустимое линейное уклонение
- `iAngularTolerance`: Максимально допустимое угловое уклонение
- `iChodalMaximumLength`: Максимально допустимая длина хорды

### `SetMeshGeneratorType(RGK.Generators.Faceter.MeshGeneratorType)`

ID: `M:RGK.Common.FacetParameters.SetMeshGeneratorType(RGK.Generators.Faceter.MeshGeneratorType)`

Parameters:
- `iMeshGeneratorType`: Тип сетки
