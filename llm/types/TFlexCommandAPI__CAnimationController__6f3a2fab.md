# CAnimationController

Assembly: `TFlexCommandAPI`

## Summary

Implements the animation controller, which provides a central interface for creating and managing UI animations.

## Remarks

The CAnimationController class is the key class that manages animations. You may create one or more instances of animation controller in an application and, optionally, connect an instance of animation controller to a CWnd object using CAnimationController::SetRelatedWnd. This connection is required to send WM_PAINT messages to the related window automatically when animation manager status has changed or animation timer has been updated. If you do not enable this relation, you must redraw a window that displays an animation manually. For this purpose you can derive a class from CAnimationController and override OnAnimationManagerStatusChanged and/or OnAnimationTimerPostUpdate and invalidate one or more windows when necessary.

## Constructors

### `CAnimationController`

ID: `M:CAnimationController.#ctor`

Constructs an animation controller.

## Methods

### `CAnimationController`

ID: `M:CAnimationController.#ctor`

Constructs an animation controller.

### `AddAnimationObject(CAnimationBaseObject*)`

ID: `M:CAnimationController.AddAnimationObject(CAnimationBaseObject*)`

Adds an animation object to a group that belongs to the animation controller.

Parameters:
- `pObject`: A pointer to an animation object.

Returns: A pointer to existing or new animation group where pObject has been added if function succeeds; NULL if pObject has already been added to a group that belongs to another animation controller.

Remarks: Call this method to add an animation object to the animation controller. An object will be added to a group according to object's GroupID (see CAnimationBaseObject::SetID). The animation controller will create a new group if it's the first object being added with the specified GroupID. An animation object can be added to one animation controller only. If you need to add an object to another controller, call RemoveAnimationObject first. If you call SetID with new GroupID for an object that has been already added to a group, the object will be removed from the old group and added to another group with specified ID.

### `AddKeyframeToGroup(System.UInt32,CBaseKeyFrame*)`

ID: `M:CAnimationController.AddKeyframeToGroup(System.UInt32,CBaseKeyFrame*)`

Adds a keyframe to group.

Parameters:
- `nGroupID`: Specifies Group ID.
- `pKeyframe`: A pointer to a keyframe.

Returns: TRUE if the function succeeds; otherwise FALSE.

Remarks: Usually you don't need to call this method, use CAnimationController::CreateKeyframe instead, which creates and adds the created keyframe to a group automatically.

### `AnimateGroup(System.UInt32,System.Int32)`

ID: `M:CAnimationController.AnimateGroup(System.UInt32,System.Int32)`

Prepares a group to run animation and optionally schedules it.

Parameters:
- `nGroupID`: Specifies GroupID.
- `bScheduleNow`: Specifies whether to run animation right away.

Returns: TRUE if animation was successfully scheduled and run.

Remarks: This method does the actual work creating storyboard, adding animation variables, applying transitions and setting keyframes. It's possible to delay scheduling if you set bScheduleNow to FALSE. In this case the specified group will hold a storyboard that has been set up for animation. At that point you can setup events for the storyboard and animation variables. When you actually need to run the animation call CAnimationController::ScheduleGroup.

### `CleanUpGroup(CAnimationGroup*)`

ID: `M:CAnimationController.CleanUpGroup(CAnimationGroup*)`

A helper that cleans up the group.

Parameters:
- `pGroup`: A pointer to animation group to clean.

Remarks: This method removes all transitions and keyframes from the specified group.

### `CleanUpGroup(System.UInt32)`

ID: `M:CAnimationController.CleanUpGroup(System.UInt32)`

Called by the framework to clean up the group when animation has been scheduled.

Parameters:
- `nGroupID`: Specifies GroupID.

Remarks: This method removes all transitions and keyframes from the specified group, because they are not relevant after an animation has been scheduled.

### `CreateKeyframe(System.UInt32,CBaseKeyFrame*,System.Double)`

ID: `M:CAnimationController.CreateKeyframe(System.UInt32,CBaseKeyFrame*,System.Double)`

Creates a keyframe that depends on other keyframe with optional offset in seconds and adds it to the specified group.

Parameters:
- `nGroupID`: Specifies Group ID for which keyframe is created.
- `pKeyframe`: A pointer to base keyframe for this keyframe.
- `offset`: Offset in seconds from the base keyframe specified by pKeyframe.

Returns: A pointer to newly created keyframe if the function succeeds.

Remarks: You can store the returned pointer and base other keyframes on the newly created keyframe (see the second overload). It's possible to begin transitions at keyframes - see CBaseTransition::SetKeyframes. You don't need to delete keyframes created in this way, because they are deleted automatically by animation groups. Be careful when creating keyframes based on other keyframes and transitions and avoid circular references.

### `CreateKeyframe(System.UInt32,CBaseTransition*)`

ID: `M:CAnimationController.CreateKeyframe(System.UInt32,CBaseTransition*)`

Creates a keyframe that depends on transition and adds it to the specified group.

Parameters:
- `nGroupID`: Specifies Group ID for which keyframe is created.
- `pTransition`: A pointer to transition. Keyframe will be inserted to storyboard after this transition.

Returns: A pointer to newly created keyframe if the function succeeds.

Remarks: You can store the returned pointer and base other keyframes on the newly created keyframe (see the second overload). It's possible to begin transitions at keyframes - see CBaseTransition::SetKeyframes. You don't need to delete keyframes created in this way, because they are deleted automatically by animation groups. Be careful when creating keyframes based on other keyframes and transitions and avoid circular references.

### `Dispose`

ID: `M:CAnimationController.Dispose`

The destructor. Called when animation controller object is being destroyed.

### `EnableAnimationManagerEvent(System.Int32)`

ID: `M:CAnimationController.EnableAnimationManagerEvent(System.Int32)`

Sets or releases a handler to call when animation manager's status changes.

Parameters:
- `bEnable`: Specifies whether to set or release a handler.

Returns: TRUE if the handler was successfully set or released.

Remarks: When a handler is set (enabled) Windows Animation calls OnAnimationManagerStatusChanged when animation manager's status changes.

### `EnableAnimationTimerEventHandler(System.Int32,__MIDL___MIDL_itf_UIAnimation_0000_0012_0001)`

ID: `M:CAnimationController.EnableAnimationTimerEventHandler(System.Int32,__MIDL___MIDL_itf_UIAnimation_0000_0012_0001)`

Sets or releases a handler for timing events and handler for timing updates.

Parameters:
- `bEnable`: Specifies whether to set or release the handlers.
- `idleBehavior`: Specifies idle behavior for timer update handler.

Returns: TRUE if handlers were successfully set or released; FALSE if this method is called for a second time without releasing the handlers first, or if any other error occurs.

Remarks: When the handlers are set (enabled) Windows Animation API calls OnAnimationTimerPreUpdate, OnAnimationTimerPostUpdate, OnRenderingTooSlow methods. You need to enable animation timers to allow Windows Animation API update storyboards. Otherwise you'll need to call CAnimationController::UpdateAnimationManager in order to direct the animation manager to update the values of all animation variables.

### `EnablePriorityComparisonHandler(System.UInt64)`

ID: `M:CAnimationController.EnablePriorityComparisonHandler(System.UInt64)`

Sets or releases the priority comparison handler to call to determine whether a scheduled storyboard can be cancelled, concluded, trimmed or compressed.

Parameters:
- `dwHandlerType`: A combination of UI_ANIMATION_PHT_ flags (see remarks), which specifies what handlers to set or release.

Returns: TRUE if the handler was successfully set or released.

Remarks: When a handler is set (enabled) Windows Animation calls the following virtual methods depending on dwHandlerType: OnHasPriorityCancel, OnHasPriorityConclude, OnHasPriorityTrim, OnHasPriorityCompress. dwHandler can be a combination of the following flags: UI_ANIMATION_PHT_NONE - release all handlers UI_ANIMATION_PHT_CANCEL - set Cancel comparison handler UI_ANIMATION_PHT_CONCLUDE - set Conclude comparison handler UI_ANIMATION_PHT_COMPRESS - set Compress comparison handler UI_ANIMATION_PHT_TRIM - set Trim comparison handler UI_ANIMATION_PHT_CANCEL_REMOVE - remove Cancel comparison handler UI_ANIMATION_PHT_CONCLUDE_REMOVE - remove Conclude comparison handler UI_ANIMATION_PHT_COMPRESS_REMOVE - remove Compress comparison handler UI_ANIMATION_PHT_TRIM_REMOVE - remove Trim comparison handler

### `EnableStoryboardEventHandler(System.UInt32,System.Int32)`

ID: `M:CAnimationController.EnableStoryboardEventHandler(System.UInt32,System.Int32)`

Sets or releases a handler for storyboard status and update events.

Parameters:
- `nGroupID`: Specifies Group ID.
- `bEnable`: Specifies whether to set or release a handler.

Returns: TRUE if the handler was successfully set or released; FALSE if the specified animation group is now found or animation for the specified group has not been initiated and its internal storyboard is NULL.

Remarks: When a handler is set (enabled) Windows Animation API calls OnStoryboardStatusChanges and OnStoryboardUpdated virtual methods. A handler must be set after CAnimationController::Animate has been called for the specified animation group, because it creates encapsulated IUIAnimationStoryboard object.

### `FindAnimationGroup(IUIAnimationStoryboard*)`

ID: `M:CAnimationController.FindAnimationGroup(IUIAnimationStoryboard*)`

Finds an animation group by its storyboard.

Parameters:
- `pStoryboard`: A pointer to a storyboard.

Returns: A pointer to animation group if succeeds, or NULL if no group plays the specified storyboard.

Remarks: This method is usually called from event handlers to find a group by pointer to storyboard that comes as a parameter to an event handler.

### `FindAnimationGroup(System.UInt32)`

ID: `M:CAnimationController.FindAnimationGroup(System.UInt32)`

Finds an animation group by its Group ID.

Parameters:
- `nGroupID`: Specifies a GroupID.

Returns: A pointer to animation group or NULL if the group with specified ID is not found.

Remarks: Use this method to find an animation group at runtime. A group is created and added to the internal list of animation groups when a first animation object with particular GroupID is being added to animation controller.

### `FindAnimationObject(IUIAnimationVariable*,CAnimationBaseObject**,CAnimationGroup**)`

ID: `M:CAnimationController.FindAnimationObject(IUIAnimationVariable*,CAnimationBaseObject**,CAnimationGroup**)`

Finds animation object containing a specified animation variable.

Parameters:
- `pVariable`: A pointer to animation variable.
- `ppObject`: Output. Contains a pointer to animation object or NULL.
- `ppGroup`: Output. Contains a pointer to animation group that holds the animation object, or NULL.

Returns: TRUE if object was found; otherwise FALSE.

Remarks: Called from event handlers when it's required to find an animation object from incoming animation variable.

### `GetKeyframeStoryboardStart`

ID: `M:CAnimationController.GetKeyframeStoryboardStart`

Returns a keyframe that identifies start of storyboard.

Returns: A pointer to base keyframe, which identifies start of storyboard.

Remarks: Obtain this keyframe to base any other keyframes or transitions on the moment in time when a storyboard starts.

### `GetUIAnimationManager`

ID: `M:CAnimationController.GetUIAnimationManager`

Provides access to encapsulated IUIAnimationManager object.

Returns: A pointer to IUIAnimationManager interface or NULL, if creation of animation manager failed.

Remarks: If current OS does not support Windows Animation API, this method returns NULL and after that all subsequent calls on CAnimationController::IsValid return FALSE. You may need to access IUIAnimationManager in order to call its interface methods, which are not wrapped by animation controller.

### `GetUIAnimationTimer`

ID: `M:CAnimationController.GetUIAnimationTimer`

Provides access to encapsulated IUIAnimationTimer object.

Returns: A pointer to IUIAnimationTimer interface or NULL, if creation of animation timer failed.

Remarks: If current OS does not support Windows Animation API, this method returns NULL and after that all subsequent calls on CAnimationController::IsValid return FALSE.

### `GetUITransitionFactory`

ID: `M:CAnimationController.GetUITransitionFactory`

A pointer to IUIAnimationTransitionFactory interface or NULL, if creation of transition library failed.

Returns: A pointer to IUIAnimationTransitionFactory or NULL, if creation of transition factory failed.

Remarks: If current OS does not support Windows Animation API, this method returns NULL and after that all subsequent calls on CAnimationController::IsValid return FALSE.

### `GetUITransitionLibrary`

ID: `M:CAnimationController.GetUITransitionLibrary`

Provides access to encapsulated IUIAnimationTransitionLibrary object.

Returns: A pointer to IUIAnimationTransitionLibrary interface or NULL, if creation of transition library failed.

Remarks: If current OS does not support Windows Animation API, this method returns NULL and after that all subsequent calls on CAnimationController::IsValid return FALSE.

### `IsAnimationInProgress`

ID: `M:CAnimationController.IsAnimationInProgress`

Tells whether at least one group is playing animation.

Returns: TRUE if there is an animation in progress for this animation controller; otherwise FALSE.

Remarks: Checks status of animation manager and returns TRUE if the status is UI_ANIMATION_MANAGER_BUSY.

### `IsValid`

ID: `M:CAnimationController.IsValid`

Tells whether animation controller is valid.

Returns: TRUE if animation controller is valid; otherwise FALSE.

Remarks: This method returns FALSE only if Windows Animation API is not supported on the current OS and creation of animation manager failed because it's not registered. You need to call GetUIAnimationManager at least once after initialization of COM libraries to cause setting of this flag.

### `OnAfterSchedule(CAnimationGroup*)`

ID: `M:CAnimationController.OnAfterSchedule(CAnimationGroup*)`

Called by the framework when an animation for the specified group has just been scheduled.

Parameters:
- `pGroup`: A pointer to an animation group, which has been scheduled.

Remarks: The default implementation removes keyframes from the specified group and transitions from animation variables that belong to the specified group. Can be overridden in a derived class to take any additional actions upon animation schedule.

### `OnAnimationIntegerValueChanged(CAnimationGroup*,CAnimationBaseObject*,IUIAnimationVariable*,System.Int32,System.Int32)`

ID: `M:CAnimationController.OnAnimationIntegerValueChanged(CAnimationGroup*,CAnimationBaseObject*,IUIAnimationVariable*,System.Int32,System.Int32)`

Called by the framework when integer value of animation variable has changed.

Parameters:
- `pGroup`: A pointer to an animation group that holds an animation object whose value has changed.
- `pObject`: A pointer to an animation object that contains an animation variable whose value has changed.
- `variable`: A pointer to an animation variable.
- `newValue`: Specifies new value.
- `prevValue`: Specifies previous value.

Remarks: This method is called if you enable animation variable events with EnableIntegerValueChangedEvent called for a specific animation variable or animation object. It can be overridden in a derived class to take application-specific actions.

### `OnAnimationManagerStatusChanged(__MIDL___MIDL_itf_UIAnimation_0000_0000_0002,__MIDL___MIDL_itf_UIAnimation_0000_0000_0002)`

ID: `M:CAnimationController.OnAnimationManagerStatusChanged(__MIDL___MIDL_itf_UIAnimation_0000_0000_0002,__MIDL___MIDL_itf_UIAnimation_0000_0000_0002)`

Called by the framework in response to StatusChanged event from animation manager.

Parameters:
- `newStatus`: New animation manager status.
- `previousStatus`: Previous animation manager status.

Remarks: This method is called if you enable animation manager events with EnableAnimationManagerEvent. It can be overridden in a derived class to take application-specific actions. The default implementation updates a related window if it has been set with SetRelatedWnd.

### `OnAnimationTimerPostUpdate`

ID: `M:CAnimationController.OnAnimationTimerPostUpdate`

Called by the framework after an animation update is finished.

Remarks: This method is called if you enable timer event handlers using EnableAnimationTimerEventHandler. It can be overridden in a derived class to take application-specific actions.

### `OnAnimationTimerPreUpdate`

ID: `M:CAnimationController.OnAnimationTimerPreUpdate`

Called by the framework before an animation update begins.

Remarks: This method is called if you enable timer event handlers using EnableAnimationTimerEventHandler. It can be overridden in a derived class to take application-specific actions.

### `OnAnimationTimerRenderingTooSlow(System.UInt32)`

ID: `M:CAnimationController.OnAnimationTimerRenderingTooSlow(System.UInt32)`

Called by the framework when the rendering frame rate for an animation falls below a minimum desirable frame rate.

Parameters:
- `fps`: The current frame rate in frames per second.

Remarks: This method is called if you enable timer event handlers using EnableAnimationTimerEventHandler. It can be overridden in a derived class to take application-specific actions. The minimum desirable frame rate is specified by calling IUIAnimationTimer::SetFrameRateThreshold.

### `OnAnimationValueChanged(CAnimationGroup*,CAnimationBaseObject*,IUIAnimationVariable*,System.Double,System.Double)`

ID: `M:CAnimationController.OnAnimationValueChanged(CAnimationGroup*,CAnimationBaseObject*,IUIAnimationVariable*,System.Double,System.Double)`

Called by the framework when value of animation variable has changed.

Parameters:
- `pGroup`: A pointer to an animation group that holds an animation object whose value has changed.
- `pObject`: A pointer to an animation object that contains an animation variable whose value has changed.
- `variable`: A pointer to an animation variable.
- `newValue`: Specifies new value.
- `prevValue`: Specifies previous value.

Remarks: This method is called if you enable animation variable events with EnableValueChangedEvent called for a specific animation variable or animation object. It can be overridden in a derived class to take application-specific actions.

### `OnBeforeAnimationStart(CAnimationGroup*)`

ID: `M:CAnimationController.OnBeforeAnimationStart(CAnimationGroup*)`

Called by the framework right before the animation is scheduled.

Parameters:
- `pGroup`: A pointer to an animation group whose animation is about to start.

Remarks: This call is routed to related CWnd and can be overridden in a derived class to perform any additional actions before the animation starts for the specified group.

### `OnHasPriorityCancel(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

ID: `M:CAnimationController.OnHasPriorityCancel(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

Called by the framework to resolve scheduling conflicts.

Parameters:
- `pGroupScheduled`: The group that owns the currently scheduled storyboard.
- `pGroupNew`: The group that owns the new storyboard that is in scheduling conflict with the scheduled storyboard owned by pGroupScheduled.
- `priorityEffect`: The potential effect on pGroupNew if pGroupScheduled has a higher priority.

Returns: Should return TRUE if storyboard owned by pGroupNew has priority. Should return FALSE if storyboard owned by pGroupScheduled has priority.

Remarks: This method is called if you enable priority comparison events using CAnimationController::EnablePriorityComparisonHandler and specify UI_ANIMATION_PHT_CANCEL. It can be overridden in a derived class to take application-specific actions. Read Windows Animation API documentation for more information about Conflict Management (http://msdn.microsoft.com/en-us/library/dd371759(VS.85).aspx).

### `OnHasPriorityCompress(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

ID: `M:CAnimationController.OnHasPriorityCompress(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

Called by the framework to resolve scheduling conflicts.

Parameters:
- `pGroupScheduled`: The group that owns the currently scheduled storyboard.
- `pGroupNew`: The group that owns the new storyboard that is in scheduling conflict with the scheduled storyboard owned by pGroupScheduled.
- `priorityEffect`: The potential effect on pGroupNew if pGroupScheduled has a higher priority.

Returns: Should return TRUE if storyboard owned by pGroupNew has priority. Should return FALSE if storyboard owned by pGroupScheduled has priority.

Remarks: This method is called if you enable priority comparison events using CAnimationController::EnablePriorityComparisonHandler and specify UI_ANIMATION_PHT_COMPRESS. It can be overridden in a derived class to take application-specific actions. Read Windows Animation API documentation for more information about Conflict Management (http://msdn.microsoft.com/en-us/library/dd371759(VS.85).aspx).

### `OnHasPriorityConclude(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

ID: `M:CAnimationController.OnHasPriorityConclude(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

Called by the framework to resolve scheduling conflicts.

Parameters:
- `pGroupScheduled`: The group that owns the currently scheduled storyboard.
- `pGroupNew`: The group that owns the new storyboard that is in scheduling conflict with the scheduled storyboard owned by pGroupScheduled.
- `priorityEffect`: The potential effect on pGroupNew if pGroupScheduled has a higher priority.

Returns: Should return TRUE if storyboard owned by pGroupNew has priority. Should return FALSE if storyboard owned by pGroupScheduled has priority.

Remarks: This method is called if you enable priority comparison events using CAnimationController::EnablePriorityComparisonHandler and specify UI_ANIMATION_PHT_CONCLUDE. It can be overridden in a derived class to take application-specific actions. Read Windows Animation API documentation for more information about Conflict Management (http://msdn.microsoft.com/en-us/library/dd371759(VS.85).aspx).

### `OnHasPriorityTrim(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

ID: `M:CAnimationController.OnHasPriorityTrim(CAnimationGroup*,CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0008_0001)`

Called by the framework to resolve scheduling conflicts.

Parameters:
- `pGroupScheduled`: The group that owns the currently scheduled storyboard.
- `pGroupNew`: The group that owns the new storyboard that is in scheduling conflict with the scheduled storyboard owned by pGroupScheduled.
- `priorityEffect`: The potential effect on pGroupNew if pGroupScheduled has a higher priority.

Returns: Should return TRUE if storyboard owned by pGroupNew has priority. Should return FALSE if storyboard owned by pGroupScheduled has priority.

Remarks: This method is called if you enable priority comparison events using CAnimationController::EnablePriorityComparisonHandler and specify UI_ANIMATION_PHT_TRIM. It can be overridden in a derived class to take application-specific actions. Read Windows Animation API documentation for more information about Conflict Management (http://msdn.microsoft.com/en-us/library/dd371759(VS.85).aspx).

### `OnStoryboardStatusChanged(CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001)`

ID: `M:CAnimationController.OnStoryboardStatusChanged(CAnimationGroup*,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001)`

Called by the framework when storyboard status has changed.

Parameters:
- `pGroup`: A pointer to an animation group that owns the storyboard whose status has changed.
- `newStatus`: Specifies the new status.
- `previousStatus`: Specifies the previous status.

Remarks: This method is called if you enable storyboard events using CAnimationController::EnableStoryboardEventHandler. It can be overridden in a derived class to take application-specific actions.

### `OnStoryboardUpdated(CAnimationGroup*)`

ID: `M:CAnimationController.OnStoryboardUpdated(CAnimationGroup*)`

Called by the framework when storyboard has been updated.

Parameters:
- `pGroup`: A pointer to a group that owns the storyboard.

Remarks: This method is called if you enable storyboard events using CAnimationController::EnableStoryboardEventHandler. It can be overridden in a derived class to take application-specific actions.

### `RemoveAllAnimationGroups`

ID: `M:CAnimationController.RemoveAllAnimationGroups`

Removes all animation groups from animation controller.

Remarks: All groups will be deleted, their pointer, if stored at the application level, must be invalidated. If CAnimationGroup::m_bAutodestroyAnimationObjects for a group being deleted is TRUE, all animation objects that belong to that group will be deleted; otherwise their references to parent animation controller will be set to NULL and they can be added to another controller.

### `RemoveAnimationGroup(System.UInt32)`

ID: `M:CAnimationController.RemoveAnimationGroup(System.UInt32)`

Removes an animation group with specified ID from animation controller.

Parameters:
- `nGroupID`: Specifies animation group ID.

Remarks: This method removes an animation group from the internal list of groups and deletes it, therefore if you stored a pointer to that animation group, it must be invalidated. If CAnimationGroup::m_bAutodestroyAnimationObjects is TRUE, all animation objects that belong to that group will be deleted; otherwise their references to parent animation controller will be set to NULL and they can be added to another controller.

### `RemoveAnimationObject(CAnimationBaseObject*,System.Int32)`

ID: `M:CAnimationController.RemoveAnimationObject(CAnimationBaseObject*,System.Int32)`

Remove an animation object from animation controller.

Parameters:
- `pObject`: A pointer to an animation object.
- `bNoDelete`: If this parameter is TRUE the object will not be deleted upon remove.

Remarks: Removes an animation object from animation controller and animation group. Call this function if a particular object should not be animated anymore, or if you need to move the object to another animation controller. In the last case bNoDelete must be TRUE.

### `RemoveTransitions(System.UInt32)`

ID: `M:CAnimationController.RemoveTransitions(System.UInt32)`

Removes transitions from animation objects that belong to the specified group.

Parameters:
- `nGroupID`: Specifies Group ID.

Remarks: The group loops over its animation objects and calls ClearTransitions(FALSE) for each animation object. This method is called by the framework after animation has been scheduled.

### `ScheduleGroup(System.UInt32,System.Double)`

ID: `M:CAnimationController.ScheduleGroup(System.UInt32,System.Double)`

Schedules an animation.

Parameters:
- `nGroupID`: Specifies animation Group ID to schedule.
- `time`: Specifies time to schedule.

Returns: TRUE if animation was scheduled successfully. FALSE if storyboard has not been created, or other error occurs.

Remarks: You must call AnimateGroup with parameter bScheduleNow set to FALSE prior ScheduleGroup. You can specify the desired animation time obtained from IUIAnimationTimer::GetTime. If the time parameter is 0.0, the animation is scheduled for the current time.

### `SetRelatedWnd(CWnd*)`

ID: `M:CAnimationController.SetRelatedWnd(CWnd*)`

Establishes a relationship between animation controller and a window.

Parameters:
- `pWnd`: A pointer to window object to set.

Remarks: If a related CWnd object is set, the animation controller can automatically update it (send WM_PAINT message) when the status of animation manager has changed or timer post update event has occurred.

### `UpdateAnimationManager`

ID: `M:CAnimationController.UpdateAnimationManager`

Directs the animation manager to update the values of all animation variables.

Remarks: Calling this method advances the animation manager to current time, changing statuses of storyboards as necessary and updating any animation variables to appropriate interpolated values. Internally this method calls IUIAnimationTimer::GetTime(timeNow) and IUIAnimationManager::Update(timeNow). Override this method in a derived class to customize this behavior.

## Fields

### `g_KeyframeStoryboardStart`

ID: `F:CAnimationController.g_KeyframeStoryboardStart`

A keyframe that represents start of storyboard.

### `m_bIsValid`

ID: `F:CAnimationController.m_bIsValid`

Specifies whether an animation controller is valid or not. This member is set to FALSE if current OS does not support Windows Animation API.

### `m_lstAnimationGroups`

ID: `F:CAnimationController.m_lstAnimationGroups`

A list of animation groups that belong to this animation controller.

### `m_pAnimationManager`

ID: `F:CAnimationController.m_pAnimationManager`

Stores a pointer to Animation Manager COM object.

### `m_pAnimationTimer`

ID: `F:CAnimationController.m_pAnimationTimer`

Stores a pointer to Animation Timer COM object.

### `m_pRelatedWnd`

ID: `F:CAnimationController.m_pRelatedWnd`

A pointer to a related CWnd object, which can be automatically redrawn when the status of animation manager has changed, or post update event has occurred. Can be NULL.

### `m_pTransitionFactory`

ID: `F:CAnimationController.m_pTransitionFactory`

Stores a pointer to Transition Factory COM object.

### `m_pTransitionLibrary`

ID: `F:CAnimationController.m_pTransitionLibrary`

Stores a pointer to Transition Library COM object.
