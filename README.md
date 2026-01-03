# MLX Whisper Transcriber

A high-performance audio and video transcriber for macOS (Apple Silicon M1/M2/M3), powered by `mlx-whisper` and OpenAI's Whisper models.

## Features

- **Apple Silicon Optimized**: Leverages MLX for efficient inference on Mac GPUs.
- **Dual Interface**:
  - **Web GUI**: Easy-to-use drag-and-drop interface built with Gradio.
  - **CLI**: Command-line tool for scripting and automation.
- **Media Support**: Handles both Audio (MP3, WAV, etc.) and Video (MP4, MOV, etc.) files by automatically extracting audio.
- **Automatic Output**: Saves transcripts as `.txt` files in the same directory as the input media.

## Prerequisites

- **Operating System**: macOS 13.0+ (Ventura or later recommended)
- **Hardware**: Apple Silicon (M1, M2, M3, etc.)
- **Software**:
  - Python 3.12 or higher
  - [uv](https://github.com/astral-sh/uv) (for dependency management)
  - `ffmpeg` (required for audio processing)

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project folder:
    ```bash
    cd whisper-transcriber
    ```

2.  **Install dependencies**:
    Ensure you have `uv` installed (`pip install uv` or `brew install uv`).
    ```bash
    uv sync
    ```
    
    *Note: `ffmpeg` is required for audio extraction. If not installed, run:*
    ```bash
    brew install ffmpeg
    ```

## Usage

### Web GUI (Recommended)

Launch the interactive web interface:

```bash
uv run python -m src.cli
```

1.  Open the provided local URL (usually `http://127.0.0.1:7860`).
2.  Drag and drop an audio or video file.
3.  Click **Transcribe**.
4.  View the text on screen or download the generated `.txt` file.

### Command Line Interface (CLI)

Transcribe files directly from your terminal:

```bash
uv run python -m src.cli transcribe <path_to_file>
```

**Example:**
```bash
uv run python -m src.cli transcribe ../test.mp4
```

**Options:**
- `--model`: Specify a different MLX Whisper model (default: `mlx-community/whisper-large-v3-turbo`).

## Project Structure

- `src/transcriber.py`: Core logic for file handling and MLX Whisper integration.
- `src/gui.py`: Gradio web interface definition.
- `src/cli.py`: Entry point for CLI and GUI launcher.
- `pyproject.toml`: Project configuration and dependencies.

## Troubleshooting

- **FFmpeg not found**: Ensure `ffmpeg` is installed and in your system PATH (`brew install ffmpeg`).
- **Memory Issues**: The default model is `large-v3-turbo`. If you have limited RAM (e.g., 8GB), you might experience slowdowns with very long files.

## Developer Setup

This project uses `pre-commit` to ensure code quality.

1.  **Install Hooks**:
    ```bash
    make install
    ```
    This sets up the git hook to run `ruff` (linting and formatting) automatically on every commit.

2.  **Make Commands**:
    - `make up`: Start the web GUI.
    - `make pc`: Run pre-commit checks on all files manually.

## License

MIT
