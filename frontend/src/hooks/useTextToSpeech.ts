import { useState } from 'react';

export const useTextToSpeech = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [signedUrl, setSignedUrl] = useState<string | null>(null);

    const fetchTextToSpeech = async (text: string) => {
        setIsLoading(true);
        setError(null);

        try {

            const response = await fetch('http://localhost:8080/text-to-speech/', {
                method: 'POST',
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                },
                body: JSON.stringify({ text: "apples" })
            });



            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            setSignedUrl(data.signed_url);
        } catch (error: any) {
            setError(error.message);
        } finally {
            setIsLoading(false);
        }
    };

    return { fetchTextToSpeech, isLoading, error, signedUrl };
};