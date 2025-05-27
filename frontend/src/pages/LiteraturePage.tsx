import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import AuthService from '../services/AuthService';
import LiteratureService from '../services/LiteratureService';

const LiteraturePage: React.FC = () => {
    const navigate = useNavigate();
    const [searchQuery, setSearchQuery] = useState('');
    const [searchResults, setSearchResults] = useState<string | null>(null);
    const [searchError, setSearchError] = useState<string | null>(null);

    const [paperTitle, setPaperTitle] = useState('');
    const [summaryResults, setSummaryResults] = useState<string | null>(null);
    const [summaryError, setSummaryError] = useState<string | null>(null);

    const handleLogout = () => {
        AuthService.logout();
        navigate('/login');
    };

    const handleSearch = async (e: React.FormEvent) => {
        e.preventDefault();
        setSearchError(null);
        setSearchResults(null);
        try {
            const results = await LiteratureService.searchLiterature(searchQuery);
            setSearchResults(typeof results === 'string' ? results : JSON.stringify(results, null, 2));
        } catch (err: any) {
            const errorMessage = err.response?.data?.detail || err.message || 'Search failed';
            setSearchError(errorMessage);
            console.error('Search error:', err);
        }
    };

    const handleSummarize = async (e: React.FormEvent) => {
        e.preventDefault();
        setSummaryError(null);
        setSummaryResults(null);
        try {
            const summary = await LiteratureService.summarizePaper(paperTitle);
            setSummaryResults(typeof summary === 'string' ? summary : JSON.stringify(summary, null, 2));
        } catch (err: any) {
            const errorMessage = err.response?.data?.detail || err.message || 'Summarization failed';
            setSummaryError(errorMessage);
            console.error('Summarize error:', err);
        }
    };

    return (
        <div className="min-h-screen bg-gray-100 p-4">
            <header className="flex justify-between items-center p-4 bg-white shadow-md rounded-md mb-6">
                <h1 className="text-3xl font-bold text-indigo-600">Thesis Assistant</h1>
                <button
                    onClick={handleLogout}
                    className="px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                >
                    Logout
                </button>
            </header>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Search Literature Section */}
                <section className="p-6 bg-white rounded-lg shadow-md">
                    <h2 className="text-xl font-semibold mb-4 text-gray-800">Search Literature</h2>
                    <form onSubmit={handleSearch} className="space-y-4">
                        <div>
                            <label htmlFor="searchQuery" className="block text-sm font-medium text-gray-700">
                                Search Query
                            </label>
                            <input
                                id="searchQuery"
                                type="text"
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                required
                                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            />
                        </div>
                        <button
                            type="submit"
                            className="w-full px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                        >
                            Search
                        </button>
                    </form>
                    {searchError && (
                        <div className="mt-4 p-2 text-sm text-red-700 bg-red-100 rounded-md">
                            {searchError}
                        </div>
                    )}
                    {searchResults && (
                        <div className="mt-4">
                            <h3 className="text-md font-semibold text-gray-700">Results:</h3>
                            <pre className="p-3 mt-2 bg-gray-50 text-sm text-gray-800 rounded-md overflow-x-auto">
                                {searchResults}
                            </pre>
                        </div>
                    )}
                </section>

                {/* Summarize Paper Section */}
                <section className="p-6 bg-white rounded-lg shadow-md">
                    <h2 className="text-xl font-semibold mb-4 text-gray-800">Summarize Paper</h2>
                    <form onSubmit={handleSummarize} className="space-y-4">
                        <div>
                            <label htmlFor="paperTitle" className="block text-sm font-medium text-gray-700">
                                Paper Title
                            </label>
                            <input
                                id="paperTitle"
                                type="text"
                                value={paperTitle}
                                onChange={(e) => setPaperTitle(e.target.value)}
                                required
                                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            />
                        </div>
                        <button
                            type="submit"
                            className="w-full px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                        >
                            Summarize
                        </button>
                    </form>
                    {summaryError && (
                        <div className="mt-4 p-2 text-sm text-red-700 bg-red-100 rounded-md">
                            {summaryError}
                        </div>
                    )}
                    {summaryResults && (
                        <div className="mt-4">
                            <h3 className="text-md font-semibold text-gray-700">Summary:</h3>
                            <pre className="p-3 mt-2 bg-gray-50 text-sm text-gray-800 rounded-md overflow-x-auto">
                                {summaryResults}
                            </pre>
                        </div>
                    )}
                </section>
            </div>
        </div>
    );
};

export default LiteraturePage;
