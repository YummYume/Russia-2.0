# Contributing

Thank you for considering contributing to this mod! Here's how you can help.

## Content

- [Contributing](#contributing)
  - [Content](#content)
  - [Reporting issues](#reporting-issues)
  - [How to install the mod locally](#how-to-install-the-mod-locally)
    - [The simple way](#the-simple-way)
    - [The manual way](#the-manual-way)

## Reporting issues

If you find a bug or have a feature request, please [open an issue](https://github.com/YummYume/Russia-2.0/issues) on GitHub after checking that there isn't already one.

You can also find answers or talk about anything else on our [Discord](https://discord.gg/xf5PUxK) or in the [GitHub Discussions](https://github.com/YummYume/Russia-2.0/discussions).

> [!NOTE]
> [CodeRabbit AI](https://www.coderabbit.ai/) is used to review pull requests automatically. You can also talk to it by tagging it using `@coderabbitai` anywhere in a PR, an issue or a discussion.

## How to install the mod locally

> [!IMPORTANT]
> You **_cannot_** have two mods with the same name (Paradox launcher won't understand).

### The simple way

- Download the mod from the desired branch (`stable` or `next`) as a ZIP file (Clone or Download > Download as ZIP),
- Unzip the file in `Documents\Paradox Interactive\Hearts of Iron IV\mod`,
- Copy the mod descriptor file (`mod/Russia-2.0/descriptor.mod`) to your mod folder (`Documents\Paradox Interactive\Hearts of Iron IV\mod`),
- Its contents should remain unchanged, except for an added `path` line at the end. Set it to the full absolute path to the mod's folder, for example: `path="C:/Users/YourName/Documents/Paradox Interactive/Hearts of Iron IV/mod/Russia 2.0"`,
- The mod should now appear in the Paradox launcher, and you can enable it.

### The manual way

If, for whatever reason, the simple way does not work for you, you can install the mod manually by following these steps:

- Download the code as a zip file (Clone or Download > Download as ZIP), make sure to download the correct branch (`stable` or `next`),
- Start the HOI4 launcher and go to Mods > Mod Tools > Create a Mod,
- Name: Russia 2.0,
- Version: The current version shown in `descriptor.mod` (e.g., `3.0.4`),
- Directory: `mod/Russia 2.0`,
- Tags: Alternative History, Events, Gameplay, Historical, National Focuses, Utilities, Military, Fixes, Balance,
- Create the Mod. Do **NOT** enable it yet (very important),
- Go to `Documents\Paradox Interactive\Hearts of Iron IV\mod`, here you should see a folder `Russia 2.0` (if not then you've done something wrong),
- Go in the `Russia 2.0` Folder and unzip the files there. All the files should be directly inside the folder (e.g. `mod\Russia 2.0\common`, NOT `mod\Russia 2.0\Russia 2.0\common`),
- Once this is done, simply enable the mod and you're good to go!

If you have any problems with the installation, feel free to ask (once you've completed the steps above).

What if you already have the mod installed locally and want to update it with the latest version?
Simply download the ZIP file again, delete everything inside the Russia 2.0 folder and then drag the new files in.
