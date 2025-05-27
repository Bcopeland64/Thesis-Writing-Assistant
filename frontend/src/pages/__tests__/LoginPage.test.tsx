import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import LoginPage from '../LoginPage';
import AuthService from '../../services/AuthService';

// Mock AuthService
jest.mock('../../services/AuthService');
const mockedAuthService = AuthService as jest.Mocked<typeof AuthService>;

// Mock react-router-dom's useNavigate
const mockedNavigate = jest.fn();
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'), // use actual for all non-hook parts
  useNavigate: () => mockedNavigate,
}));

describe('LoginPage', () => {
  beforeEach(() => {
    // Clear mocks before each test
    mockedAuthService.login.mockClear();
    mockedNavigate.mockClear();
    localStorage.clear(); // Ensure localStorage is clean
  });

  test('renders login form correctly', () => {
    render(
      <BrowserRouter>
        <LoginPage />
      </BrowserRouter>
    );

    expect(screen.getByLabelText(/Email or Username/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Sign in/i })).toBeInTheDocument();
  });

  test('allows user to type in email and password fields', () => {
    render(
      <BrowserRouter>
        <LoginPage />
      </BrowserRouter>
    );

    const emailInput = screen.getByLabelText(/Email or Username/i) as HTMLInputElement;
    fireEvent.change(emailInput, { target: { value: 'test@example.com' } });
    expect(emailInput.value).toBe('test@example.com');

    const passwordInput = screen.getByLabelText(/Password/i) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'password123' } });
    expect(passwordInput.value).toBe('password123');
  });

  test('successful login navigates to /literature', async () => {
    mockedAuthService.login.mockResolvedValueOnce({ access_token: 'fake-token' }); // Mock successful login

    render(
      <BrowserRouter>
        <LoginPage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Email or Username/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/Password/i), { target: { value: 'password123' } });
    fireEvent.click(screen.getByRole('button', { name: /Sign in/i }));

    await waitFor(() => {
      expect(mockedAuthService.login).toHaveBeenCalledWith('test@example.com', 'password123');
    });
    
    await waitFor(() => {
      expect(mockedNavigate).toHaveBeenCalledWith('/literature');
    });
  });

  test('failed login displays an error message', async () => {
    const errorMessage = 'Invalid credentials';
    mockedAuthService.login.mockRejectedValueOnce({ 
      response: { data: { detail: errorMessage } } 
    });

    render(
      <BrowserRouter>
        <LoginPage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Email or Username/i), { target: { value: 'wrong@example.com' } });
    fireEvent.change(screen.getByLabelText(/Password/i), { target: { value: 'wrongpassword' } });
    fireEvent.click(screen.getByRole('button', { name: /Sign in/i }));

    await waitFor(() => {
      expect(mockedAuthService.login).toHaveBeenCalledWith('wrong@example.com', 'wrongpassword');
    });

    await waitFor(() => {
      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });
    expect(mockedNavigate).not.toHaveBeenCalled(); // Should not navigate
  });

  test('failed login displays generic error if no detail in response', async () => {
    const genericErrorMessage = 'Login failed';
    mockedAuthService.login.mockRejectedValueOnce(new Error(genericErrorMessage)); // Simulate network error or other non-API error

    render(
      <BrowserRouter>
        <LoginPage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Email or Username/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/Password/i), { target: { value: 'password' } });
    fireEvent.click(screen.getByRole('button', { name: /Sign in/i }));

    await waitFor(() => {
      expect(screen.getByText(genericErrorMessage)).toBeInTheDocument();
    });
  });
});
