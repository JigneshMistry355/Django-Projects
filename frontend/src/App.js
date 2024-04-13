import React from "react";
import StudentTable from "./Components/StudentTable";
import CreateStudent from "./Components/createStudent";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<CreateStudent />} />
        <Route path="/student-table" element={<StudentTable />} />
      </Routes>
    </Router>
  );
}

export default App;
