import axios from 'axios';

const API_URL = '/api/v1/auth'; // Adjust if your proxy is set up differently or for production

const login = async (email_or_username: string, password_param: string) => {
    // FastAPI's OAuth2PasswordRequestForm expects 'username' and 'password' in form data
    const params = new URLSearchParams();
    params.append('username', email_or_username);
    params.append('password', password_param);

    const response = await axios.post(`${API_URL}/login`, params, {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    });
    if (response.data.access_token) {
        localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
};

const logout = () => {
    localStorage.removeItem('user');
};

const getCurrentUser = () => {
    const userStr = localStorage.getItem('user');
    if (userStr) {
        try {
            return JSON.parse(userStr);
        } catch (e) {
            // If parsing fails, remove the invalid item
            localStorage.removeItem('user');
            return null;
        }
    }
    return null;
};

const getToken = (): string | null => {
    const user = getCurrentUser();
    return user ? user.access_token : null;
}

const AuthService = {
    login,
    logout,
    getCurrentUser,
    getToken,
};

export default AuthService;
