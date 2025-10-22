# Contributing

Thank you for considering contributing to this mod! Here's how you can help.

## Table of contents

- [Contributing](#contributing)
  - [Table of contents](#table-of-contents)
  - [Reporting issues](#reporting-issues)
  - [Commit naming conventions](#commit-naming-conventions)
    - [Breaking changes](#breaking-changes)
  - [How to install the mod locally](#how-to-install-the-mod-locally)
    - [The simple way](#the-simple-way)
    - [The manual way](#the-manual-way)

## Reporting issues

If you find a bug or have a feature request, please [open an issue](https://github.com/YummYume/Russia-2.0/issues) on GitHub after checking that there isn't already one.

You can also find answers or talk about anything else on our [Discord](https://discord.gg/xf5PUxK) or in the [GitHub Discussions](https://github.com/YummYume/Russia-2.0/discussions).

> [!NOTE]
> [CodeRabbit AI](https://www.coderabbit.ai/) is used to review pull requests automatically. You can also talk to it by tagging it using `@coderabbitai` anywhere in a PR, an issue or a discussion.

## Commit naming conventions

This mod uses [conventional commits](https://www.conventionalcommits.org/) for commit messages. The following commit types are recognized by our changelog generator:

- `feat` or `feature` - New features
- `fix` - Bug fixes
- `balance` - Game balance changes
- `doc` or `documentation` - Documentation changes
- `imp` or `improvement` - General improvements
- `perf` or `performance` - Performance improvements
- `refactor` - Code refactoring
- `gfx` or `interface` - Interface and graphics changes
- `test` - Test-related changes
- `chore` or `ci` - Miscellaneous chores and CI changes
- `revert` - Reverted changes
- `security` - Security-related changes

Anything not covered by the above types will still be considered a valid change under the "Other" category.

**Format:** `type(scope): description`

Where `scope` is optional and describes what part of the mod is affected (e.g., `feat(focus): add new focus for x nation`).
You are, however, not expected to use the `scope` part in your commit messages, as it is optional.
The main goal is to keep the commit message clear and concise, thus `type: description` is sufficient.

### Breaking changes

If your commit introduces a breaking change, you should append `BREAKING CHANGE:` to the commit message, or add a `!` at the end of the type (e.g., `feat!: add new focus tree for x nation`).
Breaking changes are changes that are, most of the time, not save-game compatible, meaning that they will break existing saves or require a new game to be started to see the changes.

> [!NOTE]
> All pull requests will be **squash merged** to maintain a clean commit history.
> The final commit message will follow the conventional commit format based on your PR title and description.
> This also means that only the squashed commit matters in the final changelog, and it can always be edited before merging to ensure clarity and consistency.

## How to install the mod locally

> [!IMPORTANT]
> You **_cannot_** have two mods with the same name (Paradox launcher won't understand).

### The simple way

- Download the mod from the desired branch (`stable`, `next`, or `playtest`) as a ZIP file (Code > Download ZIP),
- Unzip the file in `Documents\Paradox Interactive\Hearts of Iron IV\mod` and ensure the extracted folder is named `Russia-2.0`,
- Copy the mod descriptor file (`mod/Russia-2.0/descriptor.mod`) to your mod folder (`Documents\Paradox Interactive\Hearts of Iron IV\mod`) and name it `Russia-2.0.mod` (the name should match the mod folder name),
- Its contents should remain unchanged, except for an added `path` line at the end. Set it to the absolute path to the mod's folder, for example: `path="C:/Users/YourName/Documents/Paradox Interactive/Hearts of Iron IV/mod/Russia-2.0"`,
- The mod should now appear in the Paradox launcher, and you can enable it.

### The manual way

If, for whatever reason, the simple way does not work for you, you can install the mod manually by following these steps:

- Download the code as a zip file (Code > Download as ZIP), make sure to download the correct branch (`stable`, `next`, or `playtest`),
- Alternatively, download the desired version from the releases,
- Start the HOI4 launcher and go to Mods > Mod Tools > Create a Mod,
- **Name**: Russia 2.0,
- **Version**: The current version shown in `descriptor.mod` (e.g., `3.0.4`),
- **Directory**: `mod/Russia-2.0`,
- **Tags**: Alternative History, Events, Gameplay, Historical, National Focuses, Utilities, Military, Fixes, Balance,
- Create the Mod. Do **NOT** enable it yet (very important),
- Go to `Documents\Paradox Interactive\Hearts of Iron IV\mod`, here you should see a `Russia-2.0` folder (if not, something went wrong),
- Go in the `Russia-2.0` Folder and unzip the files there. All the files should be directly inside (e.g. `mod\Russia-2.0\common`, NOT `mod\Russia-2.0\Russia-2.0\common`),
- Once this is done, simply enable the mod and you're good to go!

If you encounter any installation issues, feel free to ask (after completing the steps above).

What if you already have the mod installed locally and want to update it with the latest version?
Simply download the ZIP file again, delete everything inside the `Russia-2.0` folder and then drag the new files in.
