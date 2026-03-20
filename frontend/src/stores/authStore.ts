import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface User {
  id: string;
  email: string;
  role: string;
}

interface WorkerProfile {
  id: string;
  full_name: string;
  risk_score: int;
  trust_score: int;
}

interface AuthState {
  token: string | null;
  user: User | null;
  workerProfile: WorkerProfile | null;
  isAuthenticated: boolean;
  setAuth: (token: string, user: User, workerProfile?: WorkerProfile) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      user: null,
      workerProfile: null,
      isAuthenticated: false,
      setAuth: (token, user, workerProfile) => 
        set({ token, user, workerProfile, isAuthenticated: true }),
      logout: () => set({ token: null, user: null, workerProfile: null, isAuthenticated: false }),
    }),
    {
      name: 'gigguard-auth-storage',
    }
  )
);
