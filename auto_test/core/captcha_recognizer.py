"""OCR support for the TMS test-environment login captcha.

Authentication infrastructure follows
``knowledge/06_auto_test_spec/ui_code_spec.md``. No credentials are stored here.
"""

from __future__ import annotations

import re

import ddddocr


class CaptchaRecognitionError(RuntimeError):
    """Raised when OCR does not return a usable TMS captcha value."""


class CaptchaRecognizer:
    """Recognize the four-character captcha used by the TMS login page."""

    _VALID_CODE = re.compile(r"^[A-Za-z0-9]{4}$")

    def __init__(self) -> None:
        self._classifier = ddddocr.DdddOcr(show_ad=False)

    def recognize(self, image_bytes: bytes) -> str:
        """Return a validated captcha value from image bytes."""
        raw_value = self._classifier.classification(image_bytes)
        captcha = re.sub(r"[^A-Za-z0-9]", "", raw_value or "")
        if not self._VALID_CODE.fullmatch(captcha):
            raise CaptchaRecognitionError(
                f"OCR returned an invalid captcha value: {raw_value!r}"
            )
        return captcha
