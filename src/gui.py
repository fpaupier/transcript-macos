import gradio as gr
import os
from pathlib import Path
from src.transcriber import transcribe_media


def process_file(file_obj, progress=gr.Progress()):
    if file_obj is None:
        return "No file selected.", None

    file_path = file_obj.name
    filename = Path(file_path).name

    progress(0, desc="Starting transcription...")

    try:
        # We can't get real-time progress from mlx-whisper's simple API easily,
        # but we can indicate we are working.
        progress(0.2, desc=f"Transcribing {filename}... Please wait.")

        output_path = transcribe_media(file_path)

        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        progress(1.0, desc="Done!")
        return content, output_path

    except Exception as e:
        return f"Error: {str(e)}", None


def launch_gui():
    with gr.Blocks(title="MLX Whisper Transcriber") as demo:
        gr.Markdown("# MLX Whisper Transcriber (Mac M1/M2/M3)")
        gr.Markdown(
            "Upload an audio or video file to transcribe it using `mlx-community/whisper-large-v3-turbo`."
        )

        with gr.Row():
            with gr.Column():
                file_input = gr.File(
                    label="Upload Audio/Video", file_types=["audio", "video"]
                )
                submit_btn = gr.Button("Transcribe", variant="primary")

            with gr.Column():
                output_text = gr.Textbox(label="Transcription", buttons=["copy"], lines=20)
                download_file = gr.File(label="Download Text File")

        submit_btn.click(
            fn=process_file, inputs=[file_input], outputs=[output_text, download_file]
        )

    demo.launch()


if __name__ == "__main__":
    launch_gui()
