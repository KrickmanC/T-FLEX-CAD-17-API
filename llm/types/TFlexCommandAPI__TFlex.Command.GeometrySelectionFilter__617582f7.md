# TFlex.Command.GeometrySelectionFilter

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Command`

## Summary

Фильтр, позволяющий выбирать или не выбирать геометрию объектов

## Constructors

### `GeometrySelectionFilter`

ID: `M:TFlex.Command.GeometrySelectionFilter.#ctor`

Конструктор. По умолчанию устанавливается выбор всех типов объектов и геометрии

## Methods

### `GeometrySelectionFilter`

ID: `M:TFlex.Command.GeometrySelectionFilter.#ctor`

Конструктор. По умолчанию устанавливается выбор всех типов объектов и геометрии

### `Disable(TFlex.Command.SelectableGeometryType)`

ID: `M:TFlex.Command.GeometrySelectionFilter.Disable(TFlex.Command.SelectableGeometryType)`

Запретить выбор геометрии указанного типа

Parameters:
- `type`: Тип геометрии

### `Enable(TFlex.Command.SelectableGeometryType)`

ID: `M:TFlex.Command.GeometrySelectionFilter.Enable(TFlex.Command.SelectableGeometryType)`

Разрешить выбор геометрии указанного типа

Parameters:
- `type`: Тип геометрии
