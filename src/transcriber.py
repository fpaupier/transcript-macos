import os
import time
import mlx_whisper
from pathlib import Path


def transcribe_media(
    file_path: str,
    model_path: str = "mlx-community/whisper-large-v3-turbo",
    output_dir: str = None,
) -> str:
    """
    Transcribes an audio or video file to text using mlx-whisper.

    Args:
        file_path: Path to the input audio or video file.
        model_path: The mlx-whisper model to use.
        output_dir: Optional directory to save the output text file. If None, uses the input file's directory.

    Returns:
        The path to the generated text file.
    """
    print(f"Processing file: {file_path}")
    start_time = time.time()

    # Ensure file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Determine output path
    input_path = Path(file_path)
    if output_dir:
        out_path = Path(output_dir) / f"{input_path.stem}.txt"
    else:
        out_path = input_path.parent / f"{input_path.stem}.txt"

    print(f"Output will be saved to: {out_path}")
    print("Starting transcription... (this may take a moment)")

    # Transcribe
    # mlx_whisper.transcribe handles loading audio from video/audio files via ffmpeg/libav internally
    result = mlx_whisper.transcribe(str(input_path), path_or_hf_repo=model_path)

    text_content = result["text"]

    # Write to file
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text_content)

    duration = time.time() - start_time
    print(f"Transcription complete in {duration:.2f} seconds.")

    return str(out_path)
