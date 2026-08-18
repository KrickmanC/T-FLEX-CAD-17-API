# CDCRenderTarget

Assembly: `TFlexAPI3D`

## Summary

ID2D1DCRenderTarget wrapper.

## Constructors

### `CDCRenderTarget`

ID: `M:CDCRenderTarget.#ctor`

Constructs a CDCRenderTarget object.

## Methods

### `CDCRenderTarget`

ID: `M:CDCRenderTarget.#ctor`

Constructs a CDCRenderTarget object.

### `Attach(ID2D1DCRenderTarget*)`

ID: `M:CDCRenderTarget.Attach(ID2D1DCRenderTarget*)`

Attaches existing render target interface to the object

Parameters:
- `pTarget`: Existing render target interface. Cannot be NULL

### `BindDC(CDC!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CDCRenderTarget.BindDC(CDC!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Binds the render target to the device context to which it issues drawing commands

Parameters:
- `dc`: The device context to which the render target issues drawing commands
- `rect`: The dimensions of the handle to a device context (HDC) to which the render target is bound

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Create(D2D1_RENDER_TARGET_PROPERTIES!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CDCRenderTarget.Create(D2D1_RENDER_TARGET_PROPERTIES!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Creates a CDCRenderTarget.

Parameters:
- `props`: The rendering mode, pixel format, remoting options, DPI information, and the minimum DirectX support required for hardware rendering.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Detach`

ID: `M:CDCRenderTarget.Detach`

Detaches render target interface from the object

Returns: Pointer to detached render target interface.

### `GetDCRenderTarget`

ID: `M:CDCRenderTarget.GetDCRenderTarget`

Returns ID2D1DCRenderTarget interface

Returns: Pointer to an ID2D1DCRenderTarget interface or NULL if object is not initialized yet.

### `op_Implicit~ID2D1DCRenderTarget*`

ID: `M:CDCRenderTarget.op_Implicit~ID2D1DCRenderTarget*`

Returns ID2D1DCRenderTarget interface

Returns: Pointer to an ID2D1DCRenderTarget interface or NULL if object is not initialized yet.

## Fields

### `m_pDCRenderTarget`

ID: `F:CDCRenderTarget.m_pDCRenderTarget`

A pointer to an ID2D1DCRenderTarget object.
