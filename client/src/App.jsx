import { useEffect } from "react";
import "./App.css";

function App() {
  useEffect(() => {
    fetch("/api/movies")
      .then((r) => r.json())
      .then(console.log);
  }, []);

  return (
    <>
      <h1>Check the console for a list of movies!</h1>
    </>
  );
}

export default App;
