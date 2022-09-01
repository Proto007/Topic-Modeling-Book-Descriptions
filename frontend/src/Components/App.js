import Results from './Results';
import DescriptionInput from './DescriptionInput';
import { useState } from 'react';

function App() {
  // Retrieved state that tells if data is ready to be presented
  const [retrieved, setRetrieved] = useState(false);
  // Topics object that maps (topic -> probability)
  const [topics, setTopics] = useState(null);

  // If data is available, then render results; otherwise, render form
  return (
    <div className="App">
      {retrieved ? <Results topics={topics}/> : <DescriptionInput setRetrieved = {setRetrieved} setTopics = {setTopics}/>}
    </div>
  );
}

export default App;
