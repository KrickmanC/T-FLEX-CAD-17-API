# CD2DGradientBrush

Assembly: `TFlexAPI`

## Summary

The base class of CD2DLinearGradientBrush and CD2DRadialGradientBrush classes.

## Constructors

### `CD2DGradientBrush(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DGradientBrush.#ctor(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DGradientBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `gradientStops`: A pointer to an array of D2D1_GRADIENT_STOP structures.
- `gradientStopsCount`: A value greater than or equal to 1 that specifies the number of gradient stops in the gradientStops array.
- `colorInterpolationGamma`: The space in which color interpolation between the gradient stops is performed.
- `extendMode`: The behavior of the gradient outside the [0,1] normalized range.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DGradientBrush(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DGradientBrush.#ctor(CRenderTarget*,D2D1_GRADIENT_STOP!System.Runtime.CompilerServices.IsConst*,System.UInt32,D2D1_GAMMA,D2D1_EXTEND_MODE,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DGradientBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `gradientStops`: A pointer to an array of D2D1_GRADIENT_STOP structures.
- `gradientStopsCount`: A value greater than or equal to 1 that specifies the number of gradient stops in the gradientStops array.
- `colorInterpolationGamma`: The space in which color interpolation between the gradient stops is performed.
- `extendMode`: The behavior of the gradient outside the [0,1] normalized range.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Destroy`

ID: `M:CD2DGradientBrush.Destroy`

Destroys a CD2DGradientBrush object.

### `Dispose`

ID: `M:CD2DGradientBrush.Dispose`

The destructor. Called when a D2D gradient brush object is being destroyed.

## Fields

### `m_arGradientStops`

ID: `F:CD2DGradientBrush.m_arGradientStops`

Array of the D2D1_GRADIENT_STOP structures.

### `m_colorInterpolationGamma`

ID: `F:CD2DGradientBrush.m_colorInterpolationGamma`

The space in which color interpolation between the gradient stops is performed.

### `m_extendMode`

ID: `F:CD2DGradientBrush.m_extendMode`

The behavior of the gradient outside the [0,1] normalized range.

### `m_pGradientStops`

ID: `F:CD2DGradientBrush.m_pGradientStops`

A pointer to an array of D2D1_GRADIENT_STOP structures.
