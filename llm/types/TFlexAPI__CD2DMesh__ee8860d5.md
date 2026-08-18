# CD2DMesh

Assembly: `TFlexAPI`

## Summary

ID2D1Mesh wrapper.

## Constructors

### `CD2DMesh(CRenderTarget*,System.Int32)`

ID: `M:CD2DMesh.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DMesh object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DMesh(CRenderTarget*,System.Int32)`

ID: `M:CD2DMesh.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DMesh object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1Mesh*)`

ID: `M:CD2DMesh.Attach(ID2D1Mesh*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `Create(CRenderTarget*)`

ID: `M:CD2DMesh.Create(CRenderTarget*)`

Creates a CD2DMesh.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DMesh.Destroy`

Destroys a CD2DMesh object.

### `Detach`

ID: `M:CD2DMesh.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DMesh.Dispose`

The destructor. Called when a D2D mesh object is being destroyed.

### `Get`

ID: `M:CD2DMesh.Get`

Returns ID2D1Mesh interface

Returns: Pointer to an ID2D1Mesh interface or NULL if object is not initialized yet.

### `IsValid`

ID: `M:CD2DMesh.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `Open`

ID: `M:CD2DMesh.Open`

Opens the mesh for population.

Returns: A pointer to an ID2D1TessellationSink that is used to populate the mesh.

### `op_Implicit~ID2D1Mesh*`

ID: `M:CD2DMesh.op_Implicit~ID2D1Mesh*`

Returns ID2D1Mesh interface

Returns: Pointer to an ID2D1Mesh interface or NULL if object is not initialized yet.

## Fields

### `m_pMesh`

ID: `F:CD2DMesh.m_pMesh`

A pointer to an ID2D1Mesh.
