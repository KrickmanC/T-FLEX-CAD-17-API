# RGK.Generators.SelfIntersectionError

Assembly: `TFlexAPI`
Namespace: `RGK.Generators`

## Summary

Класс ошибки, связанной с дырками на сетке

## Constructors

### `SelfIntersectionError(std.shared_ptr<RGK.Mesh.SurfaceMesh>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.SelfIntersectionError.#ctor(std.shared_ptr<RGK.Mesh.SurfaceMesh>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMesh`: Сетка

## Methods

### `SelfIntersectionError(std.shared_ptr<RGK.Mesh.SurfaceMesh>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.SelfIntersectionError.#ctor(std.shared_ptr<RGK.Mesh.SurfaceMesh>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMesh`: Сетка

### `GetTriangles(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.SelfIntersectionError.GetTriangles(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `GetType`

ID: `M:RGK.Generators.SelfIntersectionError.GetType`

Returns: Тип ошибки

### `IsComplanar`

ID: `M:RGK.Generators.SelfIntersectionError.IsComplanar`

### `MakeBorder(std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32)`

ID: `M:RGK.Generators.SelfIntersectionError.MakeBorder(std.vector<RGK.Math.Vector3D,std.allocator<RGK.Math.Vector3D>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32)`

Parameters:
- `oBorder`: Полилиния
- `tIndex`: Номер треугольника пересекающегося(1 или 2)
