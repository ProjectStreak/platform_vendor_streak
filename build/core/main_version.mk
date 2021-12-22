# Build fingerprint
ifneq ($(BUILD_FINGERPRINT),)
ADDITIONAL_SYSTEM_PROPERTIES += \
    ro.build.fingerprint=$(BUILD_FINGERPRINT)
endif

# ProjectStreak Platform Display Version
ADDITIONAL_SYSTEM_PROPERTIES += \
    ro.streak.version=$(STREAK_BASE_VERSION)-$(STREAK_BUILD_TYPE)-$(BUILD_DATE)-$(BUILD_TIME) \
    ro.streak.base.version=$(STREAK_BASE_VERSION) \
    ro.streak.codename=$(STREAK_CODENAME) \
    ro.streak.build.version=$(STREAK_PLATFORM_VERSION) \
    ro.mod.version=$(BUILD_ID)-$(BUILD_DATE)-$(STREAK_BASE_VERSION) \
    ro.streak.fingerprint=$(ROM_FINGERPRINT) \
    ro.streak.buildtype=$(STREAK_BUILD_TYPE) \
    ro.streak.build_date=$(BUILD_DATE)
