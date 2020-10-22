"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""
from typing import Mapping

from gs_quant.target.risk import (
    MarketDataPattern, MarketDataPatternAndShock, MarketDataShock)
from gs_quant.target.risk import \
    MarketDataShockBasedScenario as __MarketDataShockBasedScenario


class MarketDataShockBasedScenario(__MarketDataShockBasedScenario):

    def __init__(self, shocks: Mapping[MarketDataPattern, MarketDataShock]):
        super().__init__(tuple(MarketDataPatternAndShock(p, s)
                               for p, s in shocks.items()))
