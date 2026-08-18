# CHwndRenderTarget

Assembly: `TFlexCommandAPI`

## Summary

ID2D1HwndRenderTarget wrapper.

## Constructors

### `CHwndRenderTarget(HWND__*)`

ID: `M:CHwndRenderTarget.#ctor(HWND__*)`

Constructs a CHwndRenderTarget object from HWND.

Parameters:
- `hwnd`: The HWND associated with this render target

## Methods

### `CHwndRenderTarget(HWND__*)`

ID: `M:CHwndRenderTarget.#ctor(HWND__*)`

Constructs a CHwndRenderTarget object from HWND.

Parameters:
- `hwnd`: The HWND associated with this render target

### `Attach(ID2D1HwndRenderTarget*)`

ID: `M:CHwndRenderTarget.Attach(ID2D1HwndRenderTarget*)`

Attaches existing render target interface to the object

Parameters:
- `pTarget`: Existing render target interface. Cannot be NULL

### `CheckWindowState`

ID: `M:CHwndRenderTarget.CheckWindowState`

Indicates whether the HWND associated with this render target is occluded.

Returns: A value that indicates whether the HWND associated with this render target is occluded.

### `Create(HWND__*)`

ID: `M:CHwndRenderTarget.Create(HWND__*)`

Creates a render target associated with the window

Parameters:
- `hWnd`: The HWND associated with this render target

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE

### `Detach`

ID: `M:CHwndRenderTarget.Detach`

Detaches render target interface from the object

Returns: Pointer to detached render target interface.

### `GetHwnd`

ID: `M:CHwndRenderTarget.GetHwnd`

Returns the HWND associated with this render target.

Returns: The HWND associated with this render target.

### `GetHwndRenderTarget`

ID: `M:CHwndRenderTarget.GetHwndRenderTarget`

Returns ID2D1HwndRenderTarget interface.

Returns: Pointer to an ID2D1HwndRenderTarget interface or NULL if object is not initialized yet.

### `ReCreate(HWND__*)`

ID: `M:CHwndRenderTarget.ReCreate(HWND__*)`

Re-creates a render target associated with the window

Parameters:
- `hWnd`: The HWND associated with this render target

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Resize(CD2DSizeU!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CHwndRenderTarget.Resize(CD2DSizeU!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Changes the size of the render target to the specified pixel size

Parameters:
- `size`: The new size of the render target in device pixels

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `op_Implicit~ID2D1HwndRenderTarget*`

ID: `M:CHwndRenderTarget.op_Implicit~ID2D1HwndRenderTarget*`

Returns ID2D1HwndRenderTarget interface.

Returns: Pointer to an ID2D1HwndRenderTarget interface or NULL if object is not initialized yet.

## Fields

### `m_pHwndRenderTarget`

ID: `F:CHwndRenderTarget.m_pHwndRenderTarget`

A pointer to an ID2D1HwndRenderTarget object.
