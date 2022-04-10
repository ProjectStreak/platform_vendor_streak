# ProjectStreak packages
PRODUCT_PACKAGES += \
    SimpleGallery \
    SimpleCalendar \
    ThemePicker

ifeq ($(STREAK_BUILD_TYPE),OFFICIAL)
PRODUCT_PACKAGES += \
    Updater
endif

# Charger
PRODUCT_PACKAGES += \
    charger_res_images \
    product_charger_res_images

# Extra tools
PRODUCT_PACKAGES += \
    7z \
    bash \
    curl \
    getcap \
    htop \
    lib7z \
    libsepol \
    nano \
    pigz \
    setcap \
    unrar \
    vim \
    zip

# Navbar
PRODUCT_PACKAGES += \
    NavigationBarModeGesturalOverlayFS \
    NavigationBarNoHintOverlay

# Openssh
PRODUCT_PACKAGES += \
    scp \
    sftp \
    ssh \
    sshd \
    sshd_config \
    ssh-keygen \
    start-ssh

# Root
PRODUCT_PACKAGES += \
    adb_root

# rsync
PRODUCT_PACKAGES += \
    rsync
