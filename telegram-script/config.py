class Config:
    REVANCED_APKS_RELEASE_URL = (
        "https://api.github.com/repos/Blawuken/Revanced-Apps-Building/releases/latest"
    )
    MICROG_RELEASE_URL = (
        "https://api.github.com/repos/TeamVanced/VancedMicroG/releases/latest"
    )
    REVANCED_CHANGES_URL = (
        "https://api.github.com/repos/revanced/revanced-patches/compare"
    )
    REVANCED_EXTENDED_CHANGES_URL = (
        "https://api.github.com/repos/Blawuken/revanced-patches-extended/compare"
    )

    NOTES = """*≣ Note:*
➜ Gunakan modul [zygisk-detach](https://github.com/j-hc/zygisk-detach) untuk melepaskan YouTube dan YT Music dari Play Store.
➜ Install [MicroG](https://github.com/TeamVanced/VancedMicroG/releases) untuk menggunakan YouTube dan YT Music di perangkat non-root."""

    RELEASE_MESSAGE = """📑 *RELEASE {release_name}*

{revanced_version_message}

[Changelogs (What's New)]({changelogs_url})

{notes}

*🔻 Downloads ೄྀ࿐ ˊˎ-*
`Non-Root:`
{nonroot_files}

`Magisk Modules (Root):`
{root_files}

@ExtendedApps | @ExtendedAppsGroup"""
