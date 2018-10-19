import React from "react";

const name = "Jordan";
const opinion = "works";

const JSXVariables = () => (
  <div className="main-container">
    <div className="container">
      <div className="jumbotron">
        <h1>Hi! My name is {name})</h1>
        <h2>My name has {name.length}) letters</h2>
        <h2>I think React {opinion}</h2>
      </div>
    </div>
  </div>
);

export default JSXVariables;
