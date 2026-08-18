# CLinearTransition

Assembly: `TFlexAPI3D`

## Summary

Encapsulates a linear transition.

## Remarks

During a linear transition, the value of the animation variable transitions linearly from its initial value to a specified final value. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CLinearTransition(System.Double,System.Double)`

ID: `M:CLinearTransition.#ctor(System.Double,System.Double)`

Constructs a linear transition object and initializes it with duration and final value.

Parameters:
- `duration`: The duration of the transition.
- `dblFinalValue`: The value of the animation variable at the end of the transition.

## Methods

### `CLinearTransition(System.Double,System.Double)`

ID: `M:CLinearTransition.#ctor(System.Double,System.Double)`

Constructs a linear transition object and initializes it with duration and final value.

Parameters:
- `duration`: The duration of the transition.
- `dblFinalValue`: The value of the animation variable at the end of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CLinearTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblFinalValue`

ID: `F:CLinearTransition.m_dblFinalValue`

The value of the animation variable at the end of the transition.

### `m_duration`

ID: `F:CLinearTransition.m_duration`

The duration of the transition.
