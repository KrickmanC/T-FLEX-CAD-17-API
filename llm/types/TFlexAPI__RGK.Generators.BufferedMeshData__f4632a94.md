# RGK.Generators.BufferedMeshData

Assembly: `TFlexAPI`
Namespace: `RGK.Generators`

## Summary

Класс хранения сетки в формате типизированных буферов

## Constructors

### `BufferedMeshData`

ID: `M:RGK.Generators.BufferedMeshData.#ctor`

## Methods

### `BufferedMeshData`

ID: `M:RGK.Generators.BufferedMeshData.#ctor`

### `AddVertexDeclaration(RGK.Generators.BufferedMeshData.VertexDeclaration!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BufferedMeshData.AddVertexDeclaration(RGK.Generators.BufferedMeshData.VertexDeclaration!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVertexDeclaration`: Описание вершинных данных

### `Dispose`

ID: `M:RGK.Generators.BufferedMeshData.Dispose`

### `GetEdgeAssoc`

ID: `M:RGK.Generators.BufferedMeshData.GetEdgeAssoc`

### `GetEdgeIndexBuffer`

ID: `M:RGK.Generators.BufferedMeshData.GetEdgeIndexBuffer`

### `GetEdgeIndexDataType`

ID: `M:RGK.Generators.BufferedMeshData.GetEdgeIndexDataType`

### `GetFaceAssoc`

ID: `M:RGK.Generators.BufferedMeshData.GetFaceAssoc`

### `GetFaceIndexBuffer`

ID: `M:RGK.Generators.BufferedMeshData.GetFaceIndexBuffer`

### `GetFaceIndexDataType`

ID: `M:RGK.Generators.BufferedMeshData.GetFaceIndexDataType`

### `GetVertexBuffer(RGK.Generators.BufferedMeshData.VertexDeclaration.VertexDataType)`

ID: `M:RGK.Generators.BufferedMeshData.GetVertexBuffer(RGK.Generators.BufferedMeshData.VertexDeclaration.VertexDataType)`

Parameters:
- `iVertexDataType`: Тип данных, для которых запрашивается буфер

### `GetVertexDeclaration`

ID: `M:RGK.Generators.BufferedMeshData.GetVertexDeclaration`

### `SetEdgeIndexDeclaration(std.shared_ptr<RGK.Generators.MeshBuffer>,RGK.Generators.BufferedMeshData.EdgeIndexDataType,std.shared_ptr<RGK.Generators.BufferedMeshData.AssocTopolArray>)`

ID: `M:RGK.Generators.BufferedMeshData.SetEdgeIndexDeclaration(std.shared_ptr<RGK.Generators.MeshBuffer>,RGK.Generators.BufferedMeshData.EdgeIndexDataType,std.shared_ptr<RGK.Generators.BufferedMeshData.AssocTopolArray>)`

Parameters:
- `iBuffer`: Буфер, в который пишутся данные
- `iType`: Тип индексных данных, которые пишутся в буфер
- `iAssoc`: Буфер для хранения информации о связи рёбер с индексными данными

### `SetFaceIndexDeclaration(std.shared_ptr<RGK.Generators.MeshBuffer>,RGK.Generators.BufferedMeshData.FaceIndexDataType,std.shared_ptr<RGK.Generators.BufferedMeshData.AssocTopolArray>)`

ID: `M:RGK.Generators.BufferedMeshData.SetFaceIndexDeclaration(std.shared_ptr<RGK.Generators.MeshBuffer>,RGK.Generators.BufferedMeshData.FaceIndexDataType,std.shared_ptr<RGK.Generators.BufferedMeshData.AssocTopolArray>)`

Parameters:
- `iBuffer`: Буфер, в который пишутся данные
- `iType`: Тип индексных данных, которые пишутся в буфер
- `iAssoc`: Буфер для хранения информации о связи граней с индексными данными

## Members

### `AssocTopolArrayPtr`

ID: `D:RGK.Generators.BufferedMeshData.AssocTopolArrayPtr`
