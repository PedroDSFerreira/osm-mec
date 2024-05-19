import React from 'react';
import { BrowserRouter, Routes, Route, Outlet } from 'react-router-dom'
import { NotAuthenticatedRoute, PrivateRoute } from './utils/routes'

import Login from './pages/Login'
import Test from './pages/Test'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import AppCatalog from './pages/AppCatalog';
import AppInstances from './pages/AppInstances';
import { Sidebar } from './components/Sidebar';
import TopBar from './components/Topbar';
import { SidebarProvider } from './contexts/sidebarContext';
import { Box, Toolbar } from '@mui/material';

import './App.css';
import { ToastContainer } from 'react-toastify';

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route element={<NotAuthenticatedRoute />} >
            <Route path='/login' element={<Login />} />
          </Route>
          {/* <Route element={<PrivateRoute />} > */}
          <Route element={
            <SidebarProvider>
              <Box sx={{ display: 'flex' }}>
                <TopBar />
                <Sidebar />
                <Box sx={{
                  flexGrow: 1,
                  p: 3,
                  backgroundColor: 'rgba(0, 0, 0, 0.04)',
                  height: '100vh',
                  width: '100vw',
                  boxSizing: 'border-box',
                }}>
                  <Toolbar />
                  <Outlet />
                </Box>
              </Box>
            </SidebarProvider>
          } >
            <Route path='/test' element={<Test />} />
            <Route path='/' element={<Dashboard />} />
            <Route path='/dashboard' element={<Dashboard />} />
            <Route path='/app-catalog' element={<AppCatalog />} />
            <Route path='/app-instances' element={<AppInstances />} />
            <Route path='*' element={<h1>Not Found</h1>} />
          </Route>
        </Routes>
      </BrowserRouter>
      <ToastContainer />
    </>
  )
}
export default App
