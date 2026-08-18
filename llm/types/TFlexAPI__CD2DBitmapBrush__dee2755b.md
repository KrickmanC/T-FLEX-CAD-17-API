# CD2DBitmapBrush

Assembly: `TFlexAPI`

## Summary

ID2D1BitmapBrush wrapper.

## Constructors

### `CD2DBitmapBrush(CRenderTarget*,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBitmapBrush.#ctor(CRenderTarget*,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBitmapBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `pBitmapBrushProperties`: A pointer to the extend modes and the interpolation mode of a bitmap brush.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmapBrush(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBitmapBrush.#ctor(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBitmapBrush object from file.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `lpszImagePath`: Pointer to a null-terminated string that contains the name of file.
- `sizeDest`: Destination size of the bitmap.
- `pBitmapBrushProperties`: A pointer to the extend modes and the interpolation mode of a bitmap brush.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmapBrush(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBitmapBrush.#ctor(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBitmapBrush object from resource.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `uiResID`: The resource ID number of the resource.
- `lpszType`: Pointer to a null-terminated string that contains the resource type.
- `sizeDest`: Destination size of the bitmap.
- `pBitmapBrushProperties`: A pointer to the extend modes and the interpolation mode of a bitmap brush.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DBitmapBrush(CRenderTarget*,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBitmapBrush.#ctor(CRenderTarget*,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBitmapBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `pBitmapBrushProperties`: A pointer to the extend modes and the interpolation mode of a bitmap brush.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmapBrush(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBitmapBrush.#ctor(CRenderTarget*,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBitmapBrush object from file.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `lpszImagePath`: Pointer to a null-terminated string that contains the name of file.
- `sizeDest`: Destination size of the bitmap.
- `pBitmapBrushProperties`: A pointer to the extend modes and the interpolation mode of a bitmap brush.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DBitmapBrush(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBitmapBrush.#ctor(CRenderTarget*,System.UInt32,System.Char!System.Runtime.CompilerServices.IsConst*,CD2DSizeU,D2D1_BITMAP_BRUSH_PROPERTIES*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBitmapBrush object from resource.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `uiResID`: The resource ID number of the resource.
- `lpszType`: Pointer to a null-terminated string that contains the resource type.
- `sizeDest`: Destination size of the bitmap.
- `pBitmapBrushProperties`: A pointer to the extend modes and the interpolation mode of a bitmap brush.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1BitmapBrush*)`

ID: `M:CD2DBitmapBrush.Attach(ID2D1BitmapBrush*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `CommonInit(D2D1_BITMAP_BRUSH_PROPERTIES*)`

ID: `M:CD2DBitmapBrush.CommonInit(D2D1_BITMAP_BRUSH_PROPERTIES*)`

Initializes the object

Parameters:
- `pBitmapBrushProperties`: A pointer to the bitmap brush properties.

### `Create(CRenderTarget*)`

ID: `M:CD2DBitmapBrush.Create(CRenderTarget*)`

Creates a CD2DBitmapBrush.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DBitmapBrush.Destroy`

Destroys a CD2DBitmapBrush object.

### `Detach`

ID: `M:CD2DBitmapBrush.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DBitmapBrush.Dispose`

The destructor. Called when a D2D bitmap brush object is being destroyed.

### `Get`

ID: `M:CD2DBitmapBrush.Get`

Returns ID2D1BitmapBrush interface

Returns: Pointer to an ID2D1BitmapBrush interface or NULL if object is not initialized yet.

### `GetBitmap`

ID: `M:CD2DBitmapBrush.GetBitmap`

Gets the bitmap source that this brush uses to paint

Returns: Pointer to an CD2DBitmap object or NULL if object is not initialized yet.

### `GetExtendModeX`

ID: `M:CD2DBitmapBrush.GetExtendModeX`

Gets the method by which the brush horizontally tiles those areas that extend past its bitmap

Returns: A value that specifies how the brush horizontally tiles those areas that extend past its bitmap

### `GetExtendModeY`

ID: `M:CD2DBitmapBrush.GetExtendModeY`

Gets the method by which the brush vertically tiles those areas that extend past its bitmap

Returns: A value that specifies how the brush vertically tiles those areas that extend past its bitmap

### `GetInterpolationMode`

ID: `M:CD2DBitmapBrush.GetInterpolationMode`

Gets the interpolation method used when the brush bitmap is scaled or rotated

Returns: The interpolation method used when the brush bitmap is scaled or rotated

### `SetBitmap(CD2DBitmap*)`

ID: `M:CD2DBitmapBrush.SetBitmap(CD2DBitmap*)`

Specifies the bitmap source that this brush uses to paint

Parameters:
- `pBitmap`: The bitmap source used by the brush

### `SetExtendModeX(D2D1_EXTEND_MODE)`

ID: `M:CD2DBitmapBrush.SetExtendModeX(D2D1_EXTEND_MODE)`

Specifies how the brush horizontally tiles those areas that extend past its bitmap

Parameters:
- `extendModeX`: A value that specifies how the brush horizontally tiles those areas that extend past its bitmap

### `SetExtendModeY(D2D1_EXTEND_MODE)`

ID: `M:CD2DBitmapBrush.SetExtendModeY(D2D1_EXTEND_MODE)`

Specifies how the brush vertically tiles those areas that extend past its bitmap

Parameters:
- `extendModeY`: A value that specifies how the brush vertically tiles those areas that extend past its bitmap

### `SetInterpolationMode(D2D1_BITMAP_INTERPOLATION_MODE)`

ID: `M:CD2DBitmapBrush.SetInterpolationMode(D2D1_BITMAP_INTERPOLATION_MODE)`

Specifies the interpolation mode used when the brush bitmap is scaled or rotated

Parameters:
- `interpolationMode`: The interpolation mode used when the brush bitmap is scaled or rotated

### `op_Implicit~ID2D1BitmapBrush*`

ID: `M:CD2DBitmapBrush.op_Implicit~ID2D1BitmapBrush*`

Returns ID2D1BitmapBrush interface

Returns: Pointer to an ID2D1BitmapBrush interface or NULL if object is not initialized yet.

## Fields

### `m_pBitmap`

ID: `F:CD2DBitmapBrush.m_pBitmap`

Stores a pointer to a CD2DBitmap object.

### `m_pBitmapBrush`

ID: `F:CD2DBitmapBrush.m_pBitmapBrush`

Stores a pointer to an ID2D1BitmapBrush object.

### `m_pBitmapBrushProperties`

ID: `F:CD2DBitmapBrush.m_pBitmapBrushProperties`

Bitmap brush properties.
