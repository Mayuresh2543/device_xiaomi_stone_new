#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/stone',
    'hardware/qcom-caf/sm8350',
    'hardware/xiaomi',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/camera/components/com.qti.node.mialgocontrol.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
     'vendor/lib64/libwvhidl.so': blob_fixup()
        .replace_needed(
            'libcrypto.so',
            'libcrypto-v33.so'
       ),
       'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
}

module = ExtractUtilsModule(
    'stone',
    'xiaomi',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
