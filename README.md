# Anti-Scam Discord Bot

## Overview

This Discord bot is designed to help protect users from scams by monitoring messages and checking for potentially harmful links.

https://github.com/zenozense/Antiscam-Bot/assets/53638571/df3affb2-6f58-4010-b57a-25c20e687b9f




## Features

- **Message Monitoring**: Scans messages for common scam keywords and patterns.
- **Automatic Link Verification**: Deletes messages containing disallowed links.
- **Alert System**: Notifies users with warnings when potential scam activity is detected.
- **Customizable Settings**: Allows server administrators to customize the bot's behavior and sensitivity (Optional)

## How It Works

1. **Message Monitoring**: The bot monitors incoming messages in real-time.
2. **Link Detection**: It checks if the message contains any links.
3. **Link Verification**: It verifies if the detected links are allowed or not.
4. **Automatic Deletion**: Messages containing disallowed links are automatically deleted.
5. **Log Saving**: Optionally, you can enable logging to keep a record of detected scam attempts (Optional)

## Installation

Before running the bot, make sure you have the following dependencies installed:

```bash
pip install -r requirements.txt
```
Then insert your Discord bot tokens into the .env file.
```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```
