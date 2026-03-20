import { Link } from 'react-router-dom';

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md text-center">
        <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
          GigGuard X
        </h2>
        <p className="mt-2 text-center text-sm text-gray-600">
          Intelligent Income Shield for India's Gig Economy
        </p>
        <div className="mt-8 flex justify-center gap-4">
          <Link
            to="/login"
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm xl font-medium text-white bg-brand-600 hover:bg-brand-700"
          >
            Sign in
          </Link>
          <Link
            to="/register"
            className="w-full flex justify-center py-2 px-4 border border-brand-600 rounded-md shadow-sm xl font-medium text-brand-600 bg-white hover:bg-gray-50"
          >
            Register
          </Link>
        </div>
      </div>
    </div>
  );
}
