class Config:
    REVANCED_APKS_RELEASE_URL = (
        "https://api.github.com/repos/Blawuken/Revanced-Apps-Building/releases/latest"
    )
    REVANCED_PATCHES_URL = (
        "https://api.github.com/repos/Blawuken/revanced-patches-extended/releases/latest"
    )

    NOTES = """*≣ Note:*
➜ Gunakan modul [zygisk-detach](https://github.com/j-hc/zygisk-detach/releases/latest) untuk melepaskan YouTube dan YT Music dari Play Store.
➜ Install [MicroG](https://github.com/Blawuken/MicroG-Extended/releases/latest) untuk menggunakan YouTube dan YT Music di perangkat non-root."""

    RELEASE_MESSAGE = """📑 *RELEASE {release_name}*

{revanced_version_message}

[Changelogs (What's New)]({changelogs_url})

{notes}

*🔻 Downloads ೄྀ࿐ ˊˎ-*
`Non-Root:`
{nonroot_files}

`Magisk Modules (Root):`
{root_files}

*≣ Credits:*
➜ [ReVanced](https://github.com/ReVanced)
➜ [inotia00](https://github.com/inotia00)
➜ [j-hc](https://github.com/j-hc)

@ExtendedApps | @ExtendedAppsGroup"""
