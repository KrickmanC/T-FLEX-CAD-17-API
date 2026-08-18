# CLinearTransitionFromSpeed

Assembly: `TFlexAPI`

## Summary

Encapsulates a linear-speed transition.

## Remarks

During a linear-speed transition, the value of the animation variable changes at a specified rate. The duration of the transition is determined by the difference between the initial value and the specified final value. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CLinearTransitionFromSpeed(System.Double,System.Double)`

ID: `M:CLinearTransitionFromSpeed.#ctor(System.Double,System.Double)`

Constructs a linear-speed transition object and initializes it with speed and final value.

Parameters:
- `dblSpeed`: The absolute value of the variable's velocity.
- `dblFinalValue`: The value of the animation variable at the end of the transition.

## Methods

### `CLinearTransitionFromSpeed(System.Double,System.Double)`

ID: `M:CLinearTransitionFromSpeed.#ctor(System.Double,System.Double)`

Constructs a linear-speed transition object and initializes it with speed and final value.

Parameters:
- `dblSpeed`: The absolute value of the variable's velocity.
- `dblFinalValue`: The value of the animation variable at the end of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CLinearTransitionFromSpeed.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblFinalValue`

ID: `F:CLinearTransitionFromSpeed.m_dblFinalValue`

The value of the animation variable at the end of the transition.

### `m_dblSpeed`

ID: `F:CLinearTransitionFromSpeed.m_dblSpeed`

The absolute value of the variable's velocity.
