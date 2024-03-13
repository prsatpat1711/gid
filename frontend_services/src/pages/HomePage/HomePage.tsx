import React from 'react'
import NavigationBar from '../../components/NavigationBar/NavigationBar'
import ProductCard from '../../components/ProductCards/ProductCard';
import style from './HomePage.module.css'
const HomePage = () => {
  const intel = [1,2,3,4,5,6,7,8,9,10];
  return (
    <div className={style.HomePageDiv}>
      {intel.map((el) => (
        <ProductCard/>
      ))

      }
    </div>
  )
}

export default HomePage