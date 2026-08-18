# CD2DBitmap

Assembly: `TFlexCommandAPI`

## Summary

ID2D1Bitmap wrapper.

## Constructors

### `CD2DBitmap(CRenderTarget*,HBITMAP__*,CD2DSizeU,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,HBITMAP__*,CD2DSizeU,System.Int32)`

Constructs a CD2DBitmap object from HBITMAP.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `hbmpSrc`: Handle to the bitmap.
- `sizeDest`: Destination size of the bitmap.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmap(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

Constructs a CD2DBitmap object from file.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `lpszPath`: Pointer to a null-terminated string that contains the name of file.
- `sizeDest`: Destination size of the bitmap.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmap(CRenderTarget*,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DBitmap object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmap(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

Constructs a CD2DBitmap object from resource.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `uiResID`: The resource ID number of the resource.
- `lpszType`: Pointer to a null-terminated string that contains the resource type.
- `sizeDest`: Destination size of the bitmap.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DBitmap(CRenderTarget*,HBITMAP__*,CD2DSizeU,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,HBITMAP__*,CD2DSizeU,System.Int32)`

Constructs a CD2DBitmap object from HBITMAP.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `hbmpSrc`: Handle to the bitmap.
- `sizeDest`: Destination size of the bitmap.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmap(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

Constructs a CD2DBitmap object from file.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `lpszPath`: Pointer to a null-terminated string that contains the name of file.
- `sizeDest`: Destination size of the bitmap.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmap(CRenderTarget*,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DBitmap object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmap(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

ID: `M:CD2DBitmap.#ctor(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,System.Int32)`

Constructs a CD2DBitmap object from resource.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `uiResID`: The resource ID number of the resource.
- `lpszType`: Pointer to a null-terminated string that contains the resource type.
- `sizeDest`: Destination size of the bitmap.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1Bitmap*)`

ID: `M:CD2DBitmap.Attach(ID2D1Bitmap*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `CommonInit`

ID: `M:CD2DBitmap.CommonInit`

Initializes the object

### `CopyFromBitmap(CD2DBitmap!System.Runtime.CompilerServices.IsConst*,CD2DPointU!System.Runtime.CompilerServices.IsConst*,CD2DRectU!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DBitmap.CopyFromBitmap(CD2DBitmap!System.Runtime.CompilerServices.IsConst*,CD2DPointU!System.Runtime.CompilerServices.IsConst*,CD2DRectU!System.Runtime.CompilerServices.IsConst*)`

Copies the specified region from the specified bitmap into the current bitmap

Parameters:
- `pBitmap`: The bitmap to copy from
- `destPoint`: In the current bitmap, the upper-left corner of the area to which the region specified by srcRect is copied
- `srcRect`: The area of bitmap to copy

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `CopyFromMemory(System.Void!System.Runtime.CompilerServices.IsConst*,System.UInt32,CD2DRectU!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DBitmap.CopyFromMemory(System.Void!System.Runtime.CompilerServices.IsConst*,System.UInt32,CD2DRectU!System.Runtime.CompilerServices.IsConst*)`

Copies the specified region from memory into the current bitmap

Parameters:
- `srcData`: The data to copy
- `pitch`: The stride, or pitch, of the source bitmap stored in srcData. The stride is the byte count of a scanline (one row of pixels in memory). The stride can be computed from the following formula: pixel width * bytes per pixel + memory padding
- `destRect`: In the current bitmap, the upper-left corner of the area to which the region specified by srcRect is copied

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `CopyFromRenderTarget(CRenderTarget!System.Runtime.CompilerServices.IsConst*,CD2DPointU!System.Runtime.CompilerServices.IsConst*,CD2DRectU!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DBitmap.CopyFromRenderTarget(CRenderTarget!System.Runtime.CompilerServices.IsConst*,CD2DPointU!System.Runtime.CompilerServices.IsConst*,CD2DRectU!System.Runtime.CompilerServices.IsConst*)`

Copies the specified region from the specified render target into the current bitmap

Parameters:
- `pRenderTarget`: The render target that contains the region to copy
- `destPoint`: In the current bitmap, the upper-left corner of the area to which the region specified by srcRect is copied
- `srcRect`: The area of renderTarget to copy

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Create(CRenderTarget*)`

ID: `M:CD2DBitmap.Create(CRenderTarget*)`

Creates a CD2DBitmap.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DBitmap.Destroy`

Destroys a CD2DBitmap object.

### `Detach`

ID: `M:CD2DBitmap.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DBitmap.Dispose`

The destructor. Called when a D2D bitmap object is being destroyed.

### `Get`

ID: `M:CD2DBitmap.Get`

Returns ID2D1Bitmap interface

Returns: Pointer to an ID2D1Bitmap interface or NULL if object is not initialized yet.

### `GetDPI`

ID: `M:CD2DBitmap.GetDPI`

Return the dots per inch (DPI) of the bitmap

Returns: The horizontal and vertical DPI of the bitmap.

### `GetPixelFormat`

ID: `M:CD2DBitmap.GetPixelFormat`

Retrieves the pixel format and alpha mode of the bitmap

Returns: The pixel format and alpha mode of the bitmap.

### `GetPixelSize`

ID: `M:CD2DBitmap.GetPixelSize`

Returns the size, in device-dependent units (pixels), of the bitmap

Returns: The size, in pixels, of the bitmap..

### `GetSize`

ID: `M:CD2DBitmap.GetSize`

Returns the size, in device-independent pixels (DIPs), of the bitmap

Returns: The size, in DIPs, of the bitmap.

### `IsValid`

ID: `M:CD2DBitmap.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `op_Implicit~ID2D1Bitmap*`

ID: `M:CD2DBitmap.op_Implicit~ID2D1Bitmap*`

Returns ID2D1Bitmap interface

Returns: Pointer to an ID2D1Bitmap interface or NULL if object is not initialized yet.

## Fields

### `m_bAutoDestroyHBMP`

ID: `F:CD2DBitmap.m_bAutoDestroyHBMP`

TRUE if m_hBmpSrc should be destroyed; otherwise FALSE.

### `m_hBmpSrc`

ID: `F:CD2DBitmap.m_hBmpSrc`

Source bitmap handle.

### `m_lpszType`

ID: `F:CD2DBitmap.m_lpszType`

Resource type.

### `m_pBitmap`

ID: `F:CD2DBitmap.m_pBitmap`

Stores a pointer to an ID2D1Bitmap object.

### `m_sizeDest`

ID: `F:CD2DBitmap.m_sizeDest`

Bitmap destination size.

### `m_strPath`

ID: `F:CD2DBitmap.m_strPath`

Botmap file path.

### `m_uiResID`

ID: `F:CD2DBitmap.m_uiResID`

Bitmap resource ID.
