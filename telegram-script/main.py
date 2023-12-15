from config import Config
import re
import requests
from markdown_to_telegraph import MarkdownToTelegraph

# Read release.json file
release = requests.get(Config.REVANCED_APKS_RELEASE_URL).json()
changelog_patch = requests.get(Config.REVANCED_PATCHES_URL).json()
telegraph = MarkdownToTelegraph("ExtendedApps", "YouTube Extended", "https://t.me/ExtendedApps")

def revanced_version_message():
    version_message = release["body"] or ""
    return version_message

def generate_file_bullet(file_name, file_url):
    return f"📦 [{file_name}](https://semawur.com/st/?api=12009627cdbda7809f8aa8a75007ec876ac0503c&url={file_url})"

def generate_files_message():

    # Collect browser_download_url from assets in release
    nonroot_files = []
    root_files = []

    for asset in release["assets"][::-1]:
        file_name = asset["name"]
        file_url = asset["browser_download_url"]
        if ".zip" in file_name:
            root_files.append(generate_file_bullet(file_name, file_url))
        else:
            nonroot_files.append(generate_file_bullet(file_name, file_url))

    return {"nonroot_files": nonroot_files, "root_files": root_files}

def fetch_changelogs_telegraph_url():
    return telegraph.create_page_from_string("Changelogs", changelog_patch["body"])

def main():
    files = generate_files_message()
    changelogs_url = fetch_changelogs_telegraph_url()

    # Format release message
    release_message = Config.RELEASE_MESSAGE.format(
        release_name=release["name"],
        revanced_version_message=revanced_version_message(),
        changelogs_url=changelogs_url,
        notes=Config.NOTES,
        nonroot_files="\n".join(files["nonroot_files"]),
        root_files="\n".join(files["root_files"]),
    )

    print(release_message)

    # Write release message to file
    with open("release_notification.md", "w") as f:
        f.write(release_message)
