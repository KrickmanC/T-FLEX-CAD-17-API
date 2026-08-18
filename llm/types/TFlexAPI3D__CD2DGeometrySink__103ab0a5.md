# CD2DGeometrySink

Assembly: `TFlexAPI3D`

## Summary

ID2D1GeometrySink wrapper.

## Constructors

### `CD2DGeometrySink(CD2DPathGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.#ctor(CD2DPathGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DGeometrySink object from CD2DPathGeometry object.

Parameters:
- `pathGeometry`: An existing CD2DPathGeometry object.

## Methods

### `CD2DGeometrySink(CD2DPathGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.#ctor(CD2DPathGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DGeometrySink object from CD2DPathGeometry object.

Parameters:
- `pathGeometry`: An existing CD2DPathGeometry object.

### `AddArc(D2D1_ARC_SEGMENT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.AddArc(D2D1_ARC_SEGMENT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Adds a single arc to the path geometry

Parameters:
- `arc`: The arc segment to add to the figure

### `AddBezier(D2D1_BEZIER_SEGMENT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.AddBezier(D2D1_BEZIER_SEGMENT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Creates a cubic Bezier curve between the current point and the specified end point.

Parameters:
- `bezier`: A structure that describes the control points and end point of the Bezier curve to add.

### `AddBeziers(CArray<D2D1_BEZIER_SEGMENT,D2D1_BEZIER_SEGMENT>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.AddBeziers(CArray<D2D1_BEZIER_SEGMENT,D2D1_BEZIER_SEGMENT>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Creates a sequence of cubic Bezier curves and adds them to the geometry sink.

Parameters:
- `beziers`: An array of Bezier segments that describes the Bezier curves to create. A curve is drawn from the geometry sink's current point (the end point of the last segment drawn or the location specified by BeginFigure) to the end point of the first Bezier segment in the array. if the array contains additional Bezier segments, each subsequent Bezier segment uses the end point of the preceding Bezier segment as its start point.

### `AddLine(CD2DPointF)`

ID: `M:CD2DGeometrySink.AddLine(CD2DPointF)`

Creates a line segment between the current point and the specified end point and adds it to the geometry sink.

Parameters:
- `point`: The end point of the line to draw.

### `AddLines(CArray<CD2DPointF,CD2DPointF>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.AddLines(CArray<CD2DPointF,CD2DPointF>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Creates a sequence of lines using the specified points and adds them to the geometry sink.

Parameters:
- `points`: An array of one or more points that describe the lines to draw. A line is drawn from the geometry sink's current point (the end point of the last segment drawn or the location specified by BeginFigure) to the first point in the array. if the array contains additional points, a line is drawn from the first point to the second point in the array, from the second point to the third point, and so on. An array of a sequence of the end points of the lines to draw.

### `AddQuadraticBezier(D2D1_QUADRATIC_BEZIER_SEGMENT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.AddQuadraticBezier(D2D1_QUADRATIC_BEZIER_SEGMENT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Creates a quadratic Bezier curve between the current point and the specified end point.

Parameters:
- `bezier`: A structure that describes the control point and the end point of the quadratic Bezier curve to add.

### `AddQuadraticBeziers(CArray<D2D1_QUADRATIC_BEZIER_SEGMENT,D2D1_QUADRATIC_BEZIER_SEGMENT>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometrySink.AddQuadraticBeziers(CArray<D2D1_QUADRATIC_BEZIER_SEGMENT,D2D1_QUADRATIC_BEZIER_SEGMENT>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Adds a sequence of quadratic Bezier segments as an array in a single call.

Parameters:
- `beziers`: An array of a sequence of quadratic Bezier segments.

### `BeginFigure(CD2DPointF,D2D1_FIGURE_BEGIN)`

ID: `M:CD2DGeometrySink.BeginFigure(CD2DPointF,D2D1_FIGURE_BEGIN)`

Starts a new figure at the specified point.

Parameters:
- `startPoint`: The point at which to begin the new figure.
- `figureBegin`: Whether the new figure should be hollow or filled.

### `Close`

ID: `M:CD2DGeometrySink.Close`

Closes the geometry sink

Returns: Nonzero if successful; otherwise FALSE.

### `Dispose`

ID: `M:CD2DGeometrySink.Dispose`

The destructor. Called when a D2D geometry sink object is being destroyed.

### `EndFigure(D2D1_FIGURE_END)`

ID: `M:CD2DGeometrySink.EndFigure(D2D1_FIGURE_END)`

Ends the current figure; optionally, closes it.

Parameters:
- `figureEnd`: A value that indicates whether the current figure is closed. If the figure is closed, a line is drawn between the current point and the start point specified by BeginFigure.

### `Get`

ID: `M:CD2DGeometrySink.Get`

Returns ID2D1GeometrySink interface

Returns: Pointer to an ID2D1GeometrySink interface or NULL if object is not initialized yet.

### `IsValid`

ID: `M:CD2DGeometrySink.IsValid`

Checks geometry sink validity

Returns: TRUE if geometry sink is valid; otherwise FALSE.

### `SetFillMode(D2D1_FILL_MODE)`

ID: `M:CD2DGeometrySink.SetFillMode(D2D1_FILL_MODE)`

Specifies the method used to determine which points are inside the geometry described by this geometry sink and which points are outside.

Parameters:
- `fillMode`: The method used to determine whether a given point is part of the geometry.

### `SetSegmentFlags(D2D1_PATH_SEGMENT)`

ID: `M:CD2DGeometrySink.SetSegmentFlags(D2D1_PATH_SEGMENT)`

Specifies stroke and join options to be applied to new segments added to the geometry sink.

Parameters:
- `vertexFlags`: Stroke and join options to be applied to new segments added to the geometry sink.

### `op_Implicit~ID2D1GeometrySink*`

ID: `M:CD2DGeometrySink.op_Implicit~ID2D1GeometrySink*`

Returns ID2D1GeometrySink interface

Returns: Pointer to an ID2D1GeometrySink interface or NULL if object is not initialized yet.

## Fields

### `m_pSink`

ID: `F:CD2DGeometrySink.m_pSink`

A pointer to an ID2D1GeometrySink.
