# CD2DRadialGradientBrush

Assembly: `TFlexAPI`

## Summary

ID2D1RadialGradientBrush wrapper.

## Constructors

### `CD2DRadialGradientBrush(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DRadialGradientBrush.#ctor(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DLinearGradientBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `gradientStops`: A pointer to an array of D2D1_GRADIENT_STOP structures.
- `gradientStopsCount`: A value greater than or equal to 1 that specifies the number of gradient stops in the gradientStops array.
- `RadialGradientBrushProperties`: The center, gradient origin offset, and x-radius and y-radius of the brush's gradient.
- `colorInterpolationGamma`: The space in which color interpolation between the gradient stops is performed.
- `extendMode`: The behavior of the gradient outside the [0,1] normalized range.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DRadialGradientBrush(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DRadialGradientBrush.#ctor(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DLinearGradientBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `gradientStops`: A pointer to an array of D2D1_GRADIENT_STOP structures.
- `gradientStopsCount`: A value greater than or equal to 1 that specifies the number of gradient stops in the gradientStops array.
- `RadialGradientBrushProperties`: The center, gradient origin offset, and x-radius and y-radius of the brush's gradient.
- `colorInterpolationGamma`: The space in which color interpolation between the gradient stops is performed.
- `extendMode`: The behavior of the gradient outside the [0,1] normalized range.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1RadialGradientBrush*)`

ID: `M:CD2DRadialGradientBrush.Attach(ID2D1RadialGradientBrush*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `Create(CRenderTarget*)`

ID: `M:CD2DRadialGradientBrush.Create(CRenderTarget*)`

Creates a CD2DRadialGradientBrush.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DRadialGradientBrush.Destroy`

Destroys a CD2DRadialGradientBrush object.

### `Detach`

ID: `M:CD2DRadialGradientBrush.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DRadialGradientBrush.Dispose`

The destructor. Called when a D2D radial gradient brush object is being destroyed.

### `Get`

ID: `M:CD2DRadialGradientBrush.Get`

Returns ID2D1RadialGradientBrush interface

Returns: Pointer to an ID2D1RadialGradientBrush interface or NULL if object is not initialized yet.

### `GetCenter`

ID: `M:CD2DRadialGradientBrush.GetCenter`

Retrieves the center of the gradient ellipse

Returns: The center of the gradient ellipse. This value is expressed in the brush's coordinate space

### `GetGradientOriginOffset`

ID: `M:CD2DRadialGradientBrush.GetGradientOriginOffset`

Retrieves the offset of the gradient origin relative to the gradient ellipse's center

Returns: The offset of the gradient origin from the center of the gradient ellipse. This value is expressed in the brush's coordinate space

### `GetRadiusX`

ID: `M:CD2DRadialGradientBrush.GetRadiusX`

Retrieves the x-radius of the gradient ellipse

Returns: The x-radius of the gradient ellipse. This value is expressed in the brush's coordinate space

### `GetRadiusY`

ID: `M:CD2DRadialGradientBrush.GetRadiusY`

Retrieves the y-radius of the gradient ellipse

Returns: The y-radius of the gradient ellipse. This value is expressed in the brush's coordinate space

### `SetCenter(CD2DPointF)`

ID: `M:CD2DRadialGradientBrush.SetCenter(CD2DPointF)`

Specifies the center of the gradient ellipse in the brush's coordinate space

Parameters:
- `point`: The center of the gradient ellipse, in the brush's coordinate space

### `SetGradientOriginOffset(CD2DPointF)`

ID: `M:CD2DRadialGradientBrush.SetGradientOriginOffset(CD2DPointF)`

Specifies the offset of the gradient origin relative to the gradient ellipse's center

Parameters:
- `gradientOriginOffset`: The offset of the gradient origin from the center of the gradient ellipse

### `SetRadiusX(System.Single)`

ID: `M:CD2DRadialGradientBrush.SetRadiusX(System.Single)`

Specifies the x-radius of the gradient ellipse, in the brush's coordinate space

Parameters:
- `radiusX`: The x-radius of the gradient ellipse. This value is in the brush's coordinate space

### `SetRadiusY(System.Single)`

ID: `M:CD2DRadialGradientBrush.SetRadiusY(System.Single)`

Specifies the y-radius of the gradient ellipse, in the brush's coordinate space

Parameters:
- `radiusY`: The y-radius of the gradient ellipse. This value is in the brush's coordinate space

### `op_Implicit~ID2D1RadialGradientBrush*`

ID: `M:CD2DRadialGradientBrush.op_Implicit~ID2D1RadialGradientBrush*`

Returns ID2D1RadialGradientBrush interface

Returns: Pointer to an ID2D1RadialGradientBrush interface or NULL if object is not initialized yet.

## Fields

### `m_RadialGradientBrushProperties`

ID: `F:CD2DRadialGradientBrush.m_RadialGradientBrushProperties`

The center, gradient origin offset, and x-radius and y-radius of the brush's gradient.

### `m_pRadialGradientBrush`

ID: `F:CD2DRadialGradientBrush.m_pRadialGradientBrush`

A pointer to an ID2D1RadialGradientBrush.
