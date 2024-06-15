"use client"
import React, { useState } from 'react';
import { useTextToSpeech } from '../hooks/useTextToSpeech';
import { Button } from './ui/button';

const TextToSpeechComponent = () => {
    const [text, setText] = useState('apples');
    const { fetchTextToSpeech, isLoading, error, signedUrl } = useTextToSpeech();

    const handleTextToSpeech = () => {
        fetchTextToSpeech(text);
    };

    return (
        <div>
            <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
            <Button onClick={handleTextToSpeech} disabled={isLoading}>
                Convert to Speech
            </Button>
            {error && <p>Error: {error}</p>}
            {signedUrl && <audio src={signedUrl} controls />}
        </div>
    );
};

export default TextToSpeechComponent;