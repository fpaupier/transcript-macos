import click
from src.transcriber import transcribe_media
from src.gui import launch_gui


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """
    MLX Whisper Transcriber Tool.

    Run without commands to launch the GUI.
    Use 'transcribe <file>' to run in CLI mode.
    """
    if ctx.invoked_subcommand is None:
        print("Launching GUI...")
        launch_gui()


@main.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--model", default="mlx-community/whisper-large-v3-turbo", help="Model to use"
)
def transcribe(file_path, model):
    """Transcribe a specific file from the command line."""
    try:
        output_file = transcribe_media(file_path, model_path=model)
        print(f"Successfully transcribed to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
