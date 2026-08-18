# CAnimationSize

Assembly: `TFlexCommandAPI`

## Summary

Implements the functionality of a size object whose dimensions can be animated.

## Remarks

The CAnimationSize class encapsulates two CAnimationVariable objects and can represent in applications a size. For example, you can use this class to animate a size of any two dimensional object on the screen (like rectangle, control etc). To use this class in application, just instantiate an object of this class, add it to animation controller using CAnimationController::AddAnimationObject and call AddTransition for each transition to be applied to Width and/or Height.

## Constructors

### `CAnimationSize`

ID: `M:CAnimationSize.#ctor`

Constructs an animation size object.

Remarks: The object is constructed with default values for width, height, Object ID and Group ID, which will be set to 0. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationSize(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationSize.#ctor(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation size object.

Parameters:
- `szDefault`: Specifies default size.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified values for width, height, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

## Methods

### `CAnimationSize`

ID: `M:CAnimationSize.#ctor`

Constructs an animation size object.

Remarks: The object is constructed with default values for width, height, Object ID and Group ID, which will be set to 0. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationSize(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationSize.#ctor(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation size object.

Parameters:
- `szDefault`: Specifies default size.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified values for width, height, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

### `AddTransition(CBaseTransition*,CBaseTransition*)`

ID: `M:CAnimationSize.AddTransition(CBaseTransition*,CBaseTransition*)`

Adds transitions for Width and Height.

Parameters:
- `pCXTransition`: A pointer to transition for Width.
- `pCYTransition`: A pointer to transition for Height.

Remarks: Call this function to add the specified transitions to the internal list of transitions to be applied to animation variables for Width and Height. When you add transitions, they are not applied immediately and stored in an internal list. Transitions are applied (added to a storyboard for a particular value) when you call CAnimationController::AnimateGroup. If you don't need to apply a transition to one of dimensions, you can pass NULL.

### `GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationSize.GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Puts the encapsulated animation variables into a list.

Parameters:
- `lst`: When the function returns, it contains pointers to two CAnimationVariable objects representing the width and height.

### `GetCX`

ID: `M:CAnimationSize.GetCX`

Provides access to CAnimationVariable representing Width.

Returns: A reference to encapsulated CAnimationVariable representing Width.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing Width.

### `GetCY`

ID: `M:CAnimationSize.GetCY`

Provides access to CAnimationVariable representing Height.

Returns: A reference to encapsulated CAnimationVariable representing Height.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing Height.

### `GetDefaultValue`

ID: `M:CAnimationSize.GetDefaultValue`

Returns the default values for Width and Height.

Returns: A CSize object containing default values.

Remarks: Call this function to retrieve default value, which was previously set by constructor or SetDefaultValue.

### `GetValue(CSize*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationSize.GetValue(CSize*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Returns current value.

Parameters:
- `szValue`: Output. Contains the current value when this method returns.

Returns: TRUE, if the current value was successfully retrieved; otherwise FALSE.

Remarks: Call this function to retrieve the current value of animation size. If this method fails or underlying COM objects for Width and Size have not been initialized, szValue contains default value, which was previously set in constructor or by SetDefaultValue.

### `SetDefaultValue(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationSize.SetDefaultValue(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Sets default value.

Parameters:
- `szDefault`: Specifies new default size.

Remarks: Use this function to set a default value to animation object. This methods assigns default values to Width and Height of animation size. It also recreates underlying COM objects if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Assign(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationSize.op_Assign(CSize!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Assigns szSrc to CAnimationSize.

Parameters:
- `szSrc`: Refers to CSize or SIZE.

Remarks: Assigns szSrc to CAnimationSize. It's recommended to do that before animation start, because this operator calls SetDefaultValue, which recreates the underlying COM objects for Width and Height if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Implicit~CSize`

ID: `M:CAnimationSize.op_Implicit~CSize`

Converts a CAnimationSize to a CSize.

Returns: Current value of animation size as CSize.

Remarks: This function internally calls GetValue. If GetValue for some reason fails, the returned size will contain default values for Width and Height.

## Fields

### `m_cxValue`

ID: `F:CAnimationSize.m_cxValue`

The encapsulated animation variable that represents width of animation size.

### `m_cyValue`

ID: `F:CAnimationSize.m_cyValue`

The encapsulated animation variable that represents height of animation size.
