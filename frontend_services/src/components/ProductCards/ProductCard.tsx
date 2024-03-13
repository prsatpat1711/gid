import React from 'react'
import style from './ProductCard.module.css'
const ProductCard = () => {
  return (
    <div className={style.ProductCardDiv}>
      <div className={style.productImage}>
        <img className={style.imgStyle} src='data:image/jpeg;base64,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'/>
      </div>
      <div className={style.productDesc}>
        <h5>Product name</h5>
        <h6 className={style.productText}>This is a product description. This will have a small info about the product.</h6>
        <button className='btn btn-secondary' onClick={() => console.log("Clicked")}>View</button>
      </div>
    </div>
  )
}

export default ProductCard