import { toast as Toast, Slide } from 'react-toastify'

import type { ToastType } from '../types/Component'
import 'react-toastify/dist/ReactToastify.css'

const defaultToastOptions: ToastType = {
  position: 'top-right',
  autoClose: 3000,
  hideProgressBar: false,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: false,
  progress: undefined,
  closeButton: true,
  theme: 'colored',
  icon: true,
  pauseOnFocusLoss: true,
  delay: 0,
  type: 'default',
  transition: Slide,
}

export const toast = {
  success: (message: string, options?: ToastType) => Toast(
    message,
    { ...defaultToastOptions, ...options, type: 'success' }
  ),
  error: (message: string, options?: ToastType) => Toast(
    message,
    { ...defaultToastOptions, ...options, type: 'error' }
  ),
  info: (message: string, options?: ToastType) => Toast(
    message,
    { ...defaultToastOptions, ...options, type: 'info' }
  ),
  warning: (message: string, options?: ToastType) => Toast(
    message,
    { ...defaultToastOptions, ...options, type: 'warning' }
  ),
  default: (message: string, options?: ToastType) => Toast(
    message,
    { ...defaultToastOptions, ...options, type: 'default' }
  )
}

export default toast
