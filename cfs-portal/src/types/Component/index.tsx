import type { ToastTransition } from 'react-toastify'
import type { ReactNode } from 'react'

export type ToastType = {
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right',
  autoClose?: number | false,
  hideProgressBar?: boolean,
  closeOnClick?: boolean,
  pauseOnHover?: boolean,
  draggable?: boolean,
  progress?: undefined | number | string,
  closeButton?: boolean,
  theme?: 'dark' | 'light' | 'colored',
  icon?: ReactNode | boolean,
  pauseOnFocusLoss?: boolean,
  delay?: number,
  type?: 'default' | 'success' | 'info' | 'warning' | 'error',
  transition?: ToastTransition
}

export type ConfirmationDialogProps = {
  open?: boolean,
  onClose?: () => void,
  onConfirm?: () => void,
  title?: string,
  content?: React.ReactNode
}

export type AppData = {
  _id: string,
  'product-name': string,
  provider: string,
  version: number
}
