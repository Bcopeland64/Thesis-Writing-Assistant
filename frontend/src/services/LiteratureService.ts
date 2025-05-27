import axios from 'axios';
import AuthService from './AuthService'; // To get the token

const API_URL = '/api/v1/literature'; // Adjust if your proxy is set up differently

const searchLiterature = async (query: string) => {
    const token = AuthService.getToken();
    if (!token) {
        throw new Error("No authentication token found.");
    }

    const response = await axios.get(`${API_URL}/search`, {
        params: { query },
        headers: {
            'Authorization': `Bearer ${token}`,
        },
    });
    return response.data;
};

const summarizePaper = async (paper_title: string) => {
    const token = AuthService.getToken();
    if (!token) {
        throw new Error("No authentication token found.");
    }

    const response = await axios.get(`${API_URL}/summarize`, {
        params: { paper_title }, // FastAPI endpoint expects 'paper_title'
        headers: {
            'Authorization': `Bearer ${token}`,
        },
    });
    return response.data;
};

const LiteratureService = {
    searchLiterature,
    summarizePaper,
};

export default LiteratureService;
