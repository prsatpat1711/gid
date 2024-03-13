import React from 'react'
import styles from './SideNav.module.css'

const SideNav = () => {
  return (
    <div className={styles.SideNavDiv + ` d-flex flex-column justify-content-top align-items-center`}>
        <button type='button' className={styles.SideNavButton} onClick={() => console.log("Hi")}>Chat and Find</button>
        <button type='button' className={styles.SideNavButton} onClick={() => console.log("Hi")}>Categories</button>
        <button type='button' className={styles.SideNavButton} onClick={() => console.log("Hi")}>Discount Season</button>
        <button type='button' className={styles.SideNavButton} onClick={() => console.log("Hi")}>Lightning Deals</button>
        <button type='button' className={styles.SideNavButton} onClick={() => console.log("Hi")}>About</button>
        <button type='button' className={styles.SideNavButton} onClick={() => console.log("Hi")}>Help</button>
    </div>
  )
}

export default SideNav