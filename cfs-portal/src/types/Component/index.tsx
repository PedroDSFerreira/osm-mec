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

export enum ActionType {
  DELETE = 'delete',
  DEPLOY = 'deploy'
}

export enum Item {
  APP = 'app',
  INSTANCE = 'instance'
}

export type ConfirmationDialogProps = {
  open: boolean,
  onClose: () => void,
  onConfirm: () => void,
  action: ActionType,
  item: Item
}

export type AppData = {
  id: string,
  name: string,
  provider: string,
  version: number
}

export type InstanceData = {
  name: string;
  'operational-status': string;
  'config-status': string;
  details: string;
  'created-at': Date;
}

export type VimData = {
  id: string,
  name: string
}