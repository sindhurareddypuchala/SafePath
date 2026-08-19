import React, { useState, useEffect } from 'react';

export function App() {
  const [healthStatus, setHealthStatus] = useState<string>('Connecting to API...');
  const [apiInfo, setApiInfo] = useState<Record<string, any> | null>(null);

  useEffect(() => {
    fetch('http://localhost:8000/health/liveness')
      .then((res) => res.json())
      .then((data) => {
        setHealthStatus(`Connected: ${data.status} (${data.service})`);
      })
      .catch((err) => {
        setHealthStatus('API Offline (Scaffold Mode)');
      });
  }, []);

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '100vh',
      padding: '2rem',
      backgroundColor: '#0f172a',
      color: '#f8fafc',
      fontFamily: 'Inter, sans-serif'
    }}>
      <div style={{
        maxWidth: '600px',
        width: '100%',
        backgroundColor: '#1e293b',
        borderRadius: '12px',
        padding: '2rem',
        boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.5)',
        border: '1px solid #334155'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
          <div style={{
            width: '16px',
            height: '16px',
            borderRadius: '50%',
            backgroundColor: healthStatus.includes('healthy') ? '#10b981' : '#f59e0b'
          }} />
          <h1 style={{ margin: 0, fontSize: '1.75rem', fontWeight: 700 }}>SafePath</h1>
        </div>
        
        <p style={{ color: '#94a3b8', fontSize: '0.95rem', lineHeight: 1.6 }}>
          Preventive Safety Intelligence & Journey Companion Platform.
        </p>

        <div style={{
          marginTop: '1.5rem',
          padding: '1rem',
          backgroundColor: '#0f172a',
          borderRadius: '8px',
          border: '1px solid #334155',
          fontSize: '0.875rem'
        }}>
          <strong>Backend Service Status:</strong>
          <div style={{ marginTop: '0.5rem', color: healthStatus.includes('healthy') ? '#34d399' : '#fbbf24' }}>
            {healthStatus}
          </div>
        </div>

        <div style={{ marginTop: '1.5rem', fontSize: '0.8rem', color: '#64748b' }}>
          Repository Scaffold Mode — Business features unimplemented.
        </div>
      </div>
    </div>
  );
}

export default App;
