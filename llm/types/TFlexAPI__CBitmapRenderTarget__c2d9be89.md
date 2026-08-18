# CBitmapRenderTarget

Assembly: `TFlexAPI`

## Constructors

### `CBitmapRenderTarget`

ID: `M:CBitmapRenderTarget.#ctor`

Constructs a CBitmapRenderTarget object.

## Methods

### `CBitmapRenderTarget`

ID: `M:CBitmapRenderTarget.#ctor`

Constructs a CBitmapRenderTarget object.

### `Attach(ID2D1BitmapRenderTarget*)`

ID: `M:CBitmapRenderTarget.Attach(ID2D1BitmapRenderTarget*)`

Attaches existing render target interface to the object

Parameters:
- `pTarget`: Existing render target interface. Cannot be NULL

### `Detach`

ID: `M:CBitmapRenderTarget.Detach`

Detaches render target interface from the object

Returns: Pointer to detached render target interface.

### `GetBitmap(CD2DBitmap*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CBitmapRenderTarget.GetBitmap(CD2DBitmap*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Retrieves the bitmap for this render target. The returned bitmap can be used for drawing operations.

Parameters:
- `bitmap`: When this method returns, contains the valid bitmap for this render target. This bitmap can be used for drawing operations.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `GetBitmapRenderTarget`

ID: `M:CBitmapRenderTarget.GetBitmapRenderTarget`

Returns ID2D1BitmapRenderTarget interface

Returns: Pointer to an ID2D1BitmapRenderTarget interface or NULL if object is not initialized yet.

### `op_Implicit~ID2D1BitmapRenderTarget*`

ID: `M:CBitmapRenderTarget.op_Implicit~ID2D1BitmapRenderTarget*`

Returns ID2D1BitmapRenderTarget interface

Returns: Pointer to an ID2D1BitmapRenderTarget interface or NULL if object is not initialized yet.

## Fields

### `m_pBitmapRenderTarget`

ID: `F:CBitmapRenderTarget.m_pBitmapRenderTarget`

A pointer to an ID2D1BitmapRenderTarget object.
