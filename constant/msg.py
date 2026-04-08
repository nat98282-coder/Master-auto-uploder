"""
constant/msg.py - All message string constants
Reconstructed from msg.so analysis
"""

APP = """
<b>➣━━━━━━━ 🤖 APPS ━━━━━━━➣</b>

<i>I'm your all-in-one solution for extracting and managing course content from various educational platforms.</i>

<b>Select an app to get started:</b>
"""

BATCH_ALREADY_EXISTS = "❌Batch Already Exists in my Database❌"
BATCH_DELETED = "❌Batch Deleted Successfully❌"
BATCH_NOT_FOUND = "❌Batch Not Found in my Database❌"
BATCH_SELECTION = "<b>Please enter the batch ID number from the list above that you want to set for auto-update ⬆️</b>"

BATCH_STATUS = """<b>➣━━━━━━━ 📊 BATCH STATUS ━━━━━━━➣</b>

<b>📚 Batch Information:</b>
🆔 <b>ID:</b> {}
📝 <b>Name:</b> {}
📊 <b>Status:</b> {}
📄 <b>PDFs:</b> {}
🎥 <b>Videos:</b> {}
⏰ <b>Schedule:</b> {}

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

BATCH_UPDATED = "✅Batch Updated Successfully✅"

COLLECTING_DATA = """<b>➣━━━━━━━ 📊 COLLECTING DATA ━━━━━━━➣</b>

<b>Collecting Data... Please Wait a Few Minutes</b>

<b>This may take some time depending on the batch size.</b>
"""

CONFIRM_CONFIG = """<b>➣━━━━━━━ 📋 CONFIRMATION ━━━━━━━➣</b>

<b>Configuration Summary</b>

🏠 <b>App Name:</b> {}
🆔 <b>Batch ID:</b> {}
📝 <b>Batch Name:</b> {}
👥 <b>Group ID:</b> {}
⏰ <b>Schedule:</b> {}
💰 <b>Credit:</b> {}

<b>Confirm to start processing?</b>
"""

CREDIT_OPTIONS = """<b>➣━━━━━━━ 💰 CREDIT ━━━━━━━➣</b>

<b>Enter Credit Name:</b>

1️⃣ Caption only: `Admin`
2️⃣ Caption + Watermark: `Admin | @channel`
3️⃣ No credit: Send `no`

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

DAILY_UPDATE_COMPLETED = """<b>➣━━━━━━━ 📊 DAILY UPDATE COMPLETED ━━━━━━━➣</b>

<b>Daily Update Completed!</b>

<b>📚 Batch Information:</b>
🆔 <b>ID:</b> {}
📝 <b>Name:</b> {}
📄 <b>New PDFs:</b> {}
🎥 <b>New Videos:</b> {}

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

DISCLAIMER = """
<b> ======= ⚖️ LEGAL DISCLAIMER =======</b>

<i>Please read this disclaimer carefully before using this bot.

This bot is designed for educational purposes only. The developers are not responsible for any misuse of this bot. By using this bot, you agree that:

1. You will use it only for personal learning purposes.
2. You will not distribute or sell any content obtained through this bot.
3. You acknowledge that content piracy is illegal.
4. The bot developers hold no liability for user actions.

Use at your own risk.</i>

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

ERROR_UPLOADING = """╭━━━━━━━━━━━━━━➣
┣⪼ ⚠️ **Download Failed!**
┣⪼ 📝 **Name:** <code>{}</code>
┣⪼ 🔗 **URL:** <code>{}</code>
┣⪼ ❌ **Error:** <code>{}</code>
╰━━━━━━━━━━━━━━➣"""

GENERAL_ERROR = """<b>➣━━━━━━━ ⚠️ ERROR ━━━━━━━➣</b>

<b>Error Occurred</b>

Something went wrong while processing your request. Please try again later.

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

GROUP_ERROR = """<b>➣━━━━━━━ ⚠️ ERROR ━━━━━━━➣</b>

<b>Invalid group ID or insufficient permissions</b>

Please verify:
1. The group ID is correct
2. The bot is an admin in the group
3. The group allows bot messages

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

GROUP_SETUP = """<b>➣━━━━━━━ 👥 GROUP SETUP ━━━━━━━➣</b>

<b>Group Setup Required</b>

Please follow these steps:
1️⃣ Create a group/channel
2️⃣ Add the bot as admin
3️⃣ Send the group ID here

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

HELP = """<b>➣━━━━━━━ 📚 HELP ━━━━━━━➣</b>

<b>Available Commands</b>

/start - Start the bot
/help - Show this help menu
/addbatch - Add a new batch
/mybatch - Show your batches
/deletebatch - Delete a batch
/legal - Legal disclaimer
/restart - Restart bot (admin)
/id - Get chat ID

<b>➣━━━━━━━━━━━━━━━━━➣</b>

{}"""

INVALID_TIME_FORMAT = """<b>➣━━━━━━━ ❌ ERROR ━━━━━━━➣</b>

⚠️ Invalid time format! Please use 24-hour format (HH:MM)
Example: 14:30 for 2:30 PM

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

INVALID_TOKEN = """<b>➣━━━━━━━ ❌ ERROR ━━━━━━━➣</b>

<b>Invalid Token</b>
Please provide a valid authentication token to proceed.

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

LAST_BATCH_COMPLETED = """<b>➣━━━━━━━ 📊 BATCH COMPLETED ━━━━━━━➣</b>

<b>📚 Batch Information:</b>
🆔 <b>ID:</b> {}
📝 <b>Name:</b> {}
📄 <b>PDFs Uploaded:</b> {}
🎥 <b>Videos Uploaded:</b> {}

<b>✅ Batch upload completed successfully!</b>

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

LOGIN_ERROR = """<b>➣━━━━━━━ ❌ ERROR ━━━━━━━➣</b>

<b>Login Failed!</b>
<i>Error: {}</i>

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

LOGIN_OPTIONS = """<b>➣━━━━━━━━ 🔐 LOGIN ━━━━━━━➣</b>

<b>Choose a login method:</b>

1️⃣ ID & Password Format: <code>email*password</code>
2️⃣ Token: Just paste your access token
3️⃣ Mobile Number: For OTP login (e.g., <code>+919876543210</code>)

<i>Please choose one of the above methods to continue...</i>

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

LOGIN_SUCCESS = """<b>➣━━━━━━━ ✅ SUCCESS ━━━━━━━➣</b>

<b>Login Successful!</b>
<i>Message: {}</i>

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

NO_BATCH_FOUND = """<b>➣━━━━━━━ ❌ ERROR ━━━━━━━➣</b>

<b>No Active Batches Found</b>

• Your batches may have expired
• Try adding a new batch using /addbatch

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

NO_DATA_ERROR = """<b>➣━━━━━━━ ❌ ERROR ━━━━━━━➣</b>

<b>No Data Found</b>

The selected batch appears to be empty.
Please check the batch and try again.

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

NO_NEW_CLASSES = """<b>➣━━━━━━━ ❌ NO NEW CLASSES ━━━━━━━➣</b>

<b>No new classes today for course {}</b>
<b>Go and Enjoy your day! 🎉</b>

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

OTP_SENT = """<b>➣━━━━━━━ 📱 OTP ━━━━━━━➣</b>

<b>OTP Verification</b>
An OTP has been sent to your mobile number.
Please enter the OTP below:

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

PDF_CAPTION = """╭━━━━━━━━━━━━━━➣
┣⪼ 📄 <b>PDF Title:</b>
┃  ╰─⪼ <code>{}.pdf</code>
┣⪼ 📚 <b>Topic Name:</b>
┃  ╰─⪼ <b>{}</b>
┣⪼ 📂 <b>Batch Name:</b>
┃  ╰─⪼ <b>{}</b>
╰━━━━━━━━━━━━━━➣

<b>{}</b>"""

PDF_CAPTION_V2 = """<b>[📕]File Title :</b><code>{} .pdf</code>
<blockquote><b>📌Batch Name : {}
🔗Topic Name : {}
⏰Class Time : {}</b></blockquote>

<b>{}</b>"""

RECOVERING_BATCH = """<b>➣━━━━━━━ 📊 RECOVERING BATCH ━━━━━━━➣</b>
⚠️ <b>Last Batch Incomplete</b>
📚 <b>Course:</b> <code>{}</code>

<b>Recovering batch upload... Please wait.</b>

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

SCHEDULE_TIME = """<b>➣━━━━━━━ ⏰ SCHEDULE ━━━━━━━➣</b>

Please Set the time in <code>HH:MM</code> format for Daily Update.
Example: <code>14:30</code> for 2:30 PM IST

Send <code>no</code> to skip scheduling.

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

SETUP_CANCELLED = """<b>➣━━━━━━━ ❌ CANCELLED ━━━━━━━➣</b>

<b>Setup Cancelled</b>

Batch update configuration was aborted.

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

SETUP_SUCCESS = """<b>➣━━━━━━━ ✅ SUCCESS ━━━━━━━➣</b>

<b>Setup Successful!</b>
Your batch has been configured for auto-update.

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

START = """
<b>➣━━━━━━━ 🤖 WELCOME ━━━━━━━➣</b>

<b>👋 Hey {}, Welcome to Auto Uploader Bot v1.3!</b>

<i>I'm your all-in-one solution for extracting and managing course content from various educational platforms.</i>

<b>Features:</b>
📱 Multi-App Support
📥 Auto Download & Upload
⏰ Schedule Daily Updates
📊 Batch Management

<b>➣━━━━━━━━━━━━━━━━━➣</b>

{}"""

THUMBNAIL_OPTIONS = """<b>➣━━━━━━━ 🖼 THUMBNAIL ━━━━━━━➣</b>

<b>Choose Thumbnail Option:</b>

1️⃣ Send URL (e.g., `https://example.com/thumb.jpg`)
2️⃣ Send `no` for default thumbnail
3️⃣ Send an image directly

<b>➣━━━━━━━━━━━━━━━━━➣</b>"""

VIDEO_CAPTION = """╭━━━━━━━━━━━━━━➣
┣⪼ 🎥 <b>Video Title:</b>
┃  ╰─⪼ <code>{}.mkv</code>
┣⪼ 📚 <b>Topic Name:</b>
┃  ╰─⪼ <b>{}</b>
┣⪼ 📂 <b>Batch Name:</b>
┃  ╰─⪼ <b>{}</b>
╰━━━━━━━━━━━━━━➣

<b>{}</b>"""

VIDEO_CAPTION_V2 = """<b>[🎥]Video Title :</b><code>{} .mkv</code>
<blockquote><b>📌Batch Name : {}
🔗Topic Name : {}
⏰Class Time : {}</b></blockquote>

<b>{}</b>"""

YT_VIDEO_CAPTION = """<blockquote><i>We apologize, We are unable to download YouTube videos for security reasons. However, you can watch the video using the link below.</i></blockquote>"""
