# Inherit full common Streak stuff
$(call inherit-product, vendor/streak/config/common_full.mk)

# Required packages
PRODUCT_PACKAGES += \
    LatinIME

# Include Streak LatinIME dictionaries
PRODUCT_PACKAGE_OVERLAYS += vendor/streak/overlay/dictionaries

# Enable support of one-handed mode
PRODUCT_PRODUCT_PROPERTIES += \
    ro.support_one_handed_mode=true

$(call inherit-product, vendor/streak/config/telephony.mk)
