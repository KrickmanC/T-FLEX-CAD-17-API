# RGK.Common

Assembly: `TFlexAPI`
Namespace: `RGK`

## Methods

### `CombinePartialResult(RGK.Common.Result,RGK.Common.Result)`

ID: `M:RGK.Common.CombinePartialResult(RGK.Common.Result,RGK.Common.Result)`

Returns: r - если !PartiallySucceeded(r) Success - если r == Success, r0 = Success PartialSuccess - если r == PartialSuccess, r0 = Success - если r == Success, r0 = PartialSuccess - если r == PartialSuccess, r0 = PartialSuccess

### `Failed(RGK.Common.Result)`

ID: `M:RGK.Common.Failed(RGK.Common.Result)`

Returns: r != Result::Success

Remarks: Проверка на наличие ошибки

### `PartiallySucceeded(RGK.Common.Result)`

ID: `M:RGK.Common.PartiallySucceeded(RGK.Common.Result)`

Returns: r == Result::Success или r == Result::PartialSuccess

Remarks: Проверка на наличие ошибки

### `Succeeded(RGK.Common.Result)`

ID: `M:RGK.Common.Succeeded(RGK.Common.Result)`

Returns: r == Result::Success

Remarks: Проверка на наличие ошибки

## Members

### `ErrorReportPtr`

ID: `D:RGK.Common.ErrorReportPtr`
