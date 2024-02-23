import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { NotAuthenticatedRoute, PrivateRoute } from './utils/routes'
import Login from './pages/Login' 
import Test from './pages/Test'
import Home from './pages/Home'
import './App.css';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<NotAuthenticatedRoute />} >
          <Route path='/login' element={<Login />} />
        </Route>
        <Route element={<PrivateRoute />} >
          <Route path='/' element={<Home />} />
        </Route>
          <Route path='/test' element={<Test />} />
      </Routes>
    </BrowserRouter>
  )
}
 export default App
