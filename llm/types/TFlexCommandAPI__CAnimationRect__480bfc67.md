# CAnimationRect

Assembly: `TFlexCommandAPI`

## Summary

Implements the functionality of a rectangle whose top, left, right and bottom sides can be animated.

## Remarks

The CAnimationRect class encapsulates four CAnimationVariable objects and can represent in applications a rectangle. To use this class in application, just instantiate an object of this class, add it to animation controller using CAnimationController::AddAnimationObject and call AddTransition for each transition to be applied to left, right top and bottom coordinates.

## Constructors

### `CAnimationRect`

ID: `M:CAnimationRect.#ctor`

Constructs a CAnimationRect object.

Remarks: The object is constructed with default values for left, top, right and bottom, Object ID and Group ID, which will be set to 0. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationRect(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationRect.#ctor(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation rect object.

Parameters:
- `pt`: Coordinate of top-left corner.
- `sz`: Size of rectangle.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified top-left corner coordinates and size of rectangle, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationRect(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationRect.#ctor(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation rect object.

Parameters:
- `rect`: Specifies default rectangle.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified rect coordinates, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationRect(System.Int32,System.Int32,System.Int32,System.Int32,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationRect.#ctor(System.Int32,System.Int32,System.Int32,System.Int32,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation rect object.

Parameters:
- `nLeft`: Specifies coordinate of left bound.
- `nTop`: Specifies coordinate of top bound.
- `nRight`: Specifies coordinate of right bound.
- `nBottom`: Specifies coordinate of bottom bound.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified coordinates of each side, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

## Methods

### `CAnimationRect`

ID: `M:CAnimationRect.#ctor`

Constructs a CAnimationRect object.

Remarks: The object is constructed with default values for left, top, right and bottom, Object ID and Group ID, which will be set to 0. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationRect(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationRect.#ctor(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation rect object.

Parameters:
- `pt`: Coordinate of top-left corner.
- `sz`: Size of rectangle.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified top-left corner coordinates and size of rectangle, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationRect(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationRect.#ctor(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation rect object.

Parameters:
- `rect`: Specifies default rectangle.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified rect coordinates, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationRect(System.Int32,System.Int32,System.Int32,System.Int32,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationRect.#ctor(System.Int32,System.Int32,System.Int32,System.Int32,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation rect object.

Parameters:
- `nLeft`: Specifies coordinate of left bound.
- `nTop`: Specifies coordinate of top bound.
- `nRight`: Specifies coordinate of right bound.
- `nBottom`: Specifies coordinate of bottom bound.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified coordinates of each side, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

### `AddTransition(CBaseTransition*,CBaseTransition*,CBaseTransition*,CBaseTransition*)`

ID: `M:CAnimationRect.AddTransition(CBaseTransition*,CBaseTransition*,CBaseTransition*,CBaseTransition*)`

Adds transitions for left, top, right and bottom coordinates.

Parameters:
- `pLeftTransition`: Specifies transition for the left side.
- `pTopTransition`: Specifies transition for the top side.
- `pRightTransition`: Specifies transition for the right side.
- `pBottomTransition`: Specifies transition for the bottom side.

Remarks: Call this function to add the specified transitions to the internal list of transitions to be applied to animation variables for each rectangle sides. When you add transitions, they are not applied immediately and stored in an internal list. Transitions are applied (added to a storyboard for a particular value) when you call CAnimationController::AnimateGroup. If you don't need to apply a transition to one of the rectangle sides, you can pass NULL.

### `GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationRect.GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Puts the encapsulated animation variables into a list.

Parameters:
- `lst`: When the function returns, it contains pointers to four CAnimationVariable objects representing coordinates of rectangle.

### `GetBottom`

ID: `M:CAnimationRect.GetBottom`

Provides access to CAnimationVariable representing bottom coordinate.

Returns: A reference to encapsulated CAnimationVariable representing bottom coordinate.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing the bottom coordinate.

### `GetDefaultValue`

ID: `M:CAnimationRect.GetDefaultValue`

Returns the default values for rectangle's bounds.

Returns: A CRect value containing defaults for left, right, top and bottom.

Remarks: Call this function to retrieve default value, which was previously set by constructor or SetDefaultValue.

### `GetLeft`

ID: `M:CAnimationRect.GetLeft`

Provides access to CAnimationVariable representing left coordinate.

Returns: A reference to encapsulated CAnimationVariable representing left coordinate.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing the left coordinate.

### `GetRight`

ID: `M:CAnimationRect.GetRight`

Provides access to CAnimationVariable representing right coordinate.

Returns: A reference to encapsulated CAnimationVariable representing right coordinate.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing the right coordinate.

### `GetTop`

ID: `M:CAnimationRect.GetTop`

Provides access to CAnimationVariable representing top coordinate.

Returns: A reference to encapsulated CAnimationVariable representing top coordinate.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing the top coordinate.

### `GetValue(CRect*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationRect.GetValue(CRect*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Returns current value.

Parameters:
- `rect`: Output. Contains the current value when this method returns.

Returns: TRUE, if the current value was successfully retrieved; otherwise FALSE.

Remarks: Call this function to retrieve the current value of animation rectangle. If this method fails or underlying COM objects for left, top, right and bottom have not been initialized, rect contains default value, which was previously set in constructor or by SetDefaultValue.

### `SetDefaultValue(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationRect.SetDefaultValue(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Sets default value.

Parameters:
- `rect`: Specifies new default values for left, top, right and bottom.

Remarks: Use this function to set a default value to animation object. This methods assigns default values to rectangle's bounds. It also recreates underlying COM objects if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Assign(tagRECT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationRect.op_Assign(tagRECT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Assigns rect to CAnimationRect.

Parameters:
- `rect`: The new value of animation rectangle.

Remarks: It's recommended to do that before animation start, because this operator calls SetDefaultValue, which recreates the underlying COM objects for color components if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Implicit~tagRECT`

ID: `M:CAnimationRect.op_Implicit~tagRECT`

Converts a CAnimationRect to RECT.

Returns: Current value of animation rectangle as RECT.

Remarks: This function internally calls GetValue. If GetValue for some reason fails, the returned RECT will contain default values for all rectangle coordinates.

## Fields

### `m_bFixedSize`

ID: `F:CAnimationRect.m_bFixedSize`

Specifies whether the rectangle has fixed size.

Remarks: If this member is true, then the size of rectangle is fixed and right and bottom values are recalculated each time the top-left corner is moved according to the fixed size. Set this value to TRUE to easily move the rectangle around the screen. In this case transitions applied to right and bottom coordinates are ignored. The size is stored internally when you construct the object and/or call SetDefaultValue. By default this member is set to FALSE.

### `m_bottomValue`

ID: `F:CAnimationRect.m_bottomValue`

The encapsulated animation variable that represents Bottom bound of animation rectangle.

### `m_leftValue`

ID: `F:CAnimationRect.m_leftValue`

The encapsulated animation variable that represents Left bound of animation rectangle.

### `m_rightValue`

ID: `F:CAnimationRect.m_rightValue`

The encapsulated animation variable that represents Right bound of animation rectangle.

### `m_szInitial`

ID: `F:CAnimationRect.m_szInitial`

Specifies initial size of animation rectangle.

### `m_topValue`

ID: `F:CAnimationRect.m_topValue`

The encapsulated animation variable that represents Top bound of animation rectangle.
