import io
import os
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment

from app.models.result import PodcastScript

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


class AudioGenerator:
    def generate_audio_for_line(self, line_text: str, voice_id: str) -> AudioSegment:
        # Generate the audio bytes from ElevenLabs
        audio_generator = client.text_to_speech.convert(
            text=line_text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        # Collect generator chunks into a single byte stream
        audio_bytes = b"".join(list(audio_generator))

        # Convert bytes to a Pydub AudioSegment
        return AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")

    def generate_audio(self, job_id: str, script: PodcastScript):
        audio_segments: list[AudioSegment] = []

        for line in script.content:
            # Select voice based on speaker
            voice_id = (
                "JBFqnCBsd6RMkjVDRZzb"
                if line.speaker == "host"
                else "pNInz6obpgDQGcFmaJgB"
            )

            # Generate segment
            audio = self.generate_audio_for_line(line.text, voice_id)

            # Add a small 0.5s pause between lines for natural pacing
            silence = AudioSegment.silent(duration=500)
            audio_segments.append(audio + silence)

        # Combine all segments (Pydub allows summing segments)
        final_audio = sum(audio_segments, AudioSegment.empty())

        path = "podcasts/audio"
        os.makedirs(path, exist_ok=True)

        # Export the final file
        final_audio.export(f"{path}/{job_id}.mp3", format="mp3")


audio_generator = AudioGenerator()
