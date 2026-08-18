# CD2DSolidColorBrush

Assembly: `TFlexAPI3D`

## Summary

ID2D1SolidColorBrush wrapper.

## Constructors

### `CD2DSolidColorBrush(CRenderTarget*,System.UInt32!System.Runtime.CompilerServices.IsLong,System.Int32,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DSolidColorBrush.#ctor(CRenderTarget*,System.UInt32!System.Runtime.CompilerServices.IsLong,System.Int32,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DSolidColorBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `color`: The red, green, and blue values of the brush's color.
- `nAlpha`: The opacity of the brush's color.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DSolidColorBrush(CRenderTarget*,_D3DCOLORVALUE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DSolidColorBrush.#ctor(CRenderTarget*,_D3DCOLORVALUE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DSolidColorBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `color`: The red, green, blue, and alpha values of the brush's color.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DSolidColorBrush(CRenderTarget*,System.UInt32!System.Runtime.CompilerServices.IsLong,System.Int32,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DSolidColorBrush.#ctor(CRenderTarget*,System.UInt32!System.Runtime.CompilerServices.IsLong,System.Int32,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DSolidColorBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `color`: The red, green, and blue values of the brush's color.
- `nAlpha`: The opacity of the brush's color.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `CD2DSolidColorBrush(CRenderTarget*,_D3DCOLORVALUE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DSolidColorBrush.#ctor(CRenderTarget*,_D3DCOLORVALUE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DSolidColorBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `color`: The red, green, blue, and alpha values of the brush's color.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1SolidColorBrush*)`

ID: `M:CD2DSolidColorBrush.Attach(ID2D1SolidColorBrush*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `Create(CRenderTarget*)`

ID: `M:CD2DSolidColorBrush.Create(CRenderTarget*)`

Creates a CD2DSolidColorBrush.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DSolidColorBrush.Destroy`

Destroys a CD2DSolidColorBrush object.

### `Detach`

ID: `M:CD2DSolidColorBrush.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DSolidColorBrush.Dispose`

The destructor. Called when a D2D solid brush object is being destroyed.

### `Get`

ID: `M:CD2DSolidColorBrush.Get`

Returns ID2D1SolidColorBrush interface

Returns: Pointer to an ID2D1SolidColorBrush interface or NULL if object is not initialized yet.

### `GetColor`

ID: `M:CD2DSolidColorBrush.GetColor`

Retrieves the color of the solid color brush

Returns: The color of this solid color brush

### `SetColor(_D3DCOLORVALUE)`

ID: `M:CD2DSolidColorBrush.SetColor(_D3DCOLORVALUE)`

Specifies the color of this solid color brush

Parameters:
- `color`: The color of this solid color brush

### `op_Implicit~ID2D1SolidColorBrush*`

ID: `M:CD2DSolidColorBrush.op_Implicit~ID2D1SolidColorBrush*`

Returns ID2D1SolidColorBrush interface

Returns: Pointer to an ID2D1SolidColorBrush interface or NULL if object is not initialized yet.

## Fields

### `m_colorSolid`

ID: `F:CD2DSolidColorBrush.m_colorSolid`

Brush solid color.

### `m_pSolidColorBrush`

ID: `F:CD2DSolidColorBrush.m_pSolidColorBrush`

Stores a pointer to an ID2D1SolidColorBrush object.
