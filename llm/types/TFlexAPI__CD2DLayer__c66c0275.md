# CD2DLayer

Assembly: `TFlexAPI`

## Summary

ID2D1Layer wrapper.

## Constructors

### `CD2DLayer(CRenderTarget*,System.Int32)`

ID: `M:CD2DLayer.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DLayer object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DLayer(CRenderTarget*,System.Int32)`

ID: `M:CD2DLayer.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DLayer object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1Layer*)`

ID: `M:CD2DLayer.Attach(ID2D1Layer*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `Create(CRenderTarget*)`

ID: `M:CD2DLayer.Create(CRenderTarget*)`

Creates a CD2DLayer.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DLayer.Destroy`

Destroys a CD2DLayer object.

### `Detach`

ID: `M:CD2DLayer.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DLayer.Dispose`

The destructor. Called when a D2D layer object is being destroyed.

### `Get`

ID: `M:CD2DLayer.Get`

Returns ID2D1Layer interface

Returns: Pointer to an ID2D1Layer interface or NULL if object is not initialized yet.

### `GetSize`

ID: `M:CD2DLayer.GetSize`

Returns the size of the render target in device-independent pixels

Returns: The current size of the render target in device-independent pixels

### `IsValid`

ID: `M:CD2DLayer.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `op_Implicit~ID2D1Layer*`

ID: `M:CD2DLayer.op_Implicit~ID2D1Layer*`

Returns ID2D1Layer interface

Returns: Pointer to an ID2D1Layer interface or NULL if object is not initialized yet.

## Fields

### `m_pLayer`

ID: `F:CD2DLayer.m_pLayer`

Stores a pointer to an ID2D1Layer object.
