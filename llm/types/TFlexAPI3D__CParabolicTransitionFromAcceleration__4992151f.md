# CParabolicTransitionFromAcceleration

Assembly: `TFlexAPI3D`

## Summary

Encapsulates a parabolic-acceleration transition.

## Remarks

During a parabolic-acceleration transition, the value of the animation variable changes from the initial value to the final value ending at a specified velocity. You can control how quickly the variable reaches the final value by specifying the rate of acceleration. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CParabolicTransitionFromAcceleration(System.Double,System.Double,System.Double)`

ID: `M:CParabolicTransitionFromAcceleration.#ctor(System.Double,System.Double,System.Double)`

Constructs a parabolic-acceleration transition and initializes it with specified parameters.

Parameters:
- `dblFinalValue`: The value of the animation variable at the end of the transition.
- `dblFinalVelocity`: The velocity of the animation variable at the end of the transition.
- `dblAcceleration`: The acceleration of the animation variable during the transition.

## Methods

### `CParabolicTransitionFromAcceleration(System.Double,System.Double,System.Double)`

ID: `M:CParabolicTransitionFromAcceleration.#ctor(System.Double,System.Double,System.Double)`

Constructs a parabolic-acceleration transition and initializes it with specified parameters.

Parameters:
- `dblFinalValue`: The value of the animation variable at the end of the transition.
- `dblFinalVelocity`: The velocity of the animation variable at the end of the transition.
- `dblAcceleration`: The acceleration of the animation variable during the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CParabolicTransitionFromAcceleration.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblAcceleration`

ID: `F:CParabolicTransitionFromAcceleration.m_dblAcceleration`

The acceleration of the animation variable during the transition.

### `m_dblFinalValue`

ID: `F:CParabolicTransitionFromAcceleration.m_dblFinalValue`

The value of the animation variable at the end of the transition.

### `m_dblFinalVelocity`

ID: `F:CParabolicTransitionFromAcceleration.m_dblFinalVelocity`

The velocity of the animation variable at the end of the transition.
