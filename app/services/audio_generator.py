import io
import logging
import os
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment

from app.models.result import PodcastScript

logger = logging.getLogger(__name__)

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


class AudioGenerator:
    def generate_audio_for_line(
        self, job_id: str, line_text: str, voice_id: str
    ) -> AudioSegment:
        logger.info(f"Generating audio for line for job with id '{job_id}'...")

        audio_generator = client.text_to_speech.convert(
            text=line_text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        audio_bytes = b"".join(list(audio_generator))

        logger.info(
            f"Successfully generated audio for line for job with id '{job_id}'."
        )

        # Unpacks virtual mp3 file into raw audio frames for Pydub to manipulate
        return AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")

    def generate_audio(self, job_id: str, script: PodcastScript):
        logger.info(f"Generating audio for job with id '{job_id}'...")

        audio_segments: list[AudioSegment] = []

        for line in script.content:
            voice_id = (
                "JBFqnCBsd6RMkjVDRZzb"
                if line.speaker == "host"
                else "pNInz6obpgDQGcFmaJgB"
            )

            audio = self.generate_audio_for_line(job_id, line.text, voice_id)

            silence = AudioSegment.silent(duration=500)
            audio_segments.append(audio + silence)

        final_audio = sum(audio_segments, AudioSegment.empty())

        path = "podcasts/audio"
        os.makedirs(path, exist_ok=True)

        final_audio.export(f"{path}/{job_id}.mp3", format="mp3")

        logger.info(f"Successfully generated audio for job with id '{job_id}'.")


audio_generator = AudioGenerator()
