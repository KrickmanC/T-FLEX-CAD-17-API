# CAnimationValue

Assembly: `TFlexCommandAPI`

## Summary

Implements the functionality of animation object with one value.

## Remarks

The CAnimationValue class encapsulates a single CAnimationVariable object and can represent in applications a single animated value. For example, you can use this class for animated transparency (fade effect), angle (to rotate objects), or for any other case when you need to create an animation depending on a single animated value. To use this class in application, just instantiate an object of this class, add it to animation controller using CAnimationController::AddAnimationObject and call AddTransition for each transition to be applied to the value.

## Constructors

### `CAnimationValue`

ID: `M:CAnimationValue.#ctor`

Constructs a CAnimationValue object.

Remarks: Constructs CAnimationValue object with default properties: default value, Group ID and Object ID are set to 0.

### `CAnimationValue(System.Double,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationValue.#ctor(System.Double,System.UInt32,System.UInt32,System.UInt64)`

Constructs a CAnimationValue object.

Parameters:
- `dblDefaultValue`: Specifies default value.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: specifies user-defined data.

Remarks: Constructs CAnimationValue object with specified properties.

## Methods

### `CAnimationValue`

ID: `M:CAnimationValue.#ctor`

Constructs a CAnimationValue object.

Remarks: Constructs CAnimationValue object with default properties: default value, Group ID and Object ID are set to 0.

### `CAnimationValue(System.Double,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationValue.#ctor(System.Double,System.UInt32,System.UInt32,System.UInt64)`

Constructs a CAnimationValue object.

Parameters:
- `dblDefaultValue`: Specifies default value.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: specifies user-defined data.

Remarks: Constructs CAnimationValue object with specified properties.

### `AddTransition(CBaseTransition*)`

ID: `M:CAnimationValue.AddTransition(CBaseTransition*)`

Adds a transition to be applied to a value.

Parameters:
- `pTransition`: A pointer to transition object.

Remarks: Call this function to add a transition to internal list of transitions to be applied to an animation variable. When you add transitions, they are not applied immediately and stored in an internal list. Transitions are applied (added to a storyboard for a particular value) when you call CAnimationController::AnimateGroup.

### `GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationValue.GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Puts the encapsulated animation variable into a list.

Parameters:
- `lst`: When the function returns, it contains a pointer to CAnimationVariable representing the animated value.

### `GetValue(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationValue.GetValue(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Retrieves the current value.

Parameters:
- `dblValue`: Output. When the function returns it contains a current value of animation variable.

Returns: TRUE if the current value was retrieved successfully; otherwise FALSE.

Remarks: Call this function to retrieve the current value. This implementation calls the encapsulated COM object, and if the call fails, this method returns the default value that was previously set in constructor or with SetDefaultValue.

### `GetValue(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationValue.GetValue(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Retrieves the current value.

Parameters:
- `nValue`: Output. When the function returns it contains a current value of animation variable.

Returns: TRUE if the current value was retrieved successfully; otherwise FALSE.

Remarks: Call this function to retrieve the current value. This implementation calls the encapsulated COM object, and if the call fails, this method returns the default value that was previously set in constructor or with SetDefaultValue.

### `GetVariable`

ID: `M:CAnimationValue.GetVariable`

Provides access to encapsulated animation variable.

Returns: A reference to encapsulated animation variable.

Remarks: Use this method to access the encapsulated animation variable. From CAnimationVariable you get access to underlying IUIAnimationVariable object, whose pointer can be NULL if animation variable has not been created.

### `SetDefaultValue(System.Double)`

ID: `M:CAnimationValue.SetDefaultValue(System.Double)`

Sets default value.

Parameters:
- `dblDefaultValue`: Specifies the default value.

Remarks: Use this method to set a default value. A default value is returned to application when animation has not been started and/or underlying COM object has not been created. If the underlying COM object encapsulated in CAnimationVarible was already created, this method recreates it, therefore you might need to call EnableValueChanged/EnableIntegerValueChanged methods again.

### `op_Assign(System.Double)`

ID: `M:CAnimationValue.op_Assign(System.Double)`

Assigns a DOUBLE value to CAnimationValue.

Parameters:
- `dblVal`: Specifies the value to be assigned to Animation Value.

Remarks: Assigns a DOUBLE value to CAnimationValue. This value is set as a default value for encapsulated animation variable. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Assign(System.Int32)`

ID: `M:CAnimationValue.op_Assign(System.Int32)`

Assigns an INT32 value to CAnimationValue.

Parameters:
- `nVal`: Specifies the value to be assigned to Animation Value.

Remarks: Assigns an INT32 value to CAnimationValue. This value is set as a default value for encapsulated animation variable. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

## Fields

### `m_value`

ID: `F:CAnimationValue.m_value`

The encapsulated animation variable that represents animation value.
