BUILD_DATE := $(shell date +%Y%m%d)
BUILD_TIME := $(shell date +%H%M)

ifeq ($(TARGET_BUILD_GAPPS),false)
    STREAK_VARIANT := VANILLA
else
    STREAK_VARIANT := GAPPS
endif

STREAK_BUILD_TYPE ?= UNOFFICIAL

# Set all versions
STREAK_PLATFORM_VERSION := 12.1
TARGET_PRODUCT_SHORT := $(subst streak_,,$(TARGET_PRODUCT))
STREAK_VERSION := Streak-$(STREAK_PLATFORM_VERSION)-$(STREAK_BUILD_TYPE)-$(STREAK_VARIANT)-$(TARGET_PRODUCT_SHORT)-$(BUILD_DATE)-$(BUILD_TIME)
ROM_FINGERPRINT := Streak/$(PLATFORM_VERSION)/$(STREAK_BUILD_TYPE)/$(BUILD_DATE)$(BUILD_TIME)

# Declare it's a ProjectStreak build
STREAK_BUILD := true