import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../stores/authStore';
import { useForm } from 'react-hook-form';
import apiClient from '../api/client';
import toast from 'react-hot-toast';

export default function LoginPage() {
  const { register, handleSubmit } = useForm();
  const setAuth = useAuthStore(state => state.setAuth);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const onSubmit = async (data: any) => {
    setLoading(true);
    try {
      const res = await apiClient.post('/auth/login', data);
      setAuth(res.data.access_token, res.data.user, res.data.worker_profile);
      toast.success('Logged in successfully');
      navigate('/dashboard');
    } catch (err: any) {
      toast.error(err.response?.data?.detail || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center py-12 px-6">
      <div className="max-w-md w-full mx-auto bg-white p-8 border rounded shadow">
        <h2 className="text-2xl font-bold mb-6 text-center">Login to GigGuard X</h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Email</label>
            <input type="email" {...register('email', { required: true })} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm border p-2" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Password</label>
            <input type="password" {...register('password', { required: true })} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm border p-2" />
          </div>
          <button type="submit" disabled={loading} className="w-full bg-brand-600 text-white font-bold py-2 px-4 rounded hover:bg-brand-700">
            {loading ? 'Logging in...' : 'Sign In'}
          </button>
        </form>
      </div>
    </div>
  );
}
