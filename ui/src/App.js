import './App.css';
import { ToxicText } from './ToxicText';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  return (
    <div className="App">
      <div className='TopNavbar'>
        <div className='brandname'>
          T-sense
        </div>
      </div>
      <div className='toxic_comp'>
        <ToxicText/>
      </div>
      <ToastContainer/>
    </div>
  );
}

export default App;
