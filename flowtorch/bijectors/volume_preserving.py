# Copyright (c) FlowTorch Development Team. All Rights Reserved
# SPDX-License-Identifier: MIT
from typing import Optional

import torch
import torch.distributions

import flowtorch
import flowtorch.distributions


class VolumePreserving(flowtorch.Bijector):
    def _log_abs_det_jacobian(
        self,
        x: torch.Tensor,
        y: torch.Tensor,
        params: Optional[flowtorch.ParamsModule] = None,
        context: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        # TODO: Confirm that this should involve `x`/`self.domain` and not
        # `y`/`self.codomain`
        return torch.zeros(
            x.size()[: -self.domain.event_dim],
            dtype=x.dtype,
            layout=x.layout,
            device=x.device,
        )