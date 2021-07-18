import './App.css';
import Footer from './components/Footer';
import Team from './components/Team';
import Navbar from './components/Navbar';
import Upload from './components/Upload';

function App() {
  return (
    <div>
      <Navbar/>
      <Upload/>
      <Team />
      <Footer />
    </div>
  );
}

export default App;
