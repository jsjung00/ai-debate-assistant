import { useState, useCallback } from 'react';

export const useMediaRecorder = () => {
    const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
    const [isRecording, setIsRecording] = useState(false);

    const startRecording = useCallback(() => {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                const newMediaRecorder = new MediaRecorder(stream);
                setMediaRecorder(newMediaRecorder);
                newMediaRecorder.start();
                setIsRecording(true);

                const audioChunks: BlobPart[] = [];
                newMediaRecorder.addEventListener("dataavailable", event => {
                    audioChunks.push(event.data);
                });

                newMediaRecorder.addEventListener("stop", () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
                    const formData = new FormData();
                    formData.append("file", audioBlob, "filename.mp3");

                    fetch("http://localhost:8080/upload_audio", {
                        method: "POST",
                        body: formData,
                    })
                        .then(response => response.json())
                        .then(data => console.log(data))
                        .catch(error => console.error(error));
                });
            })
            .catch(error => console.error(error));
    }, []);

    const stopRecording = useCallback(() => {
        if (mediaRecorder) {
            mediaRecorder.stop();
            setIsRecording(false);
        }
    }, [mediaRecorder]);

    return { startRecording, stopRecording, isRecording };
};