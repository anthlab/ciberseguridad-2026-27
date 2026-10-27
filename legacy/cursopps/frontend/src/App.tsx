import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { AuthProvider, useAuth } from './context/AuthContext'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import ModulesPage from './pages/ModulesPage'
import ModulePage from './pages/ModulePage'
import TerminalPage from './pages/TerminalPage'
import LoginPage from './pages/LoginPage'
import NotFound from './pages/NotFound'
import LoadingSpinner from './components/LoadingSpinner'

function ProtectedRoutes() {
  const { authenticated, loading } = useAuth()
  if (loading) return <div className="min-h-screen bg-cyber-bg flex items-center justify-center"><LoadingSpinner /></div>
  if (!authenticated) return <LoginPage />
  return (
    <Layout>
      <Routes>
        <Route path="/"                        element={<Dashboard />} />
        <Route path="/modulos"                 element={<ModulesPage />} />
        <Route path="/modulos/:slug"           element={<ModulePage />} />
        <Route path="/terminal"                element={<TerminalPage />} />
        <Route path="*"                        element={<NotFound />} />
      </Routes>
    </Layout>
  )
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* Public: player join page (accessible via QR from any device) */}
          {/* All other routes require auth */}
          <Route path="/*" element={<ProtectedRoutes />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  )
}
