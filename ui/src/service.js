import { ToastContainer, toast } from 'react-toastify';

export const TSuccess = (message) => {
	return toast.success(message, {
			position: "top-right",
			autoClose: 10000,
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
			draggable: true,
			progress: undefined,
			theme: 'colored'
		})
}


export const TError = (message) => {
	return toast.error(message, {
			position: "top-right",
			autoClose: 10000,
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
			draggable: true,
			progress: undefined,
			theme: 'colored'
		})
}

export const BACKEND_URL = "http://localhost:8000"