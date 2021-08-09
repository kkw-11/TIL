import React, {useEffect, useState} from "react";
import logo from './logo.svg';

import './App.css';

function App() {
  const [text, setText] = useState('');
  const [trans, setTrans] = useState('');

  useEffect(() => {
    if(text === ''){
      setTrans('');
      return;
    }
    setTrans(text + "입니다.");
  }, [text]);

  return (
    <div className="App">
        <p>{trans}</p>
        <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
    </div>
  );
}

export default App;
