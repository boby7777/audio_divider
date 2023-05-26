from pydub import AudioSegment

def divide_audio(file_path, piece_duration):
    audio = AudioSegment.from_file(file_path)
    total_duration = len(audio)
    piece_duration_ms = piece_duration * 60 * 1000  # Convert minutes to milliseconds

    # Calculate the number of pieces
    num_pieces = total_duration // piece_duration_ms

    for i in range(num_pieces):
        start_time = i * piece_duration_ms
        end_time = (i + 1) * piece_duration_ms
        piece = audio[start_time:end_time]
        piece.export(f"piece_{i+1}.mp3", format="mp3")

    # Export the remaining portion as the last piece if any
    if total_duration % piece_duration_ms != 0:
        last_piece = audio[-(total_duration % piece_duration_ms):]
        last_piece.export(f"piece_{num_pieces+1}.mp3", format="mp3")

# Usage example
audio_file = "path/to/audio/file.mp3"
piece_duration = 10  # minutes

divide_audio(audio_file, piece_duration)
