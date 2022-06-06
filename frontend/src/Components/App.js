import Results from './Results';
import DescriptionInput from './DescriptionInput';
import { useState } from 'react';


function App() {
  // Retrieved state that tells if data is ready to be presented
  const [retrieved, setRetrieved] = useState(false);
  // Topics object that maps (topic -> probability)
  const [topics, setTopics] = useState(null);
  const [probabilities, setProbabilities] = useState(null);
  
  // If data is available, then render results; otherwise, render form
  return (
    <div className="App">
      {retrieved ? <Results topics={topics} probabilities={probabilities}/> : <DescriptionInput setRetrieved = {setRetrieved} setTopics = {setTopics} setProbabilities = {setProbabilities}/>}
    </div>
  );
}

export default App;
