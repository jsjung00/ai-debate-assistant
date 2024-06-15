"use client"
import React from 'react';
import { useMediaRecorder } from '../hooks/useMediaRecorder';
import { Button } from './ui/button';

const RecorderComponent = () => {
    const { startRecording, stopRecording, isRecording } = useMediaRecorder();

    return (
        <div>
            <Button onClick={startRecording} disabled={isRecording}>
                Start Recording
            </Button>
            <Button onClick={stopRecording} disabled={!isRecording}>
                Stop Recording
            </Button>
        </div>
    );
};

export default RecorderComponent;