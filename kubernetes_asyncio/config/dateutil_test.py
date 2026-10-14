# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from datetime import datetime, timedelta

from kubernetes_asyncio.config.dateutil import (
    UTC,
    TimezoneInfo,
    format_rfc3339,
    parse_rfc3339,
)


class DateUtilTest(unittest.TestCase):
    def _parse_rfc3339_test(
        self, st: str, y: int, m: int, d: int, h: int, mn: int, s: int, us: int
    ) -> None:
        actual = parse_rfc3339(st)
        expected = datetime(y, m, d, h, mn, s, us, UTC)
        self.assertEqual(expected, actual)

    def test_parse_rfc3339(self) -> None:
        self._parse_rfc3339_test("2017-07-25T04:44:21Z", 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25 04:44:21Z", 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21", 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21z", 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21+03:00", 2017, 7, 25, 1, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21-03:00", 2017, 7, 25, 7, 44, 21, 0)

        self._parse_rfc3339_test(
            "2017-07-25T04:44:21,005Z", 2017, 7, 25, 4, 44, 21, 5000
        )
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.005Z", 2017, 7, 25, 4, 44, 21, 5000
        )
        self._parse_rfc3339_test(
            "2017-07-25 04:44:21.0050Z", 2017, 7, 25, 4, 44, 21, 5000
        )
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.5", 2017, 7, 25, 4, 44, 21, 500000
        )
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.005z", 2017, 7, 25, 4, 44, 21, 5000
        )
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.005+03:00", 2017, 7, 25, 1, 44, 21, 5000
        )
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.005-03:00", 2017, 7, 25, 7, 44, 21, 5000
        )

    def test_parse_rfc3339_negative_offset_with_zero_hours(self) -> None:
        actual = parse_rfc3339("2017-07-25T04:44:21-00:30")
        self.assertEqual(timedelta(minutes=-30), actual.utcoffset())
        self.assertEqual(datetime(2017, 7, 25, 5, 14, 21, 0, UTC), actual)

        actual = parse_rfc3339("2017-07-25T04:44:21+00:30")
        self.assertEqual(timedelta(minutes=30), actual.utcoffset())

        actual = parse_rfc3339("2017-07-25T04:44:21-03:30")
        self.assertEqual(timedelta(hours=-3, minutes=-30), actual.utcoffset())

    def test_parse_rfc3339_fraction_is_exact(self) -> None:
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.520519Z", 2017, 7, 25, 4, 44, 21, 520519
        )
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.999999Z", 2017, 7, 25, 4, 44, 21, 999999
        )
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.000001Z", 2017, 7, 25, 4, 44, 21, 1
        )
        # digits beyond microseconds are dropped
        self._parse_rfc3339_test(
            "2017-07-25T04:44:21.1234567Z", 2017, 7, 25, 4, 44, 21, 123456
        )

    def test_timezone_info_negative_zero_hours(self) -> None:
        self.assertEqual(timedelta(minutes=-15), TimezoneInfo(0, -15).utcoffset(None))
        self.assertEqual(
            timedelta(hours=-2, minutes=-30), TimezoneInfo(-2, 30).utcoffset(None)
        )
        self.assertEqual(
            timedelta(hours=2, minutes=30), TimezoneInfo(2, 30).utcoffset(None)
        )

    def test_format_rfc3339(self) -> None:
        self.assertEqual(
            format_rfc3339(datetime(2017, 7, 25, 4, 44, 21, 0, UTC)),
            "2017-07-25T04:44:21Z",
        )
        self.assertEqual(
            format_rfc3339(datetime(2017, 7, 25, 4, 44, 21, 0, TimezoneInfo(2, 0))),
            "2017-07-25T02:44:21Z",
        )
        self.assertEqual(
            format_rfc3339(datetime(2017, 7, 25, 4, 44, 21, 0, TimezoneInfo(-2, 30))),
            "2017-07-25T07:14:21Z",
        )
