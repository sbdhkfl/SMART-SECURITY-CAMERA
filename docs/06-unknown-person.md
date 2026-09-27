# 06 - Unknown Person Workflow

When a detected face does not match an enrolled person:

1. Create an event.
2. Save a local snapshot.
3. Start a configurable recording window.
4. Play a local voice prompt.
5. Record the person's response through the USB microphone.
6. Optionally transcribe the response locally.
7. Store the audio and transcript with the event.
8. Show the event in the dashboard.
9. Never upload the media to a cloud AI service.

The owner can configure cooldowns so the same person does not generate hundreds of identical events.
