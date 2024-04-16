# Anti-Scam Discord Bot

## Overview

This Discord bot is designed to help protect users from scams by monitoring messages and checking for potentially harmful links.
https://github.com/zenozense/Antiscam-Bot/assets/53638571/eb797b10-532a-4ce1-ab0a-477391e899b7



## Features

- **Message Monitoring**: Scans messages for common scam keywords and patterns.
- **Automatic Link Verification**: Deletes messages containing disallowed links.
- **Alert System**: Notifies users with warnings when potential scam activity is detected.
- **Customizable Settings**: Allows server administrators to customize the bot's behavior and sensitivity.

## How It Works

1. **Message Monitoring**: The bot monitors incoming messages in real-time.
2. **Link Detection**: It checks if the message contains any links.
3. **Link Verification**: It verifies if the detected links are allowed or not.
4. **Automatic Deletion**: Messages containing disallowed links are automatically deleted.
5. **Log Saving**: Optionally, you can enable logging to keep a record of detected scam attempts.

## Requirements

Before running the bot, make sure you have the following dependencies installed:

```bash
pip install -r requirements.txt
