import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function OnboardingPage() {
  const [step, setStep] = useState(1);
  const navigate = useNavigate();

  const handleNext = () => {
    if (step < 5) setStep(step + 1);
    else navigate('/dashboard');
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center py-12 px-6">
      <div className="max-w-lg w-full mx-auto bg-white p-8 border rounded shadow">
        <h2 className="text-2xl font-bold mb-6">Worker Onboarding - Step {step} of 5</h2>
        <div className="h-40 flex items-center justify-center bg-gray-100 rounded text-gray-500 mb-6">
          Mock Mockup Step {step} Details
        </div>
        <button onClick={handleNext} className="w-full bg-brand-600 text-white font-bold py-2 px-4 rounded hover:bg-brand-700">
          {step === 5 ? 'Complete Onboarding' : 'Next'}
        </button>
      </div>
    </div>
  );
}
