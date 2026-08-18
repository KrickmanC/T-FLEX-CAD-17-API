# CRenderTarget

Assembly: `TFlexAPI3D`

## Summary

ID2D1RenderTarget wrapper.

## Constructors

### `CRenderTarget`

ID: `M:CRenderTarget.#ctor`

Constructs a CRenderTarget object.

## Methods

### `CRenderTarget`

ID: `M:CRenderTarget.#ctor`

Constructs a CRenderTarget object.

### `Attach(ID2D1RenderTarget*)`

ID: `M:CRenderTarget.Attach(ID2D1RenderTarget*)`

Attaches existing render target interface to the object

Parameters:
- `pRenderTarget`: Existing render target interface. Cannot be NULL

### `BeginDraw`

ID: `M:CRenderTarget.BeginDraw`

Initiates drawing on this render target.

### `COLORREF_TO_D2DCOLOR(System.UInt32!System.Runtime.CompilerServices.IsLong,System.Int32)`

ID: `M:CRenderTarget.COLORREF_TO_D2DCOLOR(System.UInt32!System.Runtime.CompilerServices.IsLong,System.Int32)`

Converts GDI color and alpha values to the D2D1_COLOR_F object.

Parameters:
- `color`: RGB value.
- `nAlpha`: Alpha value.

Returns: D2D1_COLOR_F value.

### `Clear(_D3DCOLORVALUE)`

ID: `M:CRenderTarget.Clear(_D3DCOLORVALUE)`

Clears the drawing area to the specified color.

Parameters:
- `color`: The color to which the drawing area is cleared.

### `CreateCompatibleRenderTarget(CBitmapRenderTarget*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DSizeF,CD2DSizeU,D2D1_PIXEL_FORMAT*,D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS)`

ID: `M:CRenderTarget.CreateCompatibleRenderTarget(CBitmapRenderTarget*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DSizeF,CD2DSizeU,D2D1_PIXEL_FORMAT*,D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS)`

Creates a new bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target .

Parameters:
- `bitmapTarget`: When this method returns, contains the address of a pointer to a new bitmap render target. This parameter is passed uninitialized.
- `sizeDesired`: The desired size of the new render target in device-independent pixels if it should be different from the original render target, or NULL. For more information, see the Remarks section.
- `sizePixelDesired`: The desired size of the new render target in pixels if it should be different from the original render target, or NULL. For more information, see the Remarks section.
- `desiredFormat`: The desired pixel format and alpha mode of the new render target, or NULL. If the pixel format is set to DXGI_FORMAT_UNKNOWN or if this parameter is null, the new render target uses the same pixel format as the original render target. If the alpha mode is D2D1_ALPHA_MODE_UNKNOWN or this parameter is NULL, the alpha mode of the new render target defaults to D2D1_ALPHA_MODE_PREMULTIPLIED. For information about supported pixel formats, see Supported Pixel Formats and Alpha Modes.
- `options`: A value that specifies whether the new render target must be compatible with GDI.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Destroy(System.Int32)`

ID: `M:CRenderTarget.Destroy(System.Int32)`

Deletes one or more resources

Parameters:
- `bDeleteResources`: If bDeleteResources is TRUE, all resources located in m_lstResources will be automatically destroyed.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE

### `Detach`

ID: `M:CRenderTarget.Detach`

Detaches render target interface from the object

Returns: Pointer to detached render target interface.

### `Dispose`

ID: `M:CRenderTarget.Dispose`

The destructor. Called when a render target object is being destroyed.

### `DrawBitmap(CD2DBitmap*,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single,D2D1_BITMAP_INTERPOLATION_MODE,CD2DRectF!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CRenderTarget.DrawBitmap(CD2DBitmap*,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single,D2D1_BITMAP_INTERPOLATION_MODE,CD2DRectF!System.Runtime.CompilerServices.IsConst*)`

Draws the formatted text described by the specified IDWriteTextLayout object.

Parameters:
- `pBitmap`: The bitmap to render.
- `rectDest`: The size and position, in device-independent pixels in the render target's coordinate space, of the area to which the bitmap is drawn. If the rectangle is not well-ordered, nothing is drawn, but the render target does not enter an error state.
- `fOpacity`: A value between 0.0f and 1.0f, inclusive, that specifies an opacity value to apply to the bitmap; this value is multiplied against the alpha values of the bitmap's contents.
- `interpolationMode`: The interpolation mode to use if the bitmap is scaled or rotated by the drawing operation.
- `pRectSrc`: The size and position, in device-independent pixels in the bitmap's coordinate space, of the area within the bitmap to draw.

### `DrawEllipse(CD2DEllipse!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

ID: `M:CRenderTarget.DrawEllipse(CD2DEllipse!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

Draws the outline of the specified ellipse using the specified stroke style.

Parameters:
- `ellipse`: The position and radius of the ellipse to draw, in device-independent pixels.
- `pBrush`: The brush used to paint the ellipse's outline.
- `fStrokeWidth`: The thickness of the ellipse's stroke. The stroke is centered on the ellipse's outline.
- `strokeStyle`: The style of stroke to apply to the ellipse's outline, or NULL to paint a solid stroke.

### `DrawGeometry(CD2DGeometry*,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

ID: `M:CRenderTarget.DrawGeometry(CD2DGeometry*,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

Draws the outline of the specified geometry using the specified stroke style.

Parameters:
- `pGeometry`: The geometry to draw.
- `pBrush`: The brush used to paint the geometry's stroke.
- `fStrokeWidth`: The thickness of the geometry's stroke. The stroke is centered on the geometry's outline.
- `strokeStyle`: The style of stroke to apply to the geometry's outline, or NULL to paint a solid stroke.

### `DrawGlyphRun(CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,DWRITE_GLYPH_RUN!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,DWRITE_MEASURING_MODE)`

ID: `M:CRenderTarget.DrawGlyphRun(CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,DWRITE_GLYPH_RUN!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,DWRITE_MEASURING_MODE)`

Draws the specified glyphs.

Parameters:
- `ptBaseLineOrigin`: The origin, in device-independent pixels, of the glyphs' baseline.
- `glyphRun`: The glyphs to render.
- `pForegroundBrush`: The brush used to paint the specified glyphs.
- `measuringMode`: A value that indicates how glyph metrics are used to measure text when it is formatted. The default value is DWRITE_MEASURING_MODE_NATURAL.

### `DrawLine(CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

ID: `M:CRenderTarget.DrawLine(CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

Draws a line between the specified points using the specified stroke style.

Parameters:
- `ptFrom`: The start point of the line, in device-independent pixels.
- `ptTo`: The end point of the line, in device-independent pixels.
- `pBrush`: The brush used to paint the line's stroke.
- `fStrokeWidth`: A value greater than or equal to 0.0f that specifies the width of the stroke. If this parameter isn't specified, it defaults to 1.0f. The stroke is centered on the line.
- `strokeStyle`: The style of stroke to paint, or NULL to paint a solid line.

### `DrawRectangle(CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

ID: `M:CRenderTarget.DrawRectangle(CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

Draws the outline of a rectangle that has the specified dimensions and stroke style.

Parameters:
- `rect`: The dimensions of the rectangle to draw, in device-independent pixels
- `pBrush`: The brush used to paint the rectangle's stroke
- `fStrokeWidth`: A value greater than or equal to 0.0f that specifies the width of the rectangle's stroke. The stroke is centered on the rectangle's outline.
- `strokeStyle`: The style of stroke to paint, or NULL to paint a solid stroke.

### `DrawRoundedRectangle(CD2DRoundedRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

ID: `M:CRenderTarget.DrawRoundedRectangle(CD2DRoundedRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,System.Single,ID2D1StrokeStyle*)`

Draws the outline of the specified rounded rectangle using the specified stroke style.

Parameters:
- `rectRounded`: The dimensions of the rounded rectangle to draw, in device-independent pixels.
- `pBrush`: The brush used to paint the rounded rectangle's outline.
- `fStrokeWidth`: The width of the rounded rectangle's stroke. The stroke is centered on the rounded rectangle's outline. The default value is 1.0f.
- `strokeStyle`: The style of the rounded rectangle's stroke, or NULL to paint a solid stroke. The default value is NULL.

### `DrawTextLayout(CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DTextLayout*,CD2DBrush*,D2D1_DRAW_TEXT_OPTIONS)`

ID: `M:CRenderTarget.DrawTextLayout(CD2DPointF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DTextLayout*,CD2DBrush*,D2D1_DRAW_TEXT_OPTIONS)`

Draws the formatted text described by the specified IDWriteTextLayout object.

Parameters:
- `ptOrigin`: The point, described in device-independent pixels, at which the upper-left corner of the text described by textLayout is drawn.
- `textLayout`: The formatted text to draw. Any drawing effects that do not inherit from ID2D1Resource are ignored. If there are drawing effects that inherit from ID2D1Resource that are not brushes, this method fails and the render target is put in an error state.
- `pBrushForeground`: The brush used to paint any text in textLayout that does not already have a brush associated with it as a drawing effect (specified by the IDWriteTextLayout::SetDrawingEffect method).
- `options`: A value that indicates whether the text should be snapped to pixel boundaries and whether the text should be clipped to the layout rectangle. The default value is D2D1_DRAW_TEXT_OPTIONS_NONE, which indicates that text should be snapped to pixel boundaries and it should not be clipped to the layout rectangle.

### `DrawTextW(ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,CD2DTextFormat*,D2D1_DRAW_TEXT_OPTIONS,DWRITE_MEASURING_MODE)`

ID: `M:CRenderTarget.DrawTextW(ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*,CD2DTextFormat*,D2D1_DRAW_TEXT_OPTIONS,DWRITE_MEASURING_MODE)`

Draws the specified text using the format information provided by an IDWriteTextFormat object.

Parameters:
- `strText`: A pointer to an array of Unicode characters to draw.
- `rect`: The size and position of the area in which the text is drawn.
- `pForegroundBrush`: The brush used to paint the text.
- `textFormat`: An object that describes formatting details of the text to draw, such as the font, the font size, and flow direction.
- `options`: A value that indicates whether the text should be snapped to pixel boundaries and whether the text should be clipped to the layout rectangle. The default value is D2D1_DRAW_TEXT_OPTIONS_NONE, which indicates that text should be snapped to pixel boundaries and it should not be clipped to the layout rectangle.
- `measuringMode`: A value that indicates how glyph metrics are used to measure text when it is formatted. The default value is DWRITE_MEASURING_MODE_NATURAL.

### `EndDraw`

ID: `M:CRenderTarget.EndDraw`

Ends drawing operations on the render target and indicates the current error state and associated tags.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `FillEllipse(CD2DEllipse!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*)`

ID: `M:CRenderTarget.FillEllipse(CD2DEllipse!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*)`

Paints the interior of the specified ellipse.

Parameters:
- `ellipse`: The position and radius, in device-independent pixels, of the ellipse to paint.
- `pBrush`: The brush used to paint the interior of the ellipse.

### `FillGeometry(CD2DGeometry*,CD2DBrush*,CD2DBrush*)`

ID: `M:CRenderTarget.FillGeometry(CD2DGeometry*,CD2DBrush*,CD2DBrush*)`

Paints the interior of the specified geometry.

Parameters:
- `pGeometry`: The geometry to paint.
- `pBrush`: The brush used to paint the geometry's interior.
- `pOpacityBrush`: The opacity mask to apply to the geometry;NULL for no opacity mask. If an opacity mask (the opacityBrush parameter) is specified, brush must be an ID2D1BitmapBrush that has its x- and y-extend modes set to D2D1_EXTEND_MODE_CLAMP. For more information, see the Remarks section.

### `FillMesh(CD2DMesh*,CD2DBrush*)`

ID: `M:CRenderTarget.FillMesh(CD2DMesh*,CD2DBrush*)`

Paints the interior of the specified mesh.

Parameters:
- `pMesh`: The mesh to paint.
- `pBrush`: The brush used to paint the mesh.

### `FillOpacityMask(CD2DBitmap*,CD2DBrush*,D2D1_OPACITY_MASK_CONTENT,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CRenderTarget.FillOpacityMask(CD2DBitmap*,CD2DBrush*,D2D1_OPACITY_MASK_CONTENT,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target.

Parameters:
- `pOpacityMask`: The position and radius, in device-independent pixels, of the ellipse to paint.
- `pBrush`: The brush used to paint the region of the render target specified by destinationRectangle.
- `content`: The type of content the opacity mask contains. The value is used to determine the color space in which the opacity mask is blended.
- `rectDest`: The region of the render target to paint, in device-independent pixels.
- `rectSrc`: The region of the bitmap to use as the opacity mask, in device-independent pixels.

### `FillRectangle(CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*)`

ID: `M:CRenderTarget.FillRectangle(CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*)`

Paints the interior of the specified rectangle.

Parameters:
- `rect`: The dimension of the rectangle to paint, in device-independent pixels.
- `pBrush`: The brush used to paint the rectangle's interior.

### `FillRoundedRectangle(CD2DRoundedRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*)`

ID: `M:CRenderTarget.FillRoundedRectangle(CD2DRoundedRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DBrush*)`

Paints the interior of the specified rounded rectangle.

Parameters:
- `rectRounded`: The dimensions of the rounded rectangle to paint, in device independent pixels.
- `pBrush`: The brush used to paint the interior of the rounded rectangle.

### `Flush(System.UInt64*,System.UInt64*)`

ID: `M:CRenderTarget.Flush(System.UInt64*,System.UInt64*)`

Executes all pending drawing commands.

Parameters:
- `tag1`: Contains the tag for drawing operations that caused errors or 0 if there were no errors. This parameter is passed uninitialized.
- `tag2`: Contains the tag for drawing operations that caused errors or 0 if there were no errors. This parameter is passed uninitialized.

### `GetAntialiasMode`

ID: `M:CRenderTarget.GetAntialiasMode`

Retrieves the current antialiasing mode for nontext drawing operations.

Returns: Current antialiasing mode for nontext drawing operations.

### `GetDpi`

ID: `M:CRenderTarget.GetDpi`

Returns the render target's dots per inch (DPI)

Returns: The render target's dots per inch (DPI).

### `GetMaximumBitmapSize`

ID: `M:CRenderTarget.GetMaximumBitmapSize`

Gets the maximum size, in device-dependent units (pixels), of any one bitmap dimension supported by the render target

Returns: The maximum size, in pixels, of any one bitmap dimension supported by the render target

### `GetPixelFormat`

ID: `M:CRenderTarget.GetPixelFormat`

Retrieves the pixel format and alpha mode of the render target

Returns: The pixel format and alpha mode of the render target

### `GetPixelSize`

ID: `M:CRenderTarget.GetPixelSize`

Returns the size of the render target in device pixels

Returns: The size of the render target in device pixels

### `GetRenderTarget`

ID: `M:CRenderTarget.GetRenderTarget`

Returns ID2D1RenderTarget interface

Returns: Pointer to an ID2D1RenderTarget interface or NULL if object is not initialized yet.

### `GetSize`

ID: `M:CRenderTarget.GetSize`

Returns the size of the render target in device-independent pixels

Returns: The current size of the render target in device-independent pixels

### `GetTags(System.UInt64*,System.UInt64*)`

ID: `M:CRenderTarget.GetTags(System.UInt64*,System.UInt64*)`

Gets the label for subsequent drawing operations.

Parameters:
- `tag1`: Contains the first label for subsequent drawing operations. This parameter is passed uninitialized. If NULL is specified, no value is retrieved for this parameter.
- `tag2`: Contains the second label for subsequent drawing operations. This parameter is passed uninitialized. If NULL is specified, no value is retrieved for this parameter.

### `GetTextAntialiasMode`

ID: `M:CRenderTarget.GetTextAntialiasMode`

Gets the current antialiasing mode for text and glyph drawing operations.

Returns: Current antialiasing mode for text and glyph drawing operations.

### `GetTextRenderingParams(IDWriteRenderingParams**)`

ID: `M:CRenderTarget.GetTextRenderingParams(IDWriteRenderingParams**)`

Retrieves the render target's current text rendering options.

Parameters:
- `textRenderingParams`: When this method returns, textRenderingParamscontains the address of a pointer to the render target's current text rendering options.

### `GetTransform(D2D_MATRIX_3X2_F*)`

ID: `M:CRenderTarget.GetTransform(D2D_MATRIX_3X2_F*)`

Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space.

Parameters:
- `transform`: The transform to apply to the render target.

### `IsSupported(D2D1_RENDER_TARGET_PROPERTIES!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CRenderTarget.IsSupported(D2D1_RENDER_TARGET_PROPERTIES!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Indicates whether the render target supports the specified properties

Parameters:
- `renderTargetProperties`: The render target properties to test

Returns: TRUE if the specified render target properties are supported by this render target; otherwise, FALSE

### `IsValid`

ID: `M:CRenderTarget.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `PopAxisAlignedClip`

ID: `M:CRenderTarget.PopAxisAlignedClip`

Removes the last axis-aligned clip from the render target. After this method is called, the clip is no longer applied to subsequent drawing operations.

### `PopLayer`

ID: `M:CRenderTarget.PopLayer`

Stops redirecting drawing operations to the layer that is specified by the last PushLayer call.

### `PushAxisAlignedClip(CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,D2D1_ANTIALIAS_MODE)`

ID: `M:CRenderTarget.PushAxisAlignedClip(CD2DRectF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,D2D1_ANTIALIAS_MODE)`

Removes the last axis-aligned clip from the render target. After this method is called, the clip is no longer applied to subsequent drawing operations.

Parameters:
- `rectClip`: The size and position of the clipping area, in device-independent pixels.
- `mode`: The antialiasing mode that is used to draw the edges of clip rects that have subpixel boundaries, and to blend the clip with the scene contents. The blending is performed once when the PopAxisAlignedClip method is called, and does not apply to each primitive within the layer.

### `PushLayer(D2D1_LAYER_PARAMETERS!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DLayer*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CRenderTarget.PushLayer(D2D1_LAYER_PARAMETERS!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DLayer*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Adds the specified layer to the render target so that it receives all subsequent drawing operations until PopLayer is called.

Parameters:
- `layerParameters`: The content bounds, geometric mask, opacity, opacity mask, and antialiasing options for the layer.
- `layer`: The layer that receives subsequent drawing operations.

### `RestoreDrawingState(ID2D1DrawingStateBlock*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CRenderTarget.RestoreDrawingState(ID2D1DrawingStateBlock*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Sets the render target's drawing state to that of the specified ID2D1DrawingStateBlock.

Parameters:
- `drawingStateBlock`: The new drawing state of the render target.

### `SaveDrawingState(ID2D1DrawingStateBlock*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CRenderTarget.SaveDrawingState(ID2D1DrawingStateBlock*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Saves the current drawing state to the specified ID2D1DrawingStateBlock.

Parameters:
- `drawingStateBlock`: When this method returns, contains the current drawing state of the render target. This parameter must be initialized before passing it to the method.

### `SetAntialiasMode(D2D1_ANTIALIAS_MODE)`

ID: `M:CRenderTarget.SetAntialiasMode(D2D1_ANTIALIAS_MODE)`

Sets the antialiasing mode of the render target. The antialiasing mode applies to all subsequent drawing operations, excluding text and glyph drawing operations.

Parameters:
- `antialiasMode`: The antialiasing mode for future drawing operations.

### `SetDpi(CD2DSizeF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CRenderTarget.SetDpi(CD2DSizeF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Sets the dots per inch (DPI) of the render target.

Parameters:
- `sizeDPI`: A value greater than or equal to zero that specifies the horizontal/verticalDPI of the render target.

### `SetTags(System.UInt64,System.UInt64)`

ID: `M:CRenderTarget.SetTags(System.UInt64,System.UInt64)`

Specifies a label for subsequent drawing operations.

Parameters:
- `tag1`: A label to apply to subsequent drawing operations.
- `tag2`: A label to apply to subsequent drawing operations.

### `SetTextAntialiasMode(D2D1_TEXT_ANTIALIAS_MODE)`

ID: `M:CRenderTarget.SetTextAntialiasMode(D2D1_TEXT_ANTIALIAS_MODE)`

Specifies the antialiasing mode to use for subsequent text and glyph drawing operations.

Parameters:
- `textAntialiasMode`: The antialiasing mode to use for subsequent text and glyph drawing operations.

### `SetTextRenderingParams(IDWriteRenderingParams*)`

ID: `M:CRenderTarget.SetTextRenderingParams(IDWriteRenderingParams*)`

Specifies text rendering options to be applied to all subsequent text and glyph drawing operations.

Parameters:
- `textRenderingParams`: The text rendering options to be applied to all subsequent text and glyph drawing operations; NULL to clear current text rendering options.

### `SetTransform(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CRenderTarget.SetTransform(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space.

Parameters:
- `transform`: The transform to apply to the render target.

### `SetTransform(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CRenderTarget.SetTransform(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*)`

Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space.

Parameters:
- `transform`: The transform to apply to the render target.

### `VerifyResource(CD2DResource*)`

ID: `M:CRenderTarget.VerifyResource(CD2DResource*)`

Verifies CD2DResource object validity; creates the object if it didn't already exist.

Parameters:
- `pResource`: Pointer to CD2DResource object.

Returns: TRUE is object if valid; otherwise FALSE.

### `op_Implicit~ID2D1RenderTarget*`

ID: `M:CRenderTarget.op_Implicit~ID2D1RenderTarget*`

Returns ID2D1RenderTarget interface

Returns: Pointer to an ID2D1RenderTarget interface or NULL if object is not initialized yet.

## Fields

### `m_lstResources`

ID: `F:CRenderTarget.m_lstResources`

A list of pointers to CD2DResource objects.

### `m_pRenderTarget`

ID: `F:CRenderTarget.m_pRenderTarget`

A pointer to an ID2D1RenderTarget object.

### `m_pTextFormatDefault`

ID: `F:CRenderTarget.m_pTextFormatDefault`

A pointer to CD2DTextFormat object that contains a default text format.
