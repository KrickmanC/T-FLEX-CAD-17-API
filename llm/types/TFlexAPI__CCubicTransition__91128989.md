# CCubicTransition

Assembly: `TFlexAPI`

## Summary

Encapsulates a cubic transition.

## Remarks

During a cubic transition, the value of the animation variable changes from its initial value to a specified final value over the duration of the transition, ending at a specified velocity. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CCubicTransition(System.Double,System.Double,System.Double)`

ID: `M:CCubicTransition.#ctor(System.Double,System.Double,System.Double)`

Constructs a transition object and initializes its parameters.

Parameters:
- `duration`: The duration of the transition.
- `finalValue`: The value of the animation variable at the end of the transition.
- `finalVelocity`: The velocity of the variable at the end of the transition.

## Methods

### `CCubicTransition(System.Double,System.Double,System.Double)`

ID: `M:CCubicTransition.#ctor(System.Double,System.Double,System.Double)`

Constructs a transition object and initializes its parameters.

Parameters:
- `duration`: The duration of the transition.
- `finalValue`: The value of the animation variable at the end of the transition.
- `finalVelocity`: The velocity of the variable at the end of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CCubicTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblFinalValue`

ID: `F:CCubicTransition.m_dblFinalValue`

The value of the animation variable at the end of the transition.

### `m_dblFinalVelocity`

ID: `F:CCubicTransition.m_dblFinalVelocity`

The velocity of the variable at the end of the transition.

### `m_duration`

ID: `F:CCubicTransition.m_duration`

The duration of the transition.
