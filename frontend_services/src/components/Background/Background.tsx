import React from 'react';
import NavigationBar from '../NavigationBar/NavigationBar';
import SideNav from '../SideNav/SideNav';

interface BGProps {
    children: React.ReactNode;
}

const Background = ({ children }: BGProps) => {
    return (
        <div className='w-100 h-100 text-white d-flex flex-column' style={{ backgroundColor: "blueviolet", zIndex:"1"}}>
            <NavigationBar/>
            <div className='d-flex flex-row'>
            <SideNav/>
            {children}
            </div>
            
        </div>
    );
};

export default Background;
