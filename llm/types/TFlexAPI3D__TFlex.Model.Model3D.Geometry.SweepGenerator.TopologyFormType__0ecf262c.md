# TFlex.Model.Model3D.Geometry.SweepGenerator.TopologyFormType

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SweepGenerator`

## Summary

Тип разбиения результирующего тела на грани

## Fields

### `Columns`

ID: `F:TFlex.Model.Model3D.Geometry.SweepGenerator.TopologyFormType.Columns`

Столбики граней, соответствующие рёбрам образующего контура

### `Grid`

ID: `F:TFlex.Model.Model3D.Geometry.SweepGenerator.TopologyFormType.Grid`

Решётка граней. Каждому ребру образующего контура соответствует набор граней в направлении траектории. Количество граней больше или равно по сравнению с типом разбиения Columns, так как дополнительные рёбра создаются для каждой вершины траектории, за исключением вершин, добавленных в список игнорируемых вершин.

### `Minimal`

ID: `F:TFlex.Model.Model3D.Geometry.SweepGenerator.TopologyFormType.Minimal`

Минимальное количество граней
