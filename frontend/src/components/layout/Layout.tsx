import { Link, Outlet } from 'react-router-dom';
import { useAuthStore } from '../../stores/authStore';

export default function Layout() {
  const user = useAuthStore(state => state.user);
  const logout = useAuthStore(state => state.logout);

  return (
    <div className="min-h-screen flex flex-col">
      {/* Topbar */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="text-xl font-bold text-brand-600">GigGuard X</div>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-600">{user?.email}</span>
            <button onClick={logout} className="text-sm font-medium text-gray-500 hover:text-gray-700">Logout</button>
          </div>
        </div>
      </header>

      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <aside className="w-64 bg-white border-r hidden md:block">
          <nav className="p-4 space-y-2">
            <Link to="/dashboard" className="block px-4 py-2 text-sm text-gray-700 rounded hover:bg-gray-100">Dashboard</Link>
          </nav>
        </aside>

        {/* Main content */}
        <main className="flex-1 bg-gray-50 overflow-y-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
