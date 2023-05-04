import React from "react";

export default function NavBar({ setPage }) {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          CS103a React Demo
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <a
                onClick={() => setPage("Main")}
                className="nav-link active"
                aria-current="page"
                href="#"
              >
                Home
              </a>
            </li>
            <li className="nav-item">
              <a
                onClick={() => setPage("Transaction")}
                className="nav-link"
                href="#"
              >
                Transaction
              </a>
            </li>
            <li className="nav-item">
              <a onClick={() => setPage("ToDo")} className="nav-link" href="#">
                ToDo
              </a>
            </li>
            <li className="nav-item">
              <a onClick={() => setPage("About")} className="nav-link" href="#">
                About
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}
