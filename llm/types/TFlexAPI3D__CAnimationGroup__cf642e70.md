# CAnimationGroup

Assembly: `TFlexAPI3D`

## Summary

Implements an animation group, which combines an animation storyboard, animation objects and transitions to define an animation.

## Remarks

Animation groups are created automatically by animation controller (CAnimationController) when you add animation objects using CAnimationController::AddAnimationObject. An animation group is identified by GroupID, which is usually taken as a parameter to manipulate animation groups. The GroupID is taken from the first animation object being added to a new animation group. An encapsulated animation storyboard is created after you call CAnimationController::AnimateGroup and can be accessed via public member m_pStoryboard.

## Constructors

### `CAnimationGroup(CAnimationController*,System.UInt32)`

ID: `M:CAnimationGroup.#ctor(CAnimationController*,System.UInt32)`

Constructs an animation group.

Parameters:
- `pParentController`: A pointer to animation controller that creates a group.
- `nGroupID`: Specifies GroupID.

## Methods

### `CAnimationGroup(CAnimationController*,System.UInt32)`

ID: `M:CAnimationGroup.#ctor(CAnimationController*,System.UInt32)`

Constructs an animation group.

Parameters:
- `pParentController`: A pointer to animation controller that creates a group.
- `nGroupID`: Specifies GroupID.

### `AddKeyframes(IUIAnimationStoryboard*,System.Int32)`

ID: `M:CAnimationGroup.AddKeyframes(IUIAnimationStoryboard*,System.Int32)`

A helper that adds keyframes to a storyboard.

Parameters:
- `pStoryboard`: A pointer to a storyboard COM object.
- `bAddDeep`: Specifies whether this method should add to the storyboard keyframes that depend on other keyframes.

### `AddTransitions(IUIAnimationStoryboard*,System.Int32)`

ID: `M:CAnimationGroup.AddTransitions(IUIAnimationStoryboard*,System.Int32)`

A helper that adds transitions to a storyboard.

Parameters:
- `pStoryboard`: A pointer to a storyboard COM object.
- `bDependOnKeyframes`: Specifies whether this method should add to the storyboard transitions that depend on other keyframes.

### `Animate(IUIAnimationManager*,IUIAnimationTimer*,System.Int32)`

ID: `M:CAnimationGroup.Animate(IUIAnimationManager*,IUIAnimationTimer*,System.Int32)`

Animates a group.

Parameters:
- `pManager`: 
- `pTimer`: 
- `bScheduleNow`: 

Returns: TRUE if the method succeeds; otherwise FALSE.

Remarks: This method creates an internal storyboard, creates and applies transitions and schedules an animation if bScheduleNow is TRUE. If bScheduleNow is FALSE, you need to call Schedule to start animation at the specified time.

### `ApplyTransitions`

ID: `M:CAnimationGroup.ApplyTransitions`

Applies transitions to animation objects.

Remarks: This method ASSERTS in debug mode if storyboard has not been created. It creates all transitions first, then adds "static" keyframes (keyframes that depend on offsets), adds transitions that do not depend on keyframes, adds keyframes depending on transitions and other keyframes, and at last adds transitions that depend on keyframes.

### `CreateTransitions`

ID: `M:CAnimationGroup.CreateTransitions`

A helper that creates COM transition objects.

Returns: TRUE is the method succeeds, otherwise FALSE.

### `Dispose`

ID: `M:CAnimationGroup.Dispose`

The destructor. Called when an animation group is being destroyed.

### `FindAnimationObject(IUIAnimationVariable*)`

ID: `M:CAnimationGroup.FindAnimationObject(IUIAnimationVariable*)`

Finds an animation object that contains the specified animation variable.

Parameters:
- `pVariable`: A pointer to animation variable.

Returns: A pointer to animation object, or NULL if animation object is not found.

### `GetGroupID`

ID: `M:CAnimationGroup.GetGroupID`

Returns GroupID.

Returns: A group identifier.

### `RemoveKeyframes`

ID: `M:CAnimationGroup.RemoveKeyframes`

Removes and optionally destroys all keyframes that belong to an animation group.

Remarks: If m_bAutodestroyKeyframes member is TRUE then keyframes are removed and destroyed, otherwise keyframes are just removed from the internal list of keyframes.

### `RemoveTransitions`

ID: `M:CAnimationGroup.RemoveTransitions`

Removes transitions from animation objects that belong to an animation group.

Remarks: If m_bAutoclearTransitions flag is set to TRUE, this method loops over all animation objects that belong to the group and calls CAnimationObject::ClearTransitions(FALSE).

### `Schedule(IUIAnimationTimer*,System.Double)`

ID: `M:CAnimationGroup.Schedule(IUIAnimationTimer*,System.Double)`

Schedules an animation at the specified time.

Parameters:
- `pTimer`: A pointer to animation timer.
- `time`: Specifies time to schedule the animation.

Returns: TRUE if the method succeeds; FALSE if the method fails or if Animate has not been called with bScheduleNow set to FALSE.

Remarks: Call this function to schedule an animation at the specified time. You must call Animate with bScheduleNow set to FALSE first.

### `SetAutodestroyTransitions(System.Int32)`

ID: `M:CAnimationGroup.SetAutodestroyTransitions(System.Int32)`

Directs all animation objects that belong to group automatically destroy transitions.

Parameters:
- `bAutoDestroy`: Specifies how to destroy transitions.

Remarks: Set this value to FALSE only if you allocate transitions on the stack. The default value is TRUE, therefore it's highly recommended to allocate transition objects using operator new.

## Fields

### `m_bAutoclearTransitions`

ID: `F:CAnimationGroup.m_bAutoclearTransitions`

Specifies how to clear transitions from animation objects that belong to group. If this member is TRUE, transitions are removed automatically when an animation has been scheduled. Otherwise you need to remove transitions manually.

### `m_bAutodestroyAnimationObjects`

ID: `F:CAnimationGroup.m_bAutodestroyAnimationObjects`

Specifies how to destroy animation objects. If this parameter is TRUE, animation objects will be destroyed automatically when the group is destroyed. Otherwise animation objects must be destroyed manually. The default value is FALSE. Set this value to TRUE only if all animation objects that belong to group are allocated dynamically with operator new.

### `m_bAutodestroyKeyframes`

ID: `F:CAnimationGroup.m_bAutodestroyKeyframes`

Specifies how to destroy keyframes. If this value is TRUE, all keyframes are removed and destroyed; otherwise they are removed from the list only. The default value is TRUE.

### `m_lstAnimationObjects`

ID: `F:CAnimationGroup.m_lstAnimationObjects`

Contains a list of animation objects.

### `m_lstKeyFrames`

ID: `F:CAnimationGroup.m_lstKeyFrames`

Contains a list of keyframes.

### `m_nGroupID`

ID: `F:CAnimationGroup.m_nGroupID`

A unique identifier of animation group.

### `m_pParentController`

ID: `F:CAnimationGroup.m_pParentController`

A pointer to animation controller this group belongs to.

### `m_pStoryboard`

ID: `F:CAnimationGroup.m_pStoryboard`

Points to animation storyboard. This pointer is valid only after call on Animate.
