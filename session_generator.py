#!/usr/bin/env python3
"""
Pyrogram Session String Generator
"""

# 🔴 This script is created by The Seeker (Telegram: @MrUnknown114)

import os
import asyncio
from datetime import datetime
from pyrogram import Client
from pyrogram.errors import (
    ApiIdInvalid,
    SessionPasswordNeeded,
    PasswordHashInvalid,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    FloodWait
)

def get_credentials():
    """Get API credentials from user"""
    print("🔑 Get your API credentials from https://my.telegram.org/apps")
    print("=" * 60)

    while True:
        try:
            api_id = int(input("Enter your API ID: "))
            break
        except ValueError:
            print("❌ Invalid API ID. Please enter a valid number.")

    api_hash = input("Enter your API Hash: ").strip()

    if not api_hash:
        print("❌ API Hash cannot be empty.")
        return get_credentials()

    return api_id, api_hash


def save_session_to_file(session_string, phone_number):
    """Save session string to a text file with credits"""
    try:
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"session_string_{timestamp}.txt"

        # Prepare file content with credits and session info
        file_content = f"""# ═══════════════════════════════════════════════════════════════
# 🔐 PYROGRAM SESSION STRING
# ═══════════════════════════════════════════════════════════════
# 
# Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# Phone Number: {phone_number}
# 
# ⚠️  SECURITY WARNING:
# Keep this session string private and secure!
# Do not share it with anyone or upload it publicly.
# 
# ═══════════════════════════════════════════════════════════════
# 📱 USAGE EXAMPLE:
# ═══════════════════════════════════════════════════════════════
# 
# from pyrogram import Client
# 
# app = Client(
#     "my_account",
#     session_string="YOUR_SESSION_STRING_BELOW",
#     api_id=YOUR_API_ID,
#     api_hash=YOUR_API_HASH
# )
# 
# app.run()
# 
# ═══════════════════════════════════════════════════════════════
# 🔴 CREDITS:
# ═══════════════════════════════════════════════════════════════
# 
# Script Created by: The Seeker
# Telegram: @MrUnknown114
# GitHub: https://github.com/theseekerofficial/Pyrogram-Session-Generator
# 
# Thank you for using this tool! ⭐
# If this helped you, consider giving the repository a star.
# 
# ═══════════════════════════════════════════════════════════════

SESSION_STRING = {session_string}

# ═══════════════════════════════════════════════════════════════
# End of file - Keep this session string safe! 🔐
# ═══════════════════════════════════════════════════════════════
"""

        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(file_content)

        # Get absolute path
        file_path = os.path.abspath(filename)

        print(f"✅ Session string saved to: {filename}")
        print(f"📁 Full path: {file_path}")
        print("🔒 Remember to keep this file secure and private!")

        return True

    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

async def generate_session_string():
    """Generate Pyrogram session string"""
    api_id, api_hash = get_credentials()

    client = Client(
        name="session_generator",
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True
    )

    try:
        await client.connect()

        # Get phone number
        phone_number = input("Enter your phone number (with country code, e.g., +1234567890): ").strip()

        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number

        # Send code
        print("📱 Sending verification code...")
        try:
            sent_code = await client.send_code(phone_number)
        except PhoneNumberInvalid:
            print("❌ Invalid phone number. Please check and try again.")
            return
        except FloodWait as e:
            print(f"⏳ Flood wait: Please wait {e.value} seconds before trying again.")
            return
        except ApiIdInvalid:
            print("❌ Invalid API ID or API Hash. Please check your credentials.")
            return
        except Exception as e:
            print(f"❌ Error sending code: {e}")
            return

        # Get verification code
        code = input("Enter the verification code: ").strip()

        try:
            # Sign in with code
            await client.sign_in(phone_number, sent_code.phone_code_hash, code)

        except SessionPasswordNeeded:
            # Two-step verification is enabled
            print("🔐 Two-step verification is enabled.")

            # Get password hint if available
            password_hint = await client.get_password_hint()
            if password_hint:
                print(f"💡 Password hint: {password_hint}")
            else:
                print("💡 No password hint available")

            password = input("Enter your 2FA password: ").strip()

            try:
                await client.check_password(password)
            except PasswordHashInvalid:
                print("❌ Invalid 2FA password.")
                return
            except Exception as e:
                print(f"❌ Error with 2FA: {e}")
                return

        except PhoneCodeInvalid:
            print("❌ Invalid verification code.")
            return
        except Exception as e:
            print(f"❌ Error signing in: {e}")
            return

        # Export session string
        session_string = await client.export_session_string()

        print("\n" + "=" * 60)
        print("✅ SUCCESS! Your Pyrogram session string:")
        print("=" * 60)
        print(session_string)
        print("=" * 60)
        print("⚠️  Keep this session string private and secure!")
        print("💾 Save it in a safe place - you'll need it for your bot/userbot.")

        # Show usage example
        print("\n📖 Usage example:")
        print("from pyrogram import Client")
        print('app = Client("my_account", session_string="YOUR_SESSION_STRING")')
        print("app.run()")

        print("\n" + "=" * 60)
        save_choice = input("💾 Do you want to save this session string to a text file? (y/n): ").strip().lower()

        if save_choice in ['y', 'yes', '1']:
            print("📝 Saving session string to file...")
            if save_session_to_file(session_string, phone_number):
                print("🎉 Session string successfully saved!")
            else:
                print("⚠️  Failed to save file, but your session string is displayed above.")
        else:
            print("👍 Session string not saved to file. Make sure to copy it from above! This is the only time you'll see it.")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        await client.disconnect()


def main():
    """Main function"""
    print("🚀 Pyrogram Session String Generator")
    print("=" * 60)

    try:
        asyncio.run(generate_session_string())
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user. Exiting...")
    except Exception as e:
        print(f"❌ Fatal error: {e}")


if __name__ == "__main__":
    main()
