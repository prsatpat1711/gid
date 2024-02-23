import React from 'react';

interface BGProps {
    children: React.ReactNode;
}

const Background = ({ children }: BGProps) => {
    return (
        <div className='w-100 h-100 bg-dark text-white'>
            {children}
        </div>
    );
};

export default Background;
