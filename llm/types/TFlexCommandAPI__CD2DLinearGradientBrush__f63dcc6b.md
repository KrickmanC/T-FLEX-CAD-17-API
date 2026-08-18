# CD2DLinearGradientBrush

Assembly: `TFlexCommandAPI`

## Summary

ID2D1LinearGradientBrush wrapper.

## Constructors

### `CD2DLinearGradientBrush(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DLinearGradientBrush.#ctor(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DLinearGradientBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `gradientStops`: A pointer to an array of D2D1_GRADIENT_STOP structures.
- `gradientStopsCount`: A value greater than or equal to 1 that specifies the number of gradient stops in the gradientStops array.
- `LinearGradientBrushProperties`: The start and end points of the gradient.
- `colorInterpolationGamma`: The space in which color interpolation between the gradient stops is performed.
- `extendMode`: The behavior of the gradient outside the [0,1] normalized range.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DLinearGradientBrush(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DLinearGradientBrush.#ctor(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DLinearGradientBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `gradientStops`: A pointer to an array of D2D1_GRADIENT_STOP structures.
- `gradientStopsCount`: A value greater than or equal to 1 that specifies the number of gradient stops in the gradientStops array.
- `LinearGradientBrushProperties`: The start and end points of the gradient.
- `colorInterpolationGamma`: The space in which color interpolation between the gradient stops is performed.
- `extendMode`: The behavior of the gradient outside the [0,1] normalized range.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1LinearGradientBrush*)`

ID: `M:CD2DLinearGradientBrush.Attach(ID2D1LinearGradientBrush*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `Create(CRenderTarget*)`

ID: `M:CD2DLinearGradientBrush.Create(CRenderTarget*)`

Creates a CD2DLinearGradientBrush.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DLinearGradientBrush.Destroy`

Destroys a CD2DLinearGradientBrush object.

### `Detach`

ID: `M:CD2DLinearGradientBrush.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DLinearGradientBrush.Dispose`

The destructor. Called when a D2D linear gradient brush object is being destroyed.

### `Get`

ID: `M:CD2DLinearGradientBrush.Get`

Returns ID2D1LinearGradientBrush interface

Returns: Pointer to an ID2D1LinearGradientBrush interface or NULL if object is not initialized yet.

### `GetEndPoint`

ID: `M:CD2DLinearGradientBrush.GetEndPoint`

Retrieves the ending coordinates of the linear gradient

Returns: The ending two-dimensional coordinates of the linear gradient, in the brush's coordinate space

### `GetStartPoint`

ID: `M:CD2DLinearGradientBrush.GetStartPoint`

Retrieves the starting coordinates of the linear gradient

Returns: The starting two-dimensional coordinates of the linear gradient, in the brush's coordinate space

### `SetEndPoint(CD2DPointF)`

ID: `M:CD2DLinearGradientBrush.SetEndPoint(CD2DPointF)`

Sets the ending coordinates of the linear gradient in the brush's coordinate space

Parameters:
- `point`: The ending two-dimensional coordinates of the linear gradient, in the brush's coordinate space

### `SetStartPoint(CD2DPointF)`

ID: `M:CD2DLinearGradientBrush.SetStartPoint(CD2DPointF)`

Sets the starting coordinates of the linear gradient in the brush's coordinate space

Parameters:
- `point`: The starting two-dimensional coordinates of the linear gradient, in the brush's coordinate space

### `op_Implicit~ID2D1LinearGradientBrush*`

ID: `M:CD2DLinearGradientBrush.op_Implicit~ID2D1LinearGradientBrush*`

Returns ID2D1LinearGradientBrush interface

Returns: Pointer to an ID2D1LinearGradientBrush interface or NULL if object is not initialized yet.

## Fields

### `m_LinearGradientBrushProperties`

ID: `F:CD2DLinearGradientBrush.m_LinearGradientBrushProperties`

The start and end points of the gradient.

### `m_pLinearGradientBrush`

ID: `F:CD2DLinearGradientBrush.m_pLinearGradientBrush`

A pointer to an ID2D1LinearGradientBrush.
