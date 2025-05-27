import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import LiteraturePage from '../LiteraturePage';
import AuthService from '../../services/AuthService';
import LiteratureService from '../../services/LiteratureService';

// Mock services
jest.mock('../../services/AuthService');
const mockedAuthService = AuthService as jest.Mocked<typeof AuthService>;

jest.mock('../../services/LiteratureService');
const mockedLiteratureService = LiteratureService as jest.Mocked<typeof LiteratureService>;

// Mock react-router-dom's useNavigate
const mockedNavigate = jest.fn();
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => mockedNavigate,
}));

describe('LiteraturePage', () => {
  beforeEach(() => {
    // Clear mocks and localStorage before each test
    mockedAuthService.logout.mockClear();
    mockedAuthService.getCurrentUser.mockReturnValue({ access_token: 'fake-token' }); // Simulate logged-in user
    mockedLiteratureService.searchLiterature.mockClear();
    mockedLiteratureService.summarizePaper.mockClear();
    mockedNavigate.mockClear();
    localStorage.clear();
    // Simulate a logged-in user for AuthService.getToken via localStorage
    localStorage.setItem('user', JSON.stringify({ access_token: 'test-token', token_type: 'bearer' }));
  });

  test('renders literature page correctly with search and summarize forms', () => {
    render(
      <BrowserRouter>
        <LiteraturePage />
      </BrowserRouter>
    );

    expect(screen.getByRole('heading', { name: /Thesis Assistant/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Logout/i })).toBeInTheDocument();

    // Search section
    expect(screen.getByRole('heading', { name: /Search Literature/i })).toBeInTheDocument();
    expect(screen.getByLabelText(/Search Query/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Search/i })).toBeInTheDocument();

    // Summarize section
    expect(screen.getByRole('heading', { name: /Summarize Paper/i })).toBeInTheDocument();
    expect(screen.getByLabelText(/Paper Title/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Summarize/i })).toBeInTheDocument();
  });

  test('logout button calls AuthService.logout and navigates to /login', () => {
    render(
      <BrowserRouter>
        <LiteraturePage />
      </BrowserRouter>
    );

    fireEvent.click(screen.getByRole('button', { name: /Logout/i }));
    expect(mockedAuthService.logout).toHaveBeenCalledTimes(1);
    expect(mockedNavigate).toHaveBeenCalledWith('/login');
  });

  // Search Literature Tests
  test('successful literature search displays results', async () => {
    const searchQuery = 'test query';
    const searchResults = 'Mocked search results here.';
    mockedLiteratureService.searchLiterature.mockResolvedValueOnce(searchResults);

    render(
      <BrowserRouter>
        <LiteraturePage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Search Query/i), { target: { value: searchQuery } });
    fireEvent.click(screen.getByRole('button', { name: /Search/i }));

    await waitFor(() => {
      expect(mockedLiteratureService.searchLiterature).toHaveBeenCalledWith(searchQuery);
    });
    await waitFor(() => {
      expect(screen.getByText(searchResults)).toBeInTheDocument();
    });
  });

  test('failed literature search displays error message', async () => {
    const searchQuery = 'failing query';
    const errorMessage = 'Search failed due to network error.';
    mockedLiteratureService.searchLiterature.mockRejectedValueOnce({ message: errorMessage });

    render(
      <BrowserRouter>
        <LiteraturePage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Search Query/i), { target: { value: searchQuery } });
    fireEvent.click(screen.getByRole('button', { name: /Search/i }));

    await waitFor(() => {
      expect(mockedLiteratureService.searchLiterature).toHaveBeenCalledWith(searchQuery);
    });
    await waitFor(() => {
      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });
  });

  // Summarize Paper Tests
  test('successful paper summarization displays summary', async () => {
    const paperTitle = 'A great paper';
    const summaryResults = 'This is a mock summary of the great paper.';
    mockedLiteratureService.summarizePaper.mockResolvedValueOnce(summaryResults);

    render(
      <BrowserRouter>
        <LiteraturePage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Paper Title/i), { target: { value: paperTitle } });
    fireEvent.click(screen.getByRole('button', { name: /Summarize/i }));

    await waitFor(() => {
      expect(mockedLiteratureService.summarizePaper).toHaveBeenCalledWith(paperTitle);
    });
    await waitFor(() => {
      expect(screen.getByText(summaryResults)).toBeInTheDocument();
    });
  });

  test('failed paper summarization displays error message', async () => {
    const paperTitle = 'A difficult paper';
    const errorMessage = 'Summarization failed.';
    mockedLiteratureService.summarizePaper.mockRejectedValueOnce({ 
      response: { data: { detail: errorMessage } } 
    });

    render(
      <BrowserRouter>
        <LiteraturePage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Paper Title/i), { target: { value: paperTitle } });
    fireEvent.click(screen.getByRole('button', { name: /Summarize/i }));

    await waitFor(() => {
      expect(mockedLiteratureService.summarizePaper).toHaveBeenCalledWith(paperTitle);
    });
    await waitFor(() => {
      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });
  });

  test('LiteratureService throwing "No authentication token found" error', async () => {
    const searchQuery = 'query';
    const errorMessage = "No authentication token found.";
    // Simulate no token by having AuthService.getToken return null
    // This is done by clearing localStorage and ensuring getCurrentUser returns null for token check.
    localStorage.removeItem('user'); // Ensure no user in local storage
    mockedAuthService.getCurrentUser.mockReturnValueOnce(null); // Ensure AuthService.getToken() will fail
    
    // Have the service throw the specific error when token is missing
    mockedLiteratureService.searchLiterature.mockImplementation(async () => {
        if (!AuthService.getToken()) { // AuthService.getToken() is part of the actual service
            throw new Error(errorMessage);
        }
        return "some results";
    });


    render(
      <BrowserRouter>
        <LiteraturePage />
      </BrowserRouter>
    );

    fireEvent.change(screen.getByLabelText(/Search Query/i), { target: { value: searchQuery } });
    fireEvent.click(screen.getByRole('button', { name: /Search/i }));

    await waitFor(() => {
      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });
  });

});
