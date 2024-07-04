import wave
import struct

def payload_to_audio(payload, output_file):
    # Define audio parameters
    sample_width = 2 # 2 bytes per sample (16-bit)
    sample_rate = 44100 # 44.1 kHz sample rate
    amplitude = 32767 # Maximum amplitude for 16-bit audio
    
    # Convert payload string to binary data
    payload_bytes = payload.encode('utf-8')
    
    # Initialize audio data as empty bytes
    audio_data = b''
    
    # Loop through each byte of the payload
    for byte in payload_bytes:
        # Convert byte to signed integer (-128 to 127)
        sample = struct.unpack('b', bytes([byte]))[0]
        
        # Scale sample to maximum amplitude
        sample *= amplitude
        
        # Convert sample to binary data
        sample_data = struct.pack('<h', sample)
        
        # Add sample data to audio data
        audio_data += sample_data
    
    # Create wave file and write audio data
    with wave.open(output_file, 'wb') as wav_file:
        wav_file.setnchannels(1) # Mono channel
        wav_file.setsampwidth(sample_width) # 16-bit sample width
        wav_file.setframerate(sample_rate) # 44.1 kHz sample rate
        wav_file.writeframes(audio_data)