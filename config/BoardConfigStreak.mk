include vendor/streak/config/BoardConfigKernel.mk

ifeq ($(BOARD_USES_QCOM_HARDWARE),true)
include vendor/streak/config/BoardConfigQcom.mk
endif

include vendor/streak/config/BoardConfigSoong.mk
