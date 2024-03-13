import React from "react";
import styles from "./NavigationBar.module.css";
const NavigationBar = () => {
  return (
    <div>
      <div className={styles.NavbarDiv}>
        <div className={styles.NavbarHeader}>
          <h3 className={styles.NavbarHeaderText}>Kommercial</h3>
          <div>
            <input
              type="text"
              className={styles.NavbarSearchText}
              onChange={(event) => console.log(event.target.value)}
            ></input>
            <button
              type="button"
              className={styles.NavbarButton}
              onClick={() => console.log("Clicked")}
            >
              Search
            </button>
          </div>
        </div>
        <div className={styles.NavbarButtons}>
          <button
            type="button"
            className={styles.NavbarButton}
            onClick={() => console.log("Clicked")}
          >
            Home
          </button>
          <button
            type="button"
            className={styles.NavbarButton}
            onClick={() => console.log("Clicked")}
          >
            Categories
          </button>
          <button
            type="button"
            className={styles.NavbarButton}
            onClick={() => console.log("Clicked")}
          >
            Cart
          </button>
          <button
            type="button"
            className={styles.NavbarButton}
            onClick={() => console.log("Clicked")}
          >
            Account
          </button>
          <button
            type="button"
            className={styles.NavbarButton}
            onClick={() => console.log("Clicked")}
            style={{
              fontSize: "12px"
            }}
          >
            Login/Sign Up
          </button>
        </div>
      </div>
    </div>
  );
};

export default NavigationBar;
