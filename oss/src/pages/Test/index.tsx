import toast from '../../utils/toast'
import { ToastContainer } from 'react-toastify';

const Test = () => {
  toast.error('error test')
  toast.warning('warning test')
  toast.success('success test')
  toast.info('info test')
  toast.default('default test')
  return (
    <div> Test Page 
      <ToastContainer />
    </div>
  )
}

export default Test
