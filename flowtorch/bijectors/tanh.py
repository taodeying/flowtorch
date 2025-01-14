# Copyright (c) Meta Platforms, Inc

import math
from typing import Optional

import torch
import torch.distributions.constraints as constraints
import torch.nn.functional as F
from flowtorch.bijectors.fixed import Fixed


class Tanh(Fixed):
    r"""
    Transform via the mapping :math:`y = \tanh(x)`.
    """
    codomain = constraints.interval(-1.0, 1.0)

    def _forward(
        self,
        x: torch.Tensor,
        context: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        return torch.tanh(x)

    def _inverse(
        self,
        y: torch.Tensor,
        x: Optional[torch.Tensor] = None,
        context: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        return torch.atanh(y)

    def _log_abs_det_jacobian(
        self,
        x: torch.Tensor,
        y: torch.Tensor,
        context: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        return 2.0 * (math.log(2.0) - x - F.softplus(-2.0 * x))
