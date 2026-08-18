# CD2DResource

Assembly: `TFlexCommandAPI`

## Summary

An abstract class, which provides a interface for creating and managing D2D resources such as brushes, layers and texts.

## Constructors

### `CD2DResource(CRenderTarget*,System.Int32)`

ID: `M:CD2DResource.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DResource object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DResource(CRenderTarget*,System.Int32)`

ID: `M:CD2DResource.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DResource object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Create(CRenderTarget*)`

ID: `M:CD2DResource.Create(CRenderTarget*)`

Creates a CD2DResource.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DResource.Destroy`

Destroys a CD2DResource object.

### `Dispose`

ID: `M:CD2DResource.Dispose`

The destructor. Called when a D2D resource object is being destroyed.

### `IsAutoDestroy`

ID: `M:CD2DResource.IsAutoDestroy`

Check auto destroy flag.

Returns: TRUE if the object will be destroyed by its owner; otherwise FALSE.

### `IsValid`

ID: `M:CD2DResource.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `ReCreate(CRenderTarget*)`

ID: `M:CD2DResource.ReCreate(CRenderTarget*)`

Re-creates a CD2DResource.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Fields

### `m_bIsAutoDestroy`

ID: `F:CD2DResource.m_bIsAutoDestroy`

Resource will be destoyed by owner (CRenderTarget)

### `m_pParentTarget`

ID: `F:CD2DResource.m_pParentTarget`

Pointer to the parent CRenderTarget)
