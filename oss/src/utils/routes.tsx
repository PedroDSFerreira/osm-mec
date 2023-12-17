import { Navigate, Outlet } from 'react-router-dom'

export const PrivateRoute = () => {
  // If there is no token, redirect to /login
  // Otherwise on any other route, the Outlet will trigger the context and if there is a invalid token, it will redirect to /login
  return (
    localStorage.getItem('token') ?
      <Outlet /> :
      <Navigate to="/login" />
  )
}

export const NotAuthenticatedRoute = () => {
  // If there is token or id redirect to `/` otherwise redirect to `/login`
  return (
    localStorage.getItem('token') ?
      <Navigate to="/" /> :
      <Outlet />
  )
}
